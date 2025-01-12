# Basics of Data Analysis with Pandas
import pandas as pd
df = pd.read_csv('adult.data.csv')

race_count = df['race'].value_counts()
print(race_count)

average_age_men = df[df['sex'] == 'Male']['age'].mean()
print(f"\nThe average age of men is {average_age_men:.2f}%")

total = df['education'].count()
bachelors_count = df[df['education'] == 'Bachelors']['education'].count()
bachelors_percentage = (bachelors_count / total) * 100
print(f"\nThe percentage of people who have a Bachelor's degree is { bachelors_percentage:.2f}%")


gher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]['education']
higher_education = gher_education.count()


higher_education_rich = df[
    (df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & 
    (df['salary'] == '>50K')
].shape[0]


perc_adv = (higher_education_rich / higher_education) * 100
print(f"\nPercentage of people with advanced education who make more than 50K: {perc_adv:.2f}%")


low_edu = total - higher_education
low_sal = df[df['salary'] == '>50K'].shape[0] - higher_education_rich
perc_low = (low_sal / low_edu) * 100
print(f"\nPercentage of people with lower education earning more than 50K: { perc_low:.2f}%")


minimum_hours_per_week = df['hours-per-week'].min()
print(f"\nThe minimum number of hours a person works per week is {minimum_hours_per_week}")

total_peop_min_hr = df[df['hours-per-week'] == minimum_hours_per_week]['hours-per-week'].count()
high_Sal = df[(df['salary'] == '>50K') & (df['hours-per-week'] == minimum_hours_per_week)].shape[0]
percentage = (high_Sal / total_peop_min_hr) * 100
print(f"\nThe percentage of people working minimum hours but earning >50K is {percentage:.2f}%")


numb_country = df['native-country'].nunique()

total_count = df.groupby('native-country')['salary'].count()
greater_50k_count = df[df['salary'] == '>50K'].groupby('native-country')['salary'].count()

# Combine the results into a DataFrame
country_stats = pd.DataFrame({
    'total': total_count,
    '>50K': greater_50k_count
})


country_stats['percentage'] = (country_stats['>50K'] / country_stats['total']) * 100
print(country_stats)


highest_percentage_country = country_stats['percentage'].idxmax()
highest_percentage = country_stats['percentage'].max()
print(f"\nThe country with the highest percentage of people earning >50K is {highest_percentage_country} with {highest_percentage:.2f}%.")


india_high_earners = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
most_popular_occupation = india_high_earners['occupation'].mode()[0]
print(f"\nThe most popular occupation for those who earn >50K in India is {most_popular_occupation}.")
