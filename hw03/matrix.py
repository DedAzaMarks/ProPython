from typing import List, Self
from os.path import join as pathjoin
import numpy as np


class Matrix():
    def __init__(self, data: List[List[int | float]]):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other: Self):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(
                "Matrices must have the same dimensions for addition")
        result = [[self.data[i][j] + elem for j,
                   elem in enumerate(row)] for i, row in enumerate(other.data)]
        return Matrix(result)

    def __mul__(self, other: List[List[int | float]] | int | float):
        result: List[List[int | float]] = []
        if isinstance(other, Matrix):
            if self.cols != other.cols or self.rows != other.rows:
                raise ValueError(
                    "Matrices must have the same dimensions for element-wise multiplication")
            result = [[self.data[i][j] * elem for j,
                       elem in enumerate(row)] for i, row in enumerate(other.data)]
        elif isinstance(other, int | float):
            result: List[List[int | float]] = [
                [self.data[i][j] * other for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __matmul__(self, other: Self):
        if self.cols != other.rows:
            raise ValueError(
                "Number of columns in the first matrix must match the number of rows in the second matrix for matrix multiplication")
        result = [
            [
                sum(
                    self.data[i][k] * other.data[k][j]
                    for k in range(self.cols)
                )
                for j in range(other.cols)
            ]
            for i in range(self.rows)]
        return Matrix(result)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])


def main():
    np.random.seed(0)
    a = np.random.randint(0, 10, (10, 10))
    b = np.random.randint(0, 10, (10, 10))
    for sym, op in {"+": Matrix.__add__,
                    "*": Matrix.__mul__,
                    "@": Matrix.__matmul__}.items():
        filename = f"matrix{sym}.txt"
        with open(pathjoin("artifacts", "3.1", filename), 'w') as file:
            res = op(Matrix(a.tolist()), Matrix(b.tolist()))
            file.write(str(res))


if __name__ == "__main__":
    main()
