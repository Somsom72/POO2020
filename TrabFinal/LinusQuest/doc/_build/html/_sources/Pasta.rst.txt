Pasta
*******************************************************************************************
Classe que cria objetos do tipo Pasta que serão manipulados durante a execução do jogo.

Métodos:
===========================================================================================

1. __new__(cls, nome, change=True, perm=True)
-------------------------------------------------------------------------------------------
Método que instancia a classe ou impede a sua istanciação caso
algumas condições não sejam satisfeitas

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* cls(Pasta): Ponteiro para a classe
* nome(str): Nome do novo objeto
* change(bool): Flag que indica se o objeto pode ou não ser modificado pelo usuário
* perm(bool): Flag que indica se o objeto pode ou não ser acessado pelo usuário

Outputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* (Pasta): Objeto instanciado

2. __init__(self, nome, change=True, perm=True)
-------------------------------------------------------------------------------------------
Método construtor da classe

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(Pasta): Ponteiro para o objeto
* nome(str): Nome do novo objeto
* change(bool): Flag que indica se o objeto pode ou não ser modificado pelo usuário
* perm(bool): Flag que indica se o objeto pode ou não ser acessado pelo usuário

3. ls(self)
-------------------------------------------------------------------------------------------
Método que ista os arquivos e pastas do objet

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(Pasta): O ponteiro para o objeto

4. add(self, to_add)
-------------------------------------------------------------------------------------------
Método que adiciona um arquivo ou pasta ao objeto.

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(Pasta): O ponteiro para o objeto
* to_add(Pasta ou File): Objeto do tipo Pasta ou Arquivo

5. rm(self, to_rem)
-------------------------------------------------------------------------------------------
Método que remove um arquivo ou pasta do objeto.

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(Pasta): O ponteiro para o objeto
* to_rem(str): Nome do arquivo ou pasta a ser removido

Outputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* (Arquivo ou Pasta): Objeto que foi removido do diretorio atual

6. cd(self, to_ent)
-------------------------------------------------------------------------------------------
Método que busca pela pasta filha especificada.

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(Pasta): O ponteiro para o objeto
* to_ent(str): Nome da pasta filha desejada

Outputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* (Pasta): Ponteiro para a pasta filha desejada

7. setPerm(self, new)
-------------------------------------------------------------------------------------------
Método que altera a flag de permissão do objeto

Inputs:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* self(Pasta): O ponteiro para o objeto
* new(bool): Novo valor da flag

Atributos:
===========================================================================================
* nome(str): Nome do objeto
* pai(Pasta): Pasta na qual o objeto está contido (None caso seja raiz)
* filhos(lista): Lista com as pastas contidas no objeto
* files(lista): Lista com os arquivos contidos no objeto
* is_empty(bool): Flag que indica se o objeto está vazio
* change(bool): Flag que indica se o objeto pode ou não ser excluido pelo usuário
* perm(bool):  Flag que indica se o objeto pode ou não ser acessado pelo usuário