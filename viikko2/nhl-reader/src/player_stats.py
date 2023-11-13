class PlayerStats:
    def __init__(self, player_reader):
        self.players = player_reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = []
        for player in self.players:
            if player.nationality == nationality:
                players_by_nationality.append(player)

        sort_players = sorted(players_by_nationality, key=lambda x: x.goals + x.assists, reverse=True)
        return sort_players
