import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_summoner(conn, project):
    

    sql = ''' INSERT INTO summoner(
                                _game,
                                _id,
                                accountId,
                                puuid,
                                name,
                                profileIconId,
                                summonerLevel
                            )
                            VALUES (
                                '1',
                                '1',
                                '1',
                                '1',
                                '1',
                                '1',
                                '1'
                                
                            ); '''

    print(sql)
    cur = conn.cursor()
    print(cur)
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid
    
def create_game(conn, task):
    sql = ''' INSERT INTO league_game(platform_id,riot_game_id,queue,season,timestamp,game_duration,map,match)
          VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

    return cur.lastrowid

def main():
        
    # create a database connection
    database = r"C:\Users\Johnny786\github\django_blog\db.sqlite3"
    conn = create_connection(database)
    with conn:

        project = ('Cool',)
        project_id = create_summoner(conn, project)

        # tasks
        task_1 = ('Anal', 1, 1, 1, '3', '4')
        #task_2 = ('Confirm with user', 1, 1, 4, '5', '6')

        # create tasks
        create_game(conn, task_1)
        #self.create_task(conn, task_2)

if __name__ == '__main__':
    main()