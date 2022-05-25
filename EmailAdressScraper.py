import re

# For Scraping email adresses from paragraph or any sentence
# text = input("Type any paragraph or sentence to scrap email id's:")

text = "A random string mike@gmail.com rupam@gmail.com aeron_9-6@gmail.com"

# pattern = re.compile("A random string")
pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+")

result = pattern.search(text)
result = pattern.findall(text)

print(result)