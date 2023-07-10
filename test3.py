class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.new_list=[]
        self.count=0


    def __iter__(self):
        return self
    # Создаём рекурсивную функцию распаковки вложенных списков
    def unpacking(self,l_o_l):
        for sub in l_o_l:
            if isinstance(sub, list):
                self.unpacking(sub)
            else:
                if sub not in self.new_list:
                    self.new_list.append(sub)
                else:
                    break
        return self.new_list

    # Вызываем функцию в методе __next__()
    def __next__(self):
        unpacked_list=self.unpacking(self.list_of_list)
        if self.count>=len(self.new_list):
            raise StopIteration
        else:
            result=self.new_list[self.count]
            self.count+=1
            return result


    def __str__(self):
        return f'{self.new_list}'




def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()