class Pasta(object):
    
    def __new__(cls, nome, change=True):
        if ' ' in nome or '/' in nome:
            print("Nome invalido")
            return None

        instance = super().__new__(cls)
        instance.nome = nome
        instance.change = change
        return instance
    
    #-------------------------------------------------------
    def __init__(self, nome, change=True):
        self.nome = nome
        self.pai = None
        self.filhos = {}
        self.files = {}
        self.is_empty = True
        self.change = change
    
    #---------------------------------------------------------
    def ls(self):
        '''
        Lista os arquivos e pastas do diretorio atual
        '''
        for sub in self.filhos:
            print("\033[1;31;48m"+str(sub)+"\033[0;0;0m")
        
        for file in self.files:
            print("\033[1;33;48m"+str(file)+"\033[0;0;0m")
            
    #---------------------------------------------------------        
    def add(self, to_add):
        '''
        Adiciona um arquivo ou pasta ao diretório atual.
        inputs:
            to_add: Objeto do tipo Pasta ou Arquivo
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
        '''
        Remove um arquivo ou pasta do diretorio atual
        inputs:
            to_rem: String com o nome do arquivo ou pasta a ser removido
        outputs:
            rem: Objeto do tipo Arquivo ou Pasta que foi removido do diretorio atual
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
        '''
        Retorna a pasta filha especificada
        inputs:
            to_ent: String com o nome da pasta filha na qual se deseja entrar
        outputs:
            pasta filha desejada
        '''
        if to_ent in self.filhos:
            return self.filhos[to_ent]
        else:
            print("Pasta "+to_ent+" inexistente em "+str(self.nome))
            return self
        
#---------------------------------------------------------------------------------------------------        

class File(object):
    def __new__(cls, nome, change=True):
        if ' ' in nome or '/' in nome:
            print("Nome invalido")
            return None

        instance = super().__new__(cls)
        instance.nome = nome
        instance.change = change
        return instance
    
    def __init__(self, nome ,change=True):
        self.nome = nome
        self.pai = None
        self.conteudo = None
        self.change = change
        
    def write(self, text):
        self.conteudo = text
        
    def show(self):
        if self.conteudo == None:
            print('Arquivo vazio')
            return None
        else:
            return self.conteudo

#---------------------------------------------------------------------------------------------------
            
class Envirorment(object):
    def __init__(self, user_name):
        
        self.user_name = user_name
        
        self.root = Pasta('root', False)
        
        pst1 = Pasta('home', False)
        pst1.add(Pasta('gustavo', False))
        pst1.add(Pasta('SomSom', False))
        
        pst2 = Pasta('Nathan', False)
        pst2.add(Pasta('p1', False))
        pst2.add(Pasta('p2', False))
        pst2.add(Pasta('p3', False))
        pst2.add(Pasta('p4', False))
        
        pst1.add(pst2)
        
        file = File('teste.txt', False)
        file.write('Arquivo de teste')
        
        pst1.add(file)
        
        self.root.add(pst1)
        
        self.pat = self.root
        
    #---------------------------------------------------------    
    def cmdReader(self, cmd):
        '''
        Função que le e interpreta um comando passado ao terminal
        input:
            cmd: (String) Linha do comando dado ao terminal
            root: (Pasta) Pasta root do sistema
            pat: (Pasta) Pasta atual
        '''
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
            if cmd[-2] == '>>':
                dest = cmd[-1]
                if dest in self.pat.files:
                    if self.pat.files[dest].change:
                        self.pat.files[dest].write(cont[1:-1])
                    else:
                        print("Acho melhor não mudar esse arquivo por enqunto")
                else:
                    print('Arquivo '+dest+' inexistente')
        
        #mkdir - cria um diretorio no diretorio atual -----------
        elif cmd[0] == 'mkdir':
            #Se a pasta ja existe
            if cmd[-1] in self.pat.filhos:
                print('Pasta '+cmd[-1]+' ja existe')
            else:
                self.pat.add(Pasta(cmd[-1]))
                
        #rm - remove um diretorio
        elif cmd[0] == 'rm':
            #Se a pasta existe
            if cmd[-1] in self.pat.filhos:
                if self.pat.filhos[cmd[-1]].change:
                    self.pat.rm(cmd[-1])
                else:
                    print("Acho melhor não excluir essa pasta por enquanto")
            elif cmd[-1] in self.pat.files:
                if self.pat.files[cmd[-1]].change:
                    self.pat.rm(cmd[-1])
                else:
                    print("Acho melhor não excluir esse arquivo por enquanto")
                    
                    
    def printLine(self):
        print("\033[1;32;48m"+self.user_name+'@'+self.user_name+':'+"\033[1;34;48m"+self.pat.nome+"\033[0;0;0m"+'$', end=' ')       

#---------------------------------------------------------------------------------------------------
        
env = Envirorment('user')
env.printLine()
cmd = str(input())
while cmd != 'exit':
    env.cmdReader(cmd)
    env.printLine()
    cmd = str(input())