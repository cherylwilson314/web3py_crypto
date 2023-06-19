from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from web3 import Web3
import time
import selenium_metamask_automation as metamask

driver_path ="C:/Users/wanpc/Desktop/selenium/chromedriver.exe"
metamask_url = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html"
goplus_url = "https://linea.gopluslabs.io/"
meta_pass = "simplejazz1994"

options = Options()
service = Service(executable_path=driver_path)

options.add_experimental_option("detach", True)
options.add_argument("user-data-dir=C:/Users/wanpc/AppData/Local/Google/Chrome/User Data/")
path = '//*[@id="app-content"]/div/div[1]/div/div[2]/div/div/span'

for i in range(28,29):
    options.add_argument('--profile-directory=Profile %s' %(i))
    driver = webdriver.Chrome(service=service, options=options)

    #login metamask
    driver.get(metamask_url)
    time.sleep(3)
    element = driver.find_element(by=By.ID, value='password')
    element.send_keys(meta_pass)
    element.send_keys(Keys.ENTER)

    time.sleep(3)

    #choose linea network
    path = '//*[@id="app-content"]/div/div[1]/div/div[2]/div/div/span'
    network = driver.find_element(by=By.XPATH, value=path)
    network.click()

    time.sleep(2)

    desired_network = driver.find_element(by=By.XPATH, value="//span[contains(text(),'Linea Goerli test network')]")
    desired_network.click()
    time.sleep(3)
#///
    driver.get(goplus_url)
    time.sleep(20)
    driver.find_element(by=By.CLASS_NAME, value='mark').click()
    time.sleep(20)

    #connect
    metamask.connectToWebsite()




    # path = '//*[@id="app-content"]/div/div[1]/div/div[2]/div/div/span'
    # network = driver.find_element(by=By.XPATH, value=path)
    # net = Select(network)
    # net.select_by_visible_text("Linea Goerli test network")
    # login = driver.find_element(by=By.CLASS_NAME, value="unlock-page")
    # login.click()
    # time.sleep(2)
    driver.quit()
