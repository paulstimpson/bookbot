def main():
    word_count=0
    char_count={}
    
    print(f"--- Begin report of books/frankenstein.txt ---")
    
    with open("books/frankenstein.txt", 'r') as f:
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
            print(f"The '{char}' character was found {char_count[char]} times")

    

main()