from bs4 import BeautifulSoup
import urllib.request

def find_trending_stocks():
    """Finds trending stock names from marketwatch.com/newsviewer and returns a list of trending stocks"""
    stock_news_website = urllib.request.urlopen('http://www.marketwatch.com/newsviewer').read() # gets httml from the site
    stock_news_website_scrapper = BeautifulSoup(stock_news_website, 'html.parser') # parses sites html
    stock_website_text = stock_news_website_scrapper.findAll(text=True) # grabs text from parse html
    list_of_trending_stocks = [] # A list of the trending stocks.
    for stock_names in stock_website_text:
        if  3 <= len(stock_names) <= 5 and str(stock_names).isupper() == True:
            list_of_trending_stocks.append(stock_names) # appending stock names to trending stock list
    return  list_of_trending_stocks





























