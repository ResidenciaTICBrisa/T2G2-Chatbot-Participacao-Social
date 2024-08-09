# Estilização Avançada do Bot 

## Mudanças Suportadas

Algumas mudanças são feitas e suportadas de forma relativamente simples dentro de alguns arquvios na build do Botpress. Como a posição do widget na página web, o tamanho do widget e o tamanho da janela de texto do bot são alguns exemplos de mudanças que podem ser feitas com alterações em arquivos.

## Mudanças NÃO Suportadas (Convencionalmente)

As mudanças acima podem ser feitas com a modificação de alguns arquivos existentes dentro da build do botpress, sendo nescessário apenas o clone do repositório e modificação. Mas algumas outras cutomizações que podem ser de interesse do usuário são de certa forma "bloqueadas" pela build do Botpress.

O widget gerado pelo Botpress para ser utilizado em canais web é gerado por um arquivo Javascript, uma vez que a build do projeto ocorre este widget passa a ter alguns pontos não modificáveis como a imagem dentro do widget e a escrita no final da janela de converasção do bot. Estas configurações são definidas no momento da build, e após este momento não é mais possível realizar alterações.

Para realizar alterações nestas configurações estas alterações devem ser realizadas antes do momento do botpress ter o comando "yarn build" executado, para isso se faz nescessário acesso ao código fonte do botpress, sendo possível assim definir como será o novo "padrão" modificando de acordo com a nescessidade visual dentro de um projeto. 

### Chatbot para o Brasil Participativo

Algumas mudanças como as descritas acimas foram nescessárias para que o design do bot ficasse de acordo com o [design](https://residenciaticbrisa.github.io/T2G2-Chatbot-Participacao-Social/guiaDeEstilo/) feito pelo cliente, para isso se fez nescessário a modificação de alguns arquivos fonte do Botpress como indicado no tópico acima, o repositório com as modificações pode ser encontrado [aqui](https://github.com/ResidenciaTICBrisa/T2G2-Chatbot-Botpress)


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
