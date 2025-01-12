# we are writing a program that takes input from user as a list which consit of 9 numbers and converts it into the matirx form using numpy of order 3*3 and perform various operaiotn 
#To calculate mean ,standard deviation,maximum,minimum,variance of each row or column and flattered or whole and displas in proper format as a list using numpy
''' now lets start'''
#import numpy 
'''import numpy as np
#than assign rows and columns
rows=3
cols=3
marrix_siize=rows*cols
#create a function
def calculate():
    #take a input from user
    Data=list(map(int,input(f"Enter a matrix")))'''
import pandas as pd
df=pd.read_csv('adult.data.csv')
race_count=df['race'].value_counts()
print(race_count)

average_age_men=df[df['sex']=='Male']['age'].mean()
print (int(average_age_men))

#calculating percentage
total=df['education'].count()
bachelors_count=df[df['education']=='Bachelors']['education'].count()
bachelors_percentage=(bachelors_count/total)*100
print(bachelors_percentage)


#number of people with advanced eduaction(bachelor,masters,or doctors)
gher_education=df[df['education'].isin(['Bachelors' , 'Masters' , 'Doctorate'])]['education']
higher_education=gher_education.count()
print(higher_education)



#people who make  greater than 50k(advanced eduacation)
higher_salary=df[df['salary']=='>50K']['salary'].count()
print(higher_salary)

# number of people with higher salary with higher education(number of people)
higher_education_rich = df[
    (df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & 
    (df['salary'] == '>50K')
].shape[0]
print("\nNumber of people with higher education earning more than 50K:", higher_education_rich)

#percentage of people with advanced education make more than 50k

perc_adv=(higher_education_rich/higher_education)*100
print(perc_adv)

#percentage of people without advanced education making more than 50k
low_edu=(df['education'].count())-higher_education
low_sal=higher_salary-higher_education_rich
perc_low=(low_sal/low_edu)*100
print("\nNumber of people with lower education earning more than 50K:", perc_low)


#mimimum number of hours a person works per week

minimum_hours_per_week=df['hours-per-week'].min()
print(minimum_hours_per_week)


#percentage of the people who work the minimum number of hours per week have a salary more the  50k
total_peop_min_hr=df[df['hours-per-week']==minimum_hours_per_week]['hours-per-week'].count()
print(total_peop_min_hr)
high_Sal= df[(df['salary']=='>50K') & (df['hours-per-week']==minimum_hours_per_week)].shape[0]
print(high_Sal)
percentage=(high_Sal/total_peop_min_hr)*100
print(percentage,'%')

#what country has the highest percentage of people that earn >50k abd what is tha percentage
numb_country=df['native-country'].nunique()
print(numb_country)

# Calculate total count and '>50K' count for each country
total_count = df.groupby('native-country')['salary'].count()
greater_50k_count = df[df['salary'] == '>50K'].groupby('native-country')['salary'].count()

# Combine the results into a DataFrame
country_stats = pd.DataFrame({
    'total': total_count,
    '>50K': greater_50k_count
})


# Calculate percentage
country_stats['percentage'] = (country_stats['>50K'] / country_stats['total']) * 100
print(country_stats)

# Find the country with the highest percentage
highest_percentage_country = country_stats['percentage'].idxmax()
highest_percentage = country_stats['percentage'].max()

print(f"The country with the highest percentage of people earning >50K is {highest_percentage_country} with {highest_percentage:.2f}%.")
#identify most popular occupation for those who earn >50k
# Filter the DataFrame for individuals earning '>50K' in India
india_high_earners = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]

# Find the most popular occupation
most_popular_occupation = india_high_earners['occupation'].mode()[0]

print(f"The most popular occupation for those who earn >50K in India is {most_popular_occupation}.")
