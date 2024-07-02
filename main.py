from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


web_url = "http://orteil.dashnet.org/experiments/cookie/"
driver = webdriver.Chrome()
driver.get(url=web_url)

def update():
    global  click_grandma, click_cursor, click_factory, click_mine, click_lab, click_cookie, click_shipment
    global click_portal, click_time, money, click_cursor_cost_data, click_grandma_cost_data, click_factory_cost_data
    global click_mine_cost_data, click_shipment_cost_data, click_lab_cost_data, click_portal_cost_data
    global click_time_cost_data
    cookie = driver.find_element(By.ID, "money")
    click_cookie = driver.find_element(By.ID, "cookie")
    click_cursor = driver.find_element(By.ID, "buyCursor")
    click_grandma = driver.find_element(By.ID, "buyGrandma")
    click_factory = driver.find_element(By.ID, "buyFactory")
    click_mine = driver.find_element(By.ID, "buyMine")
    click_shipment = driver.find_element(By.ID, "buyShipment")
    click_lab = driver.find_element(By.ID, "buyAlchemy lab")
    click_portal = driver.find_element(By.ID, "buyPortal")
    click_time = driver.find_element(By.ID, "buyTime machine")
    cookie = cookie.text.strip().split()
    cookie_range = len(cookie)
    money = int(cookie[cookie_range - 1].replace(",", ""))

    click_cursor_cost = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b')
    click_cursor_cost_data = click_cursor_cost.text.strip().split()
    click_cursor_cost_data_range = len(click_cursor_cost_data)
    click_cursor_cost_data = int(click_cursor_cost_data[click_cursor_cost_data_range - 1].replace(",", ""))

    click_grandma_cost = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b')
    click_grandma_cost_data = click_grandma_cost.text.strip().split()
    click_grandma_cost_data_range = len(click_grandma_cost_data)
    click_grandma_cost_data = int(click_grandma_cost_data[click_grandma_cost_data_range - 1].replace(",", ""))

    click_factory_cost = driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b')
    click_factory_cost_data = click_factory_cost.text.strip().split()
    click_factory_cost_data_range = len(click_factory_cost_data)
    click_factory_cost_data = int(click_factory_cost_data[click_factory_cost_data_range - 1].replace(",", ""))

    click_mine_cost = driver.find_element(By.XPATH, '//*[@id="buyMine"]/b')
    click_mine_cost_data = click_mine_cost.text.strip().split()
    click_mine_cost_data_range = len(click_mine_cost_data)
    click_mine_cost_data = int(click_mine_cost_data[click_mine_cost_data_range - 1].replace(",", ""))

    click_shipment_cost = driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b')
    click_shipment_cost_data = click_shipment_cost.text.strip().split()
    click_shipment_cost_data_range = len(click_shipment_cost_data)
    click_shipment_cost_data = int(click_shipment_cost_data[click_shipment_cost_data_range - 1].replace(",", ""))

    click_lab_cost = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b')
    click_lab_cost_data = click_lab_cost.text.strip().split()
    click_lab_cost_data_range = len(click_lab_cost_data)
    click_lab_cost_data = int(click_lab_cost_data[click_lab_cost_data_range - 1].replace(",", ""))

    click_portal_cost = driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b')
    click_portal_cost_data = click_portal_cost.text.strip().split()
    click_portal_cost_data_range = len(click_portal_cost_data)
    click_portal_cost_data = int(click_portal_cost_data[click_portal_cost_data_range - 1].replace(",", ""))

    click_time_cost = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b')
    click_time_cost_data = click_time_cost.text.strip().split()
    click_time_cost_data_range = len(click_time_cost_data)
    click_time_cost_data = int(click_time_cost_data[click_time_cost_data_range - 1].replace(",", ""))

