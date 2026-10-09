# class Number:
#     __slots__ = ['x', 'y']
#     def __init__(self, x: int, y: str):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#         return f'Number(x={self.x}, y={self.y})'
#     def __eq__(self, other):        
#         return self.x == other.x and self.y == other.y
#     def __lt__(self, other):
#         if self.x == other.x:
#             return self.y < other.y
#         return self.x < other.x
#     def __gt__(self, other):
#         if self.x == other.x:
#             return self.y > other.y
#         return self.x > other.x

    
# a = Number(6, '123')
# b = Number(2, '123')
# print(a.__eq__(b))
# print(a < b)
# print(a > b)


def strategy(opponent_prev: int, my_prev_points: int) -> int:
    if not hasattr(strategy, "_last_action"):
        strategy._last_action = 1

    if opponent_prev == -1 and my_prev_points == 0:
        strategy._last_action = 1
        return 1

    if my_prev_points in (3, 5):
        action = strategy._last_action
    else:
        action = 1 - strategy._last_action

    strategy._last_action = action
    return action