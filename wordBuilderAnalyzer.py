# This Program:
# - checks if a word == "STOP". If yes, it stops the repitition, if no, it keeps going again until word == "STOP"
# - It searches for the longest and shortest word in the list
# - Counts the number of words inside the list
# - It prints out the first and last word of the list
# - Makes all letters from all words in UPPERCASE letters
# - Makes all letters of words reversed



words = []

choice = ""

while choice != "STOP":
    choice = input("Enter any word of your choice, or type 'STOP' to finish: ")

    if choice != "STOP":
        words.append(choice)

print("Words you entered:", ", ".join(words))


for word in words:
    if max(len(word) for word in words) == len(word):
        print(f"Longest word: {word}")

    if min(len(word) for word in words) == len(word):
        print(f"Shortest word: {word}")


numberOf_words = len(words)

# for count in words:
#     numberOf_words += 1  # This is also a way to count the number of words, but it's more efficient to use len() function for this purpose. Given to the variable-name (numberOf_words) right above here

print(f"Number of words: {numberOf_words}")


print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")


upper_cases = [word.upper() for word in words]

print(f"All words in upperCases: {upper_cases}")


# reversed_words = ["".join(reversed(word)) for word in words]  # Long method for reversing words inside a list. -- .join() pastes the letters of a word together again. Without .join() they will end as single letters

reversed_words = [word[::-1] for word in words]  # Short method for reversing words. No need to use the .join() method. With this short method, letters will be correct automatically

print(f"Giving words in reverse: {reversed_words}")



# Uses:

# Thinking in steps
# empty list → filling → processing
# join()
# len()
# indexing
# loops
# string‑methods

## This one is given in here for me because of clear purpose for me learning to build this Program
# Logic Programming without overthinking
