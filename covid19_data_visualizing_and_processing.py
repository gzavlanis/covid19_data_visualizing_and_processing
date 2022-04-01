from pandas import read_csv, DataFrame, concat
from matplotlib import pyplot
import seaborn as sb

print('In this session we will use pandas,matplotlib and seaborn to visualize data about corona virus cases and deaths.')
print('Data collected from the website https://www.ecdc.europa.eu/en/covid-19/data in CSV.')

# import data and print some of them
data= read_csv('covid19_data.csv', header= 0,index_col= 0, parse_dates= True, squeeze= True)
print(data.head())

# we keep only the data refer to country of Greece and print some of them
isGreece= data['countriesAndTerritories']== 'Greece'
dataGreece= data[isGreece]
print(dataGreece.head())

# plot corona virus cases and deaths daily
dataGreece.loc['26/2/2020':'22/3/2022'].plot(y='cases')
pyplot.title('Daily corona virus cases from February 2020 to March 2022 for Greece')
pyplot.grid()
pyplot.show()
dataGreece.loc['26/2/2020':'22/3/2022'].plot(y='deaths')
pyplot.title('Daily corona virus deaths from February 2020 to March 2022 for Greece')
pyplot.grid()
pyplot.show()

# create groups based on every year of cases
is2020= dataGreece['year']== 2020
data2020= dataGreece[is2020]
print(data2020.head())
is2021= dataGreece['year']== 2021
data2021= dataGreece[is2021]
print(data2021.head())
is2022= dataGreece['year']== 2022
data2022= dataGreece[is2022]
print(data2022.head())

# plot data for every year for cases and deaths
data2020.plot(y= 'cases')
pyplot.title('Corona virus daily cases for 2020')
pyplot.grid()
pyplot.show()

data2020.plot(y= 'deaths')
pyplot.title('Corona virus daily deaths for 2020')
pyplot.grid()
pyplot.show()

data2021.plot(y= 'cases')
pyplot.title('Corona virus daily cases for 2021')
pyplot.grid()
pyplot.show()

data2021.plot(y= 'deaths')
pyplot.title('Corona virus daily deaths for 2021')
pyplot.grid()
pyplot.show()

data2022.loc[:'22/3/2022'].plot(y= 'cases')
pyplot.title('Corona virus daily cases for 2022')
pyplot.grid()
pyplot.show()

data2022.loc[:'22/3/2022'].plot(y= 'deaths')
pyplot.title('Corona virus daily deaths for 2022')
pyplot.grid()
pyplot.show()

# make a comparison between August of 2020 and August 2021 for cases and deaths
# create data
isAugust2020= (dataGreece['month']== 8) & (dataGreece['year']== 2020)
August2020= dataGreece[isAugust2020]
print(August2020.head())
isAugust2021= (dataGreece['month']== 8) & (dataGreece['year']== 2021)
August2021= dataGreece[isAugust2021]
print(August2021.head())

# plot data using seaborn for cases
plotData= concat([August2020, August2021], axis= 0, keys= ['August2020', 'August2021']).reset_index()
plotData= plotData.rename(columns= {'level_0': 'Year', 'level_1': 'Day'})
sb.lineplot(data= plotData, x= 'day', y= 'cases', hue= 'year', palette= ['r', 'b'], linewidth= 1.5)
pyplot.title('Corona virus cases of August 2020 vs August 2021')
pyplot.grid()
pyplot.show()

# plot data using seaborn for deaths
sb.lineplot(data= plotData, x= 'day', y= 'deaths', hue= 'year', palette= ['r', 'g'], linewidth= 1.5)
pyplot.title('Corona virus deaths of August 2020 vs August 2021')
pyplot.grid()
pyplot.show()

# create a histogram of data
dataGreece.loc['26/2/2020':'22/3/2022'].hist(column= 'cases', grid= True, color= '#86bf91', rwidth= 0.9)
pyplot.title('Histogram of corona virus cases')
pyplot.show()
dataGreece.loc['26/2/2020':'22/3/2022'].hist(column= 'deaths', grid= True, color= 'red', rwidth= 0.9)
pyplot.title('Histogram of corona virus deaths')
pyplot.show()

# create an excel file with data for Greece
df= DataFrame(dataGreece)
print(df)
df.to_excel(r'corona_virus_Greece.xlsx', sheet_name= 'Data for Greece', index= False)

