import requests
from bs4 import BeautifulSoup
import csv
import time
import os
import typed_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SECRETS = typed_dotenv.load(".env")

def login(driver):
    try:
        print('NAVEGADOR INICIADO ...')
        url = "https://amantino.marketmine.com.br/principal"
        driver.get(url)

        print('Realizando o login ...')
        # Encontrar e clicar no botão "ENTRAR"
        entrar_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "LNKENTRARFRAMENUBASE"))
        )
        entrar_button.click()

        AMANTINO_EMAIL = SECRETS['AMANTINO_EMAIL']
        AMANTINO_SENHA = SECRETS['AMANTINO_SENHA']

        # Preencher o formulário de login
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "EDTLOGINFRALOGIN"))
        )
        email_input.send_keys(AMANTINO_EMAIL)

        senha_input = driver.find_element(By.ID, "EDTSENHALOGINFRALOGIN")
        senha_input.send_keys(AMANTINO_SENHA)

        # Clicar no botão "Entrar"
        entrar_modal_button = driver.find_element(By.ID, "BTNACESSARFRALOGIN")
        entrar_modal_button.click()


        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "LNKENTRARFRAMENUBASE"))
        )
        print("Login realizado com sucesso!")
        # time.sleep(5)

    except Exception as e:
        print("Ocorreu um erro:", e)