#Text di bawah ini

text='''

'''


import random,time,os,glob,sys
cwd = os.getcwd()
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import json
from webdriver_manager.chrome import ChromeDriverManager

from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
 
mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 650, "pixelRatio": 3.4 },
    }

firefox_options = webdriver.ChromeOptions()
firefox_options.add_argument('--no-sandbox')
 
firefox_options.headless = False
firefox_options.add_argument('--disable-setuid-sandbox')
firefox_options.add_argument('disable-infobars')
firefox_options.add_argument('--ignore-certifcate-errors')
firefox_options.add_argument('--ignore-certifcate-errors-spki-list')
firefox_options.add_argument("--mute-audio")
firefox_options.add_argument('--no-first-run')
firefox_options.add_argument('--disable-dev-shm-usage')
firefox_options.add_argument("--disable-infobars")
firefox_options.add_argument("--disable-extensions")
firefox_options.add_argument("--disable-popup-blocking")
firefox_options.add_argument('--log-level=3') 
 
firefox_options.add_argument('--disable-blink-features=AutomationControlled')
firefox_options.add_experimental_option("useAutomationExtension", False)
firefox_options.add_experimental_option("excludeSwitches",["enable-automation"])
firefox_options.add_experimental_option('excludeSwitches', ['enable-logging'])
firefox_options.add_argument('--disable-notifications')
from selenium.webdriver.common.action_chains import ActionChains
random_angka = random.randint(100,999)
random_angka_dua = random.randint(10,99)
def xpath_ex(el):
    element_all = wait(browser,15).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    try:
        element_all.click()
    except:
        try:
            browser.execute_script("arguments[0].click();", element_all)
        except:
            pass

def xpath_long(el):
    element_all = wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all) 


def xpath_fast(el):
    element_all = wait(browser,3).until(EC.presence_of_element_located((By.XPATH, el)))
    #browser.execute_script("arguments[0].scrollIntoView();", element_all)
    return browser.execute_script("arguments[0].click();", element_all) 

def xpath_type(el,word):
    return wait(browser,30).until(EC.presence_of_element_located((By.XPATH, el))).send_keys(word)
     
def login():
     
    global browser

    #firefox_options.add_experimental_option("mobileEmulation", mobile_emulation)
    firefox_options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
    browser = webdriver.Chrome(executable_path="./chromedriver.exe",options=firefox_options)
    browser.get("https://facebook.com/")
    directory_path = "./cookies"
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        file_list = os.listdir(directory_path)
        for file in file_list:
            with open(f"./cookies/{file}", 'r') as cookiesfile:
                cookies = json.load(cookiesfile)
                for cookie in cookies:
                    
                    browser.add_cookie(cookie)
                    sleep(1)
                    browser.refresh()
                    sleep(5)

                    try:
                        xpath_fast('(//*[contains(@href,"/login/?privacy_mutation_token=")])[1]')
                        xpath_type('(//input[@type="password"])[2]',file.replace(".json",''))
                        xpath_type('(//input[@type="password"])[2]', Keys.ENTER)
                    except:
                        pass
                    sleep(5)
                    get_url = open(f"{cwd}/grup.txt","r")
                    get_url = get_url.read().split("\n")
                    
                    for i in get_url:
                        try:
                            browser.get(i)
                            print(f'{i} Trying to post')
                            xpath_long('//*[text()="Tulis sesuatu..."]/parent::div/parent::div')
                            sleep(1)

                            try:
                                xpath_fast('(//form[@method="POST"])//*[@role="textbox"]')
                            except:
                                pass
                            sleep(1)
                             
                            xpath_type('(//form[@method="POST"])//*[@role="textbox"]',text)
                            sleep(2)

                            xpath_long('(//form[@method="POST"])//*[@aria-label="Foto/video"]')
                            sleep(2)
                            images_path = "./images"
                            if os.path.exists(images_path) and os.path.isdir(images_path):
                                images = os.listdir(images_path)
                                for file_image in images:
                                    xpath_type('(//form[@method="POST"])//*[@accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]',f'{cwd}/images/{file_image}')
                                    print(f'{i} Waiting load image')
                                    sleep(5)
                            xpath_long('//div[@aria-label="Posting"]')
                            print(f'{i} Waiting 30s for uploading')
                            sleep(30)
                            print(f'{i} Success post')
                        except Exception as e:
                            print(e)
                            pass
                        
                    browser.delete_all_cookies()
                    browser.refresh()
if __name__ == '__main__':
    print("[*] Auto Facebook Post Group")
    login()
     
    