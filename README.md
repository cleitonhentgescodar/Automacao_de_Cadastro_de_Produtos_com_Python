# 🤖 RPA em Python para Automação de Cadastro de Produtos

Este projeto consiste em uma automação desenvolvida em Python que realiza o cadastro automático de produtos em um sistema web, simulando exatamente as ações que um usuário humano faria, como abrir o navegador, digitar informações, navegar com TAB e clicar em botões. A automação lê os dados de um arquivo CSV e cadastra os produtos um a um, eliminando tarefas manuais repetitivas.

> 📚 Projeto desenvolvido com base em uma aula ao vivo da Hashtag Treinamentos sobre automações com Python e PyAutoGUI.

## 🚀 Tecnologias Utilizadas
- Python 3
- PyAutoGUI
- Pandas
- Google Chrome

## 📂 Estrutura do Projeto
📁 projeto-automacao  
├── produtos.csv — Base de dados com os produtos  
├── automacao.py — Script principal da automação  
└── README.md — Documentação do projeto  

## 🧠 Como a Automação Funciona
1. Abre o navegador Google Chrome  
2. Seleciona o perfil do usuário  
3. Acessa o sistema web  
4. Realiza login automaticamente  
5. Lê os dados do arquivo produtos.csv  
6. Para cada produto:  
   - Preenche o formulário  
   - Envia o cadastro  
   - Volta ao topo da página  
7. Repete o processo até finalizar a lista  

## 📊 Formato do Arquivo CSV
Colunas esperadas:
- codigo  
- marca  
- tipo  
- categoria  
- preco_unitario  
- custo  
- obs (opcional)  

Exemplo:
codigo,marca,tipo,categoria,preco_unitario,custo,obs  
1234,Nike,Tênis,Calçados,299.90,150.00,Promoção  

## ⚠️ Observações Importantes
- As coordenadas do mouse (x, y) precisam ser ajustadas conforme o monitor  
- Os tempos de espera podem variar conforme o computador e a internet  
- Durante a execução da automação, não utilize o mouse ou teclado  

## ▶️ Como Executar o Projeto
1. Instale as dependências:
pip install pyautogui pandas  

2. Ajuste as configurações no código (tempo, coordenadas, login)  

3. Execute o script:
python automacao.py  

## 📚 Fonte de Estudo
🎥 Automação de Tarefas com Python | Hashtag Treinamentos  
https://www.youtube.com/live/ts986Np0kNw  

## ✨ Objetivo do Projeto
- Praticar automação de processos (RPA)  
- Aprender a transformar tarefas manuais em código  
- Demonstrar conhecimentos em Python para portfólio  

## 🧑‍💻 Autor
Projeto desenvolvido para fins educacionais e de aprendizado em automação com Python.
