from database.DB_connect import DBConnect
from model.squadra import Squadra


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.`year` as anno
from teams t 
where t.`year` >1979"""


        cursor.execute(query)

        for row in cursor:
            result.append(row["anno"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getSquadre(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.teamCode as cod, t.name as name 
from teams t 
where t.`year` =%s"""

        cursor.execute(query,(anno,))

        for row in cursor:
            result.append(f"{row["cod"]} ({row["name"]})")

        cursor.close()
        conn.close()
        return result
    def getNodi(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT t.* , sum(s.salary) as salario
                    FROM salaries s , teams t , appearances a 
                    WHERE s.`year` = t.`year` and t.`year` = a.`year` 
                    and a.`year` = %s
                    and t.ID = a.teamID 
                    and s.playerID = a.playerID 
                    GROUP by t.teamCode
"""

        cursor.execute(query,(anno,))

        for row in cursor:
            result.append(Squadra(**row))

        cursor.close()
        conn.close()
        return result