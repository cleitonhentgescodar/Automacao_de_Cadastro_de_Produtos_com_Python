# IMPORTAÇÃO DAS BIBLIOTECAS

# Biblioteca para controlar tempo (esperas)
import time

# Biblioteca para leitura e manipulação de dados (CSV)
import pandas as pd

# Biblioteca para automação de mouse e teclado
import pyautogui
#_____________________________________________________________________

# CONFIGURAÇÕES GERAIS DA AUTOMAÇÃO

# Pausa automática entre todos os comandos do pyautogui
# Isso deixa a automação mais estável e parecida com ações humanas
pyautogui.PAUSE = 0.5

# Endereço do sistema onde os produtos serão cadastrados
URL_LOGIN = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Credenciais de acesso ao sistema
EMAIL = "pythonimpressionador@gmail.com"
SENHA = "sua senha muito muito dificilima"

# Caminho do arquivo CSV que contém os produtos
ARQUIVO_CSV = "produtos.csv"
#_____________________________________________________________________

# AJUSTES DE TEMPO E NAVEGAÇÃO (dependem do computador)

# Tempo de espera para o Chrome abrir completamente
TEMPO_ABRIR_CHROME = 2

# Tempo de espera para páginas carregarem
TEMPO_CARREGAR_PAGINA = 5

# Quantidade de TABs necessárias para selecionar o perfil do Chrome
TABS_ATE_PERFIL_CHROME = 7
#_____________________________________________________________________

# COORDENADAS DE TELA (dependem do monitor)

# Posição do campo "Código" no formulário de cadastro
CAMPO_CODIGO_X = 825
CAMPO_CODIGO_Y = 266

# Valor alto para garantir que a tela volte ao topo após o cadastro
SCROLL_SUBIR = 10_000

#_____________________________________________________________________

# FUNÇÕES AUXILIARES

def abrir_chrome():
    """
    Abre o navegador Google Chrome utilizando o menu iniciar.
    Simula exatamente o que uma pessoa faria manualmente.
    """
    pyautogui.press("win")       # Abre o menu iniciar
    pyautogui.write("chrome")    # Digita "chrome"
    pyautogui.press("enter")     # Abre o navegador
    time.sleep(TEMPO_ABRIR_CHROME)  # Aguarda o Chrome abrir


def selecionar_perfil_chrome():
    """
    Seleciona o perfil correto do Chrome usando a tecla TAB.
    A quantidade de TABs pode variar conforme o computador.
    """
    pyautogui.press("tab", presses=TABS_ATE_PERFIL_CHROME)
    pyautogui.press("enter")


def acessar_pagina(url: str):
    """
    Acessa uma página da internet digitando a URL na barra de endereço.
    """
    pyautogui.write(url)
    pyautogui.press("enter")
    time.sleep(TEMPO_CARREGAR_PAGINA)  # Aguarda carregamento da página


def fazer_login(email: str, senha: str):
    """
    Realiza o login no sistema:
    - Preenche email
    - Preenche senha
    - Clica no botão de entrar
    """
    pyautogui.press("tab")        # Vai para o campo de email
    pyautogui.write(email)

    pyautogui.press("tab")        # Vai para o campo de senha
    pyautogui.write(senha)

    pyautogui.press("tab")        # Vai para o botão "Entrar"
    pyautogui.press("enter")      # Confirma o login
    time.sleep(TEMPO_CARREGAR_PAGINA)


def carregar_dados(caminho_csv: str) -> pd.DataFrame:
    """
    Lê o arquivo CSV com os produtos e retorna uma tabela (DataFrame).
    """
    return pd.read_csv(caminho_csv)


def cadastrar_produto(registro: pd.Series):
    """
    Cadastra UM produto no sistema.
    Cada chamada dessa função corresponde a uma linha do CSV.
    """

    # Garante que o cursor esteja no primeiro campo do formulário
    pyautogui.click(x=CAMPO_CODIGO_X, y=CAMPO_CODIGO_Y)

    # Preenchimento sequencial dos campos do formulário
    pyautogui.write(str(registro["codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(registro["marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(registro["tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(registro["categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(registro["preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(registro["custo"]))
    pyautogui.press("tab")

    # Campo opcional: só preenche se não estiver vazio
    obs = registro.get("obs")
    if pd.notna(obs):
        pyautogui.write(str(obs))

    # Envia o formulário (cadastra o produto)
    pyautogui.press("tab")
    pyautogui.press("enter")

    # Volta a tela para o topo para o próximo cadastro
    pyautogui.scroll(SCROLL_SUBIR)

#_____________________________________________________________________

# CÓDIGO PRINCIPAL (FLUXO DA AUTOMAÇÃO)

def main():
    """
    Função principal.
    Define a ordem exata das ações que a automação deve executar.
    """

    # 1. Abrir o navegador
    abrir_chrome()

    # 2. Selecionar o perfil correto do Chrome
    selecionar_perfil_chrome()

    # 3. Acessar o sistema da empresa
    acessar_pagina(URL_LOGIN)

    # 4. Fazer login no sistema
    fazer_login(EMAIL, SENHA)

    # 5. Carregar a base de dados de produtos
    dados = carregar_dados(ARQUIVO_CSV)

    # (opcional) Mostrar os dados no terminal para conferência
    print(dados)

    # 6. Loop: para cada produto do CSV, cadastrar no sistema
    for _, registro in dados.iterrows():
        cadastrar_produto(registro)

#_____________________________________________________________________

# PONTO DE ENTRADA DO PROGRAMA

# Garante que a automação só rode se este arquivo
# for executado diretamente (e não importado)
if __name__ == "__main__":
    main()