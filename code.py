# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
print('Path is: ',path)
#Code starts here
data = pd.read_csv(path)    
data.rename(index=str,columns={'Total':'Total_Medals'},inplace=True)
data.head(10)


# --------------
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer',np.where(data['Total_Summer']==data['Total_Winter'],'Both','Winter'))

better_event = data['Better_Event'].value_counts().first_valid_index()
print('Better event is: ',better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
LastRow = top_countries.shape[0]-1
top_countries = top_countries.iloc[:LastRow]

def top_ten(top_countries,col):
    country_list = top_countries.nlargest(10,col)
    return list(country_list['Country_Name'])

top_10_summer,top_10_winter,top_10 = top_ten(top_countries,'Total_Summer'),top_ten(top_countries,'Total_Winter'),top_ten(top_countries,'Total_Medals')

print('Top 10 in summer is:',top_10_summer)
print('Top 10 in winter is:',top_10_winter)
print('Top 10:',top_10)

top_10_summer_set,top_10_winter_set,top_10_set = set(top_10_summer),set(top_10_winter),set(top_10)
common  = list((top_10_summer_set & top_10_winter_set)&top_10_set)

print('Common elements are: ',common)


# --------------
#Code starts here
summer_df,winter_df,top_df = data[data['Country_Name'].isin(top_10_summer)],data[data['Country_Name'].isin(top_10_winter)],data[data['Country_Name'].isin(top_10)]

plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'])
plt.xlabel('Country Name')
plt.ylabel('Total Winning')
plt.xticks(rotation=90)
plt.show()

plt.bar(winter_df['Country_Name'],winter_df['Total_Winter'])
plt.xlabel('Country Name')
plt.ylabel('Total Winning')
plt.xticks(rotation=90)
plt.show()

plt.bar(top_df['Country_Name'],top_df['Total_Medals'])
plt.xlabel('Country Name')
plt.ylabel('Total Winning')
plt.xticks(rotation=90)
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio'],winter_df['Golden_Ratio'],top_df['Golden_Ratio']  = summer_df['Gold_Summer'].values/summer_df['Total_Summer'].values,winter_df['Gold_Winter']/winter_df['Total_Winter'],top_df['Gold_Total']/top_df['Total_Medals']

summer_max_ratio,summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax()]['Golden_Ratio'],summer_df.loc[summer_df['Golden_Ratio'].idxmax()]['Country_Name']
print('Max value for summer is: ',summer_max_ratio)
print('Country assoicated with max value for summer is: ',summer_country_gold)

winter_max_ratio,winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax()]['Golden_Ratio'],winter_df.loc[winter_df['Golden_Ratio'].idxmax()]['Country_Name']
print('Max value for winter is: ',winter_max_ratio)
print('Country assoicated with max value for winter is: ',winter_country_gold)

top_max_ratio,top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax()]['Golden_Ratio'],top_df.loc[top_df['Golden_Ratio'].idxmax()]['Country_Name']
print('Max value for winter is: ',top_max_ratio)
print('Country assoicated with max value for winter is: ',top_country_gold)


# --------------
#Code starts here
lastRow = data.shape[0]-1
data_1=data.iloc[:lastRow]

data_1['Total_Points'] = 3*data_1['Gold_Total']+2*data_1['Silver_Total']+data_1['Bronze_Total']

most_points,best_country = data_1.loc[data_1['Total_Points'].idxmax()]['Total_Points'],data_1.loc[data_1['Total_Points'].idxmax()]['Country_Name']
print('Most scored points: ',most_points)
print('Country which has scored max points: ',best_country)


# --------------
#Code starts here
best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar()
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


