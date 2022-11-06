import pygame, os, time
from Controller.settings import *
from Systems.System import HandleInput, MouseCollisionSystem, Render, State, TextDrawSystem, Update
from Entities.Screens.Title import Title

class World:
    def __init__(self) -> None:
        self.systems = []
        self.components = {}
        self.entities = {}
        self.next_entity_id = 0
        # Temp var
        self.index = 0       

        # Display
        pygame.init()
        pygame.display.set_caption('ECS')
        # self.font = pygame.font.Font(None, 30)
        self.GAME_W, self.GAME_H = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.game_canvas = pygame.Surface((self.GAME_W, self.GAME_H))
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT), 0, 64)

        # Timing
        self.clock = pygame.time.Clock()
        self.dt, self.prev_time = (0, 0)

        # Network
        # self.serverEndpoint = SOCKET_SERVER_PORT
        # self.network = Network()

        # Input
        # self.controller = TypingKeyboard()
        self.click = False

        # Game State
        self.state_stack = []
        self.running, self.playing = (True, True)

        # Asset Loading
        self.load_assets()
        self.load_initial_state()  

        # Controller Systems
        self.addSystem(TextDrawSystem(self))    

    def load_assets(self):
        # pointers
        self.assets_dir = os.path.join('Graphics')
        self.sprite_dir = os.path.join('Graphics/Sprites/')
        self.cards_dir = os.path.join('Graphics/Cards/')
        self.bg_dir = os.path.join('Graphics/BG/')
        self.misc = os.path.join('Graphics/Misc/')
        self.font_dir = os.path.join('Graphics/Font/')
        self.font = pygame.font.Font(
            os.path.join(self.font_dir, "Morpheus.ttf"), 30)

    def load_initial_state(self):   
        self.title_screen = Title(world=self)
        self.state_stack.append(self.title_screen)               

    # Entities
    def addEntity(self, entity):
        self.entities.update(entity)
        self.next_entity_id += 1

    def removeEntity(self):
        pass

    def getEntity(self):
        pass

    def getEntities(self):
        pass

    # Systems
    def addSystem(self, system):
        self.systems.append(system)

    def removeSystem(self):
        pass

    def getSystem(self):
        pass

    def getSystems(self):
        pass

    def runSystems(self):
        pass

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing, self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass
                if event.key == pygame.K_BACKSPACE:
                    pass
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()                    
                           
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True                        
    
    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now              

    def gameLoop(self):
        while self.playing:
           self.get_dt()
           self.get_events()           
           HandleInput(world=self).execute()
           MouseCollisionSystem(world=self).execute()
           Update(world=self).execute(self.dt)                   
           Render(world=self).execute() 
        self.click = not self.click  