## Customizando o Widget do Bot
Existem várias modificações que podem ser feitas no widget editando os parâmetros no HTML utilizado para adicionar o widget do Chatbot a uma página Web.

**Exemplo:**
```js
window.botpressWebChat.init({
      host: "https://hml-bp-embedded-chatbot.lappis.rocks",
      botId: "chatbot_v2_17",
      extraStylesheet: "https://hml-bp-embedded-chatbot.lappis.rocks/assets/modules/channel-web/style.css",
      layoutWidth: "-",
      showPoweredBy: false,
      enableTranscriptDownload: false, 
      enableConversationDeletion: true,
      enableReset: false,
      showConversationsButton: false,
      botName: "Brasil Participativo",
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
