import os
import string

def process_text(file_path):
    stop_words = {'a', 'an', 'the', 'is', 'in', 'of', 'and', 'to', 'it', 'on', 'for', 'as', 'with', 'that'}
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    clean_words = [word for word in words if word not in stop_words]
    return clean_words

def word_search(word, essay1_words, essay2_words):
    word = word.lower()
    count1 = essay1_words.count(word)
    count2 = essay2_words.count(word)
    print(f"'{word}' appears {count1} times in essay1 and {count2} times in essay2.")
    return count1, count2

def common_words(essay1_words, essay2_words):
    set1 = set(essay1_words)
    set2 = set(essay2_words)
    common = set1.intersection(set2)
    print("\nCommon words found in both essays:")
    print(common)
    return common

def plagiarism_check(essay1_words, essay2_words):
    set1 = set(essay1_words)
    set2 = set(essay2_words)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    plagiarism_percent = (len(intersection) / len(union)) * 100
    print(f"\nPlagiarism Percentage: {plagiarism_percent:.2f}%")
    if plagiarism_percent >= 50:
        print("Similarity is likely (50% or more).")
    else:
        print("Similarity is not likely (less than 50%).")
    print("Common words (intersection):")
    print(intersection)
    choice = input("\nDo you want to save this report? (y/n): ").strip().lower()
    if choice == 'y':
        os.makedirs('reports', exist_ok=True)
        with open('reports/similarity_report.txt', 'w', encoding='utf-8') as f:
            f.write("Plagiarism Report\n")
            f.write(f"Plagiarism Percentage: {plagiarism_percent:.2f}%\n")
            f.write("Common Words:")
            f.write(", ".join(sorted(intersection)))
        print("Report saved successfully at 'reports/similarity_report.txt'")
    return plagiarism_percent

def main():
    essay1_path = 'essays/essay1.txt'
    essay2_path = 'essays/essay2.txt'
    essay1_words = process_text(essay1_path)
    essay2_words = process_text(essay2_path)
    user_word = input("\nEnter a word to search for: ").strip()
    word_search(user_word, essay1_words, essay2_words)
    common_words(essay1_words, essay2_words)
    plagiarism_check(essay1_words, essay2_words)

if __name__ == "__main__":
    main()
