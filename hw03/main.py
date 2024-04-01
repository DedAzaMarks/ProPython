import numpy as np
from os.path import join as pathjoin
from matrix import Matrix


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
