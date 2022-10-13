import pygame, json, math

class Sprite:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.sprite_sheet = pygame.image.load(self.filename).convert()
        self.activeFrame = 0
        self.animationState = 'idle'        
        self.data = [],        
        self.animations = []        
        self.frames = []      
        self.load()
       
    def load(self):
        jsonData = self.filename.replace('png','json')       
        try:
            with open(jsonData) as file:
                self.data = json.load(file)
            file.close()
        except:
            print('Failed to load sprite')
            return False
        finally:
            self.animations = self.data['animations']
            self.setFrames()                    
    
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

    # def getSprite(self, x, y, w, h):        
    #     sprite = pygame.Surface((w, h))
    #     sprite.set_colorkey((0, 0, 0,))
    #     sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))        
    #     return sprite
    
    # def parseSprite(self, frame):
    #     sprite = self.data['frames'][frame]["frame"]
    #     x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
    #     image = self.getSprite(x, y, w, h)
    #     return image
    
    # def setFrames(self, animationState):
    #     for i in self.frameCount:
    #         self.frames.append(self.parseSprite(i))

    # def setAllFrames(self, animationState):
    #     for i in self.frameCount:
    #         self.frames.append(self.parseSprite(i))                    