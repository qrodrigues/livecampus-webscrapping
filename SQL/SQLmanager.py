import psycopg2

DATABASE_URL= "postgres://livecampus__5939:JfiEu3Ss_4at2Iz3u9be@livecampus--5939.postgresql.a.osc-fr1.scalingo-dbs.com:33846/livecampus__5939?sslmode=prefer"
DB_URL_PAUL = "postgres://course_pyth_8214:WCCU-NNiG777z2cwDPIp@course-pyth-8214.postgresql.a.osc-fr1.scalingo-dbs.com:33810/course_pyth_8214?sslmode=prefer"
conn = psycopg2.connect(DATABASE_URL)

class SQLManager:
    def __init__(self, episodes):
        self.episodes = episodes

    def create_postgre_table():
        cur = conn.cursor()
        try : 
            # Définition du schéma de la table
            cur.execute('''
                CREATE TABLE IF NOT EXISTS episode (
                    id serial PRIMARY KEY,
                    air_date DATE,
                    origin_country VARCHAR(50),
                    channel VARCHAR(100),
                    series_name VARCHAR(255) NOT NULL,
                    episode_number INT NOT NULL,
                    season_number INT NOT NULL,
                    episode_url VARCHAR(255),
        )
            ''')
            conn.commit()

        except psycopg2.Error as e:
            print(e)

        finally:
            # Fermer le curseur et la connexion
            if conn:
                cur.close()
                conn.close()
                print("Connexion fermée.")

    def save_to_postgre(episodes):
        cur = conn.cursor()
        table = "duration"
        if not SQLManager.table_exists(table, conn):
            SQLManager.create_duration_table()
        try :
            for episode in episodes :
                if(episode["duration"] is not None):
                    try:
                        cur.execute("INSERT INTO episode (air_date, origin_country, channel, series_name, episode_number, season_number, episode_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id", 
                                    (episode["air_date"], episode["origin_country"], episode["channel"], episode["series_name"], episode["episode_number"], episode["season_number"], episode["episode_url"]))
                        episode_id = cur.fetchone()[0]

                        cur.execute("INSERT INTO duration (episode_id, duration) VALUES (%s, %s)", (episode_id, episode["duration"]))

                    except psycopg2.Error as e:
                        conn.rollback()
                        print("Erreur lors de l'insertion :", e)
                else:
                    cur.execute("INSERT INTO episode (air_date, origin_country, channel, series_name, episode_number, season_number, episode_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                                (episode["air_date"], episode["origin_country"], episode["channel"], episode["series_name"], episode["episode_number"], episode["season_number"], episode["episode_url"]))
            conn.commit()

        except psycopg2.Error as e:
            print("Erreur lors de l'insertion :", e)

        finally:
            # Fermer le curseur et la connexion
            if conn:
                cur.close()
                conn.close()
                print("Connexion fermée.")

    def table_exists(table_name, conn):
        cursor = conn.cursor()
        cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s);", (table_name,))
        exists = cursor.fetchone()[0]
        cursor.close()
        return exists

    def create_duration_table(self):
        cur = conn.cursor()
        try :
            cur.execute('''
                CREATE TABLE IF NOT EXISTS duration (
                    id serial PRIMARY KEY,
                    episode_id FOREIGN KEY,
                    duration INT NOT NULL,
                    CONSTRAINT fk_episode FOREIGN KEY(episode_id) REFERENCES episode(id)
        )
            ''')
            conn.commit()

        except psycopg2.Error as e:
            print(e)

        finally:
            # Fermer le curseur et la connexion
            if conn:
                cur.close()
                conn.close()
                print("Connexion fermée.")

