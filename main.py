from Controller.Controller import World

if __name__ == '__main__':
    game = World()        
    
    while game.running:
        game.gameLoop()