import pyautogui
from time import sleep


# 1- Clicar e digitar meu usuario
pyautogui.click(753,374,duration=2)
pyautogui.write('matheus')
# 2- clicar e digitar minha senha 
pyautogui.click(746,401,duration=2)
pyautogui.write('123456')
# 3- Clicar em "Entrar"
pyautogui.click(667,428,duration=2)
# 4- Extrari cada produto 
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        # 1- clicar e digitar produto 
        pyautogui.click(690,358,duration=2)
        pyautogui.write(produto)
        # 2- clicar e digitar quantidade
        pyautogui.click(691,382,duration=2)
        pyautogui.write(quantidade)
        # 3 - clicar e digitar quantidade
        pyautogui.click(696,408,duration=2)
        pyautogui.write(preco)
        #4 - clicar em registrar
        pyautogui.click(611,565,duration=1)
        sleep(1)
     

      # 4-- Clicar em registar