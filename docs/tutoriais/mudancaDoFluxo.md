# Como mudar os fluxos de um bot

## Logar no painel de admin do botpress

Para criação de um novo bot é nescessário fazer login com email e senha que foram utilizados para criação da conta no botpress, esta conta é a conta de administrador, necessária para a criação de um novo bot 


*adicionar a imagem de login*

## Selecionar o BOT a ser alterado

Para realizar a alteração do fluxo deve ser selecionado o BOT que deve ser alterado, os bots serão exibidos na página inicial do painel de administradr do botpress.

*adicionar a imagem do painel de administrador*

## Mudando os fluxos

Uma vez selecionado o bot será apresentado a tela onde é exibido os fluxos do bot

*inserir imagem do workflow*

*Caso saia da tela de visualização dos fluxos é possíve retornar clicando no primeiro ícone*

*inserir imagem de como voltar ao workflow*

## Modificando um fuxo existente

Por padrão o fluxo exibido será o fluxo main, outros fluxos podem ser acessados ao serem selecionados com o clique esquerdo em cima de seu nome.

*inserir imagem dos diversos flows*

Quando for selecionado o fluxo irá ser exibido na tela, de forma com exibindo todos os nós e transições que compõe o fluxo.

*inserir imagem do fluxo com nodes e transições*

### Como adicionar novos nós

Os nós são os pontos onde as decisões ocorrem(lógicas, po exemplo textos que serão apresentados para o usuário).

Para criar novos nós existem duas opções, existe a possibilidade de criar um novo nó com o primeiro botão das ferramentas, ou então com o clique direito do mouse no fluxo e selecionando a opção para um novo nó.

*inserir imagens para criação dos novos nós*

#### Modificando os nós 

Ao utilizar o clique esquerdo sobre um nó, é possível abrir o inspector deste nó e configurar as suas características, começando com o nome do nó. 

Além da possibilidade de modificar o nome dos nós é possível modificar os comportamentos do BOT, como o que acontecerá quando ocorrer uma entrada neste nó (On enter). Pode ser utilizado também a funcionalidade onde ocorre uma espera pela ação do usuário (On receive). A última funcionalidade do inspector é a funcionalidades de transitions, onde é possível definir como serão feitas as transições do fluxo e como serão feitas. 

*inserir imagens de cada um dos comportamentos*

### Como realizar as transições

Para realizar transições entre os nós, pode ser realizando utilizando os pontos pretos ao lado dos cartões dos nós para conectar à outro, realizando assim uma transição entre estes nós. 

*inserir imagem dos nós*

Outra forma possível seria utilizar a funcionalidade de inspector de um nó e utilizando a aba transictions. 

*inserir imagem do transictions*

### Treinamento 

Após realizar os passos para alteração de fluxo, deve ser realizao o treinamento do bot na parte inferior direita da página do botpress para que sejam refletidas assim as mudanças realizadas.

*Inserir imagem do botão de treinamento*