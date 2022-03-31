import sqlite3

class StudentDatabase():
        def __init__(self, fileName, create=False):
                self.__conn = sqlite3.connect(fileName)
                self.__cur = self.__conn.cursor()
                if create:
                        self.__cur.execute("DROP TABLE IF EXISTS Students")
                        self.__cur.execute("CREATE TABLE Students (sid INTEGER PRIMARY KEY, fn TEXT, ln TEXT, edu TEXT)")
        def add(self, fn, ln, edu):
                self.__cur.execute("INSERT INTO Students (fn, ln, edu) VALUES (?, ?, ?)", (fn, ln, edu))
                self.__conn.commit()
        def printALL(self):
                self.__cur.execute("SELECT * FROM Students")
                for row in self.__cur:
                        print(row)
        def close(self):
                self.__conn.close()
                
sdb = StudentDatabase("students.sqlite", True)
sdb.add("will", "Smith", "None")
sdb.add("Ole", "per", "None")
sdb.printALL()
sdb.close()