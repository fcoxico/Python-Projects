from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
import sys
import sqlite3
import time
import os


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(500)
        self.setFixedHeight(500)

        QBtn = QDialogButtonBox.ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        self.setWindowTitle('Sobre: ')
        title = QLabel('Cadastro de Alunos em PYQT5')
        font = title.font()
        # font.setPointSize(20)
        font.setFontSize(20)
        title.setFont(font)

        labelpic = QLabel()
        pixmap = QPixmap('icon/add1.png')
        pixmap = pixmap.scaledToWidth(275)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(150)

        layout.addWidget(title)

        layout.addWidget(QLabel('V5.0'))
        layout.addWidget(QLabel('Copyright Francisco 2019'))

        layout.addWidget(labelpic)

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('icon/g2.png'))

        file_menu = self.menuBar().addMenu('&File')
        help_menu = self.menuBar().addMenu('&Ajuda')
        self.setWindowTitle('Cadastro de Alunos de PYQT5: ')
        self.setMinimumSize(800, 600)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(6)

        # Horizontal
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        # Vertical
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.tableWidget.setHorizontalHeaderLabels(
            ('Inscrição Nº', 'Nome', 'Filial', 'Semestre', 'Telefone', 'Endereço'))

        # Toolbar
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        # Botão para adicionar alunos
        btn_ac_adduser = QAction(QIcon('icon/add1.png'), 'Add Aluno', self)
        btn_ac_adduser.setStatusTip('Add Aluno')
        toolbar.addAction(btn_ac_adduser)

        btn_ac_refresh = QAction(QIcon('icon/r3.png'), 'Atualizar', self)
        btn_ac_refresh.setStatusTip('Atualizar dados do aluno')
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon('icon/s1.png'), 'Pesquisar', self)
        btn_ac_search.setStatusTip('Pesquisar')
        toolbar.addAction(btn_ac_search)

        btn_ac_delete = QAction(QIcon('icon/d1.png'), 'Deletar', self)
        btn_ac_delete.setStatusTip('Deletar')
        toolbar.addAction(btn_ac_delete)

        about_action = QAction(QIcon('icon/i1.png'), 'Desenvolvedor', self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def about(self):
        dlg = AboutDialog(QDialog)
        dlg.exec_()


app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = MainWindow()
    window.show()
sys.exit(app.exec_())
