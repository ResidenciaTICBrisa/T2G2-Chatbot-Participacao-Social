# Backlog do Produto
## Escopo do Produto
<p align="justify">&emsp;&emsp;O produto desenvolvido tem como objetivo auxiliar os usuários da plataforma Brasil Participativo.Um dos aspectos-chave do escopo do chatbot é sua capacidade de resolver de forma eficiente as problemas comuns que os usuários possam ter. Isso inclui fornecer respostas rápidas e precisas para perguntas frequentes sobre as políticas, procedimentos e recursos disponíveis na plataforma. Ao oferecer resoluções rápidas, o chatbot tem como objetivo capacitar os usuários com as informações necessárias para se envolver de forma eficaz com a comunidade Brasil Participativo.</p>

## Histórias de Usuário

| ID   | Eu, como | Quero / Preciso / Devo / Gostaria de                                                                    | Para                                                                                                 |
|------|----------|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| US01 | Usuário  | Poder conversar com o Chatbot                                                                           | Tirar dúvidas sobre a plataforma Brasil Participativo                                                |
| US02 | Usuário  | Que o chatbot me fornecesse links para páginas específicas dentro da Plataforma do Brasil Participativo | Encontrar informações relevantes de forma rápida e fácil                                             |
| US03 | Usuário  | Que o chatbot mantivesse a mesma conversa em abas diferentes                                            | Poder continuar interagindo enquanto eu realizo outras atividades                                    |
| US04 | Usuário  | Que o chatbot me permitisse enviar feedback e sugestões de melhorias para o Brasil Participativo        | Contribuir para o aprimoramento da plataforma                                                        |
| US05 | Usuário  | Que o chatbot fosse acessível através de um widget em todas as páginas                                  | Obter acesso rápido e fácil ao suporte enquanto navego pelo site do Brasil Participativo             |
| US06 | Usuário  | Que o chatbot fosse responsivo e me respondesse em menos de 2 minutos                                   | Obter assistência rápida sempre que precisar                                                         |
| US07 | Usuário  | Que o chatbot funcionasse nos principais navegadores: Opera, Firefox e Chrome                           | Poder acessar o Brasil Participativo independentemente do navegador que estou utilizando             |
| US08 | Usuário  | Que o chatbot aderisse às políticas de privacidade e segurança de dados                                 | Garantir a proteção das minhas informações durante as interações com o chatbot                       |
| US09 | Gestor   | Que seja possível obter métricas sobre a satisfação dos usuários ao terminar de usar o chatbot          | Avaliar o desempenho do chatbot                                                                      |
| US10 | Gestor   | Poder ter acesso ao fluxos de conversas                                                                 | Gerenciar as conversas com o usuário                                                                 |
| US11 | Gestor   | Que o chatbot fosse desenvolvido com uma arquitetura escalável                                          | Garantir que o chatbot continue funcionando sem problemas, mesmo com o aumento do número de usuários |
| US12 | Usuário  | Que o chatbot entenda português                                                                         | Facilitar a minha comunicação com ele                                                                |
| US13 | Gestor   | Que houvesse métricas de análise da performance do chatbot                                              | Manutenção e evolução do chatbot                                                                     |
| US14 | Usuário  | Reiniciar a conversa do chatbot, voltando ao primeiro estado                                            | Que possa recomeçar a conversa se necessário                                                         |
| US15 | Usuário  | Que o chatbot funcione quando eu acessar o site do BP pelo celular                                      | Que eu possa conversar com o chatbot usando o celular e o desempenho não seja alterado               |                                                
| US16 | Usuário  | Que o chatbot tenha uma identidade visual                                                               | Que a conversa seja mais agradável e familiar                                                        |
| US17 | Usuário  | Enviar e-mail caso minha dúvida não seja atendida                                                       | Que eu possa me comunicar com alguém que possa solucionar minha dúvida                               |   
| US18 | Usuário  | Que o chatbot esteja disponível 24 horas por dia                                                        | Conversar com ele a qualquer momento                                                                 | 

## Requisitos

