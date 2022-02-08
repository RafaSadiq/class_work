print('\n')
print('How to Build a Custom Iterator Class in Python')
print('\n')

class Lineup:
    def __init__ (self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1)
        
    def __iter__(self):
        self.n = 0
        return self
    
    def get_player(self, n):
        return self.players[n]
    
    def __next__(self):
        if self.n < self.last_player_index:
            player = self.get_player(self.n)
            self.n += 1
            return player
        
        elif self.n == self.last_player_index:
            players = self.get_players(self.n)
            self.n += 0
            return players
        
        
astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))