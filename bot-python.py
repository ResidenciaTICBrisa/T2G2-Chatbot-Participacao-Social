

print("\nBem-vindo(a) ao atendimento virtual do Brasil Participativo." + 
       "Para começar, diga-nos o seu nome")
user = input("Qual seu nome? ")
print(f'Olá, {user}. Digite o número que corresponde à opção que deseja acessar. \
      \nCaso queira encerrar o atendimento, digite \"sair\" a qualquer momento\n')

while(True):
    print("Digite 1 - O que é o Brasil Participativo?\n" + 
        "Digite 2 - Processos Participativos\n" + 
        "Digite 3 - Dificuldade de acesso\n" + 
        "Digite 4 - Represento um órgão da Administração Pública Federal\n" + 
        "Digite 5 - Sou da imprensa\n" + 
        "Digite 6 - Perguntas Frequentes\n" + 
        "Digite 7 - Outros Assuntos\n"
        )
    opcao = input("Digite sua opção: ")

    match opcao:
        case "1":
            print("Brasil Participativo é a nova plataforma de participação social do governo federal,"
                "um espaço para que a população possa contribuir com a criação e melhoria das políticas públicas."
                "A plataforma é gerenciada pela Secretaria Nacional de Participação Social (SNPS),"
                "vinculada à Secretaria Geral da Presidência da República (SGPR). Quer saber mais informações?"
                "Acesse o site https://brasilparticipativo.presidencia.gov.br/")
              print("Sua demanda foi atendida?")
              
               print("Digite 1 - sim\
              Digite 2 - não")
        opcao = input("Digite a opção desejada")
        match opcao:
            case "1":
                print("Agradecemos o seu contato e continuamos à disposição!\
                       Para acompanhar todas as atividades realizadas pelo Brasil Participativo,\
                       acesse https://brasilparticipativo.presidencia.gov.br/")
            case "2":
                print("Digite 9 - Retornar ao menu anterior ?\
                       Caso queira encerrar o atendimento, digite “sair”")
                opcao = input("Digite a opção desejada")
                match opcao:
                    case "9":
                        continue
                    case "sair":
                        break
            
        case "2":
            print("Você escolheu a opção 2 - Processos Participativos")
        case "3":
               print("Você escolheu a opção 3 - Dificuldade de acesso\n")
               print("Por favor, entre em contato pelo e-mail: participacaodigital@presidencia.gov.br\n")
               
               print("Sua demanda foi atendida?")
               print("Digite 1 - Sim\n"+
                     "Digite 2 - Não\n")
               opcao3 = input("Digite sua opção\n")
        match opcao3:
            case "1":
                print("Agradecemos o seu contato e continuamos à disposição!\n\nPara acompanhar todas as atividades realizadas pelo Brasil Participativo, acesse https://brasilparticipativo.presidencia.gov.br/ ")
            case "2":
                opcao4 = input("Digite 9 - Retornar ao menu anterior \n Caso queira encerrar o atendimento, digite “sair”")
                
                match opcao4:
                        case "9":
                            continue;
    
                        case "sair":
                            break;    
       case "4":
              print("Você escolheu a opção 4 - Represento um órgão da Administração Pública Federal\n")
              print("Para aderir à plataforma ou tirar dúvidas sobre os processos participativos, por favor, entre em contato pelo e-mail: participacaodigital@presidencia.gov.br\n\nAcesse os nossos cursos de capacitação na plataforma EVG (quando estiverem disponibilizados)\n")
              
              print("Sua demanda foi atendida?")

              print("Digite 1 - Sim")
              print("Digite 2 - Não\n")
        opcao3 = input("Digite sua opção\n")
        match opcao3:
            case "1":
                print("Agradecemos o seu contato e continuamos à disposição!\nPara acompanhar todas as atividades realizadas pelo Brasil Participativo, acesse https://brasilparticipativo.presidencia.gov.br/ ")
            case "2":
                opcao4 = input("Digite 9 - Retornar ao menu anterior \n Caso queira encerrar o atendimento, digite “sair”")
                
                match opcao4:
                        case "9":
                            continue;
    
                        case "sair":
                            break;
        case "5":
            print("Você escolheu a opção 5 - Sou da imprensa\n")
            
            print("Por favor, entre em contato pelo e-mail:")
            print("participacaodigital@presidencia.gov.br\n")
            
            print("Sua demanda foi atendida?\n")
            
            print("Digite 1 - Sim")
            print("Digite 2 - Não\n")

            entrada = input()

            match entrada:
                case "1":
                    print("Agradecemos o seu contato e continuamos à disposição!")
                    print("Para acompanhar todas as atividades realizadas pelo Brasil Participativo, acesse https://brasilparticipativo.presidencia.gov.br/")
                    break  
                case "2":
                    print("Digite 9 - Retornar ao menu anterior")
                    print("Caso queira encerrar o atendimento, digite “sair”")

                    entrada2 = input()

                    match entrada2:
                        case "9":
                            continue 
                        case "sair":
                            break
                case "sair":
                        break
        case "6":
            print("Você escolheu a opção 6 - Perguntas Frequentes")
            print("Confira as principais perguntas sobre os serviços relacionados ao Brasil Participativo (inserir link, da plataforma, de perguntas frequentes)\n")
                            
            print("Sua demanda foi atendida?\n")
            
            print("Digite 1 - Sim")
            print("Digite 2 - Não\n")

            entrada = input()

            match entrada:
                case "1":
                    print("Agradecemos o seu contato e continuamos à disposição!")
                    print("Para acompanhar todas as atividades realizadas pelo Brasil Participativo, acesse https://brasilparticipativo.presidencia.gov.br/")
                    break  
                case "2":
                    
                    print("Digite 9 - Retornar ao menu anterior")
                    print("Caso queira encerrar o atendimento, digite “sair”")

                    entrada2 = input()

                    match entrada2:
                        case "9":
                            continue  
                        case "sair":
                            break  
                case "sair":
                        break
            
        case "7":
            print("Você escolheu a opção 7 - Outros assuntos \n")
            
            print("Para assuntos relacionados à plataforma Brasil Participativo, por favor, entre em contato pelo e-mail: participacaodigital@presidencia.gov.br\nPara outros assuntos, registre a sua manifestação na Plataforma Integrada de Ouvidoria e Acesso à Informação (Fala.BR) https://falabr.cgu.gov.br\n")
            
            print("\nSua demanda foi atendida?\n")
        
            opcao2 = input("Digite 1 - Sim\n" + 
                        "Digite 2 - Não\n" + 
                        "Caso queira encerrar o atendimento, digite \"sair\"\n\n")
            
            match opcao2:
                
                case "1":
                    print("\nAgradecemos o seu contato e continuamos à disposição!\n" + 
                            "Para acompanhar todas as atividades realizadas pelo Brasil Participativo, acesse https://brasilparticipativo.presidencia.gov.br \n")
                    break;
                        
                case "2": 
                    opcao3 = input("\nDigite 9 - Retornar ao menu anterior;\n" + "Caso queira encerrar o atendimento, digite \"sair\".\n")
                    
                    match opcao3:
                        case "9":
                            continue;
                        
                        case "sair":
                            break;
                
                case "sair":
                    break;
        case "sair":
            break
