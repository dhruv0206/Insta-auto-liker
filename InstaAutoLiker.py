import os 
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("https://www.instagram.com/accounts/login/")

sleep(2)
if(driver.current_url == 'https://www.instagram.com/accounts/login/'):

    username = input("Enter username: ")
    get_username = driver.find_element_by_name("username")
    get_username.send_keys(username)

    password = input("Enter password: ")
    get_password = driver.find_element_by_name("password")
    get_password.send_keys(password)

    login_click = driver.find_element_by_class_name("L3NKy")
    login_click.click()

    sleep(20)

likes = driver.find_elements_by_tag_name('svg')
for like in likes:
    print(like)
    likes_attr = like.get_attribute("aria-label")
    print(likes_attr)
    if(likes_attr == 'Like'):
        like.click()

driver.close()