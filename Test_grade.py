from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://127.0.0.1:8000/")
driver.find_element(By.XPATH, "//input[@name='a']").send_keys("90")
driver.find_element(By.XPATH, "//input[@name='b']").send_keys("90")
driver.find_element(By.XPATH, "//input[@name='c']").send_keys("90")
driver.find_element(By.XPATH, "//input[@name='d']").send_keys("90")
driver.find_element(By.XPATH, "//input[@name='e']").send_keys("90")
driver.find_element(By.XPATH, "//input[@name='f']").send_keys("92")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.save_screenshot("screenshot_1.png")
sleep(2)