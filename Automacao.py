# Automação de preenchimento de dados em Sistemas, automação de primeiro plano.

import pyautogui # Biblioteca de Automação
import time # Biblioteca de Delay
import pandas # Biblioteca de Base de Dados

# Observação, este código foi realizado com um monitor 24" esta informação é referente ao posicionamento do mouse, para executar a automação, sem inspecionar o código html.

pyautogui.PAUSE = 0,5 # Delay para carregar a automação.

# Open Chrome
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

# Navegador Chrome
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Aguardar Carregamento da Página Web
time.sleep(3)

# login
pyautogui.click(x=757, y=378)
pyautogui.write("teste123@teste123.com.br")
pyautogui.press("tab")
pyautogui.write("123456")
piautogui.click(x=951, y=541)

# Aguardar Carregamento da Página Web
time.sleep(3)

planilha = pandas.read_csv("produtos.csv")

# Cadastro de Produtos.
pyautogui.click(x=653, y=294)

# Para cada linha de minha planilha execute:
for linha in planilha.index:

    codigo = "MOLO000251"
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = "Logitech"
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = "Mouse"
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = "1"
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preço_unitario = "25.95"
    pyautogui.write(preço_unitario)
    pyautogui.press("tab")

    custo = "6.50"
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = ""
    pyautogui.press("tab")

    pyautogui.press("enter")

    # Voltar posição para a de início na tela.
    pyautogui.scroll(5000)

# DICAS ----------------

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

# ----------------------