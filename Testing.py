import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options= chrome_options)

driver.get('https://ytmp3.cc/67cdb/')

driver.find_element("xpath",'/html/body/div[2]/div[1]/div[1]/form/input[1]').send_keys(str('https://www.youtube.com/watch?v=KsHuVerbpLg&list=FLwrjvhJmkhsJCFiwt4f_AHw&index=1')) 

driver.find_element("xpath",'/html/body/div[2]/div[1]/div[1]/form/input[2]').click()