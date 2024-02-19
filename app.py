#f. Output to result.txt
import sys
stdoutOrigin = sys.stdout
sys.stdout = open("/home/output/result.txt", "w")

#a. List name of all the text file at location: /home/data
import os
location = "/home/data"
files = os.listdir(location)
print("a. List of files at location- " + location + "are: ")
for i in files:
    print(i)
print()

#b. Read the two text files and count total number of words in each text files.
total_words = 0
words_file1 = 0
words_file2 = 0

with open('/home/data/IF.txt', 'r') as file1:
    for line in file1:
        words = line.split()
        words_file1 += len(words)
print("b.")
print("Count of words in File IF.txt is: " + str(words_file1))

with open('/home/data/Limerick-1.txt', 'r') as file2:
    for line in file2:
        words = line.split()
        words_file2 += len(words)

print("Count of words in File Limerick-1.txt is: " + str(words_file2))
print()

#c. Add all the number of words to find the grand total (total number of words in both files)
print("c. Total count of words in both the files is: " + str(words_file1 + words_file2))
print()

#d. List the top 3 words with maximum number of counts in IF.txt.  Include the word counts for the top 3 words.
dct={}
from collections import Counter
with open('/home/data/IF.txt', 'r') as file1:
    data = file1.read()
    words = data.split()
    dct = Counter(words)
    top_three = dct.most_common(3)

print("d. The top three words with most count in IF.txt are: ")
for i in top_three:
    print(str(i[0] + " -> " + str(i[1])))
print()

#e. Find the IP address of your machine
import socket
hostname = socket.gethostname()
print("e. IP address of my machine is: " + socket.gethostbyname(hostname))
print()

#f. Write all the output to a text file at location: /home/output/result.txt (inside your container).
sys.stdout.close()
sys.stdout=stdoutOrigin

#g. Upon running your container, it should do all the above stated steps and print the information on console from result.txt file and exit
with open("/home/output/result.txt", "r") as file:
    print(file.read())