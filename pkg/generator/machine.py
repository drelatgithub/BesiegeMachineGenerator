import uuid

from . import globals
from .xml_item import Item

class Position(Item):
    def __init__(self, newCoordinate=[0, 0, 0]):
        super().__init__(newLabel="Position", newKeyValuePairs=[
            ["x", newCoordinate[0]],
            ["y", newCoordinate[1]],
            ["z", newCoordinate[2]]
        ])
    def setX(self, newX):
        self.keyValuePairs[0][1] = newX
    def setY(self, newY):
        self.keyValuePairs[1][1] = newY
    def setZ(self, newZ):
        self.keyValuePairs[2][1] = newZ
class Rotation(Item):
    def __init__(self, newQuaternion=[0, 0, 0, 1]): # Default: Identity quaternion
        super().__init__(newLabel="Rotation", newKeyValuePairs=[
            ["x", newQuaternion[0]],
            ["y", newQuaternion[1]],
            ["z", newQuaternion[2]],
            ["w", newQuaternion[3]]
        ])
    def setX(self, newX):
        self.keyValuePairs[0][1] = newX
    def setY(self, newY):
        self.keyValuePairs[1][1] = newY
    def setZ(self, newZ):
        self.keyValuePairs[2][1] = newZ
    def setW(self, newW):
        self.keyValuePairs[3][1] = newW
class Scale(Item):
    def __init__(self, newCoordinate=[1, 1, 1]):
        super().__init__(newLabel="Scale", newKeyValuePairs=[
            ["x", newCoordinate[0]],
            ["y", newCoordinate[1]],
            ["z", newCoordinate[2]]
        ])
    def setX(self, newX):
        self.keyValuePairs[0][1] = newX
    def setY(self, newY):
        self.keyValuePairs[1][1] = newY
    def setZ(self, newZ):
        self.keyValuePairs[2][1] = newZ
    def setUniform(self, newScale):
        self.setX(newScale)
        self.setY(newScale)
        self.setZ(newScale)

class Transform(Item):
    
    def __init__(self,
        newPosition=None, newRotation=None, newScale=None):
        """
        newPosition, newRotation, newScale are all "Item"s.
        """
        
        self.position = newPosition if (newPosition is not None) else Position()
        self.rotation = newRotation if (newRotation is not None) else Rotation()
        self.scale = newScale if (newScale is not None) else Scale()
        
        super().__init__(newLabel="Transform", newContents=[
            self.position,
            self.rotation,
            self.scale
        ])
    
class Data(Item):
    def __init__(self, newKeyValuePairs=[], newContents=[]):
        super().__init__(newLabel="Data", newKeyValuePairs=newKeyValuePairs, newContents=newContents)

class Block(Item):
    def __init__(self,
        newId=0, newGuid=None, newTransform=None, newData=None):
        
        self.id = newId
        self.guid = newGuid if newGuid else str(uuid.uuid1())
        self.transform = newTransform if (newTransform is not None) else Transform()
        self.data = newData if (newData is not None) else Data()
        
        super().__init__(newLabel="Block", newKeyValuePairs=[
            ["id", self.id],
            ["guid", self.guid]
        ], newContents=[
            self.transform,
            self.data
        ])

class Machine(Item):
    def __init__(self, name="Untitled"):
        self.globals = Item(newLabel="Global", newContents=[
            Position(),
            Rotation()
        ])
        self.blocks = Item(newLabel="Blocks", newContents=[
            Block() # Core block
        ])
        
        super().__init__(newLabel="Machine", newKeyValuePairs=[
            ["version", globals.MACHINE_VERSION],
            ["bsgVersion", globals.MACHINE_BSGVERSION],
            ["name", name]
        ], newContents=[
            self.globals,
            self.blocks
        ])

    def addBlock(self, newBlock):
        self.blocks.contents.append(newBlock)

    