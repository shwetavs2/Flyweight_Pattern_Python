
class Characters:
    """ This class  store  the unicode code point of the character"""

    def __init__(self, character):
        self.char = ord(character)


class CharacterFactory(object):
    """ This class is a Flyweight factory that given a unicode code point returns the Flyweight character object for
    the character.It has single point of access """

    _instance = None

    def __init__(self):
        self.character_array = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CharacterFactory, cls).__new__(cls)
        return cls._instance

    def get_character(self, current_char):
        for character in self.character_array:
            if chr(character) == current_char:
                return chr(character)
        character = Characters(current_char)
        self.character_array.append(character)
        return character
