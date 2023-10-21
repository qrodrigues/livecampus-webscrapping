from datetime import datetime

class Algorithmie:
    def __init__(self) -> None:
        pass

    def countDiffusionByKey(self, episodes, key):
        channel_count = {}
        
        for episode in episodes:
            channel = episode.get(key)
            if channel in channel_count:
                channel_count[channel] += 1
            else:
                channel_count[channel] = 1

        return channel_count
    
    def getTop3(self, channel_count, quantity):
        # Trier le dictionnaire en fonction du nombre d'occurrences des chaînes
        sorted_channels = sorted(channel_count.items(), key=lambda x: x[1], reverse=True)

        # Obtenir les trois chaînes les plus utilisées
        top_channels = sorted_channels[:quantity]

        return top_channels
    
    def getTopSeriesWords(self, episodes, quantity):
        series_name_words = {}
        
        for episode in episodes:
            series_name = episode.get('series_name')
            words = series_name.split()  # Diviser le nom de la série en mots

            for word in words:
                if word in series_name_words:
                    series_name_words[word] += 1
                else:
                    series_name_words[word] = 1

        # Trier le dictionnaire en fonction du nombre d'occurrences des mots
        sorted_words = sorted(series_name_words.items(), key=lambda x: x[1], reverse=True)

        # Obtenir les dix mots les plus présents
        top_words = sorted_words[:quantity]

        return top_words
    
    def findLongestConsecutiveDays(self, episodes):
        max_consecutive_days = 0
        current_consecutive_days = 0
        current_channel = None
        previous_date = None
        result = None

        for episode in episodes:
            air_date = episode.get('air_date')
            channel = episode.get('channel')

            if previous_date is not None:
                current_date = datetime.strptime(air_date, '%d-%m-%Y')

                if (current_date - previous_date).days == 1 and current_channel == channel:
                    current_consecutive_days += 1
                else:
                    current_consecutive_days = 1

                if current_consecutive_days > max_consecutive_days:
                    max_consecutive_days = current_consecutive_days
                    result = (current_channel, max_consecutive_days)

            current_channel = channel
            previous_date = datetime.strptime(air_date, '%d-%m-%Y')

        return result