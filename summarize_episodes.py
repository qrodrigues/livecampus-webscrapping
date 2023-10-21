import argparse
from webscrapper import ScrapEpisodes
from Algorithmie.Algorithmie import Algorithmie

algorithmie = Algorithmie()

def main():
    parser = argparse.ArgumentParser(description='Summarize episodes by month')
    parser.add_argument('--month', type=int, help='Month to summarize', required=True)
    args = parser.parse_args()

    month = args.month
    if 12 >= month > 0:
        scrapData(month)
    else:
        raise ValueError("Le mois doit être compris entre 1 et 12 compris.")

def scrapData(month):
    base_url = "https://www.spin-off.fr"

    str_month = str(month)
    if len(str_month) <= 1:
        str_month = "0" + str_month

    url = "/calendrier_des_series.html" + "?date=2023-" + str_month

    scrapper = ScrapEpisodes(base_url, url)
    episodes = scrapper.getAllEpisodes()
    
    # Nombre d'épisode du mois
    month_name = getMonthByNumber(str_month)
    print(f"{len(episodes)} seront diffusés pendant le mois de {month_name}.")

    # TOP pays diffusion épisode
    diffusions_countries_counter = algorithmie.countDiffusionByKey(episodes, "origin_country")
    top_country = algorithmie.getTop3(diffusions_countries_counter, 1)[0]
    print(f"C'est {top_country[0]} qui diffusera le plus d'épisodes avec {top_country[1]} épisodes.")

    # TOP Chaine diffusion épisode
    diffusions_channels_counter = algorithmie.countDiffusionByKey(episodes, "channel")
    top_channel = algorithmie.getTop3(diffusions_channels_counter, 1)[0]
    print(f"C'est {top_channel[0]} qui diffusera le plus d'épisodes avec {top_channel[1]} épisodes.")

    # TOP Nombre de jour consecutif
    chaine_consecutive = algorithmie.findLongestConsecutiveDays(episodes)
    print(f"C'est {chaine_consecutive[0]} qui diffusera des épisodes pendant le plus grand nombre \
de jours consécutifs avec {chaine_consecutive[1]} de jours consécutifs.")

def getMonthByNumber(numero_mois):
    mois = [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
        "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"
    ]

    try:
        numero = int(numero_mois)
        if 1 <= numero <= 12:
            return mois[numero - 1]
        else:
            return "Mois invalide"
    except ValueError:
        return "Mois invalide"

if __name__ == '__main__': # vérifie si le script n'est pas importé
    main()