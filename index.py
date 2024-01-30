import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import DataBaseController as dbc
import GraphGenerator as GG

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.MemberDB = dbc.DataBase()
        #self.Graph = GG.Graphgenerator()
        #self.canvas = self.Graph.polar()
        #self.dbColname = self.MemberDB.selectColNames()
        #self.dbCol = self.MemberDB.selectColumn()
        self.MemberDB.settable("a")
        
        self.name = [['./icon/cal.png','./icon/check.png','./icon/pentagon.png'],['./icon/member.png','./icon/change.png','./icon/db.png']]
        
        self.default = QWidget()
        self.initlayout = QWidget()
        self.calendar = QWidget()
        self.check = QWidget()
        self.graph = QWidget()
        self.member = QWidget()
        self.change = QWidget()
        self.db = QWidget()
        
        
        self.initUI()
        self.calendarUI()
        self.checkUI()
        self.graphUI()
        self.memberUI()
        self.changeUI()
        self.dbUI()
        
        
        
        
        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.initlayout)
        self.Stack.addWidget(self.calendar)
        self.Stack.addWidget(self.check)
        self.Stack.addWidget(self.graph)
        self.Stack.addWidget(self.member)
        self.Stack.addWidget(self.change)
        self.Stack.addWidget(self.db)
        
        self.buttongroup.buttonClicked[int].connect(self.changepage)
        
        layout = QHBoxLayout(self.default)
        layout.addWidget(self.Stack)
        
        self.setCentralWidget(self.default)
        self.setWindowTitle('이종찬 배드민턴 0.1v')
        self.setFixedSize(1024, 768)
        self.center()
        #self.show()
        
    def initUI(self):
        Basegrid = QGridLayout()
        self.buttongroup = QButtonGroup()
        self.buttongroup.setExclusive(False)
        for i in range(2):
            for j in range(3):
                button = QPushButton()
                button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
                button.setFlat(True)
                button.setIcon(QIcon(self.name[i][j]))
                button.setIconSize(QSize(100, 100))
                if i == 1 and j == 0:
                    self.buttongroup.addButton(button,4)
                else:
                    self.buttongroup.addButton(button,(i+1)*(j+1))
                Basegrid.addWidget(button,i,j)
        self.initlayout.setLayout(Basegrid)
    
    def calendarUI(self):
        self.pagebar()
        
        self.layout.addLayout(QHBoxLayout(),1,0)
        self.layout.addWidget(QTableWidget(),1,1)
        self.layout.addLayout(QHBoxLayout(),1,2)
        
        self.layout.addLayout(QHBoxLayout(),2,0)
        self.layout.addLayout(QHBoxLayout(),2,1)
        self.layout.addLayout(QHBoxLayout(),2,2)
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 2)
        self.layout.setRowStretch(2, 1)
        self.layout.setColumnStretch(0, 0.5)
        self.layout.setColumnStretch(1, 3)
        self.layout.setColumnStretch(2, 0.5)
        self.calendar.setLayout(self.layout)
    def checkUI(self):
        self.pagebar()
        self.layout.addLayout(QHBoxLayout(),1,0)
        self.layout.addWidget(QPushButton("출석"),1,1)
        self.layout.addLayout(QHBoxLayout(),1,2)
        
        self.layout.addLayout(QHBoxLayout(),2,0)
        self.layout.addLayout(QHBoxLayout(),2,1)
        self.layout.addLayout(QHBoxLayout(),2,2)
        
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 2)
        self.layout.setRowStretch(2, 1)
        
        self.layout.setColumnStretch(0, 0.5)
        self.layout.setColumnStretch(1, 3)
        self.layout.setColumnStretch(2, 0.5)
        self.check.setLayout(self.layout)
    def graphUI(self):
        self.pagebar()
        self.layout.addLayout(QHBoxLayout(),1,0)
        self.layout.addWidget(QPushButton("그래프"),1,1)
        self.layout.addLayout(QHBoxLayout(),1,2)
        
        self.layout.addLayout(QHBoxLayout(),2,0)
        self.layout.addLayout(QHBoxLayout(),2,1)
        self.layout.addLayout(QHBoxLayout(),2,2)
        
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 2)
        self.layout.setRowStretch(2, 1)
        
        self.layout.setColumnStretch(0, 0.5)
        self.layout.setColumnStretch(1, 3)
        self.layout.setColumnStretch(2, 0.5)
        
        self.graph.setLayout(self.layout)
    def memberUI(self):
        self.pagebar()
        
        self.layout.addLayout(QHBoxLayout(),1,0)
        self.layout.addWidget(QPushButton("회원정보"),1,1)
        self.layout.addLayout(QHBoxLayout(),1,2)
        
        self.layout.addLayout(QHBoxLayout(),2,0)
        self.layout.addLayout(QHBoxLayout(),2,1)
        self.layout.addLayout(QHBoxLayout(),2,2)
        
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 2)
        self.layout.setRowStretch(2, 1)
        
        self.layout.setColumnStretch(0, 0.5)
        self.layout.setColumnStretch(1, 3)
        self.layout.setColumnStretch(2, 0.5)
        
        self.member.setLayout(self.layout)
    def changeUI(self):
        self.pagebar()
        
        self.layout.addLayout(QHBoxLayout(),1,0)
        self.layout.addWidget(QPushButton("회원조회"),1,1)
        self.layout.addLayout(QHBoxLayout(),1,2)
        
        self.layout.addLayout(QHBoxLayout(),2,0)
        self.layout.addLayout(QHBoxLayout(),2,1)
        self.layout.addLayout(QHBoxLayout(),2,2)
        
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 2)
        self.layout.setRowStretch(2, 1)
        
        self.layout.setColumnStretch(0, 0.5)
        self.layout.setColumnStretch(1, 3)
        self.layout.setColumnStretch(2, 0.5)
        
        self.change.setLayout(self.layout)
    def dbUI(self):
        tables = self.MemberDB.selecttablenames()
        columns = self.MemberDB.selectColNames()
        values = self.MemberDB.selectColumn()
        
        Tcombo = QComboBox()
        Ccombo = QComboBox()
        Vcombo = QComboBox()

        
        
        
        
        
        
        
        if not tables:
            pass
        else:    
            for i in range(len(tables)):
                Tcombo.addItem(tables[i][0])
        
        if not columns:
            pass
        else:    
            for i in range(len(columns)):
                Ccombo.addItem(columns[i])
        
        if not values:
            pass
        else:    
            for i in range(len(values)):
                Vcombo.addItem(values[i][0])
        
        
        
        
        
        
        
        
        
        Type = QComboBox()
        Type.addItem("종류")
        Type.addItem("요소")
        Type.addItem("값")
        
        self.pagebar()
        
        self.layout.addLayout(QHBoxLayout(),1,0)
        self.layout.addWidget(Ccombo,1,1)
        self.layout.addWidget(QPushButton(),1,2)
        
        self.layout.addLayout(QHBoxLayout(),2,0)
        self.layout.addWidget(Type,2,1)
        self.layout.addLayout(QHBoxLayout(),2,2)
        
        self.layout.setRowStretch(0, 0)
        self.layout.setRowStretch(1, 0)
        self.layout.setRowStretch(2, 0)
        
        self.layout.setColumnStretch(0, 0.5)
        self.layout.setColumnStretch(1, 3)
        self.layout.setColumnStretch(2, 0.5)
        
        self.db.setLayout(self.layout)
    
    def changepage(self,id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                self.Stack.setCurrentIndex(self.buttongroup.id(button))
    
    def pagebar(self):
        self.layout = QGridLayout()
        PageChangeButtons = QGridLayout()
        for j in range(6):
                button = QPushButton()
                button.setFlat(True)
                if j>2:
                	button.setIcon(QIcon(self.name[1][j-3]))
                else:
                    button.setIcon(QIcon(self.name[0][j]))
                button.setIconSize(QSize(30, 30))
                self.buttongroup.addButton(button,j+1)
                PageChangeButtons.addWidget(button,0,j)
        self.layout.addLayout(QHBoxLayout(),0,0)        
        self.layout.addLayout(PageChangeButtons,0,1)
        self.layout.addLayout(QHBoxLayout(),0,2)
    
    
    
    
    
    
    
    
    
    
    
    
    def table(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.dbCol))
        self.tableWidget.setColumnCount(len(self.dbColname))
        
        self.tableWidget.verticalHeader().setVisible(False)
        
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        #self.tableWidget.setHorizontalHeaderLabels(["id","출석","이름","나이","휴대폰 번호","실력","요금제","최초출석일","마지막출석일"])
        
        #for i in range(len(self.dbColname)):
        #    for j in range(len(self.dbCol)):
        #        self.tableWidget.setItem(j,i,QTableWidgetItem(str(self.dbCol[j][i])))
        
    def calendar(self):
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(False)
        self.cal.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        
    def showDate(self, date):
        self.lbl.setText(self.date.toString())
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())