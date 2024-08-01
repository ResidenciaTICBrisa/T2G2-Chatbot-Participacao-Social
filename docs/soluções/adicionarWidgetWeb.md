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

Importância da Documentação Original

Esta documentação visa facilitar alguns processos básicos, mas é indispensável utilizar a documentação original para uma personalização completa.

Para mais informações sobre como personalizar o widget na sua página, consulte a página oficial do Botpress:
[Botpress Webchat Website Embedding](https://v12.botpress.com/messaging-channels/botpress-webchat/website-embedding/)