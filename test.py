from unittest import TestCase
from codes.class_dictionary.type_date import TypedDictionary

class TestTypedDictionary(TestCase):

    def setUp(self) -> None:
        self.typed_dictionary = TypedDictionary()
        self.typed_dictionary.add_data(int, [33, 45, 66])
        self.typed_dictionary.add_data(str, ['str', 'int', 'float'])
        self.typed_dictionary.add_data(float, [12.4, 23.90, 33.78])
        return super().setUp()
    
    def test_values_corrects(self):
        values_int = self.typed_dictionary.get_list_data_by_type(int)
        values_str = self.typed_dictionary.get_list_data_by_type(str)
        values_float = self.typed_dictionary.get_list_data_by_type(float)
        self.assertEqual(values_int, [33, 45, 66])
        self.assertEqual(values_str, ['str', 'int', 'float'])
        self.assertEqual(values_float, [12.4, 23.90, 33.78])
        
    def test_exceptions_type_data(self):
        with self.assertRaises(TypeError):
            self.typed_dictionary.add_data(float, [12, 'str'])
            self.typed_dictionary.add_data(int, [12, 43, '34'])
            self.typed_dictionary.add_data(str, ['str', 'name', 88])
    
    def test_exceptions_add_value_invalid(self):
        with self.assertRaises(TypeError):
            self.typed_dictionary.add_data(bool, [True, False])