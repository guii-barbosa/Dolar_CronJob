import psycopg2
from psycopg2 import Error
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time
from dotenv import load_dotenv
import os

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-headless")  # Executar o Chrome em modo headless (sem janela visível)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://economia.uol.com.br/cotacoes/cambio/")
time.sleep(2)

data_hora = datetime.now() 
data = data_hora.strftime("%Y-%m-%d")
hora = data_hora.strftime("%H:%M:%S")

cotacao_dolar = driver.find_element(By.XPATH, '/html/body/div[3]/article/div[2]/div/div[1]/div/div/div[3]/section/div[1]/div/div[2]/div/input').get_attribute('value')
cotacao_dolar = float (cotacao_dolar.replace(',', '.'))

connection=None
try:
    connection = psycopg2.connect(user=os.getenv("USER"),
                                    password=os.getenv("PASSWORD"),
                                    host=os.getenv("HOST"),
                                    port=os.getenv("PORT"),
                                    database=os.getenv("DATABASE"))
   
    print("conexão estabelecida com sucesso!")
    cursor = connection.cursor()
    
    cursor.execute('CALL INSERIR_VALOR_DOLAR(%s, %s, %s)', (data, hora, cotacao_dolar))
    connection.commit()
    print("Dados inseridos com sucesso!")

except (Exception, Error) as error:
    print("Erro ao inserir os dados:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Conexão encerrada.")