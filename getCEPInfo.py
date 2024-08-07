from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def findCEP(cep_number):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)
 
    browser.get("https://buscacep.com.br/")
    browser.find_element('xpath','/html/body/div[1]/div/div[1]/div[2]/form/input').send_keys(cep_number)
    browser.find_element('xpath','/html/body/div[1]/div/div[1]/div[2]/form/div/button').click()

    street_name = browser.find_element('xpath','/html/body/div[1]/div/div[3]/div/div/div/div/table/tbody/tr[4]/td/a').text
    district_name = browser.find_element('xpath','/html/body/div[1]/div/div[3]/div/div/div/div/table/tbody/tr[5]/td/a').text
    city_name = browser.find_element('xpath','/html/body/div[1]/div/div[3]/div/div/div/div/table/tbody/tr[6]/td/a').text
    state_name = browser.find_element('xpath','/html/body/div[1]/div/div[3]/div/div/div/div/table/tbody/tr[7]/td/a').text

    browser.close()

    return(street_name,district_name,city_name,state_name)
