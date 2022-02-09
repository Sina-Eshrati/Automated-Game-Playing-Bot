from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# ------------------------------------------------ Create Driver -------------------------------------------
service = Service(executable_path="E:\Softwares\Chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

# ------------------------------------------------ Game Logic ----------------------------------------------
game_start_time = time.time()


def play():
    timer_start = time.time()
    while True:
        check_time = time.time()
        cookie.click()
        if check_time > timer_start + 5:
            break
    money = driver.find_element(By.ID, "money")
    money_amount = int(money.text.replace(",", ""))
    cursor = driver.find_element(By.CSS_SELECTOR, "#buyCursor")
    cursor_amount = int(cursor.text.split()[2].replace(",", ""))
    grandma = driver.find_element(By.CSS_SELECTOR, "#buyGrandma")
    grandma_amount = int(grandma.text.split()[2].replace(",", ""))
    factory = driver.find_element(By.CSS_SELECTOR, "#buyFactory")
    factory_amount = int(factory.text.split()[2].replace(",", ""))
    mine = driver.find_element(By.CSS_SELECTOR, "#buyMine")
    mine_amount = int(mine.text.split()[2].replace(',', ''))
    shipment = driver.find_element(By.CSS_SELECTOR, "#buyShipment")
    shipment_amount = int(shipment.text.split()[2].replace(',', ''))
    alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
    alchemy_lab_amount = int(alchemy_lab.text.split()[3].replace(",", ""))
    portal = driver.find_element(By.CSS_SELECTOR, "#buyPortal")
    portal_amount = int(portal.text.split()[2].replace(',', ''))
    time_machine = driver.find_element(By.ID, "buyTime machine")
    time_machine_amount = int(time_machine.text.split()[3].replace(',', ''))
    if money_amount >= time_machine_amount:
        time_machine.click()
    elif money_amount >= portal_amount:
        portal.click()
    elif money_amount >= alchemy_lab_amount:
        alchemy_lab.click()
    elif money_amount >= shipment_amount:
        shipment.click()
    elif money_amount >= mine_amount:
        mine.click()
    elif money_amount >= factory_amount:
        factory.click()
    elif money_amount >= grandma_amount:
        grandma.click()
    elif money_amount >= cursor_amount:
        cursor.click()
    if time.time() >= game_start_time + 300:
        return
    else:
        play()


play()
cookies_per_second = driver.find_element(By.ID, "cps").text
print(cookies_per_second)
