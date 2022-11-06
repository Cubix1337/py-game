import pygame

class Component:
    def __init__(self) -> None:
        pass
    
    def log(self):
        print(self.value)
    
    def getValue(self):
        return self.value
    
    def setValue(self, newValue):
         self.value = newValue
        
class Position(Component):
    def __init__(self, x= 0 , y = 0) -> None:
        super().__init__()
        self.value = (x, y)        

class Colour(Component):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = colourDict[value]

class Background(Colour):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.value = colourDict[value]

class Dimensions(Component):
    def __init__(self, width=0, height=0) -> None:
        super().__init__()
        self.value = (width, height)        

class Text(Component):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

class Alignment(Component):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value        

class Font(Component):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

class Rect(Component):
    def __init__(self, pos=(0,0), dimensions=(0,0)) -> None:
        super().__init__()
        self.value = pygame.Rect(pos, dimensions)  

class Surface(Component):
    def __init__(self, dimensions = (0,0)) -> None:
        super().__init__()   
        self.value = dimensions 

class Intersecting(Component):
    def __init__(self, value = False) -> None:
        super().__init__()
        self.value = value

class Filename(Component):
    def __init__(self, value) -> None:
        super().__init__()
        self.value = value

class AnimationState(Component):
    def __init__(self, value = 'idle') -> None:
        super().__init__()
        self.value = value

class Animations(Component):
    def __init__(self, value = {}) -> None:
        super().__init__()
        self.value = value

class Image(Component):
    def __init__(self, value = {}) -> None:
        super().__init__()
        self.value = value

class ActiveFrame(Component):
    def __init__(self, value = 0) -> None:
        super().__init__()
        self.value = value

class Data(Component):
    def __init__(self, value = {}) -> None:
        super().__init__()
        self.value = value

class Frames(Component):
    def __init__(self, value = []) -> None:
            super().__init__()
            self.value = value

class FrameRate(Component):
    def __init__(self, value = 0.01) -> None:
            super().__init__()
            self.value = value    

componentDict = {
    "Position":Position,
    "Rect":Rect,
    "Colour": Colour,
    "Background": Background,
    "Dimensions": Dimensions,
    "Text": Text,
    "Font": Font,
    "Intersecting": Intersecting,
    "Surface": Surface,
    "Filename":Filename,
    "Animations": Animations,
    "AnimationState": AnimationState,
    "Image": Image,
    "ActiveFrame": ActiveFrame,
    "Data": Data,
    "Frames" : Frames,
    "FrameRate": FrameRate   
}

colourDict = {
    "white": (255,255,255),
    "black": (0,0,0),
    "red": (255,0,0),
    "green": (0,255,0),
    "blue": (0,0,255)
}

# class Button: 
#     def __init__(self, text, font, textColour, background, width, height, pos ):
#         self.text = text
#         self.font = font
#         self.textColour = textColour
#         self.background = background
#         self.width = width
#         self.height = height
#         self.pos = pos       
#         self.top_rect = pygame.Rect(pos, (width, height))   
#         self.pressed = False     

#     def draw(self, screen):
#         pygame.draw.rect(screen, self.background, self.top_rect)
#         draw_text(self.text, self.font, self.textColour, screen, self.top_rect.center, 'center' )
#         self.checkClick()
    
#     def checkClick(self):        
#         leftMouseButton = pygame.mouse.get_pressed()[0]
#         middleMouseButton = pygame.mouse.get_pressed()[1]
#         rightMouseButton = pygame.mouse.get_pressed()[2]
#         # print((leftMouseButton,middleMouseButton,rightMouseButton))
#         mousePos = pygame.mouse.get_pos()
        
#         if(self.top_rect.collidepoint(mousePos)): 
#             # print('intersecting')
#             self.background = (255,0,0)                       
#             if(leftMouseButton):                         
#                 self.pressed = True
#             else:
#                 if self.pressed == True:
#                     print('click')
#                     self.pressed = False                                                              
#         else:
#             self.background = '#475F77' 
