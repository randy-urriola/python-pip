import utils
import read_csv
import charts
import pandas as pd


def run():

    data = read_csv.read_csv('data.csv')
    country = input('Type Country => ')

    result = utils.population_by_country(data, country)
    print(result[0]['Continent'])

    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country'], labels, values)

    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == result[0]['Continent']]

    countries = df['Country'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentages)


if __name__ == '__main__':
    run()
