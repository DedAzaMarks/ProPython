from latex_gen_pro_py import generate, image, table

if __name__ == "__main__":
    path = './image.png'
    data = [
        ['Name', 'Age', 'Gender'],
        ['John', 30, 'Male'],
        ['Alice', 25, 'Female'],
        ['Bob', 35, 'Male']
    ]
    print(
        generate(
            image(png_path=path),
            table(data=data), 
            table(data=data[::-1])
        ))
    
    
