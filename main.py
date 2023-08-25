import os
import login
import extract_data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def clear_console():
    os.system('cls')


def show_menu():
    print('Selecione a opção: ')
    print('1 - Extrair dados do site')
    print('2 - Sair do console')

def main():
    while True:
        show_menu()
        choice = int(input('Opção: '))

        print(type(choice))

        if(choice == 1):
            clear_console()
            print('Opção 1 foi escolhida')

            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu') 
            driver = webdriver.Chrome(options=chrome_options)
            driver.maximize_window();
            
            login.login(driver)
            extract_data.extract_data(driver)
            
        
        elif(choice == 2):
            clear_console()
            print('Saindo do console')
            break;
        else:
            clear_console()
            print("Opção Invalida. Escolha novamente")


if __name__ == '__main__':
    main()