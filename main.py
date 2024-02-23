def main(): 
    with open('home/bruceescott/workspace/github.com/bruceescott17/bookbot/books/Frankenstein.txt') as f:
        file_contents = f.read()
    print(file_contents)



if __name__ == "__main__":
    main()