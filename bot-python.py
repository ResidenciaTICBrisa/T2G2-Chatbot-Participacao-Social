import menu_principal
import tempo_espera

print("\nBem-vindo(a) ao atendimento virtual do Brasil Participativo." 
       "Para começar, diga-nos o seu nome")
user = input("Qual seu nome? ")
print(f'Olá, {user}. Digite o número que corresponde à opção que deseja acessar.\nCaso queira encerrar o atendimento, digite "sair" a qualquer momento\n')
tempo_espera.tempo_espera()

while(True):
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
            opcao = input("Digite 1 - sim\
            Digite 2 - não")
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
            print("Hello")

        case "3":
            print("Por favor, entre em contato pelo e-mail: participacaodigital@presidencia.gov.br\n")
            tempo_espera.tempo_espera()
               
            print("Sua demanda foi atendida?")
            print("Digite 1 - Sim\n"+
                 "Digite 2 - Não\n")
            opcao = input()
            match opcao:
                case "1":
                    print("Agradecemos o seu contato e continuamos à disposição!\nPara acompanhar todas as atividades realizadas pelo Brasil Participativo, acesse https://brasilparticipativo.presidencia.gov.br/ ")
                case "2":
                    opcao = input("Digite 9 - Retornar ao menu anterior \n Caso queira encerrar o atendimento, digite “sair”")
                    
                    match opcao:
                        case "9":
                            continue;
        
                        case "sair":
                            break;    
        case "4":
            print("Para aderir à plataforma ou tirar dúvidas sobre os processos participativos, por favor, entre em contato pelo e-mail: participacaodigital@presidencia.gov.br\n\nAcesse os nossos cursos de capacitação na plataforma EVG (quando estiverem disponibilizados)\n")
              
            print("Sua demanda foi atendida?")

            print("Digite 1 - Sim")
            print("Digite 2 - Não\n")
            opcao = input("Digite sua opção\n")
    
            match opcao:
                case "1":
                    print("Agradecemos o seu contato e continuamos à disposição!\nPara acompanhar todas as atividades realizadas pelo Brasil Participativo, acesse https://brasilparticipativo.presidencia.gov.br/ ")
                case "2":
                    opcao = input("Digite 9 - Retornar ao menu anterior \n Caso queira encerrar o atendimento, digite “sair”")
                    
                    match opcao:
                            case "9":
                                continue;
        
                            case "sair":
                                break;
        case "5":
            
            print("Por favor, entre em contato pelo e-mail:")
            print("participacaodigital@presidencia.gov.br\n")
            
            print("Sua demanda foi atendida?\n")
            
            input("Digite 1 - Sim\nDigite 2 - Não\n")

            opcao = input()

            match opcao:
                case "1":
                    print("Agradecemos o seu contato e continuamos à disposição!")
                    print("Para acompanhar todas as atividades realizadas pelo Brasil Participativo, acesse https://brasilparticipativo.presidencia.gov.br/")
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
            print("Confira as principais perguntas sobre os serviços relacionados ao Brasil Participativo (inserir link, da plataforma, de perguntas frequentes)\n")
                            
            print("Sua demanda foi atendida?\n")
            
            print("Digite 1 - Sim")
            print("Digite 2 - Não\n")

            opcao = input()

            match opcao:
                case "1":
                    print("Agradecemos o seu contato e continuamos à disposição!")
                    print("Para acompanhar todas as atividades realizadas pelo Brasil Participativo, acesse https://brasilparticipativo.presidencia.gov.br/")
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
            print("Para assuntos relacionados à plataforma Brasil Participativo, por favor, entre em contato pelo e-mail: participacaodigital@presidencia.gov.br\nPara outros assuntos, registre a sua manifestação na Plataforma Integrada de Ouvidoria e Acesso à Informação (Fala.BR) https://falabr.cgu.gov.br\n")
            
            print("\nSua demanda foi atendida?\n")
        
            opcao = input("Digite 1 - Sim\n" + 
                        "Digite 2 - Não\n" + 
                        "Caso queira encerrar o atendimento, digite \"sair\"\n\n")
            
            match opcao:
                
                case "1":
                    print("\nAgradecemos o seu contato e continuamos à disposição!\n" + 
                            "Para acompanhar todas as atividades realizadas pelo Brasil Participativo, acesse https://brasilparticipativo.presidencia.gov.br \n")
                    break;
                        
                case "2": 
                    opcao = input("\nDigite 9 - Retornar ao menu anterior;\n" + "Caso queira encerrar o atendimento, digite \"sair\".\n")
                    
                    match opcao:
                        case "9":
                            continue;
                        
                        case "sair":
                            break;
                
                case "sair":
                    break;
        case "sair":
            break
