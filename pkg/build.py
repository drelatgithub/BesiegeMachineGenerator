from .blueprints import jigsaws as bp # Select blueprint to use here
from .generator import machine as machine
from .generator import xml_item as xi

class Builder(object):
    def __init__(self, newFilepath):
        self.machine = machine.Machine(name=bp.name)
        self.xo = xi.XmlObject(newContents=[self.machine])
        self.filepath = newFilepath
        
    def work(self):
        bp.build(self.machine)
        self.xo.printXml(self.filepath)
 