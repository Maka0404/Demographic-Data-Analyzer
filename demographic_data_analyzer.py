import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    df_men = df[df['sex'] == 'Male']
    average_age_men = round(df_men['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    df_bachelors = df[df['education'] == 'Bachelors']

     # Contar el número de personas con un título de Bachelor
    bachelors_count = df_bachelors.shape[0]

    # Contar el número total de personas
    total_count = df.shape[0]

    # Calcular el porcentaje de personas con un título de Bachelor
    percentage_bachelors = round((bachelors_count / total_count * 100) if total_count > 0 else 0, 1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    df_advanced_education = df[df['education'].isin(advanced_education)]
    df_no_advanced_education = df[~df['education'].isin(advanced_education)]

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df_advanced_education.shape[0]
    lower_education = df_no_advanced_education.shape[0]

    advanced_count = df_advanced_education[df_advanced_education['salary'] == '>50K'].shape[0]
    no_advanced_count = df_no_advanced_education[df_no_advanced_education['salary'] == '>50K'].shape[0]

    # percentage with salary >50K
    higher_education_rich = round((advanced_count / higher_education * 100) if total_count > 0 else 0, 1)
    lower_education_rich = round((no_advanced_count / lower_education * 100) if total_count > 0 else 0, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    minimun_hours_workers = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = minimun_hours_workers.shape[0]
    rich_workers = minimun_hours_workers[minimun_hours_workers['salary'] == '>50K'].shape[0]



    rich_percentage = round((rich_workers / num_min_workers * 100) if total_count > 0 else 0, 1)

    # What country has the highest percentage of people that earn >50K?

    normal_counts = df['native-country'].value_counts()

    most_rich = df[df['salary'] == '>50K']
    
    most_rich_counts = most_rich['native-country'].value_counts()

    porcentaje =  (most_rich_counts / normal_counts) * 100

    

    highest_earning_country = porcentaje.idxmax()
    highest_earning_country_percentage = round(porcentaje.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.

    df_india = df[df['native-country'] == 'India']

    df_india_rich = df_india[df_india['salary'] == '>50K']

    response = df_india_rich['occupation'].value_counts()

    top_IN_occupation = response.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
