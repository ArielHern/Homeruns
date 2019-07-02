import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/List_of_Major_League_Baseball_annual_home_run_leaders"
years = list(map(str, range(1901, 2018)))

# fetches the webpage from the url

r = requests.get(url)
page_soup = soup(r.text, 'html.parser')

# American l
table_american = page_soup.find_all('table')[1]
df_american = pd.read_html(str(table_american))[0]
years_a = df_american['Year']
homeruns_a = df_american['HR']

# National le
national_table = table = page_soup.find_all('table')[2]
df_national = pd.read_html(str(national_table))[0]
years_n = df_national['Year']
homeruns_n = df_national['HR']

# graph
fig, axes = plt.subplots()
axes.bar(years_n, homeruns_n, label='Natial League')
axes.bar(years_a, homeruns_a, label='American League')

axes.legend(loc='upper left', frameon=False)
plt.show()
