# Application Bot to automate playing "Cookie Clicker" game

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime
import time

# NOTE: Chromedriver must be in the below directory and must be compatible with the current Chrome version
# in order for the application to successfully run

# Selenium setup

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Cookie ID, setting score, setting while loop condition

cookie = driver.find_element(By.ID, "cookie")
score = 0
game_over = False

# Application is set to stop after running for 5 minutes

timeout = time.time() + 60*5

# IDs are defined here

cursor_upgrade = driver.find_element(By.CSS_SELECTOR, "#buyCursor b")
cursor_cost = int((cursor_upgrade.text.split(" - ")[1]).replace(",", ""))
grandma_upgrade = driver.find_element(By.CSS_SELECTOR, "#buyGrandma b")
grandma_cost = int((grandma_upgrade.text.split(" - ")[1]).replace(",", ""))
factory_upgrade = driver.find_element(By.CSS_SELECTOR, "#buyFactory b")
factory_cost = int((factory_upgrade.text.split(" - ")[1]).replace(",", ""))
mine_upgrade = driver.find_element(By.CSS_SELECTOR, "#buyMine b")
mine_cost = int((mine_upgrade.text.split(" - ")[1]).replace(",", ""))
shipment_upgrade = driver.find_element(By.CSS_SELECTOR, "#buyShipment b")
shipment_cost = int((shipment_upgrade.text.split(" - ")[1]).replace(",", ""))

# While loop keeps the bot playing the game

while game_over is False:

    # Main loop actions involve clicking the cookie and checking the current second

    cookie.click()
    seconds = datetime.datetime.now().second

    # If statement is entered every 10 seconds

    if seconds % 5 == 0:

        # Score is updated

        score = int((driver.find_element(By.ID, "money").text).replace(",", ""))

        # Bot attempts to buy as many upgrades as it can, with a priority on the cheaper upgrades,
        # up to a certain specified threshold (when the next level upgrade would be the same cost)

        if score < 100:
            try:
                cursor_upgrade_click = driver.find_element(By.ID, "buyCursor")
                cursor_upgrade_click.click()
            except selenium.common.exceptions.StaleElementReferenceException:
                continue
        elif score < 500:
            try:
                grandma_upgrade_click = driver.find_element(By.ID, "buyGrandma")
                grandma_upgrade_click.click()
            except selenium.common.exceptions.StaleElementReferenceException:
                continue
        elif score < 2000:
            try:
                factory_upgrade_click = driver.find_element(By.ID, "buyFactory")
                factory_upgrade_click.click()
            except selenium.common.exceptions.StaleElementReferenceException:
                continue
        elif score < 7000:
            try:
                mine_upgrade_click = driver.find_element(By.ID, "buyMine")
                mine_upgrade_click.click()
            except selenium.common.exceptions.StaleElementReferenceException:
                continue
        elif score > shipment_cost:
            try:
                shipment_upgrade_click = driver.find_element(By.ID, "buyShipment")
                shipment_upgrade_click.click()
            except selenium.common.exceptions.StaleElementReferenceException:
                continue

    # While loop ends after the timeout limit is reached

    if time.time() > timeout:
        game_over = True

# Optional line to exit window on completion
# driver.quit()
