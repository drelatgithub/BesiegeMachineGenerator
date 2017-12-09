from . import globals

class Item(object):
    def __init__(self, newLabel="Item", newKeyValuePairs=[], newContents=[]):
        """
        "keyValuePairs" is a list of [key, value] pair.
        "contents" could be a list of numbers, string literals, or "Item"s.
        However, AT MOST ONE non-item content is allowed.
        
        In printing to XML file, the numbers would be used as string literals.
        """
        self.label = newLabel
        self.keyValuePairs = newKeyValuePairs
        self.contents = newContents
    
    def format(self, xmlObject, depth):
        xmlObject.data += xmlObject.indent * depth + "<%s" % self.label
        for eachKeyValuePair in self.keyValuePairs:
            xmlObject.data += " %s=\"%s\"" % tuple(eachKeyValuePair)
        if self.contents:
            xmlObject.data += ">"
            isFirst = True
            for eachContent in self.contents:
                if isinstance(eachContent, Item):
                    if  isFirst:
                        xmlObject.data += xmlObject.newline
                    eachContent.format(xmlObject, depth + 1)
                else:
                    xmlObject.data += str(eachContent)
                isFirst = False
            xmlObject.data += xmlObject.indent * depth + "</%s>%s" % (self.label, xmlObject.newline)
        else:
            xmlObject.data += " />%s" % xmlObject.newline

class XmlObject(object):
    def __init__(self,
        newVersion=globals.XML_VERSION,
        newEncoding=globals.XML_ENCODING,
        newNewline=globals.XML_NEWLINE,
        newIndent=globals.XML_INDENT,
        newContents=[]):
        
        self.version = newVersion
        self.encoding = newEncoding
        self.newline = newNewline
        self.indent = newIndent
        self.contents = newContents
    
    def stringFormat(self):
        self.data = "<?xml version=\"%.1f\" encoding=\"%s\"?>%s" % (self.version, self.encoding, self.newline)

        # Recursively search for content
        for eachContent in self.contents:
            eachContent.format(self, 0)
        
    def printXml(self, filepath):
        self.stringFormat()
        with open(filepath, 'w', encoding='utf8') as f:
            f.write(self.data)
    
    