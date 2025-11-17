#!/usr/bin/env python3
import os
import string

# function to read and clean the text from a file
def process_text(file_path):
    # small list of common stop words to ignore
    stop_words = {'a', 'an', 'the', 'is', 'in', 'of', 'and', 'to', 'it', 'on', 'for', 'as', 'with', 'that'}
    
    # check if file exists
    if not os.path.exists(file_path):
        return None
    
    # open the file and read text
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().strip().lower()
    
    # check if text is empty
    if not text:
        return None
    
    # remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # split text into words
    words = text.split()
    
    # remove stop words
    clean_words = [word for word in words if word not in stop_words]
    
    # check if after cleaning there are words left
    if not clean_words:
        return None
    
    return clean_words

# function to search a word in both essays
def word_search(word, essay1_words, essay2_words):
    if not word:
        print("No word entered for search.")  # user didn't enter a word
        return 0, 0
    word = word.lower()
    count1 = essay1_words.count(word)  # count in essay1
    count2 = essay2_words.count(word)  # count in essay2
    print(f"\nThe word '{word}' appears {count1} times in essay1 and {count2} times in essay2.")
    return count1, count2

# function to find and show common words
def common_words(essay1_words, essay2_words):
    common = set(essay1_words).intersection(set(essay2_words))  # get common words
    print("\nCommon words found in both essays:")
    print(sorted(common))  # print sorted for readability
    return common

# function to calculate plagiarism and optionally save report
def plagiarism_check(essay1_words, essay2_words):
    set1 = set(essay1_words)
    set2 = set(essay2_words)
    intersection = set1.intersection(set2)  # common unique words
    union = set1.union(set2)  # all unique words
    plagiarism_percent = (len(intersection) / len(union) * 100) if union else 0  # jaccard similarity
    print(f"\nPlagiarism Percentage: {plagiarism_percent:.2f}%")
    
    # show similarity message
    if plagiarism_percent >= 50:
        print("Similarity is likely.")  
    else:
        print("Similarity is less likely.")  

    # ask user if they want to save the report
    choice = input("\nDo you want to save this report? (y/n): ").strip().lower()
    if choice == 'y':
        os.makedirs('reports', exist_ok=True)  # make folder if not exist
        with open('reports/similarity_report.txt', 'w', encoding='utf-8') as f:
            f.write("Plagiarism Report\n")
            f.write(f"Plagiarism Percentage: {plagiarism_percent:.2f}%\n")
            f.write("Common Words:\n")
            f.write(", ".join(sorted(intersection)))
        print("Report saved successfully at 'reports/similarity_report.txt'")
    return plagiarism_percent

def main():
    essay1_path = 'essays/essay1.txt'  # path for essay1
    essay2_path = 'essays/essay2.txt'  # path for essay2

    essay1_words = process_text(essay1_path)  # get words from essay1
    essay2_words = process_text(essay2_path)  # get words from essay2

    # check if essays exist or are empty
    if not essay1_words or not essay2_words:
        print("No essay found. Please insert the essays in the 'essays/' folder.")
        return

    # get word from user to search
    user_word = input("\nEnter a word to search for: ").strip()
    word_search(user_word, essay1_words, essay2_words)
    common_words(essay1_words, essay2_words)  # show common words
    plagiarism_check(essay1_words, essay2_words)  # calculate plagiarism

if __name__ == "__main__":
    main()
