## Customizando o Widget do Bot
Existem várias modificações que podem ser feitas no widget editando os parâmetros no HTML utilizado para adicionar o widget do Chatbot a uma página Web.

**Exemplo:**
```js
window.botpressWebChat.init({
      host: "host",
      botId: "iddobot",
      extraStylesheet: "caminho/para/o/style.css",
      layoutWidth: "-",
      showPoweredBy: false,
      enableTranscriptDownload: false, 
      enableConversationDeletion: true,
      enableReset: false,
      showConversationsButton: false,
      botName: "Nome do Bot",
      enablePersistHistory: false});
```
### Mostrar a mensagem "Powered By:"
**showPoweredBy:** false/true. Se o valor for false, a mensagem não será mostrada no "footer" (parte de baixo) do chat. Se o valor for true, a mensagem será mostrada.
### Mostrar o botão de "Baixar Transcrição da Conversa"

**enableTranscriptDownload:** false/true. Se o valor for false, o botão de baixar o histórico da conversa não será mostrado. Caso seja true, o botão é mostrado.
### Mostrar o botão de "Apagar conversa"
**enableConversationDeletion:** false/true. Se o valor for false, o botão de apagar conversa não será mostrado. Caso seja true, o botão é mostrado.
### Mostrar o botão de "Resetar a conversa"
**enableReset:** false/true. Se o valor for false, o botão de resetar a conversa não será mostrado, caso seja true, o botão é mostrado no canto direito superior do chat.
### Mostrar o botão de "Visualizar transcrição de conversa"
**showConversationsButton:** false/true. Se o valor for false, o botão de visualizar transcrição não será mostrado. Caso o valor seja true, o botão é mostrado no canto superior direito do chat.
### Nome do bot
**botName:** texto. Esse campo é resposável pelo nome do bot.
### Habilitar a persistência das mensagens
**enablePersistHistory:** false/true. Se o valor for false, as mensagens não são salvas persistentemente, caso o valor seja true as mensagens enviadas são salvas no armazenamento local do bot (restaura mensagens anteriores).

### Onde Buscar Informações

Para informações sobre a customização: [Documentação sobre a customização](https://botpress.com/docs/webchat)


Se você está utilizando ou explorando o Botpress versão 12, aqui estão alguns recursos importantes para ajudar na sua jornada:

- **Documentação Oficial (v12:latest):** Para acessar a documentação mais recente do Botpress v12, visite [Documentação Botpress v12:latest](https://v12.botpress.com/).

- **Documentação Botpress v12.26.7:** Caso esteja trabalhando especificamente com a versão v12.26.7, a documentação correspondente pode ser encontrada em [Documentação Botpress v12.26.7](http://botpress-docs.s3-website-us-east-1.amazonaws.com/docs/introduction/).

- **Repositório no GitHub:** Para acessar o código-fonte e contribuir para o desenvolvimento, acesse o repositório oficial do Botpress v12 no GitHub: [GitHub Botpress v12](https://github.com/botpress/v12).

Certifique-se de explorar esses recursos para obter todas as informações necessárias sobre o Botpress e seu uso!

| Versão |    Data    |                       Descrição                       |     Autor      |
| :----: | :--------: | :---------------------------------------------------: |:--------------:|
|  1.0   | 14/08/2024 |           Criação do documento                        | Isaque Augusto |