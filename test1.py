class FlatIterator:
    # Прописываем в инициализаторе добавление внутренних списков в новый список методом extend()
    def __init__(self, list_of_list):
        self.new_list=[]
        for sublist in list_of_list:
            self.new_list.extend(sublist)
        self.current = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.current<len(self.new_list):
            item=self.new_list[self.current]
            self.current += 1
            return item
        if self.current >= len(self.new_list):
            raise StopIteration



def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]




if __name__ == '__main__':
    test_1()
