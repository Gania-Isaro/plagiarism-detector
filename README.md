Plagiarism Detector

This project is a Python program that compares two essays to check similarity.
It cleans the text, removes punctuation and stop words, finds common words, and calculates plagiarism percentage using Jaccard similarity.
You can also search for a specific word in both essays and save a report.

How to Use

1. Set up folders
Run setup.sh to create the essays/ and reports/ folders:
bash setup.sh

2. Add your essays
Place your two essays inside the essays/ folder and name them:
- essay1.txt
- essay2.txt

3. Run the program
python3 plagiarism-detector.py

- If essays are missing, it will display:
  "No essay found. Please insert the essays in the 'essays/' folder."
- Enter a word to search in both essays.
- The program will show common words.
- It will calculate and display plagiarism percentage.
- You can choose to save a report in the reports/ folder.

Folder Structure

essays/ – place essay1.txt and essay2.txt here
reports/ – saved reports go here
plagiarism-detector.py – main program
setup.sh – creates folders and logs setup
Readme.md – this file

Notes

- Report is saved only if you type 'y' when prompted.
- Stop words like 'a', 'the', 'and' are ignored during similarity check.
