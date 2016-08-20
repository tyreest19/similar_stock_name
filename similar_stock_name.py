from difflib import SequenceMatcher

def similar_stock_name_checker(stock_name, similar_stock_name):
    """Takes a stockname and detrimines if similar name is similar if its above 70% similar it appends
    to a file."""
    if SequenceMatcher(None, stock_name, similar_stock_name).ratio() >= 0.70:
       file_with_stored_names = open('similar_stock_names.txt', 'a')
       file_with_stored_names.write('{} similar names are {}'.format(stock_name,similar_stock_name))


if __name__ == '__main__':
    stock_name = input('stock name: ')
    suggest_name = input('similar name: ')
    print(similar_stock_name_checker(stock_name, suggest_name))













