# Invetory Checker
For hot selling products. Check to see if they are in stock or not.

## Supported Sites
- Target
- Bestbuy
- Newegg
- Walmart
- Microcenter
- Adormama
- BHphotoVideo

## How to Use

Just put the product links you want to check in urls.txt and run checker.py.

For Linux/Mac
Run ./install.sh to install dependencies

## Dependencies

- Python3
- pip3 install requests
- pip3 install beautifulsoup4
- pip3 install selenium
- sudo apt-get install firefox (Linux)
- sudo apt-get install chrome (Optional)

### Setup Selenium

#### Linux/Mac
Download Linux/Mac version geckodriver

1. wget https://github.com/mozilla/geckodriver/releases/
2. chmod +x geckodriver
3. sudo mv geckodriver /usr/local/bin/

#### Windows
Download Windows version geckodriver

1. Download from https://github.com/mozilla/geckodriver/releases/
2. Add the path to geckodriver.exe to environment variable. May just copy it to C:\windows\system32

## Permission Issue on Windows when running in a .bat file

It may have permission issue when trying to access geckodriver.log. There are several ways to handle this.

1. Add the following to the top of the bat file. Thanks to [Here](https://stackoverflow.com/questions/6811372/how-to-code-a-bat-file-to-always-run-as-admin-mode)

    ```bash
    set "params=%*"
    cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )
    ```

2. runas /user:yourAdminAccountName "py.exe E:\inv_checker\checker.py". However, this way you still need to enter the password for the account.
