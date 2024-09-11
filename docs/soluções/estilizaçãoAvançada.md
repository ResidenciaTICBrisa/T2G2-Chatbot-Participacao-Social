# Estilização Avançada do Bot 

## Mudanças Suportadas

Algumas mudanças são feitas e suportadas de forma relativamente simples dentro de alguns arquvios na build do Botpress. Como a posição do widget na página web, o tamanho do widget e o tamanho da janela de texto do bot são alguns exemplos de mudanças que podem ser feitas com alterações em arquivos.

Os principais arquivos para fazer alterações visuais no Botpress estão localizados nos seguintes paths:

- `data/assets/modules/channel-web/default.css`
- `data/assets/modules/channel-web/inject.css`
- `data/assets/modules/channel-web/inject.js`
- `data/assets/modules/channel-web/style.css`

## default.css

O arquivo `default.css` define os estilos básicos e globais do widget de chat do Botpress, controlando a aparência de diversos componentes e garantindo uma experiência de usuário consistente e atraente. Abaixo estão as principais funcionalidades deste arquivo:

1. **Definição de Cores e Variáveis**:
   Define variáveis CSS para cores principais, como fundo, texto e estados de foco e hover. Essas variáveis são usadas ao longo do arquivo para manter consistência no design.

2. **Estilos Globais**:
   Aplica estilos globais ao documento, como margem do corpo, fonte padrão (Roboto), controle de overflow, e regras de box-sizing e outline para todos os elementos.

3. **Personalização de Bolhas de Chat**:
   Estiliza as bolhas de chat, diferenciando a aparência das mensagens enviadas pelo bot e pelo usuário. Também define estilos para a bolha de histórico no emulador.

4. **Botão do Widget**:
   Estiliza o botão flutuante do widget e define comportamentos para estados de foco e hover, garantindo uma interação visualmente agradável.

5. **Container de Chat**:
   Controla o layout e a aparência do container do chat, incluindo a posição fixa na tela, bordas, e estilo do avatar do bot.

6. **Campos de Entrada e Botões**:
   Estiliza campos de entrada, botões de ação, e botões alternativos, utilizando as variáveis de cor e definindo comportamento de hover e focus.

7. **Carregamento e Animações**:
   Define um indicador de carregamento com uma animação de rotação (spin) e várias animações para mostrar e ocultar o chat com transições suaves.


## inject.css

O arquivo `inject.css` é utilizado para definir estilos específicos que são injetados diretamente na página web onde o widget do Botpress está presente. Esse arquivo controla a aparência e o posicionamento do widget, bem como a forma como ele se adapta a diferentes tamanhos de tela. Abaixo estão as principais funcionalidades deste arquivo:

1. **Estilo Geral do Widget**:
   `.bp-widget-web`: Define as propriedades gerais do widget, como posicionamento fixo na tela, tamanho máximo, opacidade e suavização de fontes. Ele garante que o widget fique visível e em uma posição fixa na página.

2. **Posicionamento do Widget**:
   `.bp-widget-widget`: Controla o posicionamento do ícone flutuante do widget no canto inferior direito da página, bem como seu tamanho específico.
   - `.bp-widget-hidden`: Esconde o widget quando necessário, utilizando a propriedade `display: none`.

3. **Configurações de Layout de Conversa**:
   `.bp-widget-convo`: Define o layout da janela de conversa, incluindo posição, largura e altura mínima e máxima. Isso garante que a janela de chat seja exibida corretamente e com as dimensões adequadas.

4. **Layout Lateral do Widget**:
   `.bp-widget-side`: Configura a versão lateral do widget, que ocupa a altura total da página e é fixada à direita. Essa classe é especialmente útil para interfaces que utilizam uma visão expandida do chat.
   `.bp-widget-side.emulator`: Ajusta a altura do widget lateral quando utilizado no modo emulador, garantindo que ele não ultrapasse os limites da tela.

5. **Responsividade**:
   Regras @media para dispositivos com largura máxima de 768px ajustam o widget lateral para ocupar toda a largura da tela em dispositivos móveis, garantindo uma experiência de usuário otimizada em telas menores.

