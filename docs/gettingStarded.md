# Getting Started

Siga estes passos para configurar seu ambiente e começar:

## Passo 1: Instalar o Python

1. Acesse o [site oficial do Python](https://www.python.org/downloads/) para baixar e instalar o Python em seu computador.
2. Durante o processo de instalação, certifique-se de marcar a opção "Adicionar Python ao PATH" para poder executar o Python facilmente pelo terminal ou prompt de comando.

## Passo 2: Instalar Bibliotecas Necessárias

Abra o terminal ou prompt de comando e execute os seguintes comandos para instalar as bibliotecas necessárias:

```bash
pip install python-telegram-bot
pip install python-dotenv
pip install os
```

## Passo 3: Configurar Seu Bot no Telegram

1. Entrar em contato com o [@BotFather](https://web.telegram.org/k/#@BotFather) no Telegram.

2. No chat com o BotFather, use o comando "/newbot" para criar um novo bot.

3. Siga as instruções para fornecer um nome e um username para o seu bot.

4. Após a criação, o BotFather irá fornecer um token para o seu bot. Guarde esse token pois será utilizado no código Python.

## Passo 4: Configurando o ambiente

Siga estes passos para clonar o repositório, configurar o token do Telegram no arquivo `.env` e executar o bot do Telegram.

### Clonar o Repositório

1. Abra o terminal ou prompt de comando.
2. Clone o repositório usando o comando:

    ```bash
    git clone https://github.com/ResidenciaTICBrisa/T2G2-Chatbot-Participacao-Social
    ```
### Acessar a Branch 'bot_telegram'

1. Mude para a branch bot_telegram com o comando:

    ```bash
    git checkout bot_telegram
    ```

### Configurar o Arquivo .env
1. Crie um arquivo .env no diretório raiz do projeto.
2. Abra o arquivo .env com seu editor de texto preferido.
3. Adicione a seguinte linha ao arquivo .env e substitua SEU_TELEGRAM_TOKEN pelo token fornecido pelo BotFather:

    ```bash
    TELEGRAM_TOKEN= 'SEU_TELEGRAM_TOKEN'
    ```

## Passo 5: Executar o Bot do Telegram
1. Certifique-se de que você está no diretório do projeto.
2. Certifique-se de que você está na branch 'bot_telegram' com o comando:

    ```shell
    git checkout
    ```

3. Execute o script Python para iniciar o bot do Telegram:

    ```bash
    python chatbot.py
    ```

O bot do Telegram deve estar agora em execução e pronto para interagir com os usuários.

Parabéns! Você configurou e executou com sucesso o bot do Telegram.

# Histórico de versão

| Versão |    Data    |                       Descrição                       |      Autor       |
| :----: | :--------: | :---------------------------------------------------: | :--------------: |
|  1.0   | 03/04/2024 |           Criação do documento               |  Gabriel Zaranza |