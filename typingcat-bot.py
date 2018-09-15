from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

test = input('Type 1, 3, or 5 to enter different typing tests: ')
if test != 1 and test != 3 and test != 5:
    input('Please only enter 1, 3 or 5: ')

driver = webdriver.Chrome()
driver.get('https://thetypingcat.com/typing-speed-test/{}m'.format(test))

typing = True
while typing:
    try:
        actives = []
        lines = driver.find_elements_by_class_name('line')
        for line in lines:
            if line.get_attribute('class') == 'line active':
                actives.append(line)
        for char in actives[-1].text:
            if char == '⏎':
                driver.find_element_by_tag_name('body').send_keys(Keys.RETURN)
            else:
                driver.find_element_by_tag_name('body').send_keys(char)
    except:
        driver.find_element_by_class_name('btn-primary').click()
        typing = False
