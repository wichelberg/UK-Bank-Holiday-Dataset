import holidays
import pandas as pd

years = list(range(2000, 2021))
uk_holidays = holidays.UnitedKingdom(years=years)

df_Holidays = pd.DataFrame(list(uk_holidays.items()), columns=['Date', 'Holiday_Name'])
df_Holidays = df_Holidays.sort_values(by='Date')
df_Holidays.to_csv('uk_bank_holidays_2000_2020.csv', index=False)