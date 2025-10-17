import pandas as pd
import matplotlib.pyplot as plt

calc_data = pd.read_csv("calculated_index.csv")
calc_data['Date'] = pd.to_datetime(calc_data['Date'])

actual_data = pd.read_csv("nifty_pharma_2025.csv",skiprows=3,names=["Date","Close"])
actual_data['Date'] = pd.to_datetime(actual_data['Date'])

base_actual = actual_data['Close'].iloc[0]
base_calc = calc_data['Index'].iloc[0]
scale_factor = base_actual / base_calc
calc_data['Scaled_Index'] = calc_data['Index'] * scale_factor

merged = pd.merge(actual_data, calc_data[['Date','Scaled_Index']], on='Date', how='inner')

x = merged['Date']
y_actual = merged['Close']
y_calc = merged['Scaled_Index']

plt.figure(figsize=(14, 7))


plt.plot(x, y_actual, marker='o', linestyle='-', linewidth=2, markersize=6,label='Actual index',color='green')

plt.plot(x, y_calc, marker='x', linestyle='--', linewidth=2, markersize=6, label='Calculated Index (Scaled)', color='blue')

for i in range(len(x)):
    plt.text(x[i], y_actual.iloc[i], f"{y_actual.iloc[i]:.0f}", ha='center', va='bottom', fontsize=8, color='green', rotation=45)
    plt.text(x[i], y_calc.iloc[i], f"{y_calc.iloc[i]:.0f}", ha='center', va='top', fontsize=8, color='blue', rotation=45)


plt.title("Nifty Pharma Actual vs Calculated Index", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Index Value", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(x, [d.strftime('%Y-%m-%d') for d in x], rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()