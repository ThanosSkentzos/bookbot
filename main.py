def main():
    path_frankensten = "books/Frankenstein.txt"
    with open(path_frankensten) as f:
        frankenstein = f.read()
    report(frankenstein)


def count_words(book):
    words = book.split()
    return len(words)
def count_chars(book):
    chars = {}
    for c in book.lower().replace(" ",""):
        if c not in chars:
            chars[c]=1
        else:
            chars[c]+=1
    return chars

def name(dict):
    return dict["name"]
def num(dict):
    return dict["num"]

def sort_dict(dict):
    l = [{"name":c,"num":n} for c,n in dict.items()]
    l.sort(reverse=True,key=num)
    return l

def report(book):
    num_words = count_words(book)
    chars = count_chars(book)
    print("--- Begin report of books/frankenstein.txt ---")
    for d in sort_dict(chars):
        print(f'The {name(d)} character was found {num(d)} times')


if __name__ == "__main__":
    main()
