from bs4 import BeautifulSoup
from urllib.request import urlopen
from sqlalchemy import create_engine

import pandas
import re

html_date = urlopen('https://en.wikipedia.org/wiki/List_of_cities_in_Germany_by_population')
page = BeautifulSoup(html_date, features="html.parser")

names_city_and_states = [city.find('a').text for city in page.find_all('td', {'align': 'left', 'valign': None})]

cities = names_city_and_states[::2]
states = names_city_and_states[1::2]

populations = [city.text for city in page.find_all('td', {'style': 'text-align:right;'})]

census_2015 = populations[::3]
census_2011 = populations[1::3]
change_percent = populations[2::3]

array_with_square = [value for state in page.find_all('td') for value in state(text=re.compile('km'))]

land_area = array_with_square[::2]
population_density = array_with_square[1::2]

main_table = pandas.DataFrame(
    [cities, states, census_2015, census_2011, change_percent, land_area, population_density]).T
main_table.columns = ['cities', 'states', 'census_2015', 'census_2011', 'change_percent', 'land_area',
                      'population_density']

engine = create_engine('mysql+mysqlconnector://root:1919@127.0.0.1:3306/pandas')

main_table.to_sql(name='pandas', con=engine, if_exists='replace', index=False)
