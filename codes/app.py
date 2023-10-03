from class_dictionary.type_date import TypedDictionary

typed_dictionary = TypedDictionary()

typed_dictionary.add_data(str, ['str', 'int'])


if __name__ == '__main__':
    typed_dictionary.add_data(int, [12, 3, 45])
    typed_dictionary.add_datas_in_list(int, 78)
    data_int = typed_dictionary.get_list_data_by_type(int)
    print(f'Dados da classe {int}: {data_int}')

    typed_dictionary.add_datas_in_list(str, 'float')
    data_str = typed_dictionary.get_list_data_by_type(str)
    print(f'Dados da classe {str}: {data_str}')
