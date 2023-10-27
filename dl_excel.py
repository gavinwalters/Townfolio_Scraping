from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# stop browser from closing after run
options = Options()
prefs = {'download.default_directory' : '/Users/gavin/Documents/Townfolio data'}
options.add_experimental_option('prefs', prefs)
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service =  Service(ChromeDriverManager().install()), options=options)

# Open townfolio in Chrome
driver.get("https://townfolio.co/nl/whitbourne/demographics")
driver.maximize_window()

# search all a tags in dom
links = driver.find_elements("xpath", "//a")
for link in links:
    print("1")
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