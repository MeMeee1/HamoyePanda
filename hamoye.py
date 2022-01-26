import pandas as pd
import numpy as np
import math
df = pd.read_csv('C:/Users/HP/Downloads/FoodBalanceSheets_E_Africa_NOFLAG.csv',encoding='latin-1')

standard_deviation = df.Y2015.std()
print(round(standard_deviation,3))

no_mean = df.Y2015.mean()
print(round(no_mean,3))

missing_value= df.Y2016.isnull().sum()
print(round(missing_value,2))

percentage = (missing_value/len(df.Y2016))*100
total_percent=round(percentage, 2)
print(total_percent)

correlation_df = df.corr()
print(correlation_df.loc['Element Code',["Y2014","Y2015","Y2016","Y2017","Y2018"]].idxmax())

highest_value_for_y2014=df.groupby('Element')['Y2014'].sum()
print(highest_value_for_y2014.at['Production'])

highest_sum_y2018 = df.groupby("Element")["Y2018"].sum().idxmax()
print(highest_sum_y2018)

third_lowest_sum = df.groupby("Element")["Y2018"].sum().nlargest(3).idxmin()
print(third_lowest_sum)

query_algeria = df['Area']=='Algeria'
total_import_quantity = df[query_algeria].groupby('Element')['Y2018'].sum()
print(total_import_quantity.at['Import Quantity'])

unique_countries = df.Area.unique()
print(len(unique_countries))
