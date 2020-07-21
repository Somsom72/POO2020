from classes import Envirorment

#Cria o ambiente com um nome de usuario genérico
env = Envirorment('user')
#Salva o valor da saída caso o comando exit seja dado
ext = env.checkFase()
#Se o comando exit não foi dado
if not ext:
    #Le a resposta do usuario
    print('Digite a sua resposta:')
    resp = str(input())
    #Enquanto não der a resposta correta reinicia o jogo
    while(resp != 'palavras superam imagens'):
        if(resp == 'echo "turing1936" > interfaceGrafica.txt'):
            print('\n\n\n\tEscolha incorreta, tente novamente.\n\n\n')
            env = Envirorment('user')
            ext = env.checkFase()
            if not ext:
                print('Digite a sua resposta:')
                resp = str(input())
            else:
                break
        else:
            print('Não tente mudar de assunto! Faça a sua escolha!')
            print('Digite a sua resposta:')
            resp = str(input())
    print('\n\n\n\tUm dia feliz em pinguimlândia.\n\n\n')