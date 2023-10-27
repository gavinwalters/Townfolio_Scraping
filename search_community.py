from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# stop browser from closing after run
options = Options()
prefs = {'download.default_directory' : '/Users/gavin/Documents/Townfolio data'}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service =  Service(ChromeDriverManager().install()), options=options)

# Open townfolio in Chrome
driver.get("https://townfolio.co/find-community-data?country=CA&region=NL&population=all&keyword=")
driver.maximize_window()

#search community by input

community=input('Please enter a community to search: ')

search = driver.find_element(By.NAME, "query").send_keys(community)
driver.find_element("xpath","//button[contains(text(), 'Search')]").click()
driver.find_element("xpath","//a[contains(text(), \""+community+"\")]").click()






