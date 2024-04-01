from typing import List, Self


class Matrix:
    def __init__(self, data: List[List[int|float]]):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other: Self):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        result = [[self.data[i][j] + elem for j, elem in enumerate(row)] for i, row in enumerate(other.data)]
        return Matrix(result)

    def __mul__(self, other: List[List[int|float]]|int|float):
        result: List[List[int|float]] = []
        if isinstance(other, Matrix):
            if self.cols != other.cols or self.rows != other.rows:
                raise ValueError("Matrices must have the same dimensions for element-wise multiplication")
            result = [[self.data[i][j] * elem for j, elem in enumerate(row)] for i, row in enumerate(other.data)]
        elif isinstance(other, int|float):
            result: List[List[int|float]] = [[self.data[i][j] * other for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __matmul__(self, other: Self):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for matrix multiplication")
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
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
