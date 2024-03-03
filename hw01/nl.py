import sys


def main():
    OUTPUT_FORMAT = "{: >6}\t{}"
    if len(sys.argv) == 1:
        for num, line in enumerate(sys.stdin, start=1):
            print(OUTPUT_FORMAT.format(num, line.rstrip()))
        return
    for filepath in sys.argv[1:]:
        try:
            with open(filepath, 'r') as file:
                for num, line in enumerate(file.readlines(), start=1):
                    print(OUTPUT_FORMAT.format(num, line.rstrip()))
        except FileNotFoundError:
            print(f"File '{filepath}' not found.")



if __name__ == "__main__":
    main()
