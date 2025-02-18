

def main():
  with open("./books/frankenstein.txt") as f:
    content = f.read()
    # print(countWords(content))
    report(content)

def countWords(text = ""):
  return len(text.split())

def countCharacters(text = ""):
  charCount = {}
  for letter in text:
    lower = letter.lower()
    if lower in charCount:
      charCount[lower] += 1
    else:
      charCount[lower] = 1
  return charCount

def report(text = ""):
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{countWords(text)} words found in the document\n\n")
  
  for key, value in countCharacters(text).items():
    if key.isalpha():
      print(f"The '{key}' was found {value} times")

  print("--- End report ---")



main()