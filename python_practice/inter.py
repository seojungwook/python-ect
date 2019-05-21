# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

#import requests as req
from selenium import webdriver
from datetime import datetime
import codecs
from selenium.common.exceptions import NoSuchElementException,JavascriptException,NoSuchFrameException,NoSuchWindowException,ElementNotVisibleException
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoAlertPresentException


uid = ''
upw = ''


def cdrive():
    url = 'C:\chromedriver_win32\chromedriver.exe'
    
    option = webdriver.ChromeOptions()
    prefs = {'profile.default_content_setting_values': {'cookies' : 1, 'images': 1, 'plugins' : 2, 'popups': 1, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}
    option.add_experimental_option('prefs', prefs)
    #option.add_argument('headless')
    option.add_argument('--disable-gpu')
    #option.add_argument('User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36')
    driver = webdriver.Chrome(url, options=option)
    #driver = webdriver.Chrome(url)
    return driver

def login():
    
    driver.get('https://ticket.interpark.com/Gate/TPLogin.asp?CPage=B&MN=Y&tid1=main_gnb&tid2=right_top&tid3=login&tid4=login')
    driver.find_element_by_name('UID').send_keys(uid)
    driver.find_element_by_name('PWD').send_keys(upw)
    driver.execute_script('login();')
    #driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=19004306#')
    driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=19007017#')
               

def search():
    
#    headers = { 
#            "User-Agent": 
#                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36" 
#                } 
#    s = req.session() 
#    s.headers.update(headers) 
#    
#    for cookie in driver.get_cookies(): 
#        c = {cookie['name']: cookie['value']} 
#        s.cookies.update(c)
#        print(cookie['name'])
#        print(cookie['value'])
#        print("++++++++++++++++++++++++++++++++++")
#    
#    pdata ={'GroupCode' : '19004306',
#            'Tiki' : 'N',
#            'BizCode' : '',
#            'BizMemberCode' : '',
#            'PlayDate' : '',
#            'PlaySeq' : '',
#            'Point': 'N',
#            'SessionId' :'CB64E39F2D704FCE8326B384542F0658', 
#            'SIDBizCode' : 'WEBBR',
#            'FCSNo' : ''
#            
#            }
#    print(driver.session_id)
#    res = s.post('http://poticket.interpark.com/Book/BookMain.asp',data=pdata)
    
    
    try:
        driver.get('http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GoodsCode=19007017#')
        driver.execute_script('fnNormalBooking()')
        
    #    try:
    #        WebDriverWait(driver, 3).until(EC.alert_is_present(),
    #                                       'Timed out waiting for PA creation ' +
    #                                       'confirmation popup to appear.')
    #    
    #        alert = driver.switch_to.alert
    #        alert.accept()
    #        print("alert accepted")
    #    except NoAlertPresentException:
    #        print("no alert")
    #    
        
        driver.switch_to_window(driver.window_handles[1])    
        btntry('javascript:fnBookNoticeShowHide("");')    
        driver.switch_to.frame(driver.find_element_by_name('ifrmBookStep'))
        loop1('20')
        driver.implicitly_wait(2)
        loop2('14시 00분')
        driver.implicitly_wait(2)
        btnclick("//div[@class='contR']",'LargeNextBtn')
        
        
        
        
    except NoSuchElementException or JavascriptException or NoSuchFrameException or NoSuchWindowException:
        print("에러 다시시도를 눌러주세요")
    
    print("화면 전환")
    peakseat()
    

#    delay = 10  # seconds
#    
#    while 1:
#        try:
#            WebDriverWait(driver, delay).until(
#                expected_conditions.visibility_of(
#                    (By.CSS_SELECTOR, ".scrollY")
#                )
#            )
#            print("로딩중")
#        except ElementNotVisibleException:
#            print("태그가 더이상 존재하지 않습니다.")
#            loop2()
#            break

def peakseat():
    driver.switch_to.frame(driver.find_element_by_id('ifrmSeat'))
    driver.switch_to.frame(driver.find_element_by_id('ifrmSeatDetail'))
    
    box = driver.find_elements_by_xpath("//img[@class='stySeat']")
    if box == None:
    #if True:
        driver.switch_to_default_content()
        driver.switch_to.frame(driver.find_element_by_id('ifrmSeat'))
        driver.switch_to.frame(driver.find_element_by_id('ifrmSeatView'))
        btntry('javascript:GetBlockSeatList("", "", "RGN002");')
        driver.switch_to_default_content()
        driver.switch_to.frame(driver.find_element_by_id('ifrmSeat'))
        driver.switch_to.frame(driver.find_element_by_id('ifrmSeatDetail'))
        box = driver.find_elements_by_xpath("//img[@class='stySeat']")
    
  
    box[0].click()
    btnclick("//div[@class='buy_info']",'NextStepImage')
    
def btntry(t):
    try:
        driver.execute_script(t)
    except JavascriptException:

        btntry(t)

def loop1(day):
    #driver.find_element_by_link_text('12')
    try:
        box = driver.find_element_by_xpath("//div[@class='calCont']/table/tbody")
        list = box.find_elements_by_tag_name('a')
        print(list)
        for item in list :
            print(item.text)
            if( day in item.text ):#변수
                item.click()
                break
    except NoSuchElementException: 
        box = driver.find_element_by_xpath("//div[@class='calCont']/table/tbody")
        list = box.find_elements_by_tag_name('a')
        print(list)
        for item in list :
            print(item.text)
            if( day in item.text ):#변수
                item.click()
                break        
    
def loop2(time):
    try:
        box=driver.find_element_by_xpath("//span[@id='TagPlaySeq']")
        list = box.find_elements_by_tag_name('a')
        print(list)
        for item in list :
            print(item.text)
            if( time in item.text ):#변수
                item.click()
                break
    except NoSuchElementException:
        box=driver.find_element_by_xpath("//span[@id='TagPlaySeq']")
        list = box.find_elements_by_tag_name('a')
        print(list)
        for item in list :
            print(item.text)
            if( time in item.text ):#변수
                item.click()
                break
        
def btnclick(a,m):
    try:
        driver.switch_to_default_content() 
        #driver.switch_to.frame(driver.find_element_by_id('divBookMain'))
        box = driver.find_element_by_xpath(a)
        to = box.find_element_by_id(m)
        to.click()
    except NoSuchElementException or ElementNotVisibleException:
        #driver.switch_to.frame(driver.find_element_by_id('divBookMain'))
#        box = driver.find_element_by_xpath(a)
#        to = box.find_element_by_id(m)
#        to.click()
        btnclick(a,m)

        
#로그 
def log(soup):
        f= codecs.open('log.txt','w','UTF-8')
        for i in soup:
            f.write(str(i))
        f.close()


if __name__ == '__main__':
    print('시작'+str(datetime.now()))
    
    isend = True
    
    driver = cdrive()
    login()
    while isend :
        search()
        test = input("다시시도 y/n : ")
        if test in 'y':
            isend = True
        else:
            isend = False
            
    print("완료"+str(datetime.now()))
