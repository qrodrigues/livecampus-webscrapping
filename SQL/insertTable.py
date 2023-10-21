DATABASE_URL= "postgres://livecampus__5939:JfiEu3Ss_4at2Iz3u9be@livecampus--5939.postgresql.a.osc-fr1.scalingo-dbs.com:33846/livecampus__5939?sslmode=prefer"

import psycopg2
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
try : 
    cur.executemany("INSERT INTO lotr_carac (birth, death, gender, hair, height, name, race, realm, spouse, wikiUrl) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", caracs_to_insert)
    conn.commit()

except psycopg2.Error as e:
    print(e)

finally:
    # Fermer le curseur et la connexion
    if conn:
        cur.close()
        conn.close()
        print("Connexion fermée.")