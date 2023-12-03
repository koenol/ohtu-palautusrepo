class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self._get_equal_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self._get_win_or_advantage()
        else:
            return self._get_current_score()

    
    def _get_equal_score(self):
        if self.m_score1 == 0:
            return "Love-All"
        elif self.m_score1 == 1:
            return "Fifteen-All"
        elif self.m_score1 == 2:
            return "Thirty-All"
        else:
            return "Deuce"
        
    def _get_win_or_advantage(self):
        minus_result = self.m_score1 - self. m_score2

        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
    
    def _get_current_score(self):
        temp_player1 = self._get_player_score(self.m_score1)
        temp_player2 = self._get_player_score(self.m_score2)
        score = f"{temp_player1}-{temp_player2}"
        return score
    
    def _get_player_score(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"