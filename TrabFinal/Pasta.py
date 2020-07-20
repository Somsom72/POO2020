import time
#---------------------------------------------------------------------------------------------------        
class Pasta(object):
    """Classe: Pasta
    Classe que cria objetos do tipo Pasta que serão manipulados 
    durante a execução do jogo.
    *Métodos:
        __new__: Instancia um  novo objeto
        __init__: Construtor
        ls: Gera uma lista de componentes do objeto
        add: Adiciona um elemento na pasta
        rm: Remove um elemento da pasta
        cd: Acessa uma pasta filha
        changePerm: Altera a flag de permissão
    *Atributos:
        nome(str): Nome do objeto
        pai(Pasta): Pasta na qual o objeto está contido (None caso seja raiz)
        filhos(lista): Lista com as pastas contidas no objeto
        files(lista): Lista com os arquivos contidos no objeto
        is_empty(bool): Flag que indica se o objeto está vazio
        change(bool): Flag que indica se o objeto pode ou não ser excluido pelo usuário
        perm(bool):  Flag que indica se o objeto pode ou não ser acessado pelo usuário
    """
    
    def __new__(cls, nome, change=True, perm=True):
        """Método: __new__
        Método que instancia a classe ou impede a sua istanciação caso
        algumas condições não sejam satisfeitas
        *inputs:
            nome(str): Nome do novo objeto
            change(bool): Flag que indica se o objeto pode ou não ser modificado pelo usuário
            perm(bool): Flag que indica se o objeto pode ou não ser acessado pelo usuário
        *outputs:
            Objeto instanciado
            
        """
        #Se o nome do novo objeto possuir alguns caracteres ele não é criado
        if ' ' in nome or '/' in nome:
            print("Nome invalido")
            return None

        instance = super().__new__(cls)
        instance.nome = nome
        instance.change = change
        instance.perm = perm
        return instance
    
    #-------------------------------------------------------
    
    def __init__(self, nome, change=True, perm=True):
        """Método: __init__
        Método construtor da classe
        *inputs:
            nome(str): Nome do novo objeto
            change(bool): Flag que indica se o objeto pode ou não ser modificado pelo usuário
            perm(bool): Flag que indica se o objeto pode ou não ser acessado pelo usuário
        """
        self.nome = nome
        self.pai = None
        self.filhos = {}
        self.files = {}
        self.is_empty = True
        self.change = change
        self.perm = perm
        
    #---------------------------------------------------------
    
    def ls(self):
        '''Método: ls
        Método que ista os arquivos e pastas do objeto
        *inputs:
            self(Pasta): O ponteiro para o objeto
        '''
        for sub in self.filhos:
            print("\033[1;31;48m"+str(sub)+"\033[0;0;0m")
        
        for file in self.files:
            print("\033[1;33;48m"+str(file)+"\033[0;0;0m")
            
    #---------------------------------------------------------        
    
    def add(self, to_add):
        '''Método: add
        Método que adiciona um arquivo ou pasta ao objeto.
        *inputs:
            self(Pasta): O ponteiro para o objeto
            to_add(Pasta ou File): Objeto do tipo Pasta ou Arquivo
        '''
        if(type(to_add) == Pasta):
            if to_add.nome not in self.filhos:
                to_add.pai = self
                self.filhos[to_add.nome] = to_add
            else:
                print("Impossivel criar "+str(to_add.nome)+", pasta ja existe")
        
        elif(type(to_add) == File):
            if to_add.nome not in self.files:
                to_add.pai = self
                self.files[to_add.nome] = to_add
            else:
                print("Impossivel criar "+str(to_add.nome)+", arquivo ja existe")
    
    #---------------------------------------------------------
    
    def rm(self, to_rem):
        '''Método: rm
        Método que remove um arquivo ou pasta do objeto.
        *inputs:
            self(Pasta): O ponteiro para o objeto
            to_rem(str): Nome do arquivo ou pasta a ser removido
        *outputs:
            Objeto do tipo Arquivo ou Pasta que foi removido do diretorio atual
        '''
        rem = None
        
        if to_rem in self.filhos:
            rem = self.filhos.pop(to_rem)
        elif to_rem in self.files:
            rem = self.files.pop(to_rem)
        else:
            print("Pasta ou arquivo "+to_rem+" inexistente")
                
        return rem
    
    #---------------------------------------------------------
    
    def cd(self, to_ent):
        '''Método: cd
        Método que busca pela pasta filha especificada.
        *inputs:
            self(Pasta): O ponteiro para o objeto
            to_ent(str): Nome da pasta filha desejada
        *outputs:
            Ponteiro para a pasta filha desejada
        '''
        if to_ent in self.filhos:
            return self.filhos[to_ent]
        else:
            print("Pasta "+to_ent+" inexistente em "+str(self.nome))
            return self
    #---------------------------------------------------------    
    
    def changePerm(self, new):
        """Método: changePerm
        Método que altera a flag de permissão do objeto
        *inputs:
            self(Pasta): O ponteiro para o objeto
            new(bool): Novo valor da flag
        """
        self.perm = new
        
