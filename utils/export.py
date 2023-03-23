# Fichier contenant les fonctions d'extraction des données dans un format exploitable

import csv
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def getConnection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def getData():
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM performances limit 100")
    data = cursor.fetchall()
    connection.close()
    return data


def getMergedData():
    connection = getConnection()
    sql = "SELECT s.idswimmer, s.firstname, s.lastname, s.gender, s.birthdate, s.nation FROM performances p JOIN swimmers s ON p.idswimmer = s.idswimmer limit 100"
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.close()
    return data













def exportCSV(data):
    with open("data.csv", "w+", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__=="__main__":
    pass

