import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas       
import DataBaseController as dbc

class Graphgenerator:
    def __init__(self):
        self.StatusDB = dbc.DataBase("Status")
        self.AllColname = self.StatusDB.selectColNames()
        self.AllCol = self.StatusDB.selectColumn()
        self.Colname = self.AllColname[1:len(self.AllColname)]+[" "]
        self.Col = self.AllCol[0][1:len(self.AllCol)]+(self.AllCol[0][1],)
        
        self.fig = plt.Figure(figsize=(1,3))
        self.canvas = FigureCanvas(self.fig)
    
    def polar(self):
        
        theta = np.linspace(0, 2 * np.pi, len(self.Col))
        
        ax = self.fig.add_subplot(1,1,1,projection='polar')
        ax.set_rlim(0,100)
        #hfont = {'fontname':'NanumGothic'}
        ax.set_xticks(np.linspace(0, 2 * np.pi, len(self.Col)))
        ax.set_xticklabels(self.Colname)
        ax.plot(theta, self.Col,Color='darkviolet')
        ax.fill(theta, self.Col,Color='violet',alpha=0.3)
        
        return self.canvas