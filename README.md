# data-preprocessing

get gold and silver price data from web

## gold data

You can check source data [here](https://www.gold.org/goldhub/data/gold-prices).
I've downloaded it and parsed it with pandas and finally converted it to "data/gold_data.csv".
The codes are in the file 'processing/process.py'.
The columns of gold data consist of ['Date', 'US dollar', 'Euro', 'Korean dollar'].

## silver data

I've scraped silver/usd data [here](https://usagold.com/reference/prices/silverhistory.php?ddYears=2019) and processed it.
You can check scraping and processing code in 'processing/scraping.py'

