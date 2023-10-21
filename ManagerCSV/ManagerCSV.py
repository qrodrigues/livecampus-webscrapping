import pandas as pd
import csv


class ManagerCSV() : 
    def __init__(self,episodes) :
        self.episodes = episodes

    def data_to_df(self) : 
        data_to_df = {
            "series_name" : [],
            "episode_number" : [],
            "season_number" : [],
            "air_date" : [],
            "origin_country" : [],
            "channel" : [],
            "episode_url" : [],
            "duration":[]
        }
        try : 
            for episode in self.episodes :
                data_to_df.get("series_name").append(episode.get("series_name"))
                data_to_df.get("episode_number").append(episode.get("episode_number"))
                data_to_df.get("season_number").append(episode.get("season_number"))
                data_to_df.get("air_date").append(episode.get("air_date"))
                data_to_df.get("origin_country").append(episode.get("origin_country"))
                data_to_df.get("channel").append(episode.get("channel"))
                data_to_df.get("episode_url").append(episode.get("episode_url"))
                data_to_df.get("duration").append(episode.get("duration"))
                print(data_to_df)
                return data_to_df
        except : 
            print("Erreur lors de la création du dataframe !")
            return None
        


    def df_to_csv(self,datas,path_file) :
        try :
            df = pd.DataFrame(datas)
            df.to_csv(path_file,sep=';')
            print("Fichier csv créé avec succès ! : ",path_file)
            return path_file
        except :
            print("Erreur lors de la création du fichier csv")
            return False

    def csv_to_tuples(self,fichier_csv) :
        tuples = []
        try : 
            with open(fichier_csv, 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                next(csv_reader) # Enleve la premiere ligne
                for row in csv_reader:
                    index = int(row[0])
                    titre = str(row[1])
                    saison = int(row[2])
                    episode = int(row[3])
                    date_diffusion = str(row[4])
                    pays = str(row[5])
                    chaine = str(row[6])
                    lien = str(row[7])
                    duration = int(row[8])

                    tup = (index, titre, saison, episode, date_diffusion, pays, chaine, lien)
                    tuples.append(tup)
        except:
            print("Erreur lors de la lecture du fichier csv !", )
            return False
        return tuples

    
    def verify_types(self,tuples) : 
        types_tuples = []
        for tup in tuples :
            enum = {
                "int" : "integer",
                "str" : "string",
            }
            # print(type(tup[8]).__name__)
            # types = (
            #     enum.get(type(tup[0]).__name__),
            #     enum.get(type(tup[1]).__name__),
            #     enum.get(type(tup[2]).__name__),
            #     enum.get(type(tup[3]).__name__),
            #     enum.get(type(tup[4]).__name__),
            #     enum.get(type(tup[5]).__name__),
            #     enum.get(type(tup[6]).__name__),
            #     enum.get(type(tup[7]).__name__),
            #     enum.get(type(tup[8]).__name__),
            #     )

            # types_tuples.append(types)
        return types_tuples #Retourne une liste de tuples contenant les types des colonnes