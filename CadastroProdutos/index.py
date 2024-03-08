####################################################################
# Objetivo do projeto: Automação de cadastros de produtos
# Data: 05/03/24
# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer login
# Passo 3: Importar abase de dados
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o processo até acabar a base de dados
####################################################################

## pip install pandas numpy openpyxl
## pip install pyautogui
import pyautogui
import pandas
import time

## Pausa entre comandos
pyautogui.PAUSE = 0.5

## Abrindo o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

pyautogui.press("enter")

## Pausa de 3 segundos para o carregamento da página
time.sleep(3)

## Corrdenadas do input
pyautogui.click(x=663, y=464)
pyautogui.write("juliasoaresdealmeidaj@gmail.com")

pyautogui.press("tab")
pyautogui.write("123456")

## Botão de logar
pyautogui.click(x=911, y=683)
time.sleep(3)

## Import da base de dados
tabela = pandas.read_csv("produtos.csv")

## Condição de autopreenchimento
for linha in tabela.index:

    pyautogui.click(x=991, y=329)

    ## Código
    ### Pegando dados da tabela
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    ## Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    ## Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    ## Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    ## Preço
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    ## Custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    ## Obs
    obs = tabela.loc[linha, "obs"]

    ## Tratamento de condição if not
    if not pandas.isna(obs):
        pyautogui.write(obs)
           
    pyautogui.press("tab")

    ## Enviando o formulário
    pyautogui.press("enter")

    ## Retornando ao inicio da tela
    pyautogui.scroll(5000)

