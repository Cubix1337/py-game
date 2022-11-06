from Systems.System import System
import pygame
import math
import json

class SpriteLoadingSystem(System):
    def __init__(self, world) -> None:
        super().__init__(world)

    def execute(self, sprite):
        jsonData = sprite.getComponentValue('Filename').replace('png', 'json')
        try:
            with open(jsonData) as file:
                sprite.updateComponent('Data', json.load(file))
            file.close()
        except:
            print('Failed to load sprite')
            return False
        finally:
            sprite.updateComponent(
                'Animations', sprite.getComponentValue('Data')['animations'])
            SpriteUpdatingSystem(self.world).execute(sprite)


class SpriteFrameGeneration(System):
    def __init__(self, world) -> None:
        super().__init__(world)

    def execute(self, sprite, frame):
        (x, y, w, h) = frame["x"], frame["y"], frame["w"], frame["h"]
        frame = pygame.Surface((w, h))        
        color_key = sprite.getComponentValue('Data')['color_key']
        frame.set_colorkey((color_key))
        # pygame.transform.flip(frame, True, False)                         
        frame.blit(pygame.image.load(sprite.getComponentValue('Image')).convert(), (0, 0), (x, y, w, h))
        return frame
        # Inverted for facing
        # return pygame.transform.flip(frame, True, False) 

class SpriteUpdatingSystem(System):
    def __init__(self, world) -> None:
        super().__init__(world)

    def setFrames(self, sprite):
        frames = []
        sprite.updateComponent("FrameRate", sprite.getComponentValue('Animations')[
                               sprite.getComponentValue('AnimationState')]["frameRate"])

        for frame in range(len(sprite.getComponentValue('Animations')[sprite.getComponentValue('AnimationState')]["frames"])):            
            frames.append(
                SpriteFrameGeneration(self.world).execute(sprite, sprite.getComponentValue(
                    'Animations')[sprite.getComponentValue('AnimationState')]["frames"][frame]['frame'])
            )        
        sprite.updateComponent("Frames", frames)

    def execute(self, sprite):
        self.setFrames(sprite)

class UpdateActiveFrameSystem(System):
    def __init__(self, world) -> None:
        super().__init__(world)

    def resetAnimation(self, sprite):
        sprite.updateComponent('ActiveFrame', 0)

    def execute(self, sprite):        
        if math.floor(sprite.getComponentValue('ActiveFrame') + sprite.getComponentValue('FrameRate')) >= len(sprite.getComponentValue('Frames')):
            if sprite.getComponentValue('Animations')[sprite.getComponentValue('AnimationState')]["runs"] == "once":
                self.resetAnimation(sprite)
                SpriteAnimationChangeSystem(self.world).execute(sprite, 'idle')
            else:
                self.resetAnimation(sprite)                            
        else:
            sprite.updateComponent('ActiveFrame', sprite.getComponentValue(
                'ActiveFrame') + sprite.getComponentValue('FrameRate'))    

class SpriteAnimationChangeSystem(System):
    def __init__(self, world) -> None:
        super().__init__(world)
       
    def execute(self, sprite, state):
        sprite.updateComponent('AnimationState', state) 
        SpriteUpdatingSystem(self.world).execute(sprite)        


