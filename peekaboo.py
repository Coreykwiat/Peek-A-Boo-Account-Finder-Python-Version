from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import main
from main import data
from main import pin
from main import skip2
import time
from selenium.common.exceptions import NoSuchElementException


username = main.username
pin = main.pin
skip2 = main.skip2
geturl2 = ""
text2 = ""
month = 'june'
day = '10'
year = '1990'
password = "fakepassword"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('window-size=0x0')
chrome_options.add_argument("--silent")

driver = webdriver.Chrome("chromedriver", options=chrome_options)


def read_output():
    with open('output.txt', 'r') as f:
        output = f.read()
        print(output)

data[0] = username + ' \n'
data[1] = ' \n'
with open('output.txt', 'w') as file:
    file.writelines(data)


def facebook():
    driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
    driver.find_element("id", "identify_email").send_keys(username)
    driver.find_element("id", "did_submit").click()
    time.sleep(0.5)
    geturl = driver.current_url
    if geturl == ("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0"):
        with open('output.txt', 'w') as f:
            data[3] = '- Facebook Account Not Found\n'
    else:
        with open('output.txt', 'w') as f:
            data[3] = '+ Facebook Account Found\n'

facebook()
with open('output.txt', 'w') as file:
    file.writelines(data)


def instagram():
    driver.get("https://www.instagram.com/accounts/password/reset/")
    try:
        driver.find_element("name", "cppEmailOrUsername").send_keys(username)
        time.sleep(2)
        driver.find_element("xpath", '//button[text()="Send login link"]').click()
    except:
        with open('output.txt', 'w') as f:
            data[4] = '- Error with Instagram\n'
        return
    time.sleep(2)
    geturl = driver.current_url

    if geturl == "https://www.instagram.com/accounts/password/reset/":
        try:
            driver.find_element("xpath", '//button[text()="OK"]').click()
            with open('output.txt', 'w') as f:
                data[4] = '+ Instagram Account found\n'
        except NoSuchElementException:
            with open('output.txt', 'w') as f:
                data[4] = '- Instagram Account Not Found\n'
    else:
        with open('output.txt', 'w') as f:
            data[4] = '+ Instagram Account Found\n'
instagram()
with open('output.txt', 'w') as file:
    file.writelines(data)


def snapchat():
    if skip2 == 'yes':
        data[5] = '- Snapchat Skipped\n'
        return

    else:
        driver.get("https://accounts.snapchat.com/accounts/password_reset_request")
        driver.find_element("class name", "form-control").send_keys(username)
        time.sleep(5)
        driver.find_element("class name", "primary_action").click()
        time.sleep(2.5)

        errorsmsg = 'not url'
        errors_message = "Email address is invalid."
        time.sleep(1)
        try:
            if driver.find_element("id", "error_message"):
                errorsmsg = driver.find_element("id", "error_message")
                pass

            else:
                with open('output.txt', 'w') as f:
                    data[5] = ' + Snapchat Account Found\n'
        except:
            pass
        try:
         if errorsmsg.text == errors_message:
             with open('output.txt', 'w') as f:
                 data[5] = '- Snapchat Account not Found\n'
        except:
         with open('output.txt', 'w') as f:
            data[5] = '+ Snapchat Account Found\n'

snapchat()
with open('output.txt', 'w') as file:
    file.writelines(data)




def LinkedIn():
    global password
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    driver.find_element("id", "username").send_keys(username)
    driver.find_element("id", "password").send_keys(password)
    time.sleep(1)
    driver.find_element("xpath", "/html/body/div/main/div[2]/div[1]/form/div[3]/button").click()
    time.sleep(2)
    try:
        linkedintext = driver.find_element("xpath", "//*[contains(text(), 'Couldn’t find a LinkedIn account associated with this email. Please try again.')]")
        if linkedintext.text == 'Couldn’t find a LinkedIn account associated with this email. Please try again.':
            data[6] = '- LinkedIn Account Not Found\n'
        else:
            data[6] = '+ LinkedIn Account Found\n'

    except:
        data[6] = '+ LinkedIn Account Found\n'


LinkedIn()
with open('output.txt', 'w') as file:
    file.writelines(data)


