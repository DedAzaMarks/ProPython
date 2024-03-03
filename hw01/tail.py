import sys


DEFAULT_TAIL_LEN = 10
DEFAULT_STDIN_TAIL_LEN = 17
def tail(file):
    with open(file, 'r') as file:
        lines = file.readlines()
        return lines[-DEFAULT_TAIL_LEN:]

def main():
    if len(sys.argv) > 1:
        for file_num, file in enumerate(sys.argv[1:], start=1):
            print(f"==> {file} <==")
            last_lines = tail(file)
            for line in last_lines:
                print(line, end='')
            if file_num != len(sys.argv)-1:
                print() # не печатаем перенос строки для последнего файла
    else:
        lines = sys.stdin.readlines()
        last_lines = lines[-DEFAULT_STDIN_TAIL_LEN:]
        for line in last_lines:
            print(line, end='')

if __name__ == "__main__":
    main()
