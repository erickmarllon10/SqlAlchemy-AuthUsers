
from Usuarios.usuarios import registerUser, accessUser, chPasswd
from Servidores.servidores import addServer, delServer, defAdmin
import sys

def logout():
    print "Logout realizado"
    sys.exit()

def menu():
    try:
        print "\
               1 - Cadastrar usuario\n\
               2 - Acessar sistema\n\
               3 - Cadastrar Servidor\n\
               4 - Remover Servidor\n\
               5 - Definir Admnistrador\n\
               6 - Alterar Senha\n\
               7 - Logout"
        option = input ("Digite a opcao desejada: ")
        return option
    except Exception as err:
        print "Erro: %s"%err

def choose(x):
    try:
        dict_options = {1:registerUser,2:accessUser,3:addServer,4:delServer,5:defAdmin,6:chPasswd,7:logout}
        dict_options[x]()
    except Exception as err:
        print "Opcao invalida %s"%err

while True:
    choose(menu())
