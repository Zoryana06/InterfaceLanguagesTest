import time
from selenium.common.exceptions import NoSuchElementException

def test_containing_add_to_basket_button(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	xpath = "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"
	browser.get(link)
	time.sleep(3)
	assert check_exists_by_xpath(browser, xpath), f"Button is absent!"

def check_exists_by_xpath(browser, xpath):
    try:
        browser.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
    