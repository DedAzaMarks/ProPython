from latex_gen_pro_py.tex import generate, table


if __name__ == "__main__":
    data = [
        ['Name', 'Age', 'Gender'],
        ['John', 30, 'Male'],
        ['Alice', 25, 'Female'],
        ['Bob', 35, 'Male']
    ]
    print(
        generate(
            table(data=data), 
            table(data=data[::-1])))
    
