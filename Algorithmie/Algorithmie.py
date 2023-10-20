class Algorithmie:
    def __init__(self) -> None:
        pass

    def getChaineDiffusion (self, episodes):
        channel_count = {}
    
        # Parcourir la liste d'épisodes et compter le nombre d'occurrences de chaque chaîne de télévision
        for episode in episodes:
            channel = episode[2]
            if channel in channel_count:
                channel_count[channel] += 1
            else:
                channel_count[channel] = 1

        # Trier le dictionnaire en fonction du nombre d'occurrences des chaînes
        sorted_channels = sorted(channel_count.items(), key=lambda x: x[1], reverse=True)

        # Obtenir les trois chaînes les plus utilisées
        top_channels = sorted_channels[:3]

        return [channel[0] for channel in top_channels]