#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import unittest
import sys


driver = webdriver.Firefox()
driver.get("https://accounts.craigslist.org/login")


registered =['\xc2\xae', 'text2']
encode = ''.join(registered[0])
final_reg = unicode(encode, "utf-8") # If your need the "registered trademark" symbol in your post.


emailFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("inputEmailHandle"))
passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id("inputPassword"))

emailFieldElement.send_keys(sys.argv[3])
passFieldElement.send_keys(sys.argv[4])
driver.find_element_by_xpath("(//button)[1]").click()

driver.get(sys.argv[1])
driver.find_element_by_xpath(".//*[@id='post']").click()
driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form/blockquote/label[2]").click()
driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form/button").click()
driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form/blockquote/label[6]").click()

# Deal with annoying sub-area requests.
def click_subarea():
  try:
    sublocation = driver.find_element_by_xpath("//*[contains(.,'choose the location that fits best:')]")
  except NoSuchElementException:
    pass
  else:
    if (sublocation is not None):
      print "==========================================================================="
      driver.find_element_by_xpath("//label[1]/input").click()
      click_subarea()

click_subarea()

driver.find_element_by_xpath(".//*[@id='oiab']/label[3]").click()
driver.find_element_by_xpath(".//*[@id='contact_text_ok']").click()
driver.find_element_by_xpath(".//*[@id='contact_phone']").send_keys("(111)222-3333")
driver.find_element_by_xpath(".//*[@id='postal_code']").send_keys(sys.argv[2])
driver.find_element_by_xpath(".//*[@id='contact_name']").send_keys("John Smith")
driver.find_element_by_xpath(".//*[@id='PostingTitle']").send_keys("I am a Robot!")
driver.find_element_by_xpath(".//*[@id='PostingBody']").send_keys("Sample text!")
driver.find_element_by_xpath(".//*[@id='pay_label']/input").click()
driver.find_element_by_xpath(".//*[@id='remuneration']").send_keys("$500")
driver.find_element_by_xpath(".//*[@id='wantamap']").click()
driver.find_element_by_xpath(".//*[@id='postingForm']/button").click()
driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/form/button").click()
driver.find_element_by_xpath(".//*[@id='publish_top']/button").click()
link =  driver.find_element_by_xpath(".//*[@id='pagecontainer']/section/ul/li[1]/a").text
file = open('/var/www/html/links.html', 'a+')
file.write(link + '<br><br>\n\n')
file.close()
driver.quit()
