import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
df = pd.read_csv('dataset_taxi.exl', parse_dates=['timestamp'], index_col='timestamp')

# Проверим первые строки
print(df.head())