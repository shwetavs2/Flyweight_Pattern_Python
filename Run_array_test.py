import unittest
from RunArray import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        font_factory_obj = FontFactory()
        value=font_factory_obj.get_font("TIMES NEW ROMAN",12,"BOLD")
        self.assertEqual(value.font_name,"TIMES NEW ROMAN")
        self.assertEqual(value.font_size,12)
        self.assertEqual(value.font_style,"BOLD")


        run_array_obj = RunArray()
        run_array_obj.add_run(0, 250, font_factory_obj)
        get_value=run_array_obj.get_font(200)
        if get_value:
            font_val=True
        False
        self.assertEqual(font_val,True)

        character_factory_obj = CharacterFactory()
        character = character_factory_obj.get_character("A")
        self.assertEqual(character.char,ord("A"))


if __name__ == '__main__':
    unittest.main()
