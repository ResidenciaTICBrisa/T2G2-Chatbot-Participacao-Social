# Mudando o Banco de Dados 

## Bancos de dados suportados

O botpress vem por padrão configurado com um banco de dados SQLite, um banco simples para armazenamento dos dados dos bots criados e dados sobre a utilização deles, o SQLite é um banco mais leve e menos robusto, podendo ser utilizado para aplicações que demandem menos requisições do bot. 

No próprio site do botpress recomendam a migração do banco de dados para o PostgreSQL para colocar o bot em produção dependendo da escala em que o mesmo será usado.

O PostgreSQL é um banco de dados mais robusto e passa uma maior confibilidade, além disso pode ser utilizado um SGBD como o PGadmin, Adminer ou outros SGBD's, facilitando a vizualização dos dados assim gravados, e também garantindo o funcionamento correto do Banco.

## Decisão pela migração

A migração foi uma decisão tomada devido ao grande número de acessos diários ao site Brasil Participativo, onde o bot será utilizado, com isso a migração se faz nescessária para um banco de dados mais robusto e onde possamos acompanhar os dados gerados de uma forma mais simples (PGadmin).

## O processo de migração

Para realizar a migração do banco de dados do Botpress basta criar uma base de dados postgress e garantir o acesso à essa base de dados com um usuário capaz de criar tabelas. Deve ser informado de forma correta (explicado a seguir) no botpress o usuário, senha e database que deve ser acessado para que sejam criadas de forma correta as tabelas nescessárias.

### Formas de informar a URL do banco

Como dito acima o database do banco de dados deve ser informado através do seguinte comando:
```
DATABASE_URL=postgres://login:password@your-db-host.com:5432/your-db-name
```
Alguns parametros devem ser passados corretamente no comando acima para que o banco seja corretamente alterado e as tabelas criadas, modifique o comando informando conforme descrito abaixo:
- login: nome de usuário que deve seracessado
- password: senha para acesso do banco através do login informado
- @your-db-host.com: URL para o local onde o banco de dados está hospedado (localhost, ip externo...)
- :5432: porta onde o banco deve ser acessado (5432 é a porta padrão do serviço postgres)
- your_db_name: nome da base de dados onde as tabelas deverão ser criadas (certifique que o usuário pode criar tabelas nesta base de dados)

#### Utilizando Docker

Se no projeto de contrução do bot estiver sendo utilizado a ferramenta Docker, esta variável pode ser informada diretamente dentro do arquivo docker-compose.yml, na parte de enviroment do banco.

#### Utilizando .env

Se o projeto não estiver utilizando o Docker a URL da base de dados pode ser informada através de um arquivo .env na pasta raiz do projeto, isso faŕa com que a base de dados seja acessado de forma correta.

### Onde Buscar Informações

Se você está utilizando ou explorando o Botpress versão 12, aqui estão alguns recursos importantes para ajudar na sua jornada:

- **Documentação Oficial (v12:latest):** Para acessar a documentação mais recente do Botpress v12, visite [Documentação Botpress v12:latest](https://v12.botpress.com/).

- **Documentação Botpress v12.26.7:** Caso esteja trabalhando especificamente com a versão v12.26.7, a documentação correspondente pode ser encontrada em [Documentação Botpress v12.26.7](http://botpress-docs.s3-website-us-east-1.amazonaws.com/docs/introduction/).

- **Repositório no GitHub:** Para acessar o código-fonte e contribuir para o desenvolvimento, acesse o repositório oficial do Botpress v12 no GitHub: [GitHub Botpress v12](https://github.com/botpress/v12).

Certifique-se de explorar esses recursos para obter todas as informações necessárias sobre o Botpress e seu uso!

## Histórico de versão

| Versão |    Data    |                       Descrição                       |      Autor       |
| :----: | :--------: | :---------------------------------------------------: | :--------------: |
|  1.0   | 27/06/2024 |           Criação do documento                        |  Arthur Taylor   |
