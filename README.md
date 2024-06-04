
<p align="center">
  <img src="https://github.com/ResidenciaTICBrisa/T2G2-Chatbot-Participacao-Social/blob/main/site/images/rasinha_logo.jpeg" width="190" />
</p>

# Projeto Chatbot para Brasil Participativo

<!-- badges -->
<a href="https://www.gnu.org/licenses/agpl-3.0.html"><img src="https://img.shields.io/badge/licence-AGPL3-green.svg"/></a>
<a href="https://botpress.com/docs/cloud/"><img src="https://img.shields.io/badge/Botpress-v12-blue.svg"/></a>

Bem-vindo ao repositório oficial do projeto Chatbot para o Brasil Participativo! Este projeto faz parte de uma iniciativa para enriquecer a experiência na plataforma digital do Brasil Participativo, uma plataforma de participação social do governo federal.

---
<!-- Links uteis: -->
* **O que é a Chatbot para Brasil Participativo?** [Conheça o Projeto](#sobre-o-projeto-chatbot)
* **Para ver a documentação com mais detalhes acesse nosso** [GitHub Pages](https://residenciaticbrisa.github.io/T2G2-Chatbot-Participacao-Social/)
* **O que é o Brisa?** [Conheça o Brisa](https://brisa.lappis.rocks/)
* **Como rodar a chat bot no seu computador (Versão telegram)?** [Siga o passo a passo para rodar o bot no telegram](#getting-started)
* **Gostaria de Contribuir?** [Veja como contribuir](https://residenciaticbrisa.github.io/T2G2-Chatbot-Participacao-Social/Pol%C3%ADticas/CONTRIBUTING/)

---

## Sobre o Brasil Participativo

O Brasil Participativo é uma plataforma desenvolvida em software livre, com o apoio da Dataprev, colaboração da comunidade Decidim-Brasil, parceria com o Ministério da Gestão e Inovação em Serviços Públicos (MGI) e envolvimento da Universidade de Brasília (UnB). A plataforma visa permitir que a sociedade contribua ativamente para o desenvolvimento e aprimoramento das políticas públicas.

## Sobre o Projeto Chatbot

O foco central deste projeto é a implementação de um chatbot destinado a orientar os usuários durante a navegação na plataforma do Brasil Participativo, com o objetivo de esclarecer dúvidas comuns, fornecer suporte e e informar sobre os processos de participação na plataforma em tempo real. O projeto possui médio porte e complexidade, ele necessita de habilidades em Chatbot e Evolução de Software Livre, com Giovanni Alvissus atuando como mentor.

As principais tecnologias utilizadas no projeto serão o JavaScript, devido à sua ampla aceitação e eficácia na construção de aplicações interativas, e o Botpress, que oferece uma plataforma robusta e extensível para o desenvolvimento de chatbots com inteligência artificial. O Botpress facilita a integração de funcionalidades avançadas, permitindo uma interação mais natural e eficiente com os usuários.

Além disso, como o projeto Chatbot de Participação Social será um plugin para a Plataofrma do Brasil Participativo, ele poderá ser utilizado em outros projetos que utilizam a plataforma digital Decidim.

## Colaboradores e Parceiros

Este projeto é fruto da colaboração entre a empresa BRISA, o Ministério da Ciência, Tecnologia e Inovação (MCTI) e a Universidade de Brasília. Agradecemos a todos os envolvidos por contribuírem para a evolução do Brasil Participativo.

Sinta-se à vontade para explorar o código-fonte, relatar problemas (issues) e contribuir para o aprimoramento deste projeto. Juntos, estamos construindo uma plataforma mais acessível e interativa para a participação ativa da sociedade.



## Desenvolvedores

<center>
<table style="margin-left: auto; margin-right: auto;">
    <tr>
        <td align="center">
            <a href="https://github.com/GabrielSPinto">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/144184007?v=4" width="150px;"/>
                <h5 class="text-center">Gabriel Santos Pinto</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/GZaranza">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/116514986?v=4" width="150px;"/>
                <h5 class="text-center">Gabriel Pessoa Zaranza</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/Gxaite">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/111130521?v=4" width="150px;"/>
                <h5 class="text-center">Gabriel Reis Scheidt Paulino</h5>
            </a>
        </td>
        </td>
        <td align="center">
            <a href="https://github.com/seraphritt">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/84244850?v=4" width="150px;"/>
                <h5 class="text-center">Isaque Augusto da Silva Santos</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/ThiagoMarquesAeroespacial">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/125684199?v=4" width="150px;"/>
                <h5 class="text-center">Thiago Henrique Marques Rocha</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/Eruel6">
                <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/71983159?v=4" width="150px;"/>
                <h5 class="text-center">Arthur Taylor de Jesus Popov</h5>
            </a>
        </td>
</table>
</center>

# Getting Started

Este projeto foi desenvolvido no Ubuntu LTS 22.04. Pode funcionar em outros sistemas operacionais, mas ainda não foi testado. Para rodar o projeto, siga as instruções abaixo:

## Pré-requisitos
Certifique-se de estar com o sistema atualizado, no terminal rode o seguinte comado:
```bash
    sudo apt update && sudo apt upgrade
```
Antes de iniciar, certifique-se de que você tenha os seguintes softwares instalados na sua máquina:

- Git [guia de instalação](https://git-scm.com/download/linux)
- Docker [guia de instalação](https://docs.docker.com/desktop/install/ubuntu/)
- Docker compose [guia de instalação](https://docs.docker.com/compose/install/)

## Passo 2: Clonar o Repositório

1. Abra o terminal ou prompt de comando.
2. Clone o repositório usando o comando:

```bash
    git clone https://github.com/ResidenciaTICBrisa/T2G2-Chatbot-Participacao-Social
```

## Passo 3: Acessar a Branch 'botpress_nlu_duckling'

1. Mude para a branch bot_telegram com o comando:
 ```bash
    git checkout botpress_nlu_duckling'
```


## Passo 4: Executar o docker compose
Dentro da branch, de o seguinte comando para rodar o sistema:
```bash
    docker compose up
```
## Passo 5: Acessar o sistema
Se tudo tiver sido da forma adequada, acesse o projeto através do 
[http://localhost:8000](http://localhost:8000)

