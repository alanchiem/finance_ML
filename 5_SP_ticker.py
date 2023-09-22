# BeautifulSoup is a web-scraping library
import bs4 as bs
# Pickle serializes any python obj, which basically saves any object
# We can save the S&P500 list so we don't have to go back to wikipedia every time
import pickle 
import requests 

def save_sp500_tickers():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(url)
    soup = bs.BeautifulSoup(response.text, 'lxml')
    # right-click and view source
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    # we dont want to include the header row
    for row in table.findAll('tr')[1:]: 
        # we want 1st col (ticker), 2nd col would be (company name)
        ticker = row.findAll('td')[0].text.strip()  # strip removes the white space
        tickers.append(ticker)
    # write bytes
    with open("sp500tickers.pickle", "wb") as f: 
        pickle.dump(tickers, f)

    # print(tickers)

    return tickers

save_sp500_tickers()