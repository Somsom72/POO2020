File
*******************************************************************************************
Classe que cria objetos do tipo File que serão manipulados durante a execução do jogo

Métodos:
===========================================================================================

1. __new__(cls, nome, change=True)
-------------------------------------------------------------------------------------------
Método que instancia a classe ou impede a sua istanciação caso
algumas condições não sejam satisfeitas

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* cls(File): O ponteiro para a classe
* nome(str): Nome do novo objeto
* change(bool): Flag que indica se o objeto pode ou não ser modificado pelo usuário

Outputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* (File): Objeto instanciado

2. __init__(self, nome, change=True)
-------------------------------------------------------------------------------------------
Método construtor da classe

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(File): O ponteiro para o objeto
* nome(str): Nome do novo objeto
* change(bool): Flag que indica se o objeto pode ou não ser modificado pelo usuário

3. write(self, text)
-------------------------------------------------------------------------------------------
Método que salva uma string como conteudo do objeto.

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(File): O ponteiro para o objeto
* text(str): String com o conteúdo a ser salvo no objeto

4. show(self)
-------------------------------------------------------------------------------------------
Método que retorna o conteúdo de um objeto caso ele possua um ou uma mensagem caso contrário

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(File): O ponteiro para o objeto

Outputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* (str): Conteudo do objeto caso haja e None caso contrário

5. setChange(self, change)
-------------------------------------------------------------------------------------------
Método que altera a flag de modificação do objeto

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(File): O ponteiro para o objeto
* change(bool): Novo valor da flag


Atributos:
===========================================================================================
* nome(str): Nome do objeto
* pai(Pasta): Pasta na qual se encontra o objeto
* conteudo(str): Conteudo do objeto
* change(bool): Flag que indica se o ususario pode ou não modificar o objeto