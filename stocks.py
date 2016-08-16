from googlefinance import getQuotes
import json
# in the requirement.txt add in  demjson
def get_stock_information(stock_name):
    """returns a stocks:
    ExtHrsLastTradeDateTimeLong,
    Dividend,
    LastTradeTime,
    PreviousClosePrice,
    LastTradeSize,
    LastTradeDateTimeLong,
    StockSymbol,
    LastTradeDateTime,
    ID,
    ExtHrsChangePercent,
    ExtHrsLastTradePrice,
    ChangePercent,
    Index,
    LastTradeWithCurrency,
    LastTradePrice,
    Yield,
    ExtHrsChange,
    ExtHrsLastTradeWithCurrency.
    of any given NASDAQ stock
    """
    return (json.dumps(getQuotes(stock_name)[0], indent=2))
















