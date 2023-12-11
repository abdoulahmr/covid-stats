from covid import Covid
import matplotlib.pyplot as plt


covid = Covid()

#list of countries are in list of dictionary form
countries = covid.list_countries()

#change the list in the dictionary form
country_list = {i['name']:i for i in countries}

#show the names of country
def show_country_list():
    num = 0
    for name in country_list.keys():
         num += 1
         print(f'{num}- {name}')
    show_data()

#showing the data
def show_data():
    country = input("\nEnter your country name: ")
    data = covid.get_status_by_country_name(country)
    cases = {
        key : data[key]
        for key in data.keys() & {"confirmed","active","deaths","recovered"}}
    pos, val = list(cases.keys()), list(cases.values())
    print(cases)
    plt.title(country)
    plt.bar(pos, val)
    plt.show()

a = input('\nWant to see the list of countries ? (Y/N) : ')
if a == 'y' or a == 'Y' :
    show_country_list()
else:
    show_data()
