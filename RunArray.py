import SizeOfUtil
from font import *
from unshared_char import *
from Characters import *


class RunArray(object):
    """ RunArray class keeps track of runs in a sequence. also adds and appends runs in the list"""

    runs_list = []
    index_array = [None] * 3
    index = 0

    def add_run(self, start_index, length, value):
        self.index_array[0] = start_index
        self.index_array[1] = length
        self.index_array[2] = value
        self.runs_list.append(self.index_array)
        self.index += length

    def append_run(self, length, value):
        self.index_array[0] = self.index
        self.index_array[1] = self.index + length
        self.runs_list.append(self.index_array)
        self.index += length

    def get_font(self, index):
        i = 0
        for entry in self.runs_list:
            if entry[0] <= index <= entry[1]:
                return entry[2]
            i += 1
        return None


if __name__ == '__main__':
    string = """CS 635 Advanced Object-Oriented Design & Programming
    Fall Semester, 2018
    Doc 17 Mediator, Flyweight, Facade, Demeter, Active Object
    Nov 19, 2019
    Copyright ©, All rights reserved. 2019 SDSU & Roger Whitney, 5500 Campanile Drive, San
    Diego, CA 92182-7700 USA. OpenContent (http://www.opencontent.org/opl.shtml) license defines the copyright on this document."""
    text = list(string.replace(" ", ""))
    factory_characters = []
    for i in text:
        character_factory_obj = CharacterFactory()
        character = character_factory_obj.get_character(str(i))
        if not character in factory_characters:
            factory_characters.append(character)

    font_factory_obj_1 = FontFactory()
    font_factory_obj_2=FontFactory()
    font_1=font_factory_obj_1.get_font("TIMES NEW ROMAN", "BOLD", 12)
    font_2=font_factory_obj_2.get_font("Arial", "BOLD", 12)
    run_array_obj = RunArray()
    run_array_obj.add_run(0, 100, font_1)
    run_array_obj.add_run(100, 250, font_2)
    run_array_obj.get_font(200)
    run_array_obj.append_run(10, font_1)
    print(SizeOfUtil.get_size(factory_characters) + SizeOfUtil.get_size(run_array_obj) + SizeOfUtil.get_size(
        font_1) + SizeOfUtil.get_size(font_2) , "Total size of objects using flyweight factory")

    # Calculate Size of objects without flyweight factory
    character_list = []
    for j in text:
        font_a = Font("Arial", "BOLD", 12)
        unshared_character = UnSharedCharacters(j, font_a)
        character_list.append(unshared_character)
    print(SizeOfUtil.get_size(character_list),"Total size of objects without flyweight factory")
