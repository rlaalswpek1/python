from selenium import webdriver

path = "C:\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get('https://www.google.com')

assert "Google" in driver.title
assert "Naver" in driver.title

elem = driver.find_element_by_name("q")

elem.clear()

elem.send_keys("selenium")

elem.submit()

assert "No results found." not in driver.page_source

driver.close()