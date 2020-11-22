# Invetory Checker
For hot selling products. Check to see if they or in stock or not.

## Supported Sites
- Bestbuy
- Newegg
- Walmart
- Microcenter
- Adormama
- BHphotoVideo

## How to Use
Just put the product links in urls.txt and run checker.py.

## Dependencies
- Python3
- pip3 install requests
- pip3 install beautifulsoup4
- pip3 install selenium
- sudo apt-get install firefox

### Setup Selenium
1. wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz
2. tar -xvzf geckodriver*
3. chmod +x geckodriver
4. sudo mv geckodriver /usr/local/bin/