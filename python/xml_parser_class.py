"""Xml parsing with class."""

import xml.sax

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        print(name)

        handler = GroupHandler()
        parser = xml.sax.make_parser()
        parser.setContentHandler(handler)
        parser.parse("jill.xml")

    def startElement2(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("---Person---")
            id = attrs["id"]
            print("ID:%s"%id)

            def endElements(self, name):
                if self.current == "name":
                    print("Name: %s" % self.name)
                elif self.current == "age":
                    print("Age:%s"%self.age)
                elif self.current == "weight":
                    print("Weight:%s"%self.weight)
                elif self.current == "height":
                    print("Height:%s"%self.height)
                    self.curent=""

                    def characters(self, content):
                        if self.current == "name":
                            self.name = content
                        elif self.current == "age":
                            self.age = content
                        elif self.current == "weight":
                            self.weight = content
                        elif self.current == "height":
                            self.height = content
                            handler = GroupHandler()
                            parser = xml.sax.make_parser
                            parser.setContentHandler(handler)
                            parser.parse("jill.xml")
