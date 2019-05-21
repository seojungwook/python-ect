from selenium import webdriver
import time

if __name__ == "__main__":
    driver = webdriver.Edge()
    url = "http://www.naver.com"
    driver.get(url)
    elem = driver.find_element_by_id("id")
    elem.send_keys("id") 
    elem = driver.find_element_by_id("pw") 
    elem.send_keys("passward") 
    elem.submit()
    
    time.sleep(1)
    elem = driver.find_element_by_id("query") 
    elem.send_keys("naver") 
    elem.submit()
   
