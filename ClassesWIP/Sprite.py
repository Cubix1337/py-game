import pygame, json

class Frames:
    def __init__(self) -> None:
        self.value = []

class Sprite:
    def __init__(self, filename) -> None:
        self.filename = filename
        self.sprite_sheet = pygame.image.load(self.filename).convert()
        self.meta_data = self.filename.replace('png','json')

        try:
            with open(self.meta_data) as file:
                self.data = json.load(file)
            file.close()
        except:
            pass

    def load(self):
        self.sprite_sheet = pygame.image.load(self.filename).convert()

    def getSprite(self, x, y, w, h):        
        sprite = pygame.Surface((w, h))
        sprite.set_colorkey((0, 0, 0,))
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))        
        return sprite
    
    def parseSprite(self, frame):
        sprite = self.data['frames'][frame]["frame"]
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.getSprite(x, y, w, h)
        return image


    # def render(self):
    #     pass
        # sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))

# 82 x 78
# 0, 0, 41, 39
# 41, 0, 41, 39 
# 0, 39, 41, 39 
# 41, 39, 41, 39 