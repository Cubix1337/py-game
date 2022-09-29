from Components.Component import componentDict

class Entity:
    def __init__(self) -> None:
        self.id = 0
        self.components = {}

    def addComponent2(self, key, arguments):    
        self.components.update({key: componentDict[key](*arguments)})

    def addComponents(self, components):
        for component in components:
            self.components.update({component[0]: componentDict[component[0]](*component[1])})                

    def addComponent(self, component):        
        self.components.append(component)
    
    def updateComponent(self, component, newValue):        
        self.components[component].setValue(newValue)
        
    def removeComponents(self, key):
        del self.components[key]
    
    def logComponents(self):        
        for component in self.components:        
            #.items()                 
                print(component, '->',self.components[component].__dict__)

    def hasComponent(self, name):
        # for component in self.components: 
            try:
                if self.components[name]:
                    return True                
            except KeyError:
                return False
    def getComponent(self, name):
        # for component in self.components: 
            try:
                if self.components[name]:                    
                    return self.components[name]                
            except KeyError:
                return False

class Archtype(Entity):
    def __init__(self) -> None:
        super().__init__()        

# class Button(Archtype):
#     def __init__(self) -> None:
#         super().__init__()
#         self.addComponents(
#             componentDict['Colour'],componentDict['Text'],
#             componentDict['Background'],componentDict['Position'],
#             componentDict['Alignment'], componentDict['Dimensions'],
#             componentDict['Font'],componentDict['Rect']
#         )

        