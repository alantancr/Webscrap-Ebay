from selenium import webdriver
from bs4 import BeautifulSoup
import csv

# create a file, set csv writer and write first line in file
file = open("ebay_iphone.csv", "w", newline='', encoding='utf-8')
scrap = csv.writer(file, dialect=csv.excel)
scrap.writerow(["Title", "Price","Brand","Link"])
# create webdriver

driver = webdriver.Chrome()
# search up to 5 pagination
url = "https://www.ebay.co.uk/b/Apple-Mobile-Smartphones/9355/bn_449685?_pgn="
number_of_pages = 5
for i in range(number_of_pages):
    # driver.get will go to URL that we specified as its parameter and ur
    driver.get(url + str(i+1))
    # we select all parent elements which hold more granular information
    elements = driver.find_elements_by_xpath(".//li[@class='s-item   ']")
    # iterate through each element and save title, price and brand, link
    for element in elements:
        title = element.find_element_by_xpath(".//h3[@class='s-item__title']").text
        price = element.find_element_by_xpath(".//span[@class='s-item__price']").text
        brand = element.find_element_by_xpath(".//span[@class='s-item__dynamic s-item__dynamicAttributes1']").text
        link = element.find_element_by_xpath(".//a[@class='s-item__link'][1]").get_attribute("href")

        scrap.writerow([title, price,brand,link])
        file.flush()
#close everything
file.close()
driver.close()
driver.quit()