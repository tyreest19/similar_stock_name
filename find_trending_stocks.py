from bs4 import BeautifulSoup
import urllib.request

def find_trending_stocks():
    """Finds trending stock names from marketwatch.com/newsviewer"""
    stock_news_website = urllib.request.urlopen('http://www.marketwatch.com/newsviewer').read() # gets httml from the site
    stock_news_website_scrapper = BeautifulSoup(stock_news_website, 'html.parser') # parses sites html
    stock_website_text = stock_news_website_scrapper.findAll(text=True) # grabs text from parse html
    for words in stock_website_text:
        if  3 <= len(words) <= 5 and str(words).isupper() == True:
            print(words) # prints out words that are stock names




if __name__ == '__main__':
    find_trending_stocks()
























