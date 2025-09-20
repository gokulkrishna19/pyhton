# word_count.py
# Program to count words in a string

def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def main():
    print("=== Word Counter ===")
    sentence = input("Enter a sentence: ")
    print(f"Total words: {count_words(sentence)}")

if __name__ == "__main__":
    main()
