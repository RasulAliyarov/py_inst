import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def SeleniumData(username, password):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.instagram.com")
    driver.maximize_window()

    try:
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys(username)
        driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys(password)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
        driver.implicitly_wait(10)
        if driver.find_element(By.XPATH, '//div[text() = "Не сейчас"]') :
            driver.find_element(By.XPATH, '//div[text() = "Не сейчас"]').click()
        time.sleep(1)
        if driver.find_element(By.XPATH, '//button[text() = "Не сейчас"]'):
            driver.find_element(By.XPATH, '//button[text() = "Не сейчас"]').click()
        time.sleep(1)
        driver.find_element( By.CSS_SELECTOR, '[href][role="link"][tabindex="0"][style="width: 56px; height: 56px;"]').click()
        time.sleep(3)
        followings= driver.find_element(By.XPATH, './/*[contains(text(), "подписчиков")]/span').get_attribute('title')
        followers = driver.find_element(By.XPATH, './/*[contains(text(), "подписок")]/span').text
        name= driver.find_element(By.CSS_SELECTOR, '[style="line-height: var(--base-line-clamp-line-height); --base-line-clamp-line-height:25px;"]').text

        time.sleep(2)
        return  (followers, name, followings)
    except:
        return ("","","")