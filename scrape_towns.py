from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def townList():
    # stop browser from closing after run
    options = Options()
    prefs = {'download.default_directory' : '/Users/gavin/Documents/Townfolio data'}
    options.add_experimental_option('prefs', prefs)
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service =  Service(ChromeDriverManager().install()), options=options)
    driver.get("https://municipalnl.ca/about/municipal-directory/")

    towns = driver.find_elements("xpath", "//h3")
    # print(type(towns))
    town_list = []
    for town in towns:
        town_list.append(town.get_attribute("innerHTML"))
        # print(town.get_attribute("innerHTML"))
    driver.quit()
    return town_list
