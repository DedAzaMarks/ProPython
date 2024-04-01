from typing import Self
from matrix import Matrix
import numpy as np


class HashMixin:
    def __eq__(self, __value: Self) -> bool:
        return all([all(
            [self.data[i][j] == elem for j, elem in enumerate(row)])
            for i, row in enumerate(__value.data)])

    def __hash__(self):
        """pows every elemt relatievly to it's possition"""
        return sum([
            sum([(elem**i)**j for i, elem in enumerate(row, start=1)])
            for j, row in enumerate(self.data, start=1)])


class HashableMatrix(Matrix, HashMixin):
    """adds hash and cache for multiplication to basic Matrix class"""
    # это какой то дурацкий кэш, потому что он задается для одного
    # конкретного обьекта, но если выносить кэширование в отдельную
    # оболочку агрегатор, то смотрится еще хуже, потому что теперь мы
    # будем умножать передавая матрицы в функцию и смысл тогда
    # перегружать операторы -\_(:))_/-
    cache = dict()

    def __matmul__(self, other: Self):
        hash_pair = (hash(self), hash(other))
        if hash_pair in self.cache:
            return self.cache[(hash(self), hash(other))]
        result = super().__matmul__(other)
        self.cache[hash_pair] = result
        return result


def main():
    A = HashableMatrix([[1, 2], [3, 4]])
    B = HashableMatrix([[2, 4], [3, 5]])
    C = HashableMatrix([[1, 3], [2, 4]])
    D = HashableMatrix([[2, 4], [3, 5]])
    print(str(A), end='\n')
    print(str(B), end='\n')
    print(str(C), end='\n')
    print(str(D), end='\n')
    print(str(A@B), end='\n')
    print(str(C@D), end='\n')
    print(hash(A@B), end='\n')
    print(hash(C@D), end='\n')


if __name__ == "__main__":
    main()
