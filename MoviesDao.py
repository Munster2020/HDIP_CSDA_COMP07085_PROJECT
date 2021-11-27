import mysql.connector
import dbconfig as cfg

class MoviesDao:

    def initConnectToDB(self):
      db = mysql.connector.connect(
         host=      cfg.mysql['host'],
         user=      cfg.mysql['username'],
         password=  cfg.mysql['password'],
         database=  cfg.mysql['database'],
         pool_name='my_connection_pool',
         pool_size=5
      )
      return db

    def getConnection(self):
      db = mysql.connector.connect(
         pool_name='my_connection_pool'
      )
      return db

    def __init__(self):
      db = self.initConnectToDB()
      db.close()

    def create(self, dvd):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "insert into dvds (id, title, director, genre, price) values (%s, %s, %s, %s, %s)"
        values = [
            dvd['id'],
            dvd['title'],
            dvd['director'],
            dvd['genre'],
            dvd['price']
        ]
        cursor.execute(sql, values)
        db.commit()
        lastRowId = cursor.lastrowid
        db.close()
        return lastRowId

    def getAll(self):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "select * from dvds"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        db.close()
        return returnArray

    def findById(self, id):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "select * from dvds where id = %s"
        values = [id]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        resultAsDict = self.convertToDict(result)
        db.close()
        return resultAsDict

    def update(self, dvd):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "update dvds set title = %s, director = %s, genre = %s, price = %s where id = %s"
        values = [
            dvd['title'],
            dvd['director'],
            dvd['genre'],
            dvd['price'],
            dvd['id']
        ]
        cursor.execute(sql, values)
        db.commit()
        db.close
        return dvd

    def delete(self, id):
        db = self.getConnection()
        cursor = db.cursor()
        sql = "delete from dvds where id = %s"
        values = [id]
        cursor.execute(sql, values)
        db.commit()
        db.close
        return{}

    def convertToDict(self, result):
        colnames = ['id', 'title', 'director', 'genre', 'price']
        dvd = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                dvd[colName] = value
        return dvd


moviesDao = MoviesDao()
