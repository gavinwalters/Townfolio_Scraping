from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import os
import psutil
import pandas as pd
import scrape_towns

def initDriver(community):

    #def options and driver
    options = Options()
    prefs = {'download.default_directory' : '/Users/gavin/Documents/Townfolio data/' + community}
    options.add_experimental_option('prefs', prefs)
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--start-maximized")
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    # stop browser from closing after run
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service =  Service(ChromeDriverManager().install()), options=options)
    return driver
def searchTown(community):
    
    #input community

    # community=input('Please enter a community to search: ')

    driver = initDriver(community)

    # Open townfolio in Chrome
    driver.get("https://townfolio.co/find-community-data?country=CA&region=NL&population=all&keyword=")
    driver.maximize_window()

    #search community by input


    clearSearch = driver.find_element(By.NAME, "query").clear()
    search = driver.find_element(By.NAME, "query").send_keys(community)
    driver.find_element("xpath","//button[contains(text(), 'Search')]").click()
    # driver.find_element("xpath","//a[contains(text(), \""+community+"\")]").click()
    # selectTown(driver, community)
    return driver
    
def selectTown(driver, community):
    townLink = driver.find_elements("xpath","//a[contains(text(), \""+community+"\")]")
    if len(townLink) > 0:
        driver.find_element("xpath","//a[contains(text(), \""+community+"\")]").click()
        return
    else:
        print("Sorry " + community + " wasn't found, on to the next!")
        driver.quit()
        PROCNAME = "chromedriver"
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == PROCNAME:
                proc.kill()
        print("driver quit")
        # driver, community = searchTown()
        # print("new search done")
        return True

def DLExcel(driver):

        # search all a tags in dom
        links = driver.find_elements("xpath", "//a")
        for link in links:
            # print('DL')
            # If link is Download button, click it
            if "Download" in link.get_attribute("innerHTML"):
                link.click()
                # print("click")

            
                buttons = driver.find_elements("xpath", "//button")
                for button in buttons:
                    # Download excel file
                    if "Excel" in button.get_attribute("innerHTML"):
                        button.click()
                        print("DL Excel")
                        close = driver.find_element(By.CLASS_NAME, "tf-dialog__actions")
                        close.click()

def readData(community):
    directory = '/Users/gavin/Documents/Townfolio data/' + community
    path = r'/Users/gavin/Documents/Townfolio data/' + community
    file_name = 'data.txt'
    for file in os.listdir(directory):
        if file.endswith('.xlsx'):
            filepath = directory + '/' + file
            with open(os.path.join(path, file_name), 'a') as fp:
                fp.write(os.path.splitext(file)[0]+"\n")
                fp.write(str(pd.read_excel(filepath)) + "\n")
            # print(file)
    print("Data File for " + community + " Created")
            # print(pd.read_excel(filepath))



def main():
    cont = True
    townList = scrape_towns.townList()

    # driver = webdriver.Chrome(service =  Service(ChromeDriverManager().install()))
    # driver.get("driver = webdriver.Chrome(service =  Service(ChromeDriverManager().install())")
    # towns = driver.find_elements("xpath", "//h3")
    # for town in towns:
    #     print(town.get_attribute("innerHTML"))
    # driver.quit()
    skippedList = []
    for town in townList:
        driver = searchTown(town)
        cont = selectTown(driver, town)
        if cont:
            skippedList.append(town)
            print("SKIP")
            continue
        print("NOW SCRAPING "+ town)
        time.sleep(3)    # Pause 5.5 seconds
        # print(driver)
        # DLExcel(driver)
        driver.find_element("xpath", "//span[contains(text(), 'Demographics')]").click()
        time.sleep(1)
        DLExcel(driver)
        driver.find_element("xpath", "//span[contains(text(), 'Labour Force')]").click()
        time.sleep(1)
        DLExcel(driver)
        driver.find_element("xpath", "//span[contains(text(), 'Taxation')]").click()
        time.sleep(1)
        DLExcel(driver)
        driver.find_element("xpath", "//span[contains(text(), 'Quality of Life')]").click()
        time.sleep(1)
        DLExcel(driver)
        driver.find_element("xpath", "//span[contains(text(), 'Real Estate')]").click()
        time.sleep(1)
        DLExcel(driver)
        driver.find_element("xpath", "//span[contains(text(), 'Transportation')]").click()
        time.sleep(1)
        DLExcel(driver)
        driver.find_element("xpath", "//span[contains(text(), 'Education')]").click()
        time.sleep(1)
        DLExcel(driver)
        driver.find_element("xpath", "//span[contains(text(), 'Utilities')]").click()
        time.sleep(1)
        DLExcel(driver)
        driver.find_element("xpath", "//span[contains(text(), 'Companies')]").click()
        time.sleep(1)
        DLExcel(driver)
        readData(town)
        print("DRIVER QUIT")
        driver.quit()
        time.sleep(1)
    
    path = r'/Users/gavin/Documents/Townfolio data/'
    file_name = 'skipped.txt'
    with open(os.path.join(path, file_name), 'a') as fp:
        for town in skippedList:
            fp.write(str(town))


if __name__ == "__main__":
    main()