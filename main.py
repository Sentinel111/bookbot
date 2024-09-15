def sort_on(dict):
    return dict["num"]


def count_chars(words: list) -> list:
    char_count = []
    for word in words:
        for char in word:
            char_found = False
            if not char.isalpha():
                continue
            for i in range(len(char_count)):
                if char_count[i]["char"] == char:
                    char_count[i]["num"] += 1
                    char_found = True
                    break
            if not char_found:
                char_count.append({"char": char, "num": 1})
    char_count.sort(reverse=True, key=sort_on)
    return char_count


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        lower_case_words = [word.lower() for word in words]
        char_count = count_chars(lower_case_words)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document\n")
        for char in char_count:
            print(f"The '{char['char']}' character was found {char['num']} times")
        print("--- End of report ---")


if __name__ == "__main__":
    main()
