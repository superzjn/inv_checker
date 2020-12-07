from abc import ABC, abstractmethod


class Store(ABC):
    def __init__(self, name, url):
        self.storeName = name
        self.OOS_MSG = OOS_MSG
        self.url = url

    @abstractmethod
    def checkInventory(self, url):
        pass

    def findTitle(self, browser):
        return browser.title

    def printUrl(self, url):
        print('Checking %s' % url)

    def printOosMsg(self, browser):
        print(self.storeName + " OOS XXX " + self.findTitle(browser))

    def printInStoreMsg(self, browser):
        print(self.storeName + " *** HAS " + self.findTitle(browser))
