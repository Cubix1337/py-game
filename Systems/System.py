from Components.Component import Background
from Controller.helpers import draw_text 
import pygame

class System:
    def __init__(self, world) -> None:
        self.world = world
        pass

class Render(System):
    def __init__(self, world) -> None:
        super().__init__(world)

    def execute(self):
        self.world.state_stack[-1].render()
        self.world.screen.blit(pygame.transform.scale(self.world.game_canvas,(self.world.SCREEN_WIDTH,self.world.SCREEN_HEIGHT)), (0,0))
        pygame.display.flip()     

class Update(System):
    def __init__(self, world) -> None:
        super().__init__(world)
    
    def execute(self, dt):               
        self.world.state_stack[-1].update(dt)         

class State(System):
    def __init__(self, world) -> None:
        super().__init__( world )                 
        self.prev_state = None         
    
    def update(self,delta_time, actions):
        pass

    def render(self, surface):
        pass

    def enter_state(self):
        if len(self.world.state_stack) > 1:
            self.prev_state = self.world.state_stack[-1]
        self.world.state_stack.append(self)
    
    def exit_state(self):
        self.world.state_stack.pop()

class HandleInput(System):
    def __init__(self, world) -> None:
        super().__init__(world)

    def execute(self):
        self.world.state_stack[-1].handleInput(self.world)  

class MouseCollisionSystem(System): 
    def __init__(self, world) -> None:
        super().__init__(world)   

    def execute(self):
        localEntities = self.world.state_stack[-1].localEntities
        # print(localEntities)
        
        for enitity in localEntities:
            mousePos = pygame.mouse.get_pos()
            # print(localEntities[enitity])
            if localEntities[enitity].hasComponent('Intersecting'):                
                rect = localEntities[enitity].getComponent('Rect').value
                if rect.collidepoint(mousePos):                
                    localEntities[enitity].updateComponent('Colour','red')
                else:
                    localEntities[enitity].updateComponent('Colour',(0,0,0))
                           


    # loop over entities if they have rects, if so trigger a colliding component mutation
    # def executeOLD(self, entity):
    #     mousePos = pygame.mouse.get_pos()     
    #     entityRect = entity.getComponent('Rect')   
        
    #     if(entityRect.collidepoint(mousePos)):
    #         entity.addComponent('Background') 
    #         entity['Background'].colour = (255,0, 255)
                      
            # if(leftMouseButton):                         
            #     self.pressed = True
            # else:
            #     if self.pressed == True:
            #         print('click')
            #         self.pressed = False                                                              
        # else:
        #     entity.removeComponent('Background')            

class TextDrawSystem(System):
    def __init__(self, world) -> None:
        super().__init__(world)
    
    def execute(self, entity):                   
        alignment = 'center'
        components = {}
       
        for item in entity.components:     
            components.update({item: entity.components[item].value})                   
        
        text = components['Text']
        font = components['Font']
        colour = components['Colour']
        pos = components['Position']
        screen = self.world.game_canvas
        
        
        text_obj = font.render(text, 1, colour)
        text_rect = text_obj.get_rect()   
        if alignment == 'center':
            text_rect.center = (pos)
        if alignment == 'right':
            text_rect.topright = (pos)
        if alignment == 'left':
            text_rect.topleft = (pos)
        screen.blit(text_obj, text_rect)
    