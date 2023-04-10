from time import sleep
from selenium import webdriver as uc
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from pyshadow.main import Shadow
import csv


def addchrome():
    with open('Linea.csv', 'r', encoding='UTF8', newline='') as f1:
        reader = csv.reader(f1)
        csv_data = [row for row in reader if row and any(cell.strip() != '' for cell in row)]
        for row in csv_data:
            global web
            options = ChromeOptions()
            options.add_extension("metamask.crx")
            # options.add_argument("--headless=chrome")
            options.add_argument("--start-maximized")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--ignore-certificate-errors")
            web = uc.Chrome(chrome_options=options)
            sleep(2)
            web.switch_to.window(web.window_handles[-1])
            current = web.current_window_handle
            sleep(1)
            web.switch_to.window(web.window_handles[-2])
            for handle in web.window_handles:
                web.switch_to.window(handle)
                if handle != current:
                    web.close()
                    sleep(1)
            # Access the fields using the field names
            cell = row[0]
            address = row[2]
            phrases = cell.split(" ")

            print("Mở chrome và add extension")
            web.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#")

            print("Click nut Import an existing wallet")
            wait(web, 5).until(EC.presence_of_element_located((
                By.XPATH, "//button[text()='Import an existing wallet']"
            ))).click()
            sleep(0.5)

            print("Click nut I agree")
            wait(web, 5).until(EC.presence_of_element_located((
                By.XPATH, "//button[text()='I agree']"
            ))).click()
            sleep(0.5)

            print("Nhap 12 phrases")
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[1]/div[1]/div/input"))).send_keys(
                phrases[0])
            sleep(0.5)
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[2]/div[1]/div/input"))).send_keys(
                phrases[1])
            sleep(0.5)
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[3]/div[1]/div/input"))).send_keys(
                phrases[2])
            sleep(0.5)
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[4]/div[1]/div/input"))).send_keys(
                phrases[3])
            sleep(0.5)
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[5]/div[1]/div/input"))).send_keys(
                phrases[4])
            sleep(0.5)
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[6]/div[1]/div/input"))).send_keys(
                phrases[5])
            sleep(0.5)
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[7]/div[1]/div/input"))).send_keys(
                phrases[6])
            sleep(0.5)
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[8]/div[1]/div/input"))).send_keys(
                phrases[7])
            sleep(0.5)
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[9]/div[1]/div/input"))).send_keys(
                phrases[8])
            sleep(0.5)
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[10]/div[1]/div/input"))).send_keys(
                phrases[9])
            sleep(0.5)
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[11]/div[1]/div/input"))).send_keys(
                phrases[10])
            sleep(0.5)
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/div/div[3]/div[12]/div[1]/div/input"))).send_keys(
                phrases[11])
            sleep(0.5)

            print("Click nut Confirm Secret Recovery Phrase")
            wait(web, 5).until(EC.presence_of_element_located((
                By.XPATH, "//button[text()='Confirm Secret Recovery Phrase']"
            ))).click()
            sleep(0.5)

            print("Enter Password")
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input"))).send_keys(
                "12345678")
            sleep(0.5)

            print("Enter confirm password")
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input"))).send_keys(
                "12345678")
            sleep(0.5)

            print("Check box and Create")
            web.find_element(By.XPATH,
                             "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input").click()
            sleep(0.5)
            web.find_element(By.XPATH,
                             "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button").click()
            sleep(0.5)

            print("Click vao nut Got it!")
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
            sleep(0.5)

            print("Click vao nut Next")
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
            sleep(0.5)

            print("Click vao nut Done")
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
            sleep(1.5)

            print("Click vao nut X")
            wait(web, 5).until(EC.presence_of_element_located((By.XPATH,
                                                               "//button[@aria-label='Close']"))).click()
            sleep(0.5)
            print("Done acc: " + address)
            web.quit()


if __name__ == '__main__':
    try:
        addchrome()

    except Exception as e:
        print(e)
