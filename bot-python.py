import menu_principal
import tempo_espera

print("\nBem-vindo(a) ao atendimento virtual do Brasil Participativo."
      "Para começar, diga-nos o seu nome")
user = input("Qual seu nome? ")
print(
    f'Olá, {user}. Digite o número que corresponde à opção que deseja acessar.\nCaso queira encerrar o atendimento, digite "sair" a qualquer momento\n')
tempo_espera.tempo_espera()

while True:
    opcao = menu_principal.menu_principal()
    match opcao:
        case "1":
            print("Brasil Participativo é a nova plataforma de participação social do governo federal,"
                  "um espaço para que a população possa contribuir com a criação e melhoria das políticas públicas."
                  "A plataforma é gerenciada pela Secretaria Nacional de Participação Social (SNPS),"
                  "vinculada à Secretaria Geral da Presidência da República (SGPR).Quer saber mais informações?"
                  "Acesse o site https://brasilparticipativo.presidencia.gov.br/")
            tempo_espera.tempo_espera()

            print("Sua demanda foi atendida?")
            opcao = input("Digite 1 - sim "
                          "Digite 2 - não")
            match opcao:
                case "1":
                    print("Agradecemos o seu contato e continuamos à disposição!\
                        Para acompanhar todas as atividades realizadas pelo Brasil Participativo,\
                        acesse https://brasilparticipativo.presidencia.gov.br/")
                    tempo_espera.tempo_espera()
                    break
                case "2":
                    print("Digite 9 - Retornar ao menu anterior ?\
                        Caso queira encerrar o atendimento, digite “sair”")
                    opcao = input()
                    match opcao:
                        case "9":
                            continue
                        case "sair":
                            break
        case "2":
            print("Você escolheu a opção 2 - Processos Participativos\n")
            print("Digite 1 - Plano Clima/PPA Participativo\n "
                  "Digite 2 - Conferências\n "
                  "Digite 3 - Consultas Públicas\n "
                  "Digite 4 - Enquetes\n "
                  "Digite 5 - Audiências Públicas\n "
                  "Digite 6 - Colegiados\n "
                  )
            opcao = input("Digite sua opção: ")
            match opcao:
                case "1":
                    print("Digite 1 - O que é o Plano Clima/PPA Participativo?\n "
                          "Digite 2 - Como participar?\n "
                          "Digite 3 - Plano Clima/PPA abertos\n "
                          "Digite 4 - Plano Clima/PPA fechados\n "
                          )
                    opcao = input("Digite sua opção: ")
                    match opcao:
                        case "1":
                            print("O Plano Clima é uma estratégia governamental adotada pelo Brasil para lidar com as "
                                  "mudanças climáticas. Seu principal objetivo é liderar a redução das emissões de "
                                  "gases de efeito estufa, visando conter o aquecimento global abaixo de 1,5°C.\n")
                            print("O Plano Plurianual (PPA) é um documento que está previsto na Constituição de 1988. "
                                  "Ele é elaborado de quatro em quatro anos, sempre no primeiro ano de mandato do "
                                  "presidente. O PPA define metas, diretrizes e programas do Governo. Em 2023, ele será"
                                  " elaborado com apoio aberto da população por meio da plataforma Brasil"
                                  " Participativo. O PPA deve ser entregue às(aos) senadoras(es) e deputadas(os) no "
                                  "Congresso Nacional até 31 de agosto de 2023, junto à Lei Orçamentária Anual (LOA).")
                        case "2":
                            print("Basta criar uma conta no Gov.Br ou baixar o app. Se você já tem conta, "
                                  "é só entrar com seu login e senha, em seguida fazer suas escolhas e propostas "
                                  "entre 11 de maio e 14 de julho de 2023.")
                        case "3":
                            print("Para mais informações sobre o Plano Clima atual, acesse:"
                                  " https://lab-decide.dataprev.gov.br/processes/planoclima?locale=pt-BR")
                            print("Se quiser saber mais sobre o PPA aberto, acesse:"
                                  " https://www.gov.br/planejamento/pt-br/assuntos/plano-plurianual")
                        case "4":
                            print("O Plano Clima foi instituído em 2009 para consolidar a execução da Política Nacional"
                                  " de Mudança do Clima.\n"
                                  "Plano Clima de 2015: https://www.mds.gov.br/webarquivos/arquivo/seguranca_alimentar"
                                  "/caisan/Publicacao/Caisan_Nacional/PlanoNacionaldeAdaptacaoaMudancadoClima"
                                  "_Junho2015.pdf\n"
                                  "Plano Clima atual: "
                                  "https://lab-decide.dataprev.gov.br/processes/planoclima?locale=pt-BR")
                            print("Para consultar os PPAs anteriores, acesse: "
                                  "https://www.gov.br/planejamento/pt-br/assuntos/plano-plurianual/paginas/"
                                  "acesse-os-planos-plurianuais-anteriores")
                case "2":
                    print("Digite 1 - O que é uma conferência?\n "
                          "Digite 2 - Como participar?\n "
                          "Digite 3 - Conferências abertas/ativas\n "
                          "Digite 4 - Conferências fechadas/encerradas\n "
                          )
                    opcao = input("Digite sua opção: ")
                    match opcao:
                        case "1":
                            print("Uma conferência é um importante instrumento de participação social que "
                                  "reúne diversos segmentos representativos da sociedade para debater e avaliar "
                                  "políticas públicas e propor diretrizes para o seu aperfeiçoamento nos três "
                                  "níveis de governo: municipal, estadual e nacional. Elas são espaços de diálogo "
                                  "social e construção coletiva, nos quais atores diversos apontam suas demandas e "
                                  "contribuições em relação à política pública e a como ela se materializa em serviços "
                                  "nos territórios e comunidades.\n")
                        case "2":
                            print("Para participar, basta seguir o passo a passo abaixo: "
                                  "1º  Acesse o endereço: https://brasilparticipativo.presidencia.gov.br/"
                                  "2º Clique em “entrar” no canto superior direito da tela;"
                                  "3º Clique em “entrar com Gov.br” e preencha com os  seus dados;"
                                  "4º Selecione o módulo ‘Conferências’;"
                                  "5º Escolha a conferência desejada para fazer sua contribuição.")
                        case "3":
                            print("Confira as conferências abertas pelo link: "
                                  "https://brasilparticipativo.presidencia.gov.br/assemblies")
                        case "4":
                            print("Confira as conferências fechadas pelo link: "
                                  "https://brasilparticipativo.presidencia.gov.br/assemblies")
                        case "sair":
                            break
                case "3":
                    print("Digite 1 - O que é uma consulta pública?\n "
                          "Digite 2 - Como participar?\n "
                          "Digite 3 - Consultas públicas abertas\n "
                          "Digite 4 - Consultas públicas fechadas\n "
                          )
                    opcao = input("Digite sua opção: ")
                    match opcao:
                        case "1":
                            print("É um mecanismo de participação social, de caráter consultivo, realizado com prazo "
                                  "definido e aberto a qualquer interessado, com o objetivo de receber contribuições"
                                  " sobre determinado assunto. Incentiva a participação da sociedade na tomada de "
                                  "decisões relativas à formulação e definição de políticas públicas.")
                        case "2":
                            print("Para participar, siga o passo a passo abaixo: "
                                  "1º  Acesse o Sistema de Consulta Pública "
                                  "(https://www3.bcb.gov.br/audpub/HomePage?1)"
                                  "e clique no link de Consultas Ativas para "
                                  "sugerir alterações em minuta de norma a ser publicada pelo Banco Central;\n"
                                  "2º Inserir sugestões ao texto da minuta ao clicar no link “Enviar sugestão”. Deverá "
                                  "ser descrita a sugestão e a qual parte do texto se refere. "
                                  "Também é possível incluir anexos;\n"
                                  "3º Acesse o Sistema de Consulta Pública e clique no link de Consultas Encerradas. "
                                  "As sugestões e os anexos encaminhados em todas as consultas "
                                  "são disponibilizadas no sistema.")
                        case "3":
                            print("Para ver as consultas públicas abertas, acesse:"
                                  "https://www.gov.br/saude/pt-br/acesso-a-informacao/"
                                  "participacao-social/consultas-publicas")
                        case "4":
                            print("Confira as consultas púbicas fechadas pelo link: "
                                  "https://www.gov.br/saude/pt-br/acesso-a-informacao/"
                                  "participacao-social/consultas-publicas")
                        case "sair":
                            break
                case "4":
                    print("Digite 1 - O que é uma enquete?\n "
                          "Digite 2 - Como participar?\n "
                          "Digite 3 - Enquetes abertas\n "
                          "Digite 4 - Enquetes públicas fechadas\n "
                          )
                    opcao = input("Digite sua opção: ")
                    match opcao:
                        case "1":
                            print("As Enquetes visam a dar maior publicidade e transparência ao trabalho de elaboração"
                                  " de Protocolos Clínicos e Diretrizes Terapêuticas (PCDT) desenvolvido pela Conitec."
                                  " Foram criadas como mais um meio de comunicação com a sociedade, a fim de "
                                  "melhorarmos esse processo. Elas são disponibilizadas como consulta prévia, ainda na"
                                  " primeira etapa de construção do PCDT, para que possamos discutir uma proposta "
                                  "inicial e, assim, melhorá-la, identificando aspectos que podem não ter sido "
                                  "considerados anteriormente. Dessa forma, a participação popular será considerada "
                                  "desde o início do processo de elaboração do PCDT, e não apenas na Consulta Pública"
                                  " para deliberação final.\n")
                        case "2":
                            print("Para votar, o cidadão deve acessar a página de enquetes disponível no Portal da "
                                  "Câmara pelo menu superior Participe/Enquetes ou pelo endereço enquetes.camara.leg.br"
                                  " e registrar seu voto. Comentários à matéria, no entanto, não são computados "
                                  "como votos.\n")
                        case "3":
                            print("Para consultar as enquetes abertas, acesse:")
                            print("https://www.gov.br/conitec/pt-br/assuntos/participacao-social/enquetes\n")
                        case "4":
                            print("Para consultar as enquetes fechadas, acesse:")
                            print("https://www.gov.br/conitec/pt-br/assuntos/participacao-social/enquetes\n")
                        case "sair":
                            break
                case "5":
                    print("Digite 1 - O que é uma audiência?\n "
                          "Digite 2 - Como participar?\n "
                          "Digite 3 - Audiências públicas abertas\n "
                          "Digite 4 - Audiências públicas fechadas\n "
                          )
                    opcao = input("Digite sua opção: ")
                    match opcao:
                        case "1":
                            print("As Audiências Públicas são ambientes de ampla consulta à sociedade com o "
                                  "objetivo de colher"
                                  " subsídios e informações, além de oferecer aos interessados a oportunidade de "
                                  "encaminhar "
                                  "suas solicitações, pleitos, opiniões e sugestões, em especial da população "
                                  "diretamente "
                                  "afetada pelo objeto do debate.\n")
                        case "2":
                            print("Para participar, acesse:"
                                  "https://www.gov.br/pt-br/servicos/participar-de-audiencias-e-consultas-publicas\n")
                        case "3":
                            print("Para consultar as audiências abertas, acesse:")
                            print("https://www.gov.br/saude/pt-br/acesso-a-informacao/participacao-social"
                                  "/audiencias-publicas\n")
                        case "4":
                            print("Para consultar as audiências fechadas, acesse:")
                            print("https://www.gov.br/saude/pt-br/acesso-a-informacao/participacao-social/"
                                  "audiencias-publicas\n")
                        case "sair":
                            break
                case "6":
                    print("Digite 1 - O que é um colegiado?\n "
                          "Digite 2 - Como participar?\n "
                          "Digite 3 - Colegiados abertos\n "
                          "Digite 4 - Colegiados fechados\n "
                          )
                    opcao = input("Digite sua opção: ")
                    match opcao:
                        case "1":
                            print("Órgãos Colegiados referem-se a um corpo consultivo e/ou deliberativo que tem como"
                                  " objetivo reunir pessoas com a competência de emitir pareceres e deliberações sobre"
                                  " políticas públicas e atuam como canais de diálogo e de fiscalização.\n")
                        case "2":
                            print("Para participar de colegiados, bem como obter mais informações, acesse:")
                            print("https://www.gov.br/participamaisbrasil/colegiados")
                        case "3":
                            print("Consulte os colegiados abertos e as datas de reuniões em:")
                            print("https://www.gov.br/mdh/pt-br/acesso-a-informacao/governanca/"
                                  "comissao-de-etica-publica-setorial/calendario")
                        case "4":
                            print("Para consultar os colegiados encerrados, acesse:")
                            print("https://www.gov.br/mdh/pt-br/acesso-a-informacao/governanca/"
                                  "comissao-de-etica-publica-setorial/calendario")
                            # fecha das e abertas print("https://www.gov.br/participamaisbrasil/colegiados")
                case "sair":
                    break

        case "3":
            print("Por favor, entre em contato pelo e-mail: participacaodigital@presidencia.gov.br\n")
            tempo_espera.tempo_espera()

            print("Sua demanda foi atendida?")
            print("Digite 1 - Sim\n"
                  "Digite 2 - Não\n")
            opcao = input()
            match opcao:
                case "1":
                    print("Agradecemos o seu contato e continuamos à disposição!\nPara acompanhar todas as atividades "
                          "realizadas pelo Brasil Participativo, acesse https://brasilparticipativo."
                          "presidencia.gov.br/ ")
                case "2":
                    opcao = input("Digite 9 - Retornar ao menu anterior \n Caso queira encerrar o atendimento, "
                                  "digite “sair”")

                    match opcao:
                        case "9":
                            continue
                        case "sair":
                            break
        case "4":
            print("Para aderir à plataforma ou tirar dúvidas sobre os processos participativos, por favor, entre "
                  "em contato pelo e-mail: participacaodigital@presidencia.gov.br\n\nAcesse os nossos cursos de "
                  "capacitação na plataforma EVG (quando estiverem disponibilizados)\n")
            print("Sua demanda foi atendida?")
            print("Digite 1 - Sim")
            print("Digite 2 - Não\n")
            opcao = input("Digite sua opção\n")
            match opcao:
                case "1":
                    print("Agradecemos o seu contato e continuamos à disposição!\nPara acompanhar todas as atividades"
                          " realizadas pelo Brasil Participativo, "
                          "acesse https://brasilparticipativo.presidencia.gov.br/ ")
                case "2":
                    opcao = input("Digite 9 - Retornar ao menu anterior \n Caso queira encerrar o atendimento, "
                                  "digite “sair”")
                    match opcao:
                        case "9":
                            continue
                        case "sair":
                            break
        case "5":
            print("Por favor, entre em contato pelo e-mail:")
            print("participacaodigital@presidencia.gov.br\n")
            print("Sua demanda foi atendida?\n")
            input("Digite 1 - Sim\nDigite 2 - Não\n")
            opcao = input()
            match opcao:
                case "1":
                    print("Agradecemos o seu contato e continuamos à disposição!")
                    print("Para acompanhar todas as atividades realizadas pelo Brasil Participativo, acesse "
                          "https://brasilparticipativo.presidencia.gov.br/")
                    break
                case "2":
                    print("Digite 9 - Retornar ao menu anterior")
                    print("Caso queira encerrar o atendimento, digite “sair”")
                    opcao = input()
                    match opcao:
                        case "9":
                            continue
                        case "sair":
                            break
                case "sair":
                    break
        case "6":
            print("Confira as principais perguntas sobre os serviços relacionados ao Brasil Participativo "
                  "(inserir link, da plataforma, de perguntas frequentes)\n")
            print("Sua demanda foi atendida?\n")
            print("Digite 1 - Sim")
            print("Digite 2 - Não\n")
            opcao = input()
            match opcao:
                case "1":
                    print("Agradecemos o seu contato e continuamos à disposição!")
                    print("Para acompanhar todas as atividades realizadas pelo Brasil Participativo, "
                          "acesse https://brasilparticipativo.presidencia.gov.br/")
                    break
                case "2":
                    print("Digite 9 - Retornar ao menu anterior")
                    print("Caso queira encerrar o atendimento, digite “sair”")
                    opcao = input()
                    match opcao:
                        case "9":
                            continue
                        case "sair":
                            break
                case "sair":
                    break
        case "7":
            print("Para assuntos relacionados à plataforma Brasil Participativo, por favor, entre em contato pelo "
                  "e-mail: participacaodigital@presidencia.gov.br\nPara outros assuntos, registre a sua manifestação "
                  "na Plataforma Integrada de Ouvidoria e Acesso à Informação (Fala.BR) https://falabr.cgu.gov.br\n")
            print("\nSua demanda foi atendida?\n")
            opcao = input("Digite 1 - Sim\n" +
                          "Digite 2 - Não\n" +
                          "Caso queira encerrar o atendimento, digite \"sair\"\n\n")
            match opcao:
                case "1":
                    print("\nAgradecemos o seu contato e continuamos à disposição!\n" +
                          "Para acompanhar todas as atividades realizadas pelo Brasil Participativo, acesse "
                          "https://brasilparticipativo.presidencia.gov.br \n")
                    break
                case "2":
                    opcao = input(
                        "\nDigite 9 - Retornar ao menu anterior;\n"
                        "Caso queira encerrar o atendimento, "
                        "digite \"sair\".\n")
                    match opcao:
                        case "9":
                            continue
                        case "sair":
                            break
                case "sair":
                    break
        case "sair":
            break
