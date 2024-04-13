# 10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org ) and find a few texts you’d like to analyze. 
# Download the text files for these works, or copy the raw text from your browser into a text file on your computer.
# You can use the count() method to find out how many times a word or phrase appears in a string.
# Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' 
# appears in each text. This will be an approximation because it will also count words such as 'then' and 'there'. 
# Try counting 'the ', with a space in the string, and see how much lower your count is.

from pathlib import Path

path = Path("little_women.txt")
contents = path.read_text(encoding='utf-8')

the_count = contents.lower().count("the ")
book_name = str(path).removesuffix(".txt").replace("_"," ").title()

print(f"The word 'the' appears {the_count} times in '{book_name}'")