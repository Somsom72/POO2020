class Pasta(object):
    
    def __new__(cls, nome):
        if ' ' in nome or '/' in nome:
            print("Nome invalido")
            return None

        instance = super().__new__(cls)
        instance.nome = nome
        return instance
    
    #-------------------------------------------------------
    def __init__(self, nome):
        self.nome = nome
        self.pai = None
        self.filhos = {}
        self.files = {}
        self.is_empty = True
    
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
        
        
class Envirorment(object):
    def __init__(self, user_name):
        
        self.user_name = user_name
        
        self.root = Pasta('root')
        
        pst1 = Pasta('home')
        pst1.add(Pasta('gustavo'))
        pst1.add(Pasta('SomSom'))
        
        pst2 = Pasta('Nathan')
        pst2.add(Pasta('p1'))
        pst2.add(Pasta('p2'))
        pst2.add(Pasta('p3'))
        pst2.add(Pasta('p4'))
        
        pst1.add(pst2)
        
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
    
    def printLine(self):
        print("\033[1;32;48m"+self.user_name+'@'+self.user_name+':'+"\033[1;34;48m"+self.pat.nome+"\033[0;0;0m"+'$', end=' ')
        
        
env = Envirorment('user')
env.printLine()
cmd = str(input())
while cmd != 'exit':
    env.cmdReader(cmd)
    env.printLine()
    cmd = str(input())