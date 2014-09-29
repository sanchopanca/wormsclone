class LoopList(list):
    def __init__(self, iterable=None):
        list.__init__(self, iterable)
        self.next_index = 0

    def get_next(self):
        if len(self) == 0:
            return None
        try:
            res = self[self.next_index]
            self.next_index += 1
        except IndexError:
            self.next_index = 1
            res = self[0]
        return res

if __name__ == '__main__':
    l = LoopList([1, 2])
    print l.get_next(), l.get_next(), l.get_next()