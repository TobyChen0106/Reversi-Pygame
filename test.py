from Reversi import Reversi
game = Reversi(size=800, gameName='Toby\'s Game')

while True:
    if(not game.update()):
        break
