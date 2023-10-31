from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pandas as pd

def searchTown(driver, community):

    # Open townfolio in Chrome
    driver.get("https://townfolio.co/find-community-data?country=CA&region=NL&population=all&keyword=")
    driver.maximize_window()

    #search community by input


    search = driver.find_element(By.NAME, "query").send_keys(community)
    driver.find_element("xpath","//button[contains(text(), 'Search')]").click()
    driver.find_element("xpath","//a[contains(text(), \""+community+"\")]").click()
    # townLink = driver.find_element("xpath","//a[contains(text(), \""+community+"\")]")
    # if townLink.Exists():
    #     driver.find_element("xpath","//a[contains(text(), \""+community+"\")]").click()
    # else:
    #     print("Sorry that community wasn't found, try again!")
    #     community=input('Please enter a community to search: ')
    #     search = driver.find_element(By.NAME, "query").send_keys(community)
    #     driver.find_element("xpath","//button[contains(text(), 'Search')]").click()
    

def DLExcel(driver):

        # search all a tags in dom
        links = driver.find_elements("xpath", "//a")
        for link in links:
            print('DL')
            # If link is Download button, click it
            if "Download" in link.get_attribute("innerHTML"):
                link.click()
                print("click")

            
                buttons = driver.find_elements("xpath", "//button")
                for button in buttons:
                    # Download excel file
                    if "Excel" in button.get_attribute("innerHTML"):
                        button.click()
                        print("button")
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
            print(file)
            
            print(pd.read_excel(filepath))



def main():
    #input community

    community=input('Please enter a community to search: ')
    #def options and driver
        # stop browser from closing after run
    options = Options()
    prefs = {'download.default_directory' : '/Users/gavin/Documents/Townfolio data/' + community}
    options.add_experimental_option('prefs', prefs)
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service =  Service(ChromeDriverManager().install()), options=options)
    
    searchTown(driver, community)
    time.sleep(5.5)    # Pause 5.5 seconds
    DLExcel(driver)
    driver.find_element("xpath", "//span[contains(text(), 'Labour Force')]").click()
    time.sleep(5.5)
    DLExcel(driver)
    driver.find_element("xpath", "//span[contains(text(), 'Taxation')]").click()
    time.sleep(5.5)
    DLExcel(driver)
    driver.find_element("xpath", "//span[contains(text(), 'Quality of Life')]").click()
    time.sleep(5.5)
    DLExcel(driver)
    driver.find_element("xpath", "//span[contains(text(), 'Real Estate')]").click()
    time.sleep(5.5)
    DLExcel(driver)
    driver.find_element("xpath", "//span[contains(text(), 'Transportation')]").click()
    time.sleep(5.5)
    DLExcel(driver)
    driver.find_element("xpath", "//span[contains(text(), 'Education')]").click()
    time.sleep(5.5)
    DLExcel(driver)
    driver.find_element("xpath", "//span[contains(text(), 'Utilities')]").click()
    time.sleep(5.5)
    DLExcel(driver)
    driver.find_element("xpath", "//span[contains(text(), 'Companies')]").click()
    time.sleep(5.5)
    DLExcel(driver)
    readData(community)


if __name__ == "__main__":
    main()