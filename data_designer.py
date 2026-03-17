import pandas as pd

file = "uk_bank_holidays_2000_2020.csv"
df_holidays = pd.read_csv(file)

df_holidays ['Date'] = pd.to_datetime(df_holidays['Date']).dt.date

date_range = pd.date_range(start='2000-01-01', end='2021-01-01 23:00:00')
DataFrame = pd.DataFrame(date_range, columns=['Timestamp'])

DataFrame['Year'] = DataFrame['Timestamp'].dt.year
DataFrame['Month'] = DataFrame['Timestamp'].dt.month
DataFrame['Day'] = DataFrame['Timestamp'].dt.day
DataFrame['Hour'] = DataFrame['Timestamp'].dt.hour
DataFrame['Day_of_Week'] = DataFrame['Timestamp'].dt.day_name()

DataFrame['Date_Temporary'] = DataFrame['Timestamp'].dt.date

DataFrame = pd.merge(DataFrame, df_holidays, left_on='Date_Temporary', right_on='Date', how='inner')

DataFrame['Holiday_Name'] = DataFrame['Holiday_Name'].fillna("None")
DataFrame['Is_Bank_Holiday'] = (DataFrame['Holiday_Name'] != "None").astype(int)

DataFrame = DataFrame.drop(columns=['Date_Temporary', 'Date'])

DataFrame.to_csv("UK_Holiday_Data_2010_2020.csv", index=False)
