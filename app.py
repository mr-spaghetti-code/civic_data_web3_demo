import pandas as pd

# url = 'https://opendata.ecdc.europa.eu/covid19/nationalcasedeath_eueea_daily_ei/csv/data.csv'

covid_daily_df = pd.read_csv("data.csv", sep=",")

print(covid_daily_df.head())

covid_daily_df['formatted_date'] = pd.to_datetime(covid_daily_df['dateRep'])

covid_daily_df['Year-Week'] = covid_daily_df['formatted_date'].dt.strftime('%Y-%U')

weekly_country_aggregates = covid_daily_df.groupby(['Year-Week','geoId'])['cases'].sum()

weekly_country_aggregates.to_csv("new_data.csv")

print(weekly_country_aggregates.head())