## inject.js
O arquivo `inject.js` é um script JavaScript que lida com a injeção e o gerenciamento dinâmico do widget de chat do Botpress na página web. Ele define funções para configurar, inicializar e enviar eventos para o chat, garantindo que o widget seja integrado e controlado de forma adequada. Abaixo estão as principais funcionalidades deste arquivo:

1. **Compatibilidade Retroativa**:
   Define constantes para garantir que o código seja compatível com versões anteriores, como IDs padrão para o chat e o iframe.

2. **Funções de Utilidade**:
   `_getContainerId(chatId)`: Gera o ID do container do widget com base no ID do chat.
   `_getIframeId(chatId)`: Retorna o ID do iframe com base no ID do chat.
   `_injectDOMElement(tagName, selector, options)`: Cria e injeta um elemento DOM no documento com as opções especificadas.

3. **Geração do HTML do Iframe**:
   `_generateIFrameHTML(host, config)`: Gera o código HTML necessário para criar o iframe do widget de chat, incluindo a URL para carregar o conteúdo e o título configurável.

4. **Referências de Chat**:
   `chatRefs`: Armazena referências aos iframes dos chats para permitir comunicação direta com eles.
   `_getChatRef(chatId)`: Retorna a referência do chat especificado ou uma referência falsa que alerta se o chat não foi inicializado corretamente.

5. **Funções de Configuração e Comunicação**:
   `configure(payload, chatId)`: Configura o chat com base nos parâmetros fornecidos.
   `sendEvent(payload, chatId)`: Envia um evento específico para o chat.
   `sendPayload(payload, chatId)`: Envia um payload personalizado para o chat.
   `mergeConfig(payload, chatId)`: Mescla a configuração atual do chat com novos parâmetros.

6. **Inicialização do Widget**:
   `init(config, targetSelector)`: Inicializa o widget de chat, injetando o iframe e o CSS necessários na página, e armazenando uma referência ao iframe para interações futuras.

7. **Interação com Mensagens**:
   Um listener de eventos (`window.addEventListener('message', function(payload) {...}`) é configurado para reagir a mensagens recebidas pelo widget, permitindo alterações dinâmicas, como a classe do iframe ou a largura do widget, conforme necessário.

## style.css
O arquivo `style.css` é utilizado para definir e personalizar o estilo visual do widget de chat do Botpress. Ele contém regras CSS que afetam diversos elementos do widget, desde a aparência geral até detalhes mais específicos, como cores, tamanhos, bordas e comportamento responsivo. Abaixo está um resumo das principais funções e capacidades deste arquivo, vale ressaltar que dentro do snippet esse é o arquivo que será usado no parâmetro:
```bash
extraStylesheet: "http://localhost:3000/assets/modules/channel-web/style.css",
```

1. **Fontes e Direção do Texto**: Define o tamanho padrão da fonte para o documento e a direção do texto (esquerda para a direita) para parágrafos e mensagens de entrada.

2. **Cores e Estilos de Texto**: Modifica cores de texto, placeholders, e indicadores de novas mensagens, garantindo que a interface mantenha uma paleta de cores coerente e alinhada com o design desejado.

3. **Layout do Chat**: Estabelece o layout da interface de chat, incluindo a largura, altura, margens, e arredondamento de bordas das bolhas de chat e da janela do chat. Inclui também regras para design responsivo, ajustando o layout para diferentes tamanhos de tela.

4. **Estilização de Elementos de Interface**: Personaliza vários elementos da interface, como o cabeçalho do chat, bolhas de digitação, botões, avatares, e barras de rolagem, utilizando cores específicas, bordas, e preenchimento.

5. **Animações e Efeitos**: Inclui regras para animações, como a mudança de cor de ícones e botões durante interações do usuário (por exemplo, quando o botão é pressionado ou quando o cursor passa sobre ele).

6. **Elementos de Identidade Visual**: Adiciona estilos específicos para seções como o "powered by" e ícones flutuantes, garantindo que todos os aspectos da interface reflitam a identidade visual escolhida.

7. **Scrollbars**: Personaliza a aparência das barras de rolagem tanto na janela do chat quanto no restante da página, conferindo uma estética coesa.



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
|  1.0   | 14/08/2024 |           Documentação dos arquivos de customização                        |  Gabriel Scheidt   |
|  1.0   | 27/06/2024 |           Criação do documento                        |  Arthur Taylor   |
