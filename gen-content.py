def main():
    content = None
    with open("content-formatted.txt") as f:
        content = f.readlines()
        content = [x.strip("\n") for x in content] 
    
    for line in content:
        print(line)

if __name__ == "__main__":
    main()