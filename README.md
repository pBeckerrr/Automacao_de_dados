# Automação de Preenchimento de Dados em Sistemas

Este é um script de automação desenvolvido em Python para preencher automaticamente formulários em sistemas web utilizando o PyAutoGUI e base de dados Pandas. A automação é executada em **primeiro plano**, interagindo diretamente com a interface do usuário (sem inspeção de elementos HTML), ideal para testes, cadastros repetitivos ou simulações de uso real.

## Visão Geral

A automação realiza os seguintes passos:

- **Abertura do navegador:** Inicia o Google Chrome e acessa o site de login.
- **Login automático:** Preenche automaticamente o e-mail e senha.
- **Leitura da planilha:** Importa dados de um arquivo `CSV` contendo os produtos a serem cadastrados.
- **Preenchimento automático:** Para cada linha da planilha, preenche o formulário no site com os dados correspondentes.
- **Scroll automático:** Após o envio, a tela volta para o topo para continuar a automação.

## Tecnologias Utilizadas

* **PyAutoGUI:** Biblioteca Python para automação de mouse, teclado e telas.
* **Pandas:** Biblioteca Python para manipulação de dados e leitura de arquivos CSV.
* **Time:** Biblioteca nativa do Python para controle de tempo e delays.

## Pré-requisitos

Antes de executar a automação, certifique-se de ter o Python instalado e as bibliotecas necessárias.

```bash
pip install pyautogui
pip install pandas
