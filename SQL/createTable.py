DATABASE_URL= "postgres://livecampus__5939:JfiEu3Ss_4at2Iz3u9be@livecampus--5939.postgresql.a.osc-fr1.scalingo-dbs.com:33846/livecampus__5939?sslmode=prefer"

import psycopg2
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
try : 
    # Définition du schéma de la table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS episode (
            id serial PRIMARY KEY,
            series_name VARCHAR(255) NOT NULL,
            episode_number INT NOT NULL,
            season_number INT NOT NULL,
            air_date DATE,
            origin_country VARCHAR(50),
            channel VARCHAR(100),
            episode_url VARCHAR(255)
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


