from ..generator import machine as m
from ..generator import xml_item as xi
from ..generator import globals

name = "jigsaws"

def build(machineItem):
    spacing = 2.5
    
    xs = range(-3, 4)
    zs = range(-3, 4)
    ys = range(4)
    
    machineItem.globals.contents[0].setY(1.5)
    
    for x in xs:
        for y in ys:
            for z in zs:
                machineItem.addBlock(m.Block(
                    newId=globals.MACHINE_BLOCK_NAME["SMALL_WOODEN_BLOCK"],
                    newTransform=m.Transform(
                        newPosition=m.Position([x*spacing, y*spacing, z*spacing - 0.5])
                    )
                ))
                machineItem.addBlock(m.Block(
                    newId=globals.MACHINE_BLOCK_NAME["CIRCULAR_SAW"],
                    newTransform=m.Transform(
                        newPosition=m.Position([x*spacing + 0.5, y*spacing, z*spacing]),
                        newRotation=m.Rotation([0, 2**(-0.5), 0, 2**(-0.5)])
                    ),
                    newData=m.Data(
                        newContents=[
                            xi.Item(
                                newLabel="Single",
                                newKeyValuePairs=[["key", "bmt-speed"]],
                                newContents=[1]
                            ),
                            xi.Item(
                                newLabel="Single",
                                newKeyValuePairs=[["key", "bmt-acceleration"]],
                                newContents=["Infinity"]
                            ),
                            xi.Item(
                                newLabel="Boolean",
                                newKeyValuePairs=[["key", "flipped"]],
                                newContents=["False"]
                            )
                        ]
                    )
                ))
                machineItem.addBlock(m.Block(
                    newId=globals.MACHINE_BLOCK_NAME["CIRCULAR_SAW"],
                    newTransform=m.Transform(
                        newPosition=m.Position([x*spacing - 0.5, y*spacing, z*spacing]),
                        newRotation=m.Rotation([0, -2**(-0.5), 0, 2**(-0.5)])
                    ),
                    newData=m.Data(
                        newContents=[
                            xi.Item(
                                newLabel="Single",
                                newKeyValuePairs=[["key", "bmt-speed"]],
                                newContents=[1]
                            ),
                            xi.Item(
                                newLabel="Single",
                                newKeyValuePairs=[["key", "bmt-acceleration"]],
                                newContents=["Infinity"]
                            ),
                            xi.Item(
                                newLabel="Boolean",
                                newKeyValuePairs=[["key", "flipped"]],
                                newContents=["False"]
                            )
                        ]
                    )
                ))
    
