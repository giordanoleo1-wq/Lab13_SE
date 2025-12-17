from database.DB_connect import DBConnect
from model.classificazione import Classificazione
from model.gene import Gene
from model.interazione import Interazione
class DAO:

    @staticmethod
    def read_all_interazione():
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM interazione """

        cursor.execute(query)

        for row in cursor:
            result.append(Interazione(**row))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def read_all_gene():
        conn = DBConnect.get_connection()
        result = {}
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM gene"""
        cursor.execute(query)
        for row in cursor:
            gene= Gene(**row)
            result[gene.id]=gene
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def read_all_classificazione():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM classificazione"""
        cursor.execute(query)
        for row in cursor:
            result.append(Classificazione(**row))
        cursor.close()
        conn.close()
        return result