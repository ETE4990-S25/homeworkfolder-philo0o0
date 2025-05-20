import pandas as pd
import matplotlib.pyplot as plt
import json
import os

#Here I will load the data for EDA using Pandas and Matplotlib
#look at that using what you taught us in class!!
currency_data = {}
for currency in os.listdir("data"):
    if currency.endswith(".json"):
        with open(f"data/{currency}", "r") as f:
            currency_data[currency.replace(".json", "")] = json.load(f)
print(currency_data)
#Now its in a json file and then I will convert that data to dataframe
df_list = []
for currency, contents in currency_data.items():
    for date, info in contents.items():
        rate = info.get("exchangeRate", 0)
        target_currency = info.get("TargetCurrency", "Unkown")
        df_list.append([target_currency, date, rate])
df = pd.DataFrame(df_list, columns=['Currency', 'Date', 'ExchangeRate'])
#Here will be the date format that we needed to fix
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.dropna(subset=['Date'], inplace=True)
df.sort_values(by='Date', inplace=True)

#here will be the Matplotlib
plt.figure(figsize=(12, 6))
for currency in ['USD', 'EUR', 'GBP', 'CNY', 'JPY']:
    df_filtered = df[df['Currency'] == currency]
    plt.plot(df_filtered['Date'], df_filtered['ExchangeRate'], label=currency)
plt.title('Exchange Rate Trends')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.show()


