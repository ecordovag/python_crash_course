# 10-5. Guest Book: Write a while loop that prompts users for their name. 
# Collect all the names that are entered, and then write these names to 
# a file called guest_book.txt. Make sure each entry appears on a new 
# line in the file.

from pathlib import Path

prompt="Write your name. "
prompt += "If you're done, insert quit. "

active=True
name_list=[]
while active:
    name=input(prompt)
    name_list.append(name)
    if name=="quit":
        active=False
        name_list.remove("quit")

path=Path("guest_book.txt")

content=""
for number in range(0,len(name_list)):
    content += name_list[number]+"\n"

path.write_text(content)