click_cookie = driver.find_element(By.ID, "cookie")
click_cursor = driver.find_element(By.ID, "buyCursor")
click_grandma = driver.find_element(By.ID, "buyGrandma")
click_factory = driver.find_element(By.ID, "buyFactory")
click_mine = driver.find_element(By.ID, "buyMine")
click_shipment = driver.find_element(By.ID, "buyShipment")
click_lab = driver.find_element(By.ID, "buyAlchemy lab")
click_portal = driver.find_element(By.ID, "buyPortal")
click_time = driver.find_element(By.ID, "buyTime machine")
cookie = driver.find_element(By.ID, "money")
money = int(cookie.text.strip())
start = True
i = 0
click_cursor_cost = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b')
click_cursor_cost_data = click_cursor_cost.text.strip().split()
click_cursor_cost_data_range = len(click_cursor_cost_data)
click_cursor_cost_data = int(click_cursor_cost_data[click_cursor_cost_data_range-1].replace(",", ""))

click_grandma_cost = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b')
click_grandma_cost_data = click_grandma_cost.text.strip().split()
click_grandma_cost_data_range = len(click_grandma_cost_data)
click_grandma_cost_data = int(click_grandma_cost_data[click_grandma_cost_data_range-1].replace(",", ""))


click_factory_cost = driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b')
click_factory_cost_data = click_factory_cost.text.strip().split()
click_factory_cost_data_range = len(click_factory_cost_data)
click_factory_cost_data = int(click_factory_cost_data[click_factory_cost_data_range-1].replace(",", ""))

click_mine_cost = driver.find_element(By.XPATH, '//*[@id="buyMine"]/b')
click_mine_cost_data = click_mine_cost.text.strip().split()
click_mine_cost_data_range = len(click_mine_cost_data)
click_mine_cost_data = int(click_mine_cost_data[click_mine_cost_data_range-1].replace(",", ""))

click_shipment_cost = driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b')
click_shipment_cost_data = click_shipment_cost.text.strip().split()
click_shipment_cost_data_range = len(click_shipment_cost_data)
click_shipment_cost_data = int(click_shipment_cost_data[click_shipment_cost_data_range-1].replace(",", ""))

click_lab_cost = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b')
click_lab_cost_data = click_lab_cost.text.strip().split()
click_lab_cost_data_range = len(click_lab_cost_data)
click_lab_cost_data = int(click_lab_cost_data[click_lab_cost_data_range-1].replace(",", ""))

click_portal_cost = driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b')
click_portal_cost_data = click_portal_cost.text.strip().split()
click_portal_cost_data_range = len(click_portal_cost_data)
click_portal_cost_data = int(click_portal_cost_data[click_portal_cost_data_range-1].replace(",", ""))


click_time_cost = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b')
click_time_cost_data = click_time_cost.text.strip().split()
click_time_cost_data_range = len(click_time_cost_data)
click_time_cost_data = int(click_time_cost_data[click_time_cost_data_range-1].replace(",", ""))



while start:
    click_cookie.click()
    i +=1
    if i % 10 == 0:
        update()


        if money > click_time_cost_data:
            i = 0
            update()
            driver.implicitly_wait(1)
            click_time.click()
            update()


        if money > click_portal_cost_data:
            i = 0
            update()
            driver.implicitly_wait(1)

            click_portal.click()
            update()


        if money > click_lab_cost_data:
            i = 0
            update()
            driver.implicitly_wait(2)

            click_lab.click()
            update()

        if money > click_shipment_cost_data:
            i = 0
            update()
            driver.implicitly_wait(2)

            click_shipment.click()
            update()


        if money > click_mine_cost_data:
            i = 0
            update()
            driver.implicitly_wait(2)

            click_mine.click()
            update()


        if money > click_factory_cost_data:

            i = 0
            update()
            driver.implicitly_wait(2)
            click_factory.click()
            update()

        if money > click_grandma_cost_data:

            i = 0
            update()
            driver.implicitly_wait(2)
            click_grandma.click()
            update()

        if money > click_cursor_cost_data:

            i = 0
            update()
            driver.implicitly_wait(2)
            click_cursor.click()
            update()

        i = 0
