from Systems.System import State
from Systems.SpriteRenderSystem import SpriteLoadingSystem

from Entities.Entity import Entity
# from Entities.Entity import Sprite

from ClassesWIP.Sprite import Sprite

class Title(State):
    def __init__(self, world) -> None:
        super().__init__(world) 
        self.localEntities = []             
        self.textEntity = Entity()              
        self.textEntity.addComponents([
            ('Text', ["Games States asdasd"]), ('Colour', ['black']),
            ('Font', [world.font]), ('Background', ['white']),
            ('Position', [self.world.GAME_W/2, self.world.GAME_H/2]),
            ('Intersecting', [False]),
            ('Rect',[(self.world.GAME_W/2 - 150, self.world.GAME_H/2 -20), (270, 50)])
        ])     

        self.poring2 = Entity()
        self.poring2.addComponents([            
            ('Position', [(100,100)]),
            ('Rect',[(100,100), (60,60)]),
            ('Intersecting', []),
            ('Surface',[]),
            ('Animations',[]),
            ('AnimationState',[]),
            ('ActiveFrame',[]),
            ('Data',[]),
            ('Filename', [world.sprite_dir+'poring.png'])            
        ])
        SpriteLoadingSystem(world).execute(self.poring2)


        self.poring = Sprite(world.sprite_dir+'poring.png')

        # self.goat_sprite = Sprite(world.sprite_dir+'goat.png')

        self.localEntities.append(self.poring2)
        self.localEntities.append(self.textEntity)        

    def handleInput(self, input):        
        if input.click:
            self.textEntity.updateComponent('Text',"New text boiiii")
            self.poring.setAnimationState('die')            
            input.click = not input.click        
                                  
    # def update(self, delta_time, actions, bindings):
    def update(self, delta_time):
        self.poring.updateActiveFrame()
        # for entity in self.localEntities:
        #     if self.localEntities[entity].getComponentValue('Intersecting') == True:
        #         print(self.localEntities[entity])
       
        # print(delta_time)
        # update animations here
        pass
        # print(delta_time)        

    def render(self):
        self.world.game_canvas.fill((255,255,255))
        self.world.systems[0].execute(self.textEntity)
        if self.poring.animationState == 'die':
            self.world.game_canvas.blit(self.poring.getActiveFrame(),(75, 75))       
        else:
            self.world.game_canvas.blit(self.poring.getActiveFrame(),(100, 100))       
