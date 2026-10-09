def Nikitin_A_P_pair(opp_answer: int, points: int, _state={}):

    if opp_answer == -1 or "step" not in _state:
        _state.clear()
        _state.update({
            "step": 1,
            "balance": 0,          
            "revenge": 0,          
            "last_my": 1,          
            "same_run": 1,         
            "recent_opp": []       
        })
        return 1

    _state["step"] += 1

    _state["recent_opp"].append(opp_answer)
    if len(_state["recent_opp"]) > 6:
        _state["recent_opp"].pop(0)

    # Обновление оценки оппонента по предыдущему раунду
    if opp_answer == 0 and points == 0:
        # нас предали, пока мы сотрудничали
        _state["balance"] -= 4
        _state["revenge"] = 2
    elif opp_answer == 0 and points == 1:
        # взаимное предательство
        _state["balance"] -= 2
        _state["revenge"] = max(_state["revenge"], 1)
    elif opp_answer == 1 and points == 3:
        # честное взаимное сотрудничество
        _state["balance"] += 3
        if _state["revenge"] > 0:
            _state["revenge"] -= 1
    elif opp_answer == 1 and points == 5:
        # мы выиграли на предательстве, оппонент сотрудничал
        _state["balance"] += 2
        if _state["revenge"] > 0:
            _state["revenge"] -= 1

    recent_defects = _state["recent_opp"].count(0)
    recent_coops = len(_state["recent_opp"]) - recent_defects

    # Принятие решения
    if _state["revenge"] > 0 and opp_answer == 0:
        my_answer = 0
        _state["revenge"] -= 1
    elif opp_answer == 0 and points == 0:
        # немедленный ответ на явное предательство
        my_answer = 0
    elif recent_defects >= 4 and _state["balance"] < 0:
        # если в последних ходах слишком много предательств — уходим в защиту
        my_answer = 0
    elif _state["balance"] >= -1 or recent_coops >= recent_defects:
        # при приемлемом фоне сохраняем сотрудничество
        my_answer = 1
    else:
        my_answer = 0

    
    projected_run = _state["same_run"] + 1 if my_answer == _state["last_my"] else 1
    if projected_run >= 6:
        my_answer = 1 - _state["last_my"]
        projected_run = 1

    _state["same_run"] = projected_run
    _state["last_my"] = my_answer

    return my_answer


def Nikitin_A_P_net(opp_answer: int, points: int, _state={}):


    if opp_answer == -1 or "step" not in _state:
        _state.clear()
        _state.update({
            "step": 1,
            "trust": 0,           
            "toxicity": 0,         
            "direct_hits": 0,      
            "bad_row": 0,          
            "last_my": 1,
            "same_run": 1
        })
        return 1

    _state["step"] += 1

    # Анализ качества текущего оппонента
    if opp_answer == 0 and points == 0:
        _state["trust"] -= 4
        _state["toxicity"] += 3
        _state["direct_hits"] += 1
        _state["bad_row"] += 1
    elif opp_answer == 0 and points == 1:
        _state["trust"] -= 2
        _state["toxicity"] += 2
        _state["bad_row"] += 1
    elif opp_answer == 1 and points == 3:
        _state["trust"] += 3
        _state["toxicity"] = max(0, _state["toxicity"] - 2)
        _state["bad_row"] = 0
    elif opp_answer == 1 and points == 5:
        _state["trust"] += 1
        _state["toxicity"] = max(0, _state["toxicity"] - 1)
        _state["bad_row"] = 0
    else:
        if points <= 1:
            _state["bad_row"] += 1

    # Решение о смене оппонента:
    # уходим не сразу, а только если накопились жесткие признаки токсичности
    if _state["step"] >= 10:
        if (_state["direct_hits"] >= 3 and _state["toxicity"] >= 6) or _state["bad_row"] >= 5:
            _state.clear()
            return -1

    # Основная логика ответа
    if opp_answer == 0 and points == 0:
        my_answer = 0
    elif _state["toxicity"] >= 4:
        my_answer = 0
    elif _state["trust"] >= -1:
        my_answer = 1
    else:
        my_answer = 0

    projected_run = _state["same_run"] + 1 if my_answer == _state["last_my"] else 1
    if projected_run >= 6:
        my_answer = 1 - _state["last_my"]
        projected_run = 1

    _state["same_run"] = projected_run
    _state["last_my"] = my_answer

    return my_answer



def Nikitin_A_P_chain(opp_name: str, opp_answer: int, points: int, _memory={}):

    if opp_name not in _memory:
        _memory[opp_name] = {
            "step": 0,
            "rating": 0,           
            "retaliation": 0,      
            "last_my": 1,
            "same_run": 0,
            "window": []           
        }

    s = _memory[opp_name]

    if opp_answer == -1:
        s.clear()
        s.update({
            "step": 1,
            "rating": 0,
            "retaliation": 0,
            "last_my": 1,
            "same_run": 1,
            "window": []
        })
        return 1

    s["step"] += 1

    s["window"].append(opp_answer)
    if len(s["window"]) > 5:
        s["window"].pop(0)

    # Обновление личного "профиля" оппонента
    if opp_answer == 0 and points == 0:
        s["rating"] -= 4
        s["retaliation"] = 2
    elif opp_answer == 0 and points == 1:
        s["rating"] -= 2
        s["retaliation"] = max(s["retaliation"], 1)
    elif opp_answer == 1 and points == 3:
        s["rating"] += 3
        if s["retaliation"] > 0:
            s["retaliation"] -= 1
    elif opp_answer == 1 and points == 5:
        s["rating"] += 1
        if s["retaliation"] > 0:
            s["retaliation"] -= 1

    recent_defects = s["window"].count(0)
    recent_coops = len(s["window"]) - recent_defects

    # Логика выбора ответа именно для данного opp_name
    if s["retaliation"] > 0 and opp_answer == 0:
        my_answer = 0
        s["retaliation"] -= 1
    elif s["rating"] >= 2:
        my_answer = 1
    elif s["rating"] <= -3:
        my_answer = 0
    elif recent_coops >= recent_defects:
        my_answer = 1
    else:
        my_answer = 0

    
    projected_run = s["same_run"] + 1 if my_answer == s["last_my"] else 1
    if projected_run >= 6:
        my_answer = 1 - s["last_my"]
        projected_run = 1

    s["same_run"] = projected_run
    s["last_my"] = my_answer

    return my_answer