from Systems.System import System
import pygame, math, json

class SpriteFrameGeneration(System):
    def __init__(self) -> None:
        super().__init__() 
    
    def execute(self, sprite):
        frame = sprite.getComponentValue("Frames")         
        (x, y, w, h) = frame["x"], frame["y"], frame["w"], frame["h"]
        frame = pygame.Surface((w, h))
        frame.set_colorkey((0, 0, 1,))
        frame.blit(self.sprite_sheet, (0, 0), (x, y, w, h)) 
        return frame


class SpriteUpdatingSystem(System):
    def __init__(self) -> None:
        super().__init__()

    def setFrames(self, sprite):        
        frames = []
        sprite.updateComponent("frameRate", sprite.animations[sprite.animationState]["frameRate"])        

        for frame in range(len(sprite.animations[sprite.animationState]["frames"])):                    
            self.frames.append(                
                SpriteFrameGeneration().execute(sprite.animations[sprite.animationState]["frames"][frame]['frame'])
                # self.generateFrame(sprite.animations[sprite.animationState]["frames"][frame]['frame'])
            )
        sprite.updateComponent("Frames", frames)        
    
    def execute(self, sprite):
        self.setFrames(sprite)

class SpriteLoadingSystem(System):
    def __init__(self, world) -> None:
        super().__init__(world)              

    def generateFrame(self, frame):        
        (x, y, w, h) = frame["x"], frame["y"], frame["w"], frame["h"]
        frame = pygame.Surface((w, h))
        frame.set_colorkey((0, 0, 1,))
        frame.blit(self.sprite_sheet, (0, 0), (x, y, w, h)) 
        return frame
    
    def setFrames(self):
        self.frames = []
        self.frameRate = self.animations[self.animationState]["frameRate"]

        for frame in range(len(self.animations[self.animationState]["frames"])):                    
            self.frames.append(
                self.generateFrame(self.animations[self.animationState]["frames"][frame]['frame'])
            )

    def load(self, sprite): 
        print(sprite.logComponents())
        location = sprite.getComponentValue('Filename').replace('png','json') 
        
        try:
            with open(location) as file:     
                sprite.updateComponent('Data', json.load(file))                 
            file.close()                

        except:
            print('Failed to load sprite')
            return False
                       
        sprite.updateComponent('Animations',sprite.getComponentValue('Data')['animations'])                    
        # self.setFrames()   
    
    def execute(self, sprite):                      
        self.load(sprite) 
        sprite.logComponents()

        

class SpriteRenderSystem(System):
    def __init__(self, world, filename) -> None:
        super().__init__(world)
        self.filename = filename
        self.sprite_sheet = pygame.image.load(self.filename).convert()
        self.activeFrame = 0
        self.animationState = 'idle'        
        self.data = [],        
        self.animations = []        
        self.frames = []      
        self.load()
   
    def generateFrame(self, frame):        
        (x, y, w, h) = frame["x"], frame["y"], frame["w"], frame["h"]
        frame = pygame.Surface((w, h))
        frame.set_colorkey((0, 0, 1,))
        frame.blit(self.sprite_sheet, (0, 0), (x, y, w, h)) 
        return frame
    
    def setFrames(self):
        self.frames = []
        self.frameRate = self.animations[self.animationState]["frameRate"]

        for frame in range(len(self.animations[self.animationState]["frames"])):                    
            self.frames.append(
                self.generateFrame(self.animations[self.animationState]["frames"][frame]['frame'])
            )

    def updateActiveFrame(self):                
        if self.activeFrame >= len(self.frames) - 1:
            if self.animations[self.animationState]["runs"] == "once":
                pass
            else:
                self.activeFrame = 0
        else:
            self.activeFrame += self.frameRate

    def resetAnimation(self):
        self.activeFrame = 0        

    def setAnimationState(self, state):
        self.animationState = state
        self.setFrames()
    
    def getActiveFrame(self):
        return self.frames[math.floor(self.activeFrame)]

    def execute(self):        
        self.world.game_canvas.blit(self.getActiveFrame(),(75, 100))        
        pass