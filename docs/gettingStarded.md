# Getting Started

Este projeto foi desenvolvido no Ubuntu LTS 22.04. Pode funcionar em outros sistemas operacionais, mas ainda não foi testado. Para rodar o projeto, siga as instruções abaixo:

## Pré-requisitos
Certifique-se de estar com o sistema atualizado, no terminal rode o seguinte comado:
```bash
    sudo apt update && sudo apt upgrade
```
Antes de iniciar, certifique-se de que você tenha os seguintes softwares instalados na sua máquina:

- Git [guia de instalação](https://git-scm.com/download/linux)
- Docker e docker compose [guia de instalação](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

## Passo 2: Clonar o Repositório

1. Abra o terminal ou prompt de comando.
2. Clone o repositório usando o comando:

```bash
    git clone https://github.com/ResidenciaTICBrisa/T2G2-Chatbot-Participacao-Social
```

## Passo 3: Configurar o Arquivo .env
1. Crie um arquivo .env no diretório raiz do projeto.
2. Abra o arquivo .env com seu editor de texto preferido.
3. Adicione a seguintes linhas ao arquivo .env e substitua os '*' pelas credenciais que deseja criar no botpress:

    ```bash
        #Credenciais do postgres
        POSTGRES_DB= * #Nome do dbanco de dados
        POSTGRES_USER= * #Usuário postgress
        POSTGRES_PASSWORD= * #Senha do usuário postgres

        #Credenciais da conta de administrador do pgadmin
        PGADMIN_DEFAULT_EMAIL= * #email do usuário pgadmin
        PGADMIN_DEFAULT_PASSWORD= * #Senha do usuário pgadmin

        #Credencias da conta administrador do botpress
        BOTPRESS_ADMIN_EMAIL= * #Email da conta administrador
        BOTPRESS_ADMIN_PASSWORD=* #Senha da conta administrador
    ```
## Passo 4: Executar o docker compose
De o seguinte comando para rodar o sistema:
```bash
    docker compose -f docker-compose-local.yml up
```

## Passo 5: Acessar o sistema
Se tudo tiver sido da forma adequada, acesse o projeto através do 
[http://localhost:3000](http://localhost:3000)

# Histórico de versão

| Versão |    Data    |                       Descrição                       |      Autor       |
| :----: | :--------: | :---------------------------------------------------: | :--------------: |
|  1.0   | 03/04/2024 |                  Criação do documento                 |  Gabriel Zaranza |
|  1.1   | 15/07/2024 |               Atualização para versão atual           |   Arthur Taylor  |