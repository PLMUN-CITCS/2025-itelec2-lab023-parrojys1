"""Count the number of words in a sentence based on user input."""
def get_sentence_input():
    """Prompt user for sentence input and return it."""
    x = input("Enter a sentence: ")
    return x

def count_words(y):
    """Count the number of words in a sentence."""
    words = y.split()
    return len(words)

if __name__ == "__main__":
    sentence = get_sentence_input()
    word_count = count_words(sentence)
    print("The sentence has", word_count, "words.")