class SpriteRenderSystem(System):
    def __init__(self, world) -> None:
        super().__init__(world)
   
    def getActiveFrame(self, sprite):        
        return sprite.getComponentValue('Frames')[math.floor(sprite.getComponentValue('ActiveFrame'))]

    def execute(self, sprite, position):
        self.world.game_canvas.blit(self.getActiveFrame(sprite), position)       
        
        # class SpriteLoadingSystem(System):
        #     def __init__(self, world) -> None:
        #         super().__init__(world)

        #     def generateFrame(self, frame):
        #         (x, y, w, h) = frame["x"], frame["y"], frame["w"], frame["h"]
        #         frame = pygame.Surface((w, h))
        #         frame.set_colorkey((0, 0, 1,))
        #         frame.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        #         return frame

        #     def setFrames(self):
        #         self.frames = []
        #         self.frameRate = self.getComponentValue('Animations')[self.getComponentValue('AnimationState')]["frameRate"]

        #         for frame in range(len(self.getComponentValue('Animations')[self.getComponentValue('AnimationState')]["frames"])):
        #             self.frames.append(
        #                 self.generateFrame(self.getComponentValue('Animations')[self.getComponentValue('AnimationState')]["frames"][frame]['frame'])
        #             )

        #     def load(self, sprite):
        #         print(sprite.logComponents())
        #         location = sprite.getComponentValue('Filename').replace('png','json')

        #         try:
        #             with open(location) as file:
        #                 sprite.updateComponent('Data', json.load(file))
        #             file.close()

        #         except:
        #             print('Failed to load sprite')
        #             return False

        #         sprite.updateComponent('Animations',sprite.getComponentValue('Data')['animations'])
        #         # self.setFrames()

        #     def execute(self, sprite):
        #         self.load(sprite)
        #         sprite.logComponents()

        # class SpriteRenderSystem(System):
        #     def __init__(self, world) -> None:
        #         super().__init__(world)

        #     def generateFrame(self, frame):
        #         (x, y, w, h) = frame["x"], frame["y"], frame["w"], frame["h"]
        #         frame = pygame.Surface((w, h))
        #         frame.set_colorkey((0, 0, 1,))
        #         frame.blit(self.getComponentValue('data'), (0, 0), (x, y, w, h))
        #         return frame

        #     def setFrames(self):
        #         self.frames = []
        #         self.frameRate = self.getComponentValue('Animations')[self.getComponentValue('AnimationState')]["frameRate"]

        #         for frame in range(len(self.getComponentValue('Animations')[self.getComponentValue('AnimationState')]["frames"])):
        #             self.frames.append(
        #                 self.generateFrame(self.getComponentValue('Animations')[self.getComponentValue('AnimationState')]["frames"][frame]['frame'])
        #             )

        #     def updateActiveFrame(self):
        #         if self.getComponentValue('ActiveFrame') >= len(self.frames) - 1:
        #             if self.getComponentValue('Animations')[self.getComponentValue('AnimationState')]["runs"] == "once":
        #                 pass
        #             else:
        #                 self.updateComponent('ActiveFrame', 0)
        #         else:
        #             updatedFrame = self.getComponentValue('ActiveFrame') + self.getComponentValue('Animations')[self.getComponentValue('AnimationState')]["frameRate"]
        #             self.updateComponent('ActiveFrame', updatedFrame)

        #     def resetAnimation(self):
        #         self.updateComponent('ActiveFrame', 0)

        #     def setAnimationState(self, state):
        #         self.updateComponent('AnimationState', state)
        #         self.setFrames()

        #     def getActiveFrame(self):
        #         return self.frames[math.floor(self.activeFrame)]

        # def execute(self, entities):
        #     #  print(entities)
        #     for entity in entities:
        #          if(entity.hasComponent('Animations')):
        #             print(entity.getComponentValue('AnimationState'))

        # class SpriteRenderSystem(System):
        # def __init__(self, world, filename) -> None:
        #     super().__init__(world)
        #     self.filename = filename
        #     self.sprite_sheet = pygame.image.load(self.filename).convert()
        #     self.activeFrame = 0
        #     self.animationState = 'idle'
        #     self.data = [],
        #     self.animations = []
        #     self.frames = []
        #     self.load()

        # def generateFrame(self, frame):
        #     (x, y, w, h) = frame["x"], frame["y"], frame["w"], frame["h"]
        #     frame = pygame.Surface((w, h))
        #     frame.set_colorkey((0, 0, 1,))
        #     frame.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        #     return frame

        # def setFrames(self):
        #     self.frames = []
        #     self.frameRate = self.animations[self.animationState]["frameRate"]

        #     for frame in range(len(self.animations[self.animationState]["frames"])):
        #         self.frames.append(
        #             self.generateFrame(self.animations[self.animationState]["frames"][frame]['frame'])
        #         )

        # def updateActiveFrame(self):
        #     if self.activeFrame >= len(self.frames) - 1:
        #         if self.animations[self.animationState]["runs"] == "once":
        #             pass
        #         else:
        #             self.activeFrame = 0
        #     else:
        #         self.activeFrame += self.frameRate

        # def resetAnimation(self):
        #     self.activeFrame = 0

        # def setAnimationState(self, state):
        #     self.animationState = state
        #     self.setFrames()

        # def getActiveFrame(self):
        #     return self.frames[math.floor(self.activeFrame)]

        # def execute(self):
        #     self.world.game_canvas.blit(self.getActiveFrame(),(75, 100))
        #     pass
