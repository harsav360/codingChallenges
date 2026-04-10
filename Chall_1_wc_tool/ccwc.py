import argparse
import sys

def main():
    # 1. Initialize the argument parser
    parser = argparse.ArgumentParser(description="A custom implementation of the wc utility.")
    
    # 2. Define the flags
    parser.add_argument('-c', '--bytes', action='store_true', help='Print the byte counts')
    parser.add_argument('-l', '--lines', action='store_true', help='Print the newline counts')
    parser.add_argument('-w', '--words', action='store_true', help='Print the word counts')
    parser.add_argument('-m', '--chars', action='store_true', help='Print the character counts')
    
    # 3. Define the file argument
    # nargs='?' means it's optional (allowing us to read from standard input later)
    # type=argparse.FileType('rb') safely opens the file for reading bytes
    parser.add_argument('file', nargs='?', type=argparse.FileType('rb'), default=sys.stdin.buffer, help='File to process')

    args = parser.parse_args()
    
    file_content = args.file.read();

    # Determine if no specific flags were provided (default behavior)
    no_flags = not (args.bytes or args.lines or args.words or args.chars)

    result = []

    if args.lines or no_flags:
        line_count = file_content.count(b'\n')
        result.append(str(line_count))
    if args.words or no_flags:
        words = file_content.split()
        word_count = len(words)
        result.append(str(word_count))
    if args.chars:
        text_content = file_content.decode('utf-8')
        char_count = len(text_content)
        result.append(str(char_count))
    if args.bytes or no_flags:
        byte_count = len(file_content)
        result.append(str(byte_count))

    file_name = args.file.name if args.file.name != '<stdin>' else ""
    print(f"{' '.join(result)} {file_name}".strip())


if __name__ == "__main__":
    main()