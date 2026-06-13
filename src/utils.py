# ============================================
# EDA: Customer Support Ticket Analysis
# System Analyst Portfolio Project
# ============================================

# 1. Импорты библиотек
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Настройки отображения
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# 2. Загрузка данных
df = pd.read_csv('../data/tickets.csv')

# 3. Первичный осмотр
print("=" * 60)
print("РАЗМЕР ДАТАСЕТА")
print("=" * 60)
print(f"Строк: {df.shape[0]}, Колонок: {df.shape[1]}")

print("\n" + "=" * 60)
print("ПЕРВЫЕ 5 СТРОК")
print("=" * 60)
display(df.head())

print("\n" + "=" * 60)
print("ИНФОРМАЦИЯ О КОЛОНКАХ")
print("=" * 60)
df.info()

print("\n" + "=" * 60)
print("СТАТИСТИКА ПО ЧИСЛОВЫМ КОЛОНКАМ")
print("=" * 60)
df.describe()

print("\n" + "=" * 60)
print("ПРОПУСКИ В ДАННЫХ")
print("=" * 60)
missing = df.isnull().sum()
missing_pct = (df.isnull().sum() / len(df)) * 100
missing_df = pd.DataFrame({'Missing Count': missing, 'Missing %': missing_pct})
print(missing_df[missing_df['Missing Count'] > 0])