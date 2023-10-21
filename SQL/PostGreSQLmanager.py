import psycopg2

DATABASE_URL = "postgres://course_pyth_8214:WCCU-NNiG777z2cwDPIp@course-pyth-8214.postgresql.a.osc-fr1.scalingo-dbs.com:33810/course_pyth_8214?sslmode=prefer"
conn = psycopg2.connect(DATABASE_URL)

class PostGreSQLManager:
    def __init__(self, episodes, connexion):
        self.episodes = episodes
        self.connexion = connexion

    def create_episode_table(self):
        cur = conn.cursor()
        try : 
            # Définition du schéma de la table
            cur.execute('''
                CREATE TABLE IF NOT EXISTS episode (
                    id serial PRIMARY KEY,
                    air_date VARCHAR(50),
                    origin_country VARCHAR(50),
                    channel VARCHAR(100),
                    series_name VARCHAR(255) NOT NULL,
                    episode_number INT NOT NULL,
                    season_number INT NOT NULL,
                    episode_url VARCHAR(255)
        )''')
            conn.commit()

        except psycopg2.Error as e:
            print("Erreur lors de la création de la table episode ", e)

        finally:
            # Fermer le curseur uniquement
            if conn:
                cur.close()

    def drop_tables(self):
        cur = conn.cursor()
        try :
            cur.execute('''
                DROP TABLE duration
            ''')
            cur.execute('''
                DROP TABLE episode
            ''')
            conn.commit()

        except psycopg2.Error as e:
            print("Erreur lors de la suppression des tables ", e)

        finally:
            if conn:
                cur.close()

    def create_duration_table(self):
        cur = conn.cursor()
        try :
            cur.execute('''
                CREATE TABLE IF NOT EXISTS duration (
                    id serial PRIMARY KEY,
                    duration INT NOT NULL,
                    episode_id INT NOT NULL, FOREIGN KEY(episode_id) REFERENCES episode(id)
        )
            ''')
            conn.commit()

        except psycopg2.Error as e:
            print("Erreur lors de la creation de la table duration ", e)

        finally:
            # Fermer le curseur uniquement
            if conn:
                cur.close()

    def table_exists(self, table_name):
        cursor = conn.cursor()
        try :
            cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s);", (table_name,))
            exists = cursor.fetchone()[0]
            return exists
        except psycopg2.Error as e:
            print(f"Erreur lors de la recherche de la table {table_name} {e}")

        finally:
            if conn:
                cursor.close()

    def save_to_postgres(self, episodes):
        cur = conn.cursor()
        tb_duration = "duration"
        tb_episode = "episode"
        if not self.table_exists(tb_episode):
            self.create_episode_table()
            print("Table episode créée avec succès")
        if not self.table_exists(tb_duration):
            self.create_duration_table()
            print("Table duration créée avec succès")

        try :
            for episode in episodes :
                try:
                    cur.execute("INSERT INTO episode (air_date, origin_country, channel, series_name, episode_number, season_number, episode_url) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id", 
                                (episode["air_date"], episode["origin_country"], episode["channel"], episode["series_name"], episode["episode_number"], episode["season_number"], episode["episode_url"]))
                    row = cur.fetchone()
                    if row is not None:
                        episode_id = row[0]
                        if episode["duration"] is not None:
                            cur.execute("INSERT INTO duration (duration, episode_id) VALUES (%s, %s)", (episode["duration"], episode_id))
                        conn.commit()

                except psycopg2.Error as e:
                    conn.rollback()
                    print("Erreur lors de l'insertion avec le champ duration :", e)

        except psycopg2.Error as e:
            print("Erreur lors de l'insertion :", e)

        finally:
            # Fermer le curseur et la connexion
            if conn:
                cur.close()
                conn.close()
                print("Connexion fermée.")
