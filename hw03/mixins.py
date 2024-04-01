from typing import List, Self
from os.path import join as pathjoin
import numpy as np


class FileIO:
    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self))


class ConsoleOutput:
    def __str__(self):
        return str(self)


class GetterSetter:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data


class NumPyMixin:
    def __init__(self, data: List[List[int | float]]):
        self.data = np.array(data)
        self.rows = self.data.shape[0]
        self.cols = self.data.shape[1]

    def __add__(self, other: Self):
        l = self.data
        r = other.data
        return NumPyMixin((l+r).tolist())

    def __mul__(self, other: Self):
        l = np.array(self.data)
        r = np.array(other.data)
        return NumPyMixin((l*r).tolist())

    def __matmul__(self, other: Self):
        l = np.array(self.data)
        r = np.array(other.data)
        return NumPyMixin((l@r).tolist())

    def __str__(self):
        return str(np.array(self.data))


class MixinedMatrix(ConsoleOutput, GetterSetter, FileIO, NumPyMixin):
    pass


def main():
    np.random.seed(0)
    a = np.random.randint(0, 10, (10, 10))
    b = np.random.randint(0, 10, (10, 10))
    for sym, op in {"+": MixinedMatrix.__add__,
                    "*": MixinedMatrix.__mul__,
                    "@": MixinedMatrix.__matmul__}.items():
        filename = f"matrix{sym}.txt"
        with open(pathjoin("artifacts", "3.2", filename), 'w') as file:
            res = op(MixinedMatrix(a.tolist()), MixinedMatrix(b.tolist()))
            file.write(str(res))


if __name__ == "__main__":
    main()
