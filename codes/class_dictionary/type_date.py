from typing import List, Dict, Generic, Type, TypeVar

T = TypeVar('T')

class TypedDictionary(Generic[T]):
    """
    Uma classe que implementa um dicionário tipado, capaz de armazenar listas de diferentes tipos de dados.

    Attributes:
        _data (Dict[Type[T], List[T]]): Um dicionário que mapeia tipos de dados para listas de dados desse tipo.
        _types (List[T]): Uma lista que contém os tipos de dados válidos que podem ser armazenados no dicionário.

    Methods:
        validate_internal_data(type_data: Type[T]) -> None:
            Valida se um tipo de dado é válido, levantando uma exceção se não estiver presente em _types.

        add_data(key_data: Type[T], list_data: List[T]) -> None:
            Adiciona uma lista de dados ao dicionário, associada a um tipo de dado específico.

        show_data() -> Dict[Type[T], List[Type[T]]]:
            Retorna o dicionário interno (_data) que armazena as listas de dados.

        add_datas_in_list(type_data: Type[T], data: Type[T]) -> None:
            Adiciona um dado a uma lista específica no dicionário, criando a lista se ainda não existir.

        get_list_data_by_type(type_data: Type[T]) -> List[T]:
            Retorna a lista de dados associada a um tipo de dado específico.

    Exemplo de Uso:
        # Criando uma instância da classe TypedDictionary
        typed_dict = TypedDictionary()

        # Adicionando uma lista de strings ao dicionário, associada ao tipo str
        typed_dict.add_data(str, ["apple", "banana", "cherry"])

        # Adicionando um único dado à lista de inteiros no dicionário
        typed_dict.add_datas_in_list(int, 42)

        # Obtendo a lista de dados associada ao tipo str
        str_data = typed_dict.get_list_data_by_type(str)

        # Exibindo o dicionário completo
        all_data = typed_dict.show_data()
    """
    def __init__(self) -> None:
        self._data: Dict[Type[T], List[T]] = {}
        self._types: List[T] = [str, int, float]
    
    def validate_internal_data(self, type_date: Type[T]):
        if type_date not in self._types:
            raise TypeError({"message": "Tipo de dado inválido", "valid_types": self._types})
        
    def add_data(self, key_data: Type[T], list_datas: List[T]) -> None:
        self.validate_internal_data(key_data)
        for date in list_datas:
            if type(date) != key_data:
                raise TypeError({"message": "Tipo de dado incompatível", "valid_types": key_data})
        self._data[key_data] = list_datas
            
    def show_data(self) -> Dict[Type[T], List[Type[T]]]:
        return self._data

    def add_datas_in_list(self, type_data: Type[T], data: Type[T]) -> None:
        self.validate_internal_data(type_data)
        if type(data) != type_data:
            raise TypeError({"message": "Tipo de dado incompatível", "valid_types": type_data})
        if type_data not in self._data.keys():
            self._data[type_data]: List[T] = []
        self._data[type_data].append(data)
    
    def get_list_data_by_type(self, type_data: Type[T]) -> List[T]:
        self.validate_internal_data(type_data)
        if type_data not in self._data.keys():
            raise TypeError({"message": "Tipo de dado não salvo anteriormente", "saved_data": self._data.keys()})
        return self._data[type_data]
        
