import requests
from bs4 import BeautifulSoup
import csv
import time
import export_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException



def extract_data(driver):
    print('Redirecionando para os meus pedidos ...')
    driver.get("https://amantino.marketmine.com.br/MeusPedidos")
    data = []
    
    while True:
        pedidos_table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "GRDLISTCADASTROFRAAPPLISTAGEMCAD"))
        )   
        
        item_pedidos = pedidos_table.find_elements(By.TAG_NAME, "tr")

        info_quantidade_pedido = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "LABINFOREGISTROSFRAAPPLISTAGEMCAD"))
        )

        quantidade_pedido = int(info_quantidade_pedido[0].text.split()[-1])
        iteracao_pedido = int(info_quantidade_pedido[0].text.split()[0])
        
        # Iterar pelas linhas da tabela de pedidos
        for pedido in item_pedidos[1:]:
            pedido.click()
            pedido.click()
            time.sleep(1)

            colunas = pedido.find_elements(By.TAG_NAME, "td")
            
            numero_pedido = colunas[0].text  
            data_pedido = colunas[1].text    
            total_produtos = colunas[2].text  
            taxa_entrega = colunas[3].text  
            valor_total = colunas[4].text  
            situacao = colunas[5].text  
            tipo_entrega = colunas[6].text  
            observacao = colunas[7].text 
            
            tabela_produtos = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "GRDLISTCADASTROFRAAPPITENSPED"))
            ) 
            
            item_produtos = tabela_produtos.find_elements(By.TAG_NAME, "tr")

            for produto in item_produtos[1:]:
                time.sleep(1)
                
                try:
                    driver.execute_script("arguments[0].scrollIntoView();", produto)
                except NoSuchElementException:
                    print("Não conseguiu escrolar")
                
                colunas = produto.find_elements(By.TAG_NAME, "td")
                nome_produto = colunas[1].text
                quantidade = colunas[2].text
                preco_unitario = colunas[3].text
                valor_total_produto = colunas[4].text
                observacao_produto = colunas[5].text

                data.append([
                    numero_pedido, data_pedido, total_produtos, taxa_entrega, valor_total, situacao,
                    tipo_entrega, observacao, nome_produto, quantidade, preco_unitario, valor_total_produto, observacao_produto
                ])

            print(f'Pedidos de numero: {numero_pedido} extraido com sucesso')                

        try:
            
            trocar_pagina_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "BTNPROXIMOFRAAPPLISTAGEMCAD"))
            )
            trocar_pagina_button.click()

            time.sleep(1)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "GRDLISTCADASTROFRAAPPLISTAGEMCAD"))
            )

            if iteracao_pedido == quantidade_pedido:
                print('CHEGAMOS NA ULTIMA PAGINA SAINDO')
                export_data.export_to_csv(data, 'compras.csv')
                break;           
        except NoSuchElementException:
            print("Não há mais páginas para trocar.")
            break 
        