from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome(
    'C:\\Users\이수민\Desktop\chromedriver_win32\chromedriver.exe')


def crawl_with_login(target_url, filename, id, pw):
    driver.get(target_url)
    driver.find_element_by_xpath(
        '/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a').click()
    driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(id)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(pw)
    driver.find_element_by_xpath(
        '//*[@id="login"]/div[4]/form/div/input[12]').click()
    time.sleep(2)

    f = open(filename, 'w')
    f.write(BeautifulSoup(driver.page_source, 'html.parser').prettify())
    f.close()


crawl_with_login('https://github.com/',
                 "logincrawler.html", "sumin21", '200724s@')
