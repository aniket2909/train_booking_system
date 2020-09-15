import selenium
import time
import urllib.request as u 
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r'C:\Users\anike\webdriver\chromedriver.exe')
driver.maximize_window()

file = open('passengerdata.txt',"r")
# for roll in file: 
# 	print(roll)
# 	driver.get('https://oa.cc.iitk.ac.in/Oa/Jsp/Photo/'+str(roll)+'_0.jpg')
# 	# id_box = driver.find_element_by_id('mat-input-1')
# 	# id_box.send_keys('170111')
# 	images = driver.find_elements_by_tag_name('img')
# 	for image in images:
# 	    c = image.get_attribute('src')
# 	    u.urlretrieve(c, tosave+str(roll[0:6])+"_0.jpg")

driver.get('https://www.irctc.co.in/nget/train-search')



try:
    myElem = WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Journey Date(dd-mm-yyyy)*']")))
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")

time.sleep(1)    

a = driver.find_element_by_xpath("//input[@placeholder='From*']") 
a.send_keys('LUCKNOW NR - LKO') 

a = driver.find_element_by_xpath("//input[@placeholder='To*']") 
a.send_keys('SAHARANPUR - SRE')

a = driver.find_element_by_xpath("//input[@placeholder='Journey Date(dd-mm-yyyy)*']") 
a.send_keys('\b\b\b\b\b\b\b\b\b\b02-02-2020')
time.sleep(1)
 

driver.find_element_by_xpath('//a[@aria-label="Click here to Login in application"]').click()

a = driver.find_element_by_xpath("//input[@id='userId']")
a.send_keys('Dragon64')
time.sleep(0.5)

a = driver.find_element_by_xpath("//input[@id='pwd']")
a.send_keys('Joker123')










try:
    myElem = WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.XPATH, "//label[@class = 'ng-tns-c13-13 ui-dropdown-label ui-inputtext ui-corner-all ng-star-inserted']")))
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")


time.sleep(0.4)
driver.find_element_by_xpath("//label[@class = 'ng-tns-c13-13 ui-dropdown-label ui-inputtext ui-corner-all ng-star-inserted']").click()
driver.find_element_by_xpath("//span[contains(text(),'TATKAL')]").click()
# driver.find_element_by_xpath("//*[@id='divMain']/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[4]/div[4]/div[1]/app-train-avl-enq/div[2]/div[1]/div[3]/div[1]/form/select").click()
# driver.find_element_by_xpath('//*[@id="divMain"]/div/app-train-list/div/div[5]/div/div[2]/div[1]/div[2]/div[4]/div[4]/div[1]/app-train-avl-enq/div[2]/div[1]/div[3]/div[1]/form/select/option[1]').click()







try:
    myElem = WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[6]/div/button[2]')))
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")


time.sleep(2)
a = driver.find_element_by_xpath('//*[@id="psgn-name"]')
a.send_keys('Rajeev Sharma')
time.sleep(1)

a = driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[3]/div[1]/div/div[2]/app-passenger/div/div[1]/div[2]/input')
a.send_keys('51')
time.sleep(0.1)

driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[3]/div[1]/div/div[2]/app-passenger/div/div[1]/div[3]').click()
time.sleep(0.05)
driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[3]/div[1]/div/div[2]/app-passenger/div/div[1]/div[3]/select/option[2]').click()
time.sleep(0.05)
driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[3]/div[1]/div/div[2]/app-passenger/div/div[1]/div[4]/select').click()
time.sleep(0.05)
driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[3]/div[1]/div/div[2]/app-passenger/div/div[1]/div[4]/select/option[2]').click()
time.sleep(0.05)
driver.find_element_by_xpath('//*[@id="divMain"]/div/app-passenger-input/div[5]/form/div/div[1]/div[6]/div/button[2]').click()








try:
    myElem = WebDriverWait(driver, 1000000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-tabpanel-3"]/div[2]/div[1]/div/div')))
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")



time.sleep(2)
driver.find_element_by_xpath('//*[@id="divMain"]/div/app-payment-options/div/div[4]/div/div[3]/div[2]/div[1]/app-payment/div[4]/div/form/p-tabview/div/ul/li[4]').click()
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="ui-tabpanel-3"]/div[2]/div[1]/div/div').click()
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="ui-tabpanel-3"]/div[2]/div[1]/div/div').click()
time.sleep(0.1)
