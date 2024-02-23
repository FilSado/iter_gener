class FlatIterator:

    def __init__(self, list_of_list : list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.lv1 = 0
        self.lv2 = -1
        self.main_len = len(self.list_of_list)
        return self

    def __next__(self):
        self.lv2 += 1
        if self.lv2 == len(self.list_of_list[self.lv1]):
            self.lv1 += 1
            self.lv2 = 0
        if self.main_len == self.lv1:
            raise StopIteration
        return self.list_of_list[self.lv1][self.lv2]


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