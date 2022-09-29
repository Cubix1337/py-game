from Systems.System import State
from Entities.Entity import Entity
from ClassesWIP.Sprite import Sprite
import math

class Title(State):
    def __init__(self, world) -> None:
        super().__init__(world) 
        self.localEntities = {}             
        self.textEntity = Entity()              
        self.textEntity.addComponents([
            ('Text', ["Games States asdasd"]), ('Colour', ['black']),
            ('Font', [world.font]), ('Background', ['white']),
            ('Position', [self.world.GAME_W/2, self.world.GAME_H/2]),
            ('Intersecting', [False]),
            ('Rect',[(self.world.GAME_W/2 - 150, self.world.GAME_H/2 -20), (270, 50)])
        ])
        self.sprite = Sprite(world.sprite_dir+'poring.png')
        self.goat_sprite = Sprite(world.sprite_dir+'goat.png')
        self.goat = [
            self.goat_sprite.parseSprite(0), self.goat_sprite.parseSprite(1), self.goat_sprite.parseSprite(2),
            self.goat_sprite.parseSprite(3), self.goat_sprite.parseSprite(4), self.goat_sprite.parseSprite(5),
            self.goat_sprite.parseSprite(6),self.goat_sprite.parseSprite(7)
        ]

        # self.poring = [
        #     self.sprite.parseSprite(0), self.sprite.parseSprite(1),
        #     self.sprite.parseSprite(2), self.sprite.parseSprite(3)
        # ]

        self.localEntities.update({ self.localEntities.__len__: self.textEntity})

    def handleInput(self, input):        
        if input.click:
            self.textEntity.updateComponent('Text',"New text boiiii")
            self.world.index += 1
            input.click = not input.click
        
            # print(self.textEntity.hasComponent('Text'))
                                  
    # def update(self, delta_time, actions, bindings):
    def update(self, delta_time):
        # update animations here
        pass
        # print(delta_time)        

    def render(self):
        self.world.game_canvas.fill((255,255,255))
        self.world.systems[0].execute(self.textEntity)
        if self.world.index >= 7:
            self.world.index = 0
        else:
             self.world.index += 0.025
        # self.world.game_canvas.blit(self.poring[math.floor(self.world.index)], (0, 0))
        self.world.game_canvas.blit(self.goat[math.floor(self.world.index)], (self.world.GAME_W/2, 100))

