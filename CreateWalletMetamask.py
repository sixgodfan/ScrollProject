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

    print("Mở chrome và add extension")
    web.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#")

    print("Click nut Create new wallet")
    wait(web,5).until(EC.presence_of_element_located((
        By.XPATH, "//button[text()='Create a new wallet']"
    ))).click()
    sleep(0.5)

    print("Click nut I agree")
    wait(web,5).until(EC.presence_of_element_located((
        By.XPATH, "//button[text()='I agree']"
    ))).click()
    sleep(0.5)

    print("Enter Password")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "(//input[@class='form-field__input'])[1]"))).send_keys("12345678")
    sleep(0.5)

    print("Enter confirm password")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "(//input[@class='form-field__input'])[2]"))).send_keys("12345678")
    sleep(0.5)

    print("Check box and Create")
    web.find_element(By.XPATH, 
    "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input").click()
    sleep(0.5)
    web.find_element(By.XPATH, 
    "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button").click()
    sleep(0.5)
    
    print("Click nut Remind me later")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "/html/body/div[1]/div/div[2]/div/div/div/div[5]/button[1]"))).click()
    sleep(0.5)

    print("Click vao o checkbox")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "/html/body/div[2]/div/div/section/div[1]/div/div/label/input"))).click()
    sleep(0.5)

    print("Click vao nut Skip")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "/html/body/div[2]/div/div/section/div[2]/div/button[2]"))).click()
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
    
    print("Click vao nut Account")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "/html/body/div[1]/div/div[1]/div/div[2]/button"))).click()
    sleep(0.5)
    
    print("Click vao nut Settings")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "//div[text()='Settings']"))).click()
    sleep(0.5)
    
    print("Click vao nut Security")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "//div[@class='tab-bar']//div[text()='Security & privacy']"))).click()
    sleep(0.5)
    
    print("Click vao nut Reveal")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "//button[text()='Reveal Secret Recovery Phrase']"))).click()
    sleep(0.5)

    print("Nhap password")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "/html/body/div[1]/div/div[3]/div/form/div/input"))).send_keys('12345678')
    sleep(0.5)
    
    print("Click vao nut Next")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "/html/body/div[1]/div/div[3]/div/div[2]/button[2]"))).click()
    sleep(0.5)
  
    print("Hold vao nut reveal")
    button_reveal = wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "/html/body/div[1]/div/span/div[1]/div/div/button")))
    sleep(0.5)
    action = ActionChains(web)
    action.move_to_element(button_reveal)
    # hold the button for 5 seconds
    action.click_and_hold(button_reveal).perform()
    sleep(3)
    # release the button
    action.release().perform()  

    print("Lay phrase")
    element = wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/p")))
    phrase = element.text

    print("Click nut Close")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "/html/body/div[1]/div/div[3]/div/div[3]/button"))).click()
    sleep(0.5)
  
    print("Lay private key")
    print("Click vao nut 3 cham ")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "/html/body/div[1]/div/div[3]/div/div/div/div[1]/span/button"))).click()
    sleep(0.5)
    
    print("Click vao nut Account Details")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "//div[text()='Account details']"))).click()
    sleep(0.5)

    print("Lay address")
    element1 = wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "//div[@class='qr-code__address']")))
    address = element1.text
    
    print("Click vao nut Export private key")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "/html/body/div[1]/div/span/div[1]/div/div/div/button[3]"))).click()
    sleep(0.5)
    
    print("Nhap password")
    wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "/html/body/div[1]/div/span/div[1]/div/div/div/div[5]/input"))).send_keys('12345678')
    sleep(0.5)

    print("Click nut Confirm")
    wait(web,5).until(EC.presence_of_element_located((By.XPATH,
    '/html/body/div[1]/div/span/div[1]/div/div/div/div[7]/button[2]'))).click()
    sleep(0.5)
    
    print("Lay address")
    element2 = wait(web, 5).until(EC.presence_of_element_located((By.XPATH, 
    "/html/body/div[1]/div/span/div[1]/div/div/div/div[5]/div")))
    privatekey = element2.text
    sleep(0.5)

    print("Click nut Done")
    wait(web,5).until(EC.presence_of_element_located((By.XPATH, 
    "/html/body/div[1]/div/span/div[1]/div/div/div/div[7]/button"))).click()
    sleep(0.5)

    # Save phrase, pk, address vao file
    fieldnames = ['phrase', 'privatekey', 'address']
    rows = [
        {
            'phrase': phrase,
            'privatekey': privatekey,
            'address' : address

        }
    ]
    with open('Linea.csv', 'a', encoding='UTF8', newline='') as f1:
        writer = csv.DictWriter(f1, fieldnames=fieldnames)
        writer.writerows(rows)
        print("Save Wallet")
    web.quit()




if __name__ == '__main__':
    while True:
        try:
            addchrome()

        except Exception as e:
            print(e)