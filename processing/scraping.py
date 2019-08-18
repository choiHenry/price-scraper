import requests
from processing import utils
import pandas as pd
from bs4 import BeautifulSoup

dfs = []
for i in range(1970, 2016):
    url='https://www.usagold.com/reference/silverprices/{}.html'.format(i)
    #Create a handle, page, to handle the contents of the website
    res = requests.get(url)
    #Store the contents of the website under doc
    soup = BeautifulSoup(res.text, "html.parser")
    #Parse data that are stored between <tr>..</tr> of HTML
    div = soup.findAll("div", attrs = {"id":"quotes"})

    table = div[0].findAll("table")
    rows = table[0].findAll('tr')

    dates = []
    prices = []

    for tr in rows[1:]:
        cols = tr.findAll('td')
        dates.append(cols[0].get_text().strip())
        prices.append(cols[1].get_text().strip())

    #print(dates)
    #print(prices)
    data = {'Date': dates, 'US dollar': prices}
    df = pd.DataFrame(data=data)
    dfs.append(df)

for i in range(2016, 2017):
    url='https://www.usagold.com/reference/silverprices/{}B.html'.format(i)
    #Create a handle, page, to handle the contents of the website
    res = requests.get(url)
    #Store the contents of the website under doc
    soup = BeautifulSoup(res.text, "html.parser")
    #Parse data that are stored between <tr>..</tr> of HTML
    div = soup.findAll("div", attrs = {"id":"quotes"})

    table = div[0].findAll("table")
    rows = table[0].findAll('tr')

    dates = []
    prices = []

    for tr in rows[1:]:
        cols = tr.findAll('td')
        dates.append(cols[0].get_text().strip())
        prices.append(cols[1].get_text().strip())

    #print(dates)
    #print(prices)
    data = {'Date': dates, 'US dollar': prices}
    df = pd.DataFrame(data=data)
    dfs.append(df)

for i in range(2017, 2020):
    url='http://usagold.com/reference/prices/silverhistory.php?ddYears={}'.format(i)
    #Create a handle, page, to handle the contents of the website
    res = requests.get(url)
    #Store the contents of the website under doc
    soup = BeautifulSoup(res.text, "html.parser")
    #Parse data that are stored between <tr>..</tr> of HTML
    div = soup.findAll("div", attrs = {"id":"quotes"})

    table = div[0].findAll("table")
    rows = table[0].findAll('tr')

    dates = []
    prices = []

    for tr in rows[1:]:
        cols = tr.findAll('td')
        dates.append(cols[0].get_text().strip())
        prices.append(cols[1].get_text().strip())

    #print(dates)
    #print(prices)
    data = {'Date': dates, 'US dollar': prices}
    df = pd.DataFrame(data=data)
    dfs.append(df)

dfs.reverse()
df = utils.concat_n_dfs(dfs)
df['Date'] = pd.to_datetime(df['Date'])
print(df)
utils.pickle_object(df, '../data/XAGUSD.pkl')
df.to_csv('../data/XAGUSD.csv')