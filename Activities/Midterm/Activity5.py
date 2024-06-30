"""
Created by Angelo John Benedict Laus of SF231
Created on May 02, 2024
"""

names = ["Amanda", "Gregory", "Leonard", "Lucas", "Anabelle", "Michelle", "Roderick", "Beverly", "Evangeline", "Cristel", "Maybeline", "Peter", "Roxanne", "Deborah", "RoseAnn"]

print("Contents of list:\n:",names,"\n\n")

names.append("Marianne")
names.append("Roselle")
names.append("Shirley")
names.append("Rodel")

print("Appended names:\n",names,"\n\n")

names[5:5] = ["Melody", "Victoria"]

print("Names at 5th:\n",names,"\n\n")

print("Length:",len(names),"\n\n")

names.reverse()
print("Reversed:\n",names,"\n\n")

print("Sorted:\n",sorted(names))