#---------------------------------------------------------------------------------------------------        

class File(object):
    """Classe: File
    Classe que cria objetos do tipo File que serão manipulados 
    durante a execução do jogo
    *Métodos:
        __new__:
        __init__:
        write:
        show:
        setChange:
    """
    def __new__(cls, nome, change=True):
        if ' ' in nome or '/' in nome:
            print("Nome invalido")
            return None

        instance = super().__new__(cls)
        instance.nome = nome
        instance.change = change
        return instance
    
    #--------------------------------------------------------- 
    
    def __init__(self, nome ,change=True):
        self.nome = nome
        self.pai = None
        self.conteudo = None
        self.change = change
        
    #--------------------------------------------------------- 
        
    def write(self, text):
        self.conteudo = text
        
    #--------------------------------------------------------- 
        
    def show(self):
        if self.conteudo == None:
            print('Arquivo vazio')
            return None
        else:
            return self.conteudo
        
    #--------------------------------------------------------- 
        
    def setChange(self, change):
        self.change = change
        
#---------------------------------------------------------------------------------------------------
            
class Envirorment(object):
    def __init__(self, user_name):
        
        self.user_name = user_name
        
        self.root = self.createEnv()
        
        self.pat = self.root
        
        self.fase = 1
        
        self.exit = False
        
        self.senha = None
        
    #--------------------------------------------------------- ---------------   
    def createEnv(self):
        root = Pasta('root', False)
        
        floresta = Pasta('floresta', False)
        
        rio = Pasta('rio', False)
        
        agua = File('agua.txt', False)
        agua.write('Muito oxigênio, e o dobro de hidrogênio!')
        peixe = File('peixe.txt', False)
        peixe.write('Vertebrado aquático de médio porte.')
        ponte = File('ponte.txt', False)
        ponte.write('instável...')
        rio.add(agua)
        rio.add(peixe)
        rio.add(ponte)
        
        floresta.add(rio)
        
        mar = Pasta('mar', False)
        
        root.add(floresta)
        root.add(mar)
        
        return root
    #--------------------------------------------------------- --------------- 
    def changeEnv(self):
        entrada = Pasta('entrada', False)

        caverna = Pasta('caverna', False)
        
        manual = File('ManualQuartus.txt', False)
        manual.write('Saudações '+self.user_name+', sou o Manual do Quartus, um livro falante que por alguma razão \nsabe seu nome!\nPara sobreviver a Caverna da Criptografia, terá de decifrar meu enigma, e criar um arquivo \n“enigma.txt” contendo sua resposta.\nSe "a" é "c" e "c" é "e", "ekhtc fg eguct" é o que?')
        
        caverna.add(manual)
        
        entrada.add(caverna)

        return entrada
    
    #--------------------------------------------------------- ---------------   
    def cmdReader(self, cmd, rep):
        '''
        Função que le e interpreta um comando passado ao terminal
        input:
            cmd: (String) Linha do comando dado ao terminal
            root: (Pasta) Pasta root do sistema
            pat: (Pasta) Pasta atual
        '''
        if cmd == 'segue':
            return
        elif cmd == 'repete':
            print(rep)
            return
        
        cmd = cmd.split(" ")
        
        #ls = List ------------------------------------------
        if cmd[0] == 'ls':
            self.pat.ls()

        #cd = Change Directory ------------------------------
        elif cmd[0] == 'cd':
            #Se for o comando de retornar
            if cmd[-1] == '..':
                #Se estiver na root retorna apropria root 
                if self.pat.pai == None:
                    return
                #Se não estiver na root retorna apasta pai
                else:
                    self.pat = self.pat.pai
        
            #Se for o comando de entrar em uma pasta    
            else:
                #Se começar por / o caminho é definido a partir da root
                if cmd[-1][0] == '/':
                    self.pat = self.root
                    #Se for apenas o /
                    if cmd[-1] == '/':
                        return
                #Separa o caminho nos caracteres /
                path = cmd[-1].split('/')
                #Itera pelas pastas do caminho
                for pasta in path:
                    #Entra em cada pasta do caminho
                    self.pat = self.pat.cd(pasta)
                    if(self.pat.perm == False):
                        self.pat = self.pat.pai
                        print("Acesso negado")
                        break
                return
            
        #cat = Inspecionar conteudo de arquivo ----------------
        elif cmd[0] == 'cat':
            #Se o arquivo existir no diretorio atual
            if cmd[-1] in self.pat.files:
                cont = self.pat.files[cmd[-1]].show()
                if cont != None:
                    print('> '+cont)
            #Se o arquivo não exixtir    
            else:
                print('Arquivo inexistente')
                
        #touch - Cria um arquivo -------------------------------      
        elif cmd[0] == 'touch':
            #Se o arquivo ja existe
            if cmd[-1] in self.pat.files:
                pass
            else:
                self.pat.add(File(cmd[-1]))
                
        #echo - escreve em um arquivo --------------------------
        elif cmd[0] == 'echo':
            cont = ' '.join(cmd[1:-2])
            if cmd[-2] == '>':
                dest = cmd[-1]
                if dest in self.pat.files:
                    if self.pat.files[dest].change:
                        self.pat.files[dest].write(cont[1:-1])
                    else:
                        print("Você não pode mudar esse arquivo por enquanto")
                else:
                    print('Arquivo '+dest+' inexistente')
        
        #mkdir - cria um diretorio no diretorio atual -----------
        elif cmd[0] == 'mkdir':
            #Se a pasta ja existe
            if cmd[-1] in self.pat.filhos:
                print('Pasta '+cmd[-1]+' ja existe')
            else:
                self.pat.add(Pasta(cmd[-1]))
                
        #rm - remove um diretorio -------------------------------
        elif cmd[0] == 'rm':
            #Se a pasta existe
            if cmd[-1] in self.pat.filhos:
                if self.pat.filhos[cmd[-1]].change:
                    self.pat.rm(cmd[-1])
                else:
                    print("Você não pode excluir essa pasta por enquanto")
            elif cmd[-1] in self.pat.files:
                if self.pat.files[cmd[-1]].change:
                    self.pat.rm(cmd[-1])
                else:
                    print("Você não pode excluir esse arquivo por enquanto")
        
        #exit - finaliza o programa ------------------------------
        elif cmd[0] == 'exit':
            self.exit = True
        
        return          
    #--------------------------------------------------------- ---------------               
    def printLine(self):
        print("\033[1;32;48m"+self.user_name+'@'+self.user_name+':'+"\033[1;34;48m"+self.pat.nome+"\033[0;0;0m"+'$', end=' ')
        
    #--------------------------------------------------------- ---------------       
    def segue(self , rep, cmd = None):
        if cmd==None:
            self.printLine()
            cmd = str(input())
        self.cmdReader(cmd, rep)
        if self.exit: return True
        while cmd != 'segue':
            self.printLine()
            cmd = str(input())
            self.cmdReader(cmd, rep)
            if self.exit: return
    
    #--------------------------------------------------------- ---------------
    def segue_cond(self, cmd_obj, txt, pat_nome):
        self.printLine()
        cmd = str(input())
        while(cmd != cmd_obj or self.pat.nome != pat_nome):
            if(cmd == cmd_obj and self.pat.nome != pat_nome):
                print("Va para a pasta "+pat_nome+" antes de usar esse comando")
            self.cmdReader(cmd, txt)
            if self.exit: return
            self.printLine()
            cmd = str(input())
        self.cmdReader(cmd, txt)
        return
    #--------------------------------------------------------- ---------------   
    def checkFase(self):
        #Se estiver na fase 1
        if(self.fase == 1):
            print("Capítulo 1 - A Tragédia e o Pinguim")
            time.sleep(2)
            print('Linus: Não, de novo não…')
            time.sleep(2)
            print('Linus: O Delamaro Mestre Hacker do Mal precisa parar com essas travessuras.')
            time.sleep(2)
            txt = 'Linus: Lá vamos nós então, consegue me ouvir err.. ler? (Não consigo te ouvir, responda \nteclando “segue", depois pressionando ENTER. Se não me entendeu, tecle "repete" e ENTER.)'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Perfeito, esse teclado vai ser nossa única forma de comunicação por enquanto, tente \nnão perdê-lo.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Deve ter várias perguntas. Por que o céu é azul? Por que a minha tela está preta? \nComo amarro uma gravata? '
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Da forma mais indolor então, respectivamente, a luz azul se espalha facilmente por \nter uma maior frequência de onda; a tela está assim por conta do Malvado Mestre \nDelamaro, que sugou sua interface gráfica, deixando apenas este “Terminal”; por fim, não \nsei dar nós em gravatas ou em qualquer outra coisa, pois sou um pinguim virtual. Me chame \nde Linus.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            print('Linus: A propósito, como você chama? (Responda e pressione ENTER.)')
            name = str(input())
            while '/' in name or ' ' in name or name == '':
                print('Nome invalido! Favor inserir um novo nome')
                name = str(input())
            self.user_name = name
            print('Linus: Interessante. '+self.user_name+', vai também ser útil uma senha simples, digite e nao \nesqueça dela. (Responda e pressione ENTER.)')
            self.senha = str(input())
            txt = '...'
            self.segue(txt)
            if self.exit: return True
            print('Linus: Ótimo, alguma pergunta antes de embarcarmos?')
            time.sleep(2)
            txt = 'Linus: Brincadeira, não fui programado para responder perguntas, vamos começar antes \nque o Delamaro tenha outra ideia brilhante...'
            print(txt)

            self.fase = 2
        
        #Se estiver na fase 2
        if(self.fase == 2):
            print("\nCapítulo 2 - A Volta ao Mundo")
            time.sleep(2)
            txt = 'Linus: Bom, já consegue falar, mas ainda não tomou seus primeiros passos.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Literalmente. Se quiser recuperar a interface gráfica, vai ter que aprender a andar por \naqui.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Diga “ls” ao terminal se quiser enxergar o mundo ao seu redor.'
            print(txt)
            self.segue_cond('ls', txt, 'root')
            if self.exit: return True
            txt = 'Linus: Isso! Veja só que belas paisagens! Não consegue ver? Bom você pode pelo menos \n imaginar, aqui as coisas são simples para que funcionem mais rápido, não tem aquela \n demora toda de abrir uma coisa naquela tela cheia de pastas e ícones, eheheh. Enfim, para \n se movimentar, diga “cd x” ao terminal, onde x representa o lugar para onde deseja \n ir. Experimente entrar na floresta.'
            print(txt)
            self.segue_cond('cd floresta', txt, 'root')
            if self.exit: return True
            txt = 'Linus: Agora que estamos na floresta, olhe ao seu redor com “ls” e vá para o único lugar \navistado usando “cd”. (Use "cd .." se quiser andar para trás.)'
            print(txt)
            self.segue_cond('cd rio', txt, 'floresta')
            if self.exit: return True

            self.fase = 3
    
        if(self.fase == 3):
            print("\nCapítulo 3 - A Ponte da Miragem")
            time.sleep(2)
            print("Linus: Vamos precisar atravessar este rio. Olhe ao seu redor. Ideias?")
            self.segue_cond('ls', "Linus: Vamos precisar atravessar este rio. Olhe ao seu redor. Ideias?", 'rio')
            if self.exit: return True
            txt = 'Linus: Por ser difícil montar em um peixe, a ponte parece ser útil, mas nem a ponte nem a \nágua nem o peixe são lugares. Todos são itens. No mundo do terminal, lugares chamam \n“diretórios” e itens chamam “arquivos”.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Sabemos ir para diretórios usando “cd” mas para inspecionar um arquivo, o comando \né “cat x” (onde x = nome de um arquivo). Tente inspecionar o conteúdo da ponte.'
            print(txt)
            self.segue_cond('cat ponte.txt', txt, 'rio')
            if self.exit: return True
            txt = 'Linus: Instável?! O Delamaro deve ter corrompido nossa única passagem! Não se \ndesespere, o terminal consegue nos ajudar.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Digamos que o terminal tem uma lojinha chamada “apt-get”. Esse mercado é muito \npopular entre os moradores do terminal por vender tudo que a imaginação possa desejar.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Nós queremos apenas um martelo para consertar a ponte.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Para comprar um da apt-get, digite “apt-get martelo”'
            print(txt)
            self.segue_cond('apt-get martelo', txt, 'rio')
            print("Fabricando cabo...")
            time.sleep(1)
            print("Forjando a cabeça...")
            time.sleep(1)
            print("Acoplando partes...")
            time.sleep(1)
            print("Martelo adquirido !")
            txt = 'Linus: Martelo em mãos, vamos agora tentar mudar a ponte “instável” para uma ponte \n“firme”.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            print("Linus: Basta pegar seu martelo e…")
            time.sleep(1.5)
            self.root.filhos['floresta'].filhos['rio'].files['ponte.txt'].setChange(True)
            self.root.filhos['floresta'].filhos['rio'].rm('ponte.txt')
            txt = 'Linus: Você está vendo isso ? ... Use o ls para ver !'
            print(txt)
            self.segue_cond('ls', txt, 'rio')
            if self.exit: return True
            txt = 'Linus: A ponte estava tão instável que deve ter desabado.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Não queria te dar tanto poder tão cedo, mas não vejo outra forma…'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: A realidade é que nem precisávamos ir ao mercado apt-get comprar o martelo para \nconsertar a ponte, pois o terminal faz coisas mágicas para quem pede educadamente.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            print("Linus: Vamos brincar de Deus por um instante.")
            txt = 'Linus: Do éter, faça surgir uma ponte, dizendo: “touch ponte.txt”.'
            print(txt)
            self.segue_cond('touch ponte.txt', txt, 'rio')
            if self.exit: return True
            txt = 'Linus: Confirme que ela de fato está lá ... Use “cat” para inspecioná-la.'
            print(txt)
            self.segue_cond('cat ponte.txt', txt, 'rio')
            if self.exit: return True
            txt = 'Linus: Vazia! Nem instável nem firme. Vamos resolver isso de vez.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            print("Linus: Se “touch” fornece poderes de criação, “echo” fornece o poder da transformação.")
            txt = 'Linus: Use “echo “firme” > ponte.txt” para caracterizar a ponte que você criou como firme.'
            print(txt)
            self.segue_cond('echo "firme" > ponte.txt', txt, 'rio')
            if self.exit: return True
            txt = 'Linus: Perfeito, sempre bom confirmar que de fato funcionou. Use o cat no arquivo para verificar.'
            print(txt)
            self.segue_cond('cat ponte.txt', txt, 'rio')
            if self.exit: return True
            print("Linus: Olha só! Quem precisa de martelos quando temos o terminal?! Agora vamos tentar não morrer \ndo outro lado dessa ponte. Siga-me.")
            
            self.fase = 4
        
        if(self.fase == 4):
            print("\nCapitulo 4 - A Caverna da Criptografia")
            self.root = self.changeEnv()
            self.pat = self.root
            time.sleep(1)
            txt = 'Linus: Hm… parece que essa caverna sinistra é o único caminho avante.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: '+self.user_name+' acredito no seu bom senso, veja bem, um lugar desses está longe \ndemais do habitat de um pinguim.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Vou ter que te abandonar por aqui, mas que te desejo sucesso na reconquista da sua \ninterface gráfica.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Ah, quase me esqueci! Lá dentro deve encontrar um arquivo razoavelmente prestativo \npelo nome de “ManualQuartus.txt”, recomendo a leitura… até mais!'
            print(txt)
            self.segue_cond('touch enigma.txt', 'Leia o manual...', 'caverna')
            if self.exit: return True
            self.segue_cond('echo "cifra de cesar" > enigma.txt', 'Leia o manual...', 'caverna')
            if self.exit: return True
            txt = 'Manual: O que?! Saiba que antigamente, ludibriava exércitos inteiros com esse meu enigma!'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Manual: Mas para um livro, a palavra é a única coisa que me resta, então tome aqui sua saída. \nSabia que deveria ter mandado o enigma do RSA…'
            print(txt)
            saida = Pasta('saida', True)
            letras = File('letras.txt', False)
            letras.write('l c d m p g h r j x k e b s n u o y v q a t i w z f')
            ordenador = File('ordenador', False)
            ordenador.write('Arquivo executável')
            saida.add(letras)
            saida.add(ordenador)
            self.root.filhos['caverna'].add(saida)
            print('Manual: Você me parece digno de seguir adiante ... a saída foi criada, use o ls para vê-la.')
            self.segue_cond('cd saida', 'Entre na saída (isso faz algum sentido ?)', 'caverna')
            if self.exit: return True
            
            self.fase = 5
            
        if(self.fase == 5):
            print("\nCapitulo 5 - O Deserto da Desordem")
            time.sleep(1)
            txt = 'Knuth: Um túnel na caverna de criptografia?? Nao vejo isso faz um bom tempo.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Knuth: Também foi aprisionado nesse mundo escuro e mágico voluntariamente? Como está \naquele pinguim?'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Knuth: Desculpa, não interajo com organismos do mundo de fora há séculos, devo me apresentar.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Knuth: Sou o Donald, passo a eternidade aqui, neste deserto, testando algoritmos de ordenação… \nquer testar um?'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Knuth: Está vendo aquele monte de letras? Use o cat! Sei que se chegou aqui, deve conhecê-lo.'
            print(txt)
            self.segue_cond('cat letras.txt', txt, 'saida')
            if self.exit: return True
            txt = 'Knuth: Não há tempo em uma vida humana para manualmente ordenar essas letras em ordem \nalfabética! Por isso acabei hoje de preparar um belo algoritmo de ordenação, seria uma honra ter \nvocê aqui para presenciar o funcionamento.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Knuth: Tente você rodar minha obra! Para executar um programa, use “./x < y”, em que “x” \nrepresenta o nome do programa e “y”, o nome da entrada.'
            print(txt)
            self.segue_cond('./ordenador < letras.txt', txt, 'saida')
            self.root.filhos['caverna'].filhos['saida'].files['letras.txt'].write('a b c d e f g h i j k l m n o p q r s t u v w x y z')
            if self.exit: return True
            time.sleep(1)
            print('--- execução completa ---')
            txt = 'Knuth: Olha só a rapidez!! Será que finalmente criei um sort O(n)?? Essa vai para o livro!'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Knuth: err… perdoe o diálogo retórico, me empolgo às vezes. Obrigado pela companhia, \nmas dizem que está aqui para recuperar sua interface gráfica (não entendo o porque).'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Knuth: Posso te ajudar a criar um portal diretamente para o lar do famigerado Delamaro.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Knuth: Se “touch” cria arquivos, “mkdir” cria diretórios! Quando quiser partir, só crie um \ndiretório chamado “portal” e entre nele. Fico por aqui mesmo, bom sort, ops, boa sorte na empreitada!'
            txt = print(txt)
            self.segue_cond('mkdir portal', txt, 'saida')
            if self.exit: return True
            self.segue_cond('cd portal', 'Entre no portal', 'saida')
            if self.exit: return True
            
            self.fase = 6
        
        if(self.fase == 6):
            print('\nCapitulo 6 - O Castelo das Trevas ')
            time.sleep(1)
            portal = Pasta('portal', False)
            castelo = Pasta('entradaCastelo', False, False)
            corda = File('corda.txt')
            corda.write('Corda grossa de palha.')
            castelo.add(corda)
            portal.add(castelo)
            self.root = portal
            self.pat = self.root
            self.segue_cond('cd entradaCastelo', 'Entre no castelo', 'portal')
            if self.exit: return True
            txt = 'Voz: Usuário detectado.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Voz: Usuário sem permissões para acessar entradaCastelo, lar de sua majestade Dela, o \ninatingível.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Voz: Permissões concedidas apenas para super-usuários. Ativa-se modo super-usuário com “sudo x”, \nonde x = comando qualquer.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Voz: Porque um sistema programado com o fim único de proteger esta fortaleza te fornece essa \ninformação?'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Voz: Porque sei que nao lembra da sua senha. (*gargalhadas metálicas*)'
            print(txt)
            self.segue_cond('sudo cd entradaCastelo', 'use o "sudo" antes de entrar no castelo', 'portal')
            if self.exit: return True
            print("Insira a senha do usuario: ")
            senha = str(input())
            while(senha != self.senha):
                print("Senha incorreta! Tente novamente:")
                senha = str(input())
            txt = 'Voz: Aquele Knuth me programou bobão demais! O Mestre Dela não ficará contente com isso…'
            castelo.changePerm(True)
            self.pat = castelo
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Ei! '+self.user_name+'! Pra cá!'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Sim, pendurado do teto! Servos do Delamaro me capturaram logo depois que te deixei \nna caverna. Mas não me arrependo de ter te ajudado, apesar de não enxergar a grande vantagem de \nviver nessa tal de “interface gráfica”.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Agora chega de conversa, sabe que pinguins tem medo de altura! Remova essa corda que \nme pendura usando o comando “rm x”, onde x é um arquivo ou diretório.'
            print(txt)
            self.segue_cond('rm corda.txt', txt, 'entradaCastelo')
            if self.exit: return True
            txt = 'Linus: Certo, tenho que fugir antes que ele me ache de novo, porém não antes de resolver seu \npepino, estamos tão próximos.'
            esconde = File('escondeesconde.txt', False)
            esconde.write('Lectus vivamus erat placerat magna netus integer tincidunt primis, ultricies aliquam urna amet\n \
                          turpis etiam himenaeos lacus, quis leo eu nisi lorem nullam amet. dolor dictum volutpat molestie\n \
                          curae proin varius arcu, sed enim vehicula dictumst leo ornare orci, suspendisse varius feugiat\n \
                          sodales quisque praesent. nisi aptent sed primis fringilla leo malesuada quisque aliquet ad varius\n \
                          class, habitasse ullamcorper justo platea velit aliquam porttitor venenatis iaculis. blandit ornare\n \
                          netus sollicitudin ut vulputate euismod, bibendum eu sem maecenas molestie. venenatis varius\n \
                          vehicula iaculis at velit nisi, at class ornare nunc etiam hendrerit urna, nullam rhoncus nisi velit eu.\n \
                          \tDictumst felis gravida et velit sodales aliquet sodales dui consequat ultricies ad diam eleifend, at\n \
                          venenatis massa suspendisse viverra laoreet libero commodo interdum eros est primis. dictumst\n \
                          nisl quam convallis mi inceptos dolor molestie neque purus quam, fusce mollis et facilisis\n \
                          consequat netus nam quisque nullam sit, neque praesent ad ullamcorper magna tellus arcu proin\n \
                          phasellus. potenti phasellus arcu dictum in ultricies torquent aliquam pulvinar, ornare dapibus\n \
                          faucibus praesent nec ornare enim facilisis, vehicula fames tempus ornare nam venenatis congue.\n \
                          netus curabitur vulputate rutrum fringilla maecenas sodales arcu hac, euismod sagittis per felis\n \
                          sapien mattis taciti pulvinar, aenean non mattis est convallis massa nullam. \n \
                          \tPhasellus molestie consequat facilisis eros habitasse viverra congue metus, habitant eu hac\n \
                          lobortis sem ligula aenean habitasse ligula, dictum rutrum curabitur pretium tincidunt id quam.\n \
                          congue cursus fermentum blandit batata senha super secreta: turing1936 malesuada donec\n \
                          condimentum, dui tempor bibendum blandit vel, massa rhoncus nec class lorem. sollicitudin primis\n \
                          luctus etiam nisi hac primis nunc quisque, platea lobortis aptent lacinia eu ante curae, ultrices\n \
                          cubilia felis libero dolor euismod netus. tempor libero consequat sociosqu rhoncus sagittis sed\n \
                          tristique lobortis vivamus phasellus aptent bibendum, sapien fringilla eu cursus tincidunt lectus\n \
                          lobortis per consequat nunc elit mauris, donec urna vulputate eleifend at curae sodales suscipit class \n \
                          fusce nam. \n \
                          \tNisi velit torquent senectus faucibus nec senectus luctus, vivamus nulla ullamcorper\n \
                          fermentum porta nec dictum, luctus integer nostra pulvinar torquent etiam. vivamus vestibulum\n \
                          pretium cubilia magna maecenas vehicula egestas nostra neque pellentesque, suscipit sociosqu\n \
                          vehicula commodo venenatis faucibus habitant sociosqu orci. auctor metus curabitur class semper\n \
                          netus tristique sed eget praesent pellentesque, lacus a adipiscing morbi blandit cras tempus quisque\n \
                          fames, primis elit donec massa pretium sagittis ut sapien arcu. vestibulum erat tempor aenean\n \
                          fringilla platea cursus, vel bibendum dui potenti tempor, egestas tortor nunc dictum etiam. sed leo\n \
                          mauris donec odio dui facilisis ut porttitor, hendrerit velit tellus elit proin molestie posuere ac\n \
                          aliquam, id consectetur dui tempus nisi varius tristique. \n \
                          \tJusto ad non aptent ultrices facilisis nunc proin ad lobortis, enim potenti fermentum\n \
                          pellentesque sem varius accumsan justo tempor, imperdiet luctus dolor suspendisse leo id mollis\n \
                          lorem. pretium ultrices maecenas dictum fermentum vulputate class consequat praesent urna\n \
                          mauris, cubilia tempus primis orci vel nisl litora iaculis. sit eu ligula praesent class massa\n \
                          malesuada ultrices diam sit lacus, hendrerit congue sagittis congue quisque scelerisque id habitant\n \
                          dui accumsan, ac erat habitant lectus condimentum ultricies suspendisse etiam sociosqu. tellus\n \
                          malesuada rhoncus per semper diam, erat primis quisque aliquam. \n')
            self.root.filhos['entradaCastelo'].add(esconde)
            txt = 'Linus: Enquanto estava amarrado, vi o Dela retirando uma senha desse arquivo \nescondeesconde.txt e usando ela para sair do terminal.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Não guardei a senha direito, mas lembro que estava escrita na mesma linha em que \ntambém estava escrito “batata”.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: O terminal sempre teve um comando para nos salvar e dessa vez não vai ser diferente. O \ncomando “grep” mostra a linha toda de um arquivo, que contém um certo trecho já conhecido!'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Use ele assim: “grep “x” y”, onde x seria seu trecho conhecido e y, um arquivo. Agilidade!'
            print(txt)
            self.segue_cond('grep "batata" escondeesconde.txt', txt, 'entradaCastelo')
            if self.exit: return True
            print('congue cursus fermentum blandit batata senha super secreta: turing1936 malesuada donec')
            interface = File('interfaceGrafica.txt', False)
            self.pat.add(interface)
            txt = 'Linus: Ótimo, em breve deve abrir um portal para a interface gráfica, você escreve essa senha lá \ndentro e voilá!'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Delamaro: Para onde pensa que vai Linus?? Este estrupício te liberou?'
            dela = File('Delamaro.txt', False)
            dela.write('Entranhas malignas.')
            self.root.filhos['entradaCastelo'].add(dela)
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Delamaro: '+self.user_name+' deveria me agradecer por estar entre a metade dos usuários de \ncomputadores que eu suguei para este mundo! Usuários de interface gráfica estão muito mal \nacostumados, nunca experimentaram o poder de verdade, e parecem nem querer!'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            print('Delamaro: Ademais,')
            time.sleep(1.5)
            txt = 'Linus: Psst, sinto que esse discurso vai longe, tá aqui sua chance - nunca achei que diria isso \nmas - o que será que aconteceria se tentasse remover o Delamaro?'
            print(txt)
            self.segue_cond('rm Delamaro.txt', txt, 'entradaCastelo')
            self.root.filhos['entradaCastelo'].files['Delamaro.txt'].setChange(True)
            print('Delamaro: … e tenho sim um sonho em que o mundo reconhece … hm ...')
            time.sleep(1.5)
            print('Delamaro: … dizem que um braço esquerdo dormente não é bom sinal …')
            time.sleep(1.5)
            txt = 'Linus: Tá funcionando! Tenta de novo, com super-usuário ativado!'
            print(txt)
            self.segue_cond('sudo rm Delamaro.txt', txt, 'entradaCastelo')
            print("Insira a senha do usuario: ")
            senha = str(input())
            while(senha != self.senha):
                print("Senha incorreta! Tente novamente:")
                senha = str(input())
            self.root.filhos['entradaCastelo'].rm('Delamaro.txt')
            if self.exit: return True
            txt = 'Linus: Funcionou! Como não pensei nisso antes?!'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Bom, chamo isso de um dia produtivo.'
            print(txt)
            self.segue(txt)
            if self.exit: return True
            txt = 'Linus: Acho que vou visitar o Donald e ver como está indo o quarto volume daquele livro. Olha só, \no portal que eu tinha mencionado abriu! Só depositar a senha nele - a menos que quiser ficar por \naqui comigo. Garanto a diversão! Nesse caso, digite “palavras superam imagens”.'
            print(txt)
            return False
#---------------------------------------------------------------------------------------------------
        
env = Envirorment('user')
ext = env.checkFase()
if not ext:
    print('Digite a sua resposta:')
    resp = str(input())
    while(resp != 'palavras superam imagens'):
        if(resp == 'echo "turing1936" > interfaceGrafica.txt'):
            print('\tEscolha incorreta, tente novamente.\n\n\n')
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