import psycopg2
from webscrapper import ScrapEpisodes

DATABASE_URL= "postgres://livecampus__5939:JfiEu3Ss_4at2Iz3u9be@livecampus--5939.postgresql.a.osc-fr1.scalingo-dbs.com:33846/livecampus__5939?sslmode=prefer"

conn = psycopg2.connect(DATABASE_URL)

scrapper = ScrapEpisodes("https://www.spin-off.fr/calendrier_des_series.html")
episodes = scrapper.getAllEpisodes()
episodes.save_to_postgre()

def save_to_postgre(episodes):
    cur = conn.cursor()

    try : 
        cur.executemany("INSERT INTO episode (air_date, origin_country, channel, series_name, episode_number, season_number, episode_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", episodes)
        conn.commit()

    except psycopg2.Error as e:
        print(e)

    finally:
        # Fermer le curseur et la connexion
        if conn:
            cur.close()
            conn.close()
            print("Connexion fermée.")