def TikTok():
    driver.get("https://www.tiktok.com/login/email/forget-password")
    try:
        driver.find_element("name", "email").send_keys(username)
        driver.find_element("xpath", '/html/body/div[2]/div/div[2]/div/form/div[3]/div/button').click()
        time.sleep(4)
        try:
            element = driver.find_element("xpath","/html/body/div[2]/div/div[2]/div/form/div[2]/div[2]")
            text = element.text
            text2 = "Email address isn't registered yet"
            if text == text2:
                with open('output.txt', 'w') as f:
                    data[7] = '- TikTok Account not found\n'
            else:
                with open('output.txt', 'w') as f:
                    data[7] = '+ TikTok Account Found\n'
        except:
            with open('output.txt', 'w') as f:
                data[7] = '= Potential TikTok Account Found\n'

    except:
        with open('output.txt', 'w') as f:
            data[7] = '- Error Finding TikTok\n'
TikTok()
with open('output.txt', 'w') as file:
    file.writelines(data)


def twitter():
    driver.get("https://twitter.com/i/flow/signup")
    time.sleep(2)
    driver.find_element("xpath",
                        "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/div/span/span").click()
    time.sleep(2)
    driver.find_element("xpath",
                        "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/span").click()
    driver.find_element("name", "email").send_keys(username)
    time.sleep(2)
    try:
        if driver.find_element("xpath", "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div/span"):
            data[8] = '+ Twitter Account Found\n'
        else:
            data[8] = '- Twitter Account Not Found\n'

    except:
        data[8] = '- Twitter Account Not Found\n'


twitter()

with open('output.txt', 'w') as file:
    file.writelines(data)


def pinterest():
    if pin == 'none':
        data[9] = '- Pinterest Skipped\n'
        return
    else:
        driver.get("https://www.pinterest.com/password/reset/")
        time.sleep(5)
        try:
            driver.find_element("id", "userQuery").send_keys(pin)
            time.sleep(2)
            driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div/div/div[2]/div/div/div/div/form/div[2]/div[2]/button").click()
            time.sleep(2)
        except:
            data[9] = '- Error with Pinterest\n'

        try:
            if driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div/div/div[2]/div/div/div/div/form/div[3]"):
              data[9] = '= Potential Pinterest Account Found\n'
            else:
              data[9] = '- Pinterest Account Not Found\n'

        except:
            data[9] = '- Pinterest Account Not Found\n'

pinterest()

with open('output.txt', 'w') as file:
    file.writelines(data)

def roblox():
    if pin == 'none':
        data[10] = '- Roblox Skipped\n'
    else:
        global month
        global day
        global year
        driver.get("https://www.roblox.com/")
        driver.find_element("id", "MonthDropdown").send_keys(month)
        driver.find_element("id", "DayDropdown").send_keys(day)
        driver.find_element("id", "YearDropdown").send_keys(year)
        driver.find_element("id", "signup-username").send_keys(pin)
        time.sleep(1)
        try:
            text2 = driver.find_element("xpath", "//*[contains(text(), 'This username is already in use.')]")
            if text2.text == 'This username is already in use.':
                if text2.text == 'This username is already in use.':
                    data[10] = '+ Roblox Account Found\n'
            else:
                data[10]= '- Roblox Account Not Found\n'
        except:
            data[10] = '- Roblox Not Account Found\n'

roblox()
with open('output.txt', 'w') as file:
    file.writelines(data)

def vsco():
    if skip2 == 'yes':
        data[11] = '- VSCO Skipped\n'
    else:
        driver.get("https://vsco.co/user/forgotpassword")
        driver.find_element("id", "email").send_keys(username)
        driver.find_element("id", 'forgotPasswordBtn').click()
        time.sleep(1)
        try:
            geturl2 = driver.current_url
            if geturl2 == 'https://vsco.co/user/forgotpassword':
                data[11] = '- VSCO Account Not Found\n'
            else:
                data[11] = '+ VSCO Account Found\n'
        except:
            data[11] = '- VSCO Error\n'


vsco()
with open('output.txt', 'w') as file:
    file.writelines(data)






#Snoopin around I see. :) -CK

