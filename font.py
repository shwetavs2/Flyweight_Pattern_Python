

class Font:
    """ This class  store  the font information of the character"""
    def __init__(self, name, size, style):
        self.font_name = name
        self.font_size = size
        self.font_style = style

    def get_style(self):
        return self.font_style

    def get_size(self):
        return self.font_size

    def get_name(self):
        return self.font_name



class FontFactory(object):

    """ This is Flyweight factory that given attributes for fonts returns the Flyweight  character object for the
    font. It has single point of access """

    _instance = None
    def __init__(self):
        self.font_array = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FontFactory, cls).__new__(cls)
        return cls._instance

    def get_font(self, name, style, size):
        for font in self.font_array:
            if font.get_name() == name and style == font.get_style() and size == font.get_size():
                return font
        font = Font(name, style, size)
        self.font_array.append(font)
        return font
