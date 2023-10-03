from class_dictionary.type_date import TypedDictionary

typed_dictionary = TypedDictionary()

typed_dictionary.add_data(str, ['str', 'ui'])

print(typed_dictionary.get_list_data_by_type(str))
