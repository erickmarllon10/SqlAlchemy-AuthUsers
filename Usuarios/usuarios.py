
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import sessionmaker,relationship
from Models.model import session,Users

def registerUser():
    print "----------------------------------"
    print "------ Cadastro de usuarios ------"
    print "----------------------------------"
    userName = raw_input("Digite o nome do usuario: ")
    userLogin = raw_input("Digite o email do usuario %s: "%userName)
    userPass = raw_input("Digite a senha do usuario %s: "%userName)
    try:
        usuario = Users(userName, userLogin, userPass)
        session.add(usuario)
        session.commit()
        print "Usuario %s registrado com sucesso!"%userName
    except Exception as e:
        print "Erro: %s"%e
        session.rollback()
		
def accessUser():
    print "--------------------------------------"
    print "------ Autenticacao de usuarios ------"
    print "--------------------------------------"
    login = raw_input("Digite o seu login: ")
    passw = raw_input("Digite a sua senha: ")
    try:
        usuario = session.query(Users).filter(Users.nome==login).first()
        if usuario.senha == passw:
            print "Autenticado com sucesso"
        else:
            print "Erro de autenticacao"
    except Exception as e:
        print "Erro: %s"%e

def chPasswd():
    print "--------------------------------"
    print "------ Alteracao de senha ------"
    print "--------------------------------"
    try:
        usuarios = session.query(Users).all()
        for u in usuarios:
            print u.id," - ",u.nome," - ",u.senha
        opcao = input("Digite o id do usuario que deseja definir a nova senha: ")
        usuario = session.query(Users).filter(Users.id==opcao).first()
        newPass = raw_input("Digite a nova senha do usuario %s: "%usuario.nome)
        usuario.senha = newPass
        session.commit()
        print "Senha alterada com sucesso"
    except Exception as e:
        print "Erro ao alterar a senha: \n%s"%e
        session.rollback()

