import sqlite3
from sqlite3 import Error

class Database(object):
    def __init__(self):
        self.database = r"C:\Users\Johnny786\github\django_blog\db.sqlite3"
    
    def hello(self):
        return None

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    def create_participant(conn, project):

        sql = ''' INSERT INTO league_participant (
                                   id,
                                   summonerName,
                                   accountId,
                                   summonerId,
                                   profileIcon,
                                   participantId,
                                   teamId,
                                   championId,
                                   spell1Id,
                                   spell2Id,
                                   win,
                                   item0,
                                   item1,
                                   item2,
                                   item3,
                                   item4,
                                   item5,
                                   item6,
                                   kills,
                                   deaths,
                                   assists,
                                   totalDamageDealtToChampions,
                                   damageDealtToTurrets,
                                   visionScore,
                                   totalDamageTaken,
                                   visionWardsBoughtInGame
                               )
                               VALUES (
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                                   '?',
                               ); '''
        cur = conn.cursor()
        cur.execute(sql, project)
        conn.commit()
        return cur.lastrowid
    
    # def create_task(self, conn, task):
    #     sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
    #           VALUES(?,?,?,?,?,?) '''
    #     cur = conn.cursor()
    #     cur.execute(sql, task)
    #     conn.commit()

    #     return cur.lastrowid

def main(self):
        
        # create a database connection
        conn = self.create_connection(self.database)
        #exit()
        with conn:

            project = ('Cool App with SQLite & Python',)
            project_id = self.create_project(conn, project)

            # tasks
            #task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
            #task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

            # create tasks
            #self.create_task(conn, task_1)
            #self.create_task(conn, task_2)

if __name__ == '__main__':
    main()