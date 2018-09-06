import re
from re import split
from re import sub
from re import subn
from re import escape



def regexCompile(text1, text2, text3):
    print("\n\nCompile")

    # Compile() creates an Regex character class from [a-e]
    # Regex patterns are compiled into pattern objects

    # [a-e]
    pattern = re.compile('[a-e]')
    print("[a-e]: ", pattern.findall(text1))

    # [abcde]
    pattern = re.compile("[abcde]")
    print("[abcde]: ", pattern.findall(text1))

    print("Notice the [a-e] & [abcde] return the same value\n")

    # \d is equivalent to [0-9]
    pattern = re.compile("\d")
    print("\d:", pattern.findall(text2))

    # \d+ will match a group on [0-9], group of one or greater size
    pattern = re.compile("\d+")
    print("\d+: ", pattern.findall(text2))

    print("Notice how \d+ will group numbers together\n")

    # \w is equivalent to [a-zA-Z0-9]
    pattern = re.compile("\w")
    print("\w: ", pattern.findall(text2))

    # \w+ matches to a group of alphanumeric characters
    pattern = re.compile("\w+")
    print("\w+: ", pattern.findall(text2))

    print("Notice how \w+ will group characters together\n")

    # \W matches to NON alphanumeric characters
    pattern = re.compile("\W")
    print("W: ", pattern.findall(text3))

    pass


def regexSplit(text1, text2, text3):

    print("\n\nSplit")

    # Split using Non Alpha Numeric Character
    print("Split using [.]: ", split("[.]", text1))
    print("Split using . :", split(".", text1))

    # Upon finding ',' or whitespace ' ', the split(), splits the string from that point", text2))
    print("Split using \W+: ", split("\W+", 'Words, words , Words'))
    print("Split using \W+: ", split("\W+", "Word's, words , Words"))

    print("Split using [.]: ", split("\W+", text2))
    print("Split using . :", split("t", text2))

    pass


def regexSub(text1):


    print("\n\nSub")

    print("No Flag: Replace letter a with '*': ", re.sub("a", "*", text1))
    print("Flag Present: Replace letter a with '*': ", re.sub("a", "*", text1, re.IGNORECASE))
    print("Flag & Count Present: Replace letter a with '*': ", re.sub("a", "*", text1, 1, re.IGNORECASE))

    pass


def regexSubn(text1, text2, text3):

    print("\n\nSubn")

    print("No Flag: Replace letter a with '*': ", re.subn("a", "*", text1))
    print("Flag Present: Replace letter a with '*': ", re.subn("a", "*", text1, re.IGNORECASE))
    print("Flag & Count Present: Replace letter a with '*': ", re.subn("a", "*", text1, 1, re.IGNORECASE))

    print("Remember that Subn returns a tuple with the # of replacement and the String after replacement")

    pass





def main():

    text1 = "Hello Mr. Tim. How are you today ?"
    text2 = "I went to him at 11 A.M, on 4th July 1886"
    text3 = "he said *** in some_language."

    regexCompile(text1, text2, text3)

    regexSplit(text1, text2, text3)

    regexSub(text1)

    regexSubn(text1, text2, text3)


    pass


if __name__ == '__main__':
    main()



'''

Regex in Python

There are a total of 14 metacharcters and will be discussed as they follow into functions:

\   Used to drop the special meaning of character
    following it (discussed below)
[]  Represent a character class ....REPRESENTS ONLY ONE CHARACTER PER []
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One ore more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs




\d   Matches any decimal digit, this is equivalent
     to the set class [0-9].
\D   Matches any non-digit character.
\s   Matches any whitespace character.
\S   Matches any non-whitespace character
\w   Matches any alphanumeric character, this is
     equivalent to the class [a-zA-Z0-9_].
\W   Matches any non-alphanumeric character. 


Compile() - Regex expressions are compiled into pattern objects. Used for searching or pattern matching

Split() - Splits the string by the occurence of a character or pattern 
    re.split(pattern, string, maxsplit=0, flags=0)

Sub() - Gets the Substring but can replace a character with one of its parameters
    re.sub(pattern, repl, string, count=0, flags=0)

Subn() - Similar to Sub() but provides output. It returns a tuple with total count of replacement and new String 

'''