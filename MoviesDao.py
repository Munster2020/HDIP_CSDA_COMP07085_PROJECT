import mysql.connector
import dbconfig as cfg


class MoviesDAO:
    db = ""

    def __init__(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql["host"],
            user=cfg.mysql["user"],
            password=cfg.mysql["password"],
            database=cfg.mysql["datarep"]
        )

    def create(self, dvds):
        cursor = self.db.cursor()
        sql = "insert into dvds (id, title, director, genre, price) values (%s, %s, %s, %s, %s)"
        values = [
            dvds['id'],
            dvds['title'],
            dvds['director'],
            dvds['genre'],
            dvds['price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from dvds"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql = "select * from dvds where id = %s"
        values = [id]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    def update(self, dvds):
        cursor = self.db.cursor()
        sql = "update dvds set title = %s, director = %s, genre = %s, price = %s where id = %s"
        values = [
            dvds['title'],
            dvds['director'],
            dvds['genre'],
            dvds['price'],
            dvds['id']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return dvds

    def delete(self, id):
        cursor = self.db.cursor()
        sql = "delete from dvds where id = %s"
        values = [id]
        cursor.execute(sql, values)
        return {}

    def convertToDict(self, result):
        colnames = ['id', 'title', 'director', 'genre', 'price']
        dvds = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                dvds[colName] = value
        return dvds


moviesDAO = MoviesDAO()