<table>
    <tr>
        <td rowspan="13" colspan="3">Funcionais</td>
        <td>RF01</td>	
        <td>O bot precisa interagir com vários usuários ao mesmo tempo</td>
        <td>US04, US07, US12</td>
    </tr>
    <tr>
        <td>RF02</td>
        <td>O bot precisa tirar dúvidas das pessoas acerca do Brasil participativo</td>
        <td>US01, US02, US03</td>
    </tr>
    <tr>
        <td >RF03</td>
        <td>O chatbot precisa fornecer links para páginas que o usuário deseja ir dentro do brasil participativo</td>
        <td>US03</td>
    </tr>
    <tr>
        <td>RF04</td>
        <td>O chatbot terá que auxiliar o usuário com problemas de login</td>
        <td>US01</td>
    </tr>
    <tr>
        <td>RF05</td>
        <td>O chatbot deve manter a conversa mesmo que várias abas estejam abertas, mantendo um fluxo de conversa</td>
        <td>US04</td>
    </tr>
    <tr>
        <td>RF06</td>
        <td>O chatbot deve permitir que os usuários enviem feedback sobre as conversas e melhorias</td>
        <td>US05</td>
    </tr>
    <tr>
        <td>RF07</td>
        <td>O chatbot deve fazer relatórios e ter métricas sobre a satisfação dos usuários</td>
        <td>US10</td>
    </tr>
    <tr>
        <td>RF08</td>
        <td>O chatbot deve permitir que um gestor acesse o fluxo de conversas</td>
        <td>US11</td>
    </tr>
    <tr>
        <td>RF09</td>
        <td>O chatbot precisa entender e conversar em português</td>
        <td>US13</td>
    </tr>
    <tr>
        <td>RF10</td>
        <td>O chatbot deve gerar métricas para avaliar a sua performance/desempenho</td>
        <td>US14</td>
    </tr>
    <tr>
        <td>RF11</td>
        <td>O chatbot deve ter a capacidade de reiniciar a conversa e começá-la do zero</td>
        <td>US15</td>
    </tr>
    <tr>
        <td>RF12</td>
        <td>O chatbot deve ser capaz de fornecer um e-mail de endereço de contato caso a dúvida do usuário não seja respondida</td>
        <td>US19</td>
    </tr>
        <tr>
        <td>RF13</td>
        <td>O chatbot deve ser navegado através de botões na tela</td>
        <td>US18</td>
    </tr>
    <tr>
        <td rowspan="11" colspan="3">Não Funcionais</td>
        <td>RNF01</td>	
        <td>O bot precisa estar disponível 24 horas por dia</td>
        <td>US20</td>
    </tr>
    <tr>
        <td>RNF02</td>
        <td>O acesso ao chatbot precisa ser feito através de um widget</td>
        <td>US06</td>
    </tr>
    <tr>
        <td>RNF03</td>
        <td>O chatbot terá que responder o usuário em menos de 2 minutos</td>
        <td>US07</td>
    </tr>
    <tr>
        <td>RNF04</td>
        <td>O widget do chatbot, precisa ser acessado em todas as páginas</td>
        <td>US06</td>
    </tr>   
    <tr>
        <td>RNF05</td>
        <td>O chatbot deve ser desenvolvido utilizando uma arquitetura escalável para lidar com um aumento no número de usuários</td>
        <td>US12</td>
    </tr>  
    <tr>
        <td>RNF06</td>
        <td>O chatbot deve funcionar nos principais navegadores: Opera, Firefox, Chrome</td>
        <td>US08</td>
    </tr>  
    <tr>
        <td>RNF07</td>
        <td>O chatbot deve aderir às políticas de privacidade e segurança de dados, garantindo a proteção das informações dos usuários durante as interações</td>
        <td>US09</td>
    </tr> 
    <tr>
        <td>RNF08</td>
        <td>O chatbot deve ter um fluxo de conversa intuitivo para o usuário</td>
        <td>US02</td>
    </tr>
    <tr>
        <td>RNF09</td>
        <td>O chatbot deve poder ser acessado tanto no computador (WEB) como no celular (Mobile)</td>
        <td>US16</td>
    </tr>
    <tr>
        <td>RNF10</td>
        <td>O chatbot deve ter uma identidade visual agradável</td>
        <td>US18</td>
    </tr>
        <tr>
        <td>RNF11</td>
        <td>O chatbot deve ter a logo do brasil participativo</td>
        <td>US18</td>
</table>


## Histórico de versão

| Versão |    Data    |                     Descrição                     |     Autor      |
|:------:|:----------:|:-------------------------------------------------:|:--------------:|
|  1.0   | 28/03/2024 |                Criação do Backlog                 | Isaque Augusto |
|  2.0   | 02/04/2024 | Modificação das histórias de usuário e requisitos | Isaque Augusto |
|  2.1   | 15/07/2024 | Atualização das histórias de usuário e requisitos | Arthur Taylor  |