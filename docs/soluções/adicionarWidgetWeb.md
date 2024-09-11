## Adicionando o Widget do Bot à sua Página

Para adicionar o widget do seu bot à sua página, basta incluir o trecho de código HTML abaixo na página desejada. Este código já estará funcional. Existem diversas configurações que podem ser feitas diretamente no HTML, então recomendamos fortemente a consulta à documentação oficial para ajustes mais avançados.

```html
<script src="<sua-url-aqui>/assets/modules/channel-web/inject.js"></script>

<script>
  window.botpressWebChat.init({
    host: "<sua-url-aqui>",
    botId: "<id-bot>"
    extraStylesheet: "<sua-url-aqui>/assets/modules/channel-web/style.css"
  })
</script>
```
## Script Recomendado

Recomendamos o uso do script abaixo. Com ele, você poderá modificar o arquivo localizado em extraStylesheet:"<sua-url-aqui>/assets/modules/channel-web/style.css", adicionando elementos de CSS para customizar seu widget de acordo com as necessidades do seu site. Além disso, o widget já estará configurado para iniciar com uma mensagem automática quando clicado pelo usuário.


```html
<script src="<sua-url-aqui>/assets/modules/channel-web/inject.js"></script>

<script>
  window.botpressWebChat.init({
    host: "<sua-url-aqui>",
    botId: "<id-bot>",
    extraStylesheet: "<sua-url-aqui>/assets/modules/channel-web/style.css"
  });

  window.addEventListener('message', function(event) {
    if (event.data.name === 'webchatReady') {
      window.botpressWebChat.sendEvent({
        type: 'proactive-trigger',
        channel: 'web',
        payload: { text: 'oi' }
      });
    }
  });
</script>
```

### Onde Buscar Informações

Se você está utilizando ou explorando o Botpress versão 12, aqui estão alguns recursos importantes para ajudar na sua jornada:

- **Documentação Oficial (v12:latest):** Para acessar a documentação mais recente do Botpress v12, visite [Documentação Botpress v12:latest](https://v12.botpress.com/).

- **Documentação Botpress v12.26.7:** Caso esteja trabalhando especificamente com a versão v12.26.7, a documentação correspondente pode ser encontrada em [Documentação Botpress v12.26.7](http://botpress-docs.s3-website-us-east-1.amazonaws.com/docs/introduction/).

- **Repositório no GitHub:** Para acessar o código-fonte e contribuir para o desenvolvimento, acesse o repositório oficial do Botpress v12 no GitHub: [GitHub Botpress v12](https://github.com/botpress/v12).

Certifique-se de explorar esses recursos para obter todas as informações necessárias sobre o Botpress e seu uso!


| Versão |    Data    |                       Descrição                       |      Autor       |
| :----: | :--------: | :---------------------------------------------------: | :--------------: |
|  1.0   | 09/08/2024 |           Criação do documento                        |  Gabriel Scheidt  |