Envirorment
*******************************************************************************************
Classe que cria objetos do tipo envirorment, que simulam o terminal de uma máquina e realizam a progressão do jogo

Métodos:
===========================================================================================

1. __init__(self, user_name)
-------------------------------------------------------------------------------------------
Construtor do objeto

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(Envirorment): Ponteiro para o objeto
* user_name(str): Nome do usuario

2. changeEnv(self)
-------------------------------------------------------------------------------------------
Método que cria uma nova estrututra para o ambiente

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(Envirorment): Ponteiro para o objeto

Outputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* (Pasta): Pasta raiz do novo sistema

3. cmdReader(self, cmd, rep)
-------------------------------------------------------------------------------------------
Função que le e interpreta um comando passado ao terminal

Input:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(Envirorment): Ponteiro para o objeto
* cmd: (str) Linha do comando dado ao terminal
* rep(str): Frase que será repetida caso seja dado o comando repete

4. printLine(self)
-------------------------------------------------------------------------------------------
Método que imprime a linha do terminal

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(Envirorment): Ponteiro para o objeto

5. segue(self, rep)
-------------------------------------------------------------------------------------------
Método que processa os comandos inseridos pelo usuario e segue o fluxo do jogo caso o comando segue seja dado

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(Envirorment): Ponteiro para o objeto
* rep(str): Mensagem passada para o cmdReader para ser repetido

6. segueCond(self, cmd_obj, txt, pat_nome)
-------------------------------------------------------------------------------------------
Método que segue o fluxo do jogo caso um comando específicado seja dado em uma pasta especificada

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(Envirorment): Ponteiro para o objeto
* cmd_obj(str): string com o comando que deve ser dado para a continuação do jogo
* txt(str): texto que será passado para o cmdReader para ser repetido
* pat_nome(str): Nome da pasta na qual o comando deve ser dado

7. checkFase(self)
-------------------------------------------------------------------------------------------
Método que realiza a progressão do jogo

Input:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(Envirorment): Ponteiro para o objeto

Output:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* (bool): Valor booleano que indica se o comando exit foi dado ou não

Atributos:
===========================================================================================
* user_name(str): Nome do usuario do ambiente
* root(Pasta): Pasta raiz do ambiente
* pat(Pasta): Pasta atual do ambiente
* fase(int): Fase atual do jogo
* exit(bool): Flag que indica se o comando exit foi dado
* senha(str): Senha do usuario