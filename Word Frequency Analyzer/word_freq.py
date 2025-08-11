import sys
import string
from collections import Counter
import matplotlib.pyplot as plt

def analyze_word_frequency(file_path, top_n=10):
    word_count = Counter()
    translator = str.maketrans("", "", string.punctuation)

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:  # Read line by line (efficient for large files)
                # Normalize: lowercase & remove punctuation
                cleaned_line = line.lower().translate(translator)
                words = cleaned_line.split()
                word_count.update(words)

        # Get the top N most frequent words
        most_common = word_count.most_common(top_n)
        print(f"\nTop {top_n} Most Frequent Words:")
        for word, count in most_common:
            print(f"{word}: {count}")

        return most_common

    except FileNotFoundError:
        print("File not found.")


def plot_bar_chart(word_data):
    words, counts = zip(*word_data)
    plt.bar(words, counts, color="skyblue")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Top Word Frequencies")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = str(input("Enter the file path: "))

    top_words = analyze_word_frequency(file_path, top_n=10)

    plot_bar_chart(top_words)
