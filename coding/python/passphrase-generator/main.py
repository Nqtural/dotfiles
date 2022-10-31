import random as r
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("lenght", type=int)
parser.add_argument("-s", "--sepparator", type=str)
args = parser.parse_args()

LENGTH = args.lenght

if args.sepparator == None:
    sepparator = "-"
else:
    sepparator = str(args.sepparator)

words = open("words.txt", "r").readlines()
passphrase = []

for i in range(LENGTH):
    passphrase.append(words[r.randint(0, len(words))].replace("\n", ""))

print(sepparator.join(passphrase))
