import sqlite3

conn_lite = sqlite3.connect("data/databases/database.db")
class SQLiteManager:
    def __init__(self, episodes):
        self.episodes = episodes

    def create_episode_table(self):
        cur = conn_lite.cursor()
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
            conn_lite.commit()

        except sqlite3.Error as e:
            print("Erreur lors de la création de la table episode ", e)

        finally:
            # Fermer le curseur uniquement
            if conn_lite:
                cur.close()

    def drop_tables(self):
        cur = conn_lite.cursor()
        try :
            cur.execute('''
                DROP TABLE duration
            ''')
            cur.execute('''
                DROP TABLE episode
            ''')
            conn_lite.commit()

        except sqlite3.Error as e:
            print("Erreur lors de la suppression des tables ", e)

        finally:
            if conn_lite:
                cur.close()

    def create_duration_table(self):
        cur = conn_lite.cursor()
        try :
            cur.execute('''
                CREATE TABLE IF NOT EXISTS duration (
                    id serial PRIMARY KEY,
                    duration INT NOT NULL,
                    episode_id INT NOT NULL, FOREIGN KEY(episode_id) REFERENCES episode(id)
        )''')
            conn_lite.commit()

        except sqlite3.Error as e:
            print("Erreur lors de la creation de la table duration ", e)

        finally:
            # Fermer le curseur uniquement
            if conn_lite:
                cur.close()

    def table_exists(self, table_name):
        cursor = conn_lite.cursor()
        try :
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
            return cursor.fetchone() is not None
        
        except sqlite3.Error as e:
            print(f"Erreur lors de la recherche de la table {table_name} {e}")

        finally:
            if conn_lite:
                cursor.close()

    def save_to_postgres(self, episodes):
        cur = conn_lite.cursor()
        tb_duration = "duration"
        tb_episode = "episode"
        if not self.table_exists(tb_episode):
            self.create_episode_table()
            print("Table episode créée avec succès")
        if not self.table_exists(tb_duration):
            self.create_duration_table()
            print("Table duration créée avec succès")

        print('Sauvegarde des données...')
        try :
            for episode in episodes :
                try:
                    cur.execute("INSERT INTO episode (air_date, origin_country, channel, series_name, episode_number, season_number, episode_url) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                                (episode["air_date"], episode["origin_country"], episode["channel"], episode["series_name"], episode["episode_number"], episode["season_number"], episode["episode_url"]))
                    episode_id = cur.lastrowid
                    if episode_id is not None:
                        if episode["duration"] is not None:
                            cur.execute("INSERT INTO duration (duration, episode_id) VALUES (?, ?)", (episode["duration"], episode_id)) 
                    conn_lite.commit()

                except sqlite3.Error as e:
                    conn_lite.rollback()
                    print("Erreur lors de l'insertion avec le champ duration :", e)

        finally:
            # Fermer le curseur et la connexion
            if conn_lite:
                cur.close()
                conn_lite.close()
                print("Connexion fermée.")
