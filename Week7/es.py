# Write a program that reads in a text file and outputs the number of e's it contains.
# Author: Brendan Tunney

# Opening the file & reading the content. Encoding added as system default is different to text file method.

import sys # Importing SYS to use sys.argv{1}. This allows for command line arguments 

with open (sys.argv[1], "rt", encoding="utf-8") as f:
    data = f.read()

# Count number of occurrences of letter 'e' - Lower and Upper case

x = (data.count("e"))
y = (data.count("E"))

print ("Hi, this file contains" , x + y, "occurrences of the letter 'e'.")

# Closing the file 

f.close()


#References - https://www.pitt.edu/~naraehan/python3/mbb12.html
#           - https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/
#           - Lecture notes
#           - https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python/7439162





