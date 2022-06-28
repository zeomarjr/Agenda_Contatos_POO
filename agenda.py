from contato import *

class Agenda:
    def __init__(self):
        self.listaContatos = []

    def salvar_contatos(self):
        self.listaContatos.append(Contato())

    def listar_contatos(self):
        for i in range(len(self.listaContatos)):
            print('Cod:', self.listaContatos[i].cod,
                  '- Nome:', self.listaContatos[i].nome,
                  '- Telefone:', self.listaContatos[i].telefone)

    def modificar_telefone(self):
        controle = input('Informe o codigo do contato que deseja alterar:')
        for i in range(len(self.listaContatos)):
            if controle == self.listaContatos[i].cod:
                self.listaContatos[i].telefone = input('Digite o novo telefone')