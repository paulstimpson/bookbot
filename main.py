import sys

def main():
    word_count=0
    char_count={}
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookfile=sys.argv[1]

    print(f"--- Begin report of {bookfile} ---")
    
    with open(bookfile, 'r') as f:
        file_contents = f.read()

    words=file_contents.split()
    word_count=len(words)
    
    print(f"{word_count} words found in the document")

    for char in file_contents:
        if char.lower() in char_count:
            char_count[char.lower()]+=1
        else:
            char_count[char.lower()]=1

    for char in char_count:
        if char in "abcdefghijklmnopqrstuvwxyz":
            print(f"{char}: {char_count[char]}")

    

main()