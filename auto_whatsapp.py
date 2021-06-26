import selenium   #pip install selenium
from selenium import webdriver
import keyboard
import time

######
#NOTE
#Dont run this before changing xpath , orelse it may send messages to other groups
#TimePassCoders


######

driver=webdriver.Chrome(executable_path='C:\\Users\\DELL\\Documents\\webdrivers\\chromedriver.exe')  #Replace this path with the path where you have extracted ur driver
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
driver.implicitly_wait(200)
driver.find_element_by_xpath("//*[@id='pane-side']/div[1]/div/div/div[9]/div/div/div[2]/div[1]/div[1]/span").click()   #change the Xpath
driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]").click()   #Change the Xpath
for i in range(100):
    # keyboard.write(f"{i}\n")
    keyboard.write("{0}.Subscribe timepass coders for more such stuff\n".format(i))
    # time.sleep(1)
    
