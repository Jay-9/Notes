import requests     # from urllib.request import urlopen
import pandas
from bs4 import BeautifulSoup


def get_web_info(the_stocks):
    the_url = 'http://quote.eastmoney.com/'
    for the_stock in the_stocks:
        the_stock_info = requests.get(the_url + the_stock)
        return the_stock_info.text


def info_collect(the_stock_info_text):
    one_stock_all_info = []

    the_soup = BeautifulSoup(the_stock_info_text, 'lxml')
    # print(the_soup.prettify())  # 结构化本地html

    stock_name = the_soup.select('#name')[0].get_text()    # 股票名称
    # 1. <class 'bs4.element.ResultSet'> 是字典外套了一个列表  textPid = pid[0]
    # 2. <class 'bs4.element.Tag'> print(textPid.get_text())
    one_stock_all_info.append(stock_name)

    stock_total_market_value = the_soup.select('#cwzbDataBox > tr:nth-child(1) > td:nth-child(2)')[0].get_text()
    one_stock_all_info.append(stock_total_market_value)

    return one_stock_all_info


def info_analysis(the_soup_prettify, ):
    stock_columns = []
    stock_index = ['股票名称', '总市值', '净资产', '净利润', '市盈率(动)', '市净率', '毛利率', '净利率', 'ROE']

    all_stock_final_info = pandas.DataFrame(index=stock_index)

    # for stock_column in stock_columns:
    #     all_stock_final_info[stock_column] = the_one_stock_all_info
    # print(all_stock_final_info)

if __name__ == '__main__':
    stocks = ['sh601929.html']

    stock_info_text = get_web_info(stocks)
    soup_prettify = info_collect(stock_info_text)
    # info_analysis(soup_prettify)