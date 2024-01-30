import sqlite3

class DataBase:
    def __init__(self):
        self.DataBaseCon = sqlite3.connect("Members.db")
        self.Cursor = self.DataBaseCon.cursor()
        self.settable("a")
    
    def create(self,column):
    	self.Cursor.execute("create table IF NOT EXISTS "+self.Type+" (id INTEGER PRIMARY KEY AUTOINCREMENT,"+column+" DEFAULT NULL)")
        
    def add(self, colname,Values):
        self.Cursor.execute("INSERT INTO "+self.Type+" ("+colname+") VALUES("+Values+")")
        
    def addcol(self, colname):
        self.Cursor.execute("alter table "+self.Type+" add column "+colname)
    
    def update(self,colname,Value,n):
        self.Cursor.execute("UPDATE "+self.Type+" SET "+colname+" = "+str(Value)+" WHERE id= "+str(n))
    
    def delete(self,n):
        self.Cursor.execute("DELETE FROM "+self.Type+" WHERE id= "+str(n))
        
    def save(self):
        self.DataBaseCon.commit()
    
    def quit(self):
        self.DataBaseCon.close()
    
    def rollback(self):
        self.DataBaseCon.rollback()
        
    def selectColumn(self):
        self.Cursor.execute("SELECT * FROM "+self.Type)
        return self.Cursor.fetchall()
    
    def selectColNames(self):
        self.Cursor.execute("SELECT * FROM "+self.Type)
        col_names = [col[0] for col in self.Cursor.description]
        return col_names
    
    def selecttablenames(self):
        self.Cursor.execute("SELECT name FROM sqlite_master WHERE type IN ('table', 'view') AND name NOT LIKE 'sqlite_%' UNION ALL SELECT name FROM sqlite_temp_master WHERE type IN ('table', 'view') ORDER BY 1")
        return self.Cursor.fetchall()
    
    def settable(self,tablename):
        self.Type = str(tablename)
