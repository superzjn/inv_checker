import bs4
import requests
import time
import threading
import concurrent.futures

from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from stores.bestbuy import Bestbuy
from stores.newegg import Newegg
from stores.microcenter import MicroCenter
from stores.walmart import Walmart
from stores.adorama import Adorama
from stores.bhphotovideo import BHPhotoVideo
from stores.target import Target


def setup_browser():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    opts.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36")
    opts.set_preference("geo.enable", True)
    browser = webdriver.Firefox(options=opts)
    return browser


def check_site(url, in_stock_list):
    browser = setup_browser()
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

    try:
        if (site.checkInventory(url, browser)):
            in_stock_list[site.storeName] = site.url
    except Exception as exc:
        print('Error: %s' % (exc))
    finally:
        browser.close()
        browser.quit()


def check_all(list, in_stock_list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        to_do = []
        for site in list:
            future = executor.submit(check_site, site, in_stock_list)
            to_do.append(future)
        for future in concurrent.futures.as_completed(to_do):
            future.result()


def main():
    start_time = time.perf_counter()

    file = open('urls.txt')
    site_list = file.readlines()
    in_stock_list = {}

    check_all(site_list, in_stock_list)

    print("****************************************")
    if (len(in_stock_list) == 0):
        print("All OOS")
    else:
        print(in_stock_list)

    end_time = time.perf_counter()
    print('Checked {} sites in {} seconds'.format(
        len(site_list), end_time - start_time))


if __name__ == '__main__':
    main()
