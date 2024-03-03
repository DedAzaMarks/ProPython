import sys

def wc(filepath):
    lines = 0
    words = 0
    chars = 0

    with open(filepath, 'r') as f:
        for line in f:
            lines += 1
            words += len(line.split())
            chars += len(line)

    return lines, words, chars

def main():
    
    DEFAULT_FORMAT = "{: >6}\t{: >6}\t{: >6}"
    
    total_lines = 0
    total_words = 0
    total_chars = 0

    if len(sys.argv) > 1:
        for file in sys.argv[1:]:
            lines, words, chars = wc(file)
            total_lines += lines
            total_words += words
            total_chars += chars
            print(f"{DEFAULT_FORMAT}\t{file}".format(lines, words, chars, file))

        if len(sys.argv) > 2:
            print(f"{DEFAULT_FORMAT}\ttotal".format(total_lines, total_words, total_chars))
        return
    content = sys.stdin.read()
    lines = content.count('\n')
    words = len(content.split())
    chars = len(content)
    print(DEFAULT_FORMAT.format(lines, words, chars))

if __name__ == "__main__":
    main()
