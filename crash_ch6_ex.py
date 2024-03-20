# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

glossary={
    "integer":"Número entero en inglés",
    "loop":"Bucle",
    "Boolean":"Valor que es verdadero o falso",
    "F_format":"formato que permite usar el valor de una variable a la hora de imprimirla",
    "list_comprehension":"forma de hacer una lista de forma resumida en una línea",
    }
# Solución 1:
for key in glossary.keys():
    print(f"{key}".upper()+":\n\t"+glossary[key].capitalize()+".\n")

# Solución 2:
for key,value in glossary.items():
    print(key.upper()+":\n\t"+value.capitalize()+".\n")