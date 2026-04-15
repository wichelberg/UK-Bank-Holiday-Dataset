import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

holiday_df = pd.read_csv('UK_Holiday_Data_2000_2020.csv')

holiday_df['date'] = pd.to_datetime(holiday_df['Timestamp'])
holiday_cleaned = holiday_df[holiday_df['date'].dt.year >= 2010].copy()
holiday_cleaned = holiday_cleaned[['date', 'Is_Bank_Holiday', 'Day_of_Week']]
holiday_cleaned = holiday_cleaned.rename(columns={'Is_Bank_Holiday': 'is_bank_holiday',
                                                  'Day_of_Week': 'day_of_week'})

holiday_cleaned.to_csv('Holiday_Cleaned_2010to2020.csv', index=False)