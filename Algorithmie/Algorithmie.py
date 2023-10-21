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