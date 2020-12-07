import bs4
import requests
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from stores.bestbuy import Bestbuy
from stores.newegg import Newegg
from stores.microcenter import MicroCenter
from stores.walmart import Walmart
from stores.adorama import Adorama
from stores.bhphotovideo import BHPhotoVideo
from stores.target import Target


try:
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    opts.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36")
    opts.set_preference("geo.enable", True)

    browser = webdriver.Firefox(options=opts)

    file = open('urls.txt')
    list = file.readlines()
    inStockList = {}

    for url in list:
        url = url.replace('\n', '')
        if ('bestbuy' in url):
            site = Bestbuy(url)
        elif ('newegg' in url):
            site = Newegg(url)
        elif ('walmart' in url):
            site = Walmart(url)
        elif ('microcenter' in url):
            site = MicroCenter(url)
        elif ('adorama' in url):
            site = Adorama(url)
        elif ('bhphotovideo' in url):
            site = BHPhotoVideo(url)
        elif ('target' in url):
            site = Target(url)

        if (site.checkInventory(url, browser)):
            inStockList[site.storeName] = site.url

    browser.close()
    browser.quit()

    print("****************************************")
    if (len(inStockList) == 0):
        print("All OOS")
    else:
        print(inStockList)

except Exception as exc:
    print('Error: %s' % (exc))
