
print("\nBem-vindo(a) ao atendimento virtual do Brasil Participativo."
      "Para começar, diga-nos o seu nome")
user = input("Qual seu nome? ")
print(f'Olá, {user}. Digite o número que corresponde à opção que deseja acessar. \
      \nCaso queira encerrar o atendimento, digite \"sair\" a qualquer momento')


while True:
    print("Digite 1 - O que é o Brasil Participativo?\n "
          "Digite 2 - Processos Participativos\n "
          "Digite 3 - Dificuldade de acesso\n "
          "Digite 4 - Represento um órgão da Administração Pública Federal\n "
          "Digite 5 - Sou da imprensa\n "
          "Digite 6 - Perguntas Frequentes\n "
          "Digite 7 - Perguntas Frequentes\n"
          )
    opcao = input("Digite sua opção: ")
    match opcao:
        case "1":
            print("Você escolheu a opção 1 - O que é o Brasil Participativo?")
            
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
                            print("")
                            print("Para consultar os PPAs anteriores, acesse: "
                                  "https://www.gov.br/planejamento/pt-br/assuntos/plano-plurianual/paginas/"
                                  "acesse-os-planos-plurianuais-anteriores")

        case "3":
            print("Você escolheu a opção 3 - Dificuldade de acesso")

        case "4":
            print("Você escolheu a opção 4 - Represento um órgão da Administração Pública Federal")
        case "5":
            print("Você escolheu a opção 5 - Sou da imprensa")
        case "6":
            print("Você escolheu a opção 6 - Perguntas Frequentes")
        
        case "7":
            print("Você escolheu a opção 7 - Outros assuntos \n")
            
            print \
                ("Para assuntos relacionados à plataforma Brasil Participativo, por favor, entre em contato pelo e-mail: participacaodigital@presidencia.gov.br\nPara outros assuntos, registre a sua manifestação na Plataforma Integrada de Ouvidoria e Acesso à Informação (Fala.BR) https://falabr.cgu.gov.br\n")
            
            print("\nSua demanda foi atendida?\n")
        
            opcao2 = input("Digite 1 - Sim\n "+
                        "Digite 2 - Não\n "+
                        "Caso queira encerrar o atendimento, digite \"sair\"\n\n")
            
            match opcao2:
                
                case "1":
                    print("\nAgradecemos o seu contato e continuamos à disposição!\n "+
                            "Para acompanhar todas as atividades realizadas pelo Brasil Participativo, acesse https://brasilparticipativo.presidencia.gov.br \n")
                    break;
                
                        
                case "2": 
                    opcao3 = input \
                        ("\nDigite 9 - Retornar ao menu anterior;\n " +"Caso queira encerrar o atendimento, digite \"sair\".\n")
                    
                    match opcao3:
                        case "9":
                            continue;
                        
                        case "sair":
                            break;
                
                case "sair":
                    break;
