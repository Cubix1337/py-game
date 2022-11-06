from Systems.System import State
from Systems.SpriteRenderSystem import SpriteLoadingSystem, SpriteRenderSystem, UpdateActiveFrameSystem, SpriteAnimationChangeSystem
from Entities.Entity import Entity

class Title(State):
    def __init__(self, world) -> None:
        super().__init__(world) 
        self.localEntities = []             
        self.textEntity = Entity()              
        self.textEntity.addComponents([
            ('Text', ["Games States asdasd"]), ('Colour', ['black']),
            ('Font', [world.font]), ('Background', ['white']),
            ('Position', [world.GAME_W/2, world.GAME_H/2]),
            ('Intersecting', [False]),
            ('Rect',[(world.GAME_W/2 - 150, world.GAME_H/2 -20), (270, 50)])
        ])     

        self.poring = Entity()
        self.poring.addComponents([            
            ('Position', [(100,100)]),
            ('Rect',[(100,100), (60,60)]),
            ('Intersecting', []),
            ('Surface',[]),
            ('Animations',[]),
            ('Frames',[]),
            ('AnimationState',[]),
            ('ActiveFrame',[]),
            ('FrameRate',[]),
            ('Data',[]),  
            ('Image',[world.sprite_dir+'poring.png']),            
            ('Filename', [world.sprite_dir+'poring.png'])            
        ])

        self.goat = Entity()
        self.goat.addComponents([            
            ('Position', [(200,200)]),
            ('Rect',[(200,200), (90,90)]),
            ('Intersecting', []),
            ('Surface',[]),
            ('Animations',[]),
            ('Frames',[]),
            ('AnimationState',[]),
            ('ActiveFrame',[]),
            ('FrameRate',[]),
            ('Data',[]),  
            ('Image',[world.sprite_dir+'goat.png']),            
            ('Filename', [world.sprite_dir+'goat.png'])            
        ])  

        self.fillir = Entity()
        self.fillir.addComponents([            
            ('Position', [(300,300)]),
            ('Rect',[(300,300), (108,116)]),
            ('Intersecting', []),
            ('Surface',[]),
            ('Animations',[]),
            ('Frames',[]),
            ('AnimationState',[]),
            ('ActiveFrame',[]),
            ('FrameRate',[]),
            ('Data',[]),  
            ('Image',[world.sprite_dir+'fillir.png']),            
            ('Filename', [world.sprite_dir+'fillir.png'])            
        ])                
               
        SpriteLoadingSystem(world).execute(self.poring)       
        SpriteLoadingSystem(world).execute(self.goat)
        SpriteLoadingSystem(world).execute(self.fillir)

        self.localEntities.append(self.poring)
        self.localEntities.append(self.goat)
        self.localEntities.append(self.fillir)

        self.localEntities.append(self.textEntity)        

    def handleInput(self, input):        
        if input.click:
            self.textEntity.updateComponent('Text',"New text boiiii")
            # SpriteAnimationChangeSystem(self.world).execute(self.poring, 'die')                      
            input.click = not input.click        
                                  
    # def update(self, delta_time, actions, bindings):
    def update(self, delta_time):
        for entity in self.localEntities:
            if entity.hasComponent('Animations'):
                UpdateActiveFrameSystem(self.world).execute(entity)
            if entity.getComponentValue('Intersecting') == True:                               
                print(entity)      
     
        # print(delta_time)
        # update animations here                

    def render(self):
        self.world.game_canvas.fill((255,255,255))
        self.world.systems[0].execute(self.textEntity)

        for entity in self.localEntities:
            if entity.hasComponent('Animations'):
                # Fix me later  (the 0 index for Pos)              
                SpriteRenderSystem(self.world).execute(entity, entity.getComponentValue('Position')[0])
        
        if self.poring.getComponentValue('AnimationState') == 'die':
            # Fix me later  (the 0 index for Pos)
            # self.poring.updateComponent('Position',((75,75),0))            
            pass
