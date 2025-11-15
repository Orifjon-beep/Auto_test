from selenium import webdriver
from selenium.webdriver.common.by import By


def test_rasm():
    browser = webdriver.Chrome()
    browser.get('https://www.olx.uz/oz/')
    rasm_link = browser.find_element(By.LINK_TEXT, value = 'Bolalar dunyosi')
    rasm_link.click()
    title = browser.find_element(By.LINK_TEXT, value = 'Bolalar kiyimi')
    assert title.text == 'Bolalar kiyimi'
