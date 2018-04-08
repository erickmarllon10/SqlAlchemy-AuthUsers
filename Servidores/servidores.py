from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import sessionmaker,relationship
from Models.model import session,Servers
from Usuarios import usuarios

def addServer():
    print "------------------------------------"
    print "------ Cadastro de Servidores ------"
    print "------------------------------------"
    serverName = raw_input ("Digite o nome do servidor: ")
    serverIP = raw_input ("Digite o endereco IP do servidor: ")
    admLogin = raw_input ("Digite o nome do Sysadmin: ")
    try:
        servidor = Servers(serverName, serverIP, admLogin)
        session.add(servidor)
        session.commit()
        print "Servidor %s registrado com sucesso"%serverName
    except Exception as e:
        print "Erro: %s"%e
        session.rollback()

def delServer():
    try:
        servidores = session.query(Servers).all()
        for s in servidores:
            print s.id," - ",s.nome," - ",s.endereco
        opcao = input("Digite o id do servidor que deseja remover: ")
        deleteServer = session.query(Servers).filter(Servers.id==opcao).first()
        session.delete(deleteServer)
        session.commit()
        print "Servidor %s removido com sucesso"%deleteServer.nome
    except Exception as e:
        print "Erro: %s"%e
        session.rollback()

def defAdmin():
    try:
        servidores = session.query(Servers).all()
        for s in servidores:
            print s.id," - ",s.nome," - ",s.endereco," - ",s.administrador
        opcao = input("Digite o id do servidor que deseja definir o novo adm: ")
        newName = raw_input("Digite o nome do novo administrador: ")
        newAdmin = session.query(Servers).filter(Servers.id==opcao).first()
        newAdmin.administrador = newName
        session.commit()
        print "Novo adm %s definido com sucesso"%newName
    except Exception as e:
        print "Falha ao definir administrador: \n%s"%e

