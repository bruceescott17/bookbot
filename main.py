def main(): 
    with open('/books/Frankenstein.txt') as f:
        file_contents = f.read()
    print(file_contents)



if __name__ == "__main__":
    main()