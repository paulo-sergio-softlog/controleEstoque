# -*- coding: utf-8 -*-
from PySide2 import QtGui, QtCore, QtWidgets
from functools import partial
import re


class Funcao(object):

    def LimpaFrame(self, frame):
        for i in range(len(frame.children())):
            frame.children()[i].deleteLater()

    def DesativaBotao(self, frame, botao):
        for filho in frame.findChildren(QtWidgets.QPushButton):
            filho.setEnabled(True)

        botao.setEnabled(False)

    def ativaBotoes(self, frame):
        for filho in frame.findChildren(QtWidgets.QPushButton):
            filho.setEnabled(True)

    def IconeBotaoTopo(self, botao, imagem):

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(imagem),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # icon.addPixmap(QtGui.QPixmap((os.path.join(caminho, imagem)),
        #                              QtGui.QIcon.Normal, QtGui.QIcon.Off))
        botao.setIcon(icon)
        botao.setIconSize(QtCore.QSize(50, 35))

    def IconeBotaoMenu(self, botao, imagem):

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(imagem),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        botao.setIcon(icon)
        botao.setIconSize(QtCore.QSize(25, 25))

    def IconeBotaoForm(self, botao, imagem):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(imagem),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        botao.setIcon(icon)
        botao.setIconSize(QtCore.QSize(80, 35))
    
    # Mascara Telefone
    def TelefoneMask(self, telefone):
        if len(telefone) == 11:
            self.tx_Telefone.setInputMask("(00) 00000-0000")
        else:
            self.tx_Telefone.setInputMask("(00) 0000-0000")
        pass
    
    #Formatando numero de telefone as tabelas
    def formatoNumTelefone(self, telefone):
        telefone = re.sub('[^0-9]+', '', telefone)
        if len(telefone) == 11:
            formato = re.sub('(\d{2})(\d{5})(\d{4})', r'(\1) \2-\3', telefone)
        elif len(telefone) == 10:
            formato = re.sub('(\d{2})(\d{4})(\d{4})', r'(\1) \2-\3', telefone)
        else:
            formato = ""
        
        return formato


