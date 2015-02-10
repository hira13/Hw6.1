accs= ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

# Will print if it contains a 5 by searching for it and then printing it 
print("contains 5:")
for acc in accs: 
    if re.search(r"5", acc): 
        print("\t" + acc) 

#Will print if it has a d or e 
print("contains d or e:")
for acc in accs: 
    if re.search(r"(d|e)", acc): 
        print("\t" + acc) 
#will print if it has d and then e consequtively 
print("contains d and e in that order:")
for acc in accs: 
    if re.search(r"d.*e", acc): 
        print("\t" + acc)

#will print if d and e have a letter in between them 
print("contains d and e separated by a single letter:")
for acc in accs: 
    if re.search(r"(d.e)", acc): 
        print("\t" + acc) 
#will print if it has d and e in any order 
print("contains d and e in any order:")
for acc in accs: 
    if re.search(r"d.*e", acc) or re.search(r"e.*d", acc): 
        print("\t" + acc) 

#will print anything starting with an x or y 
print("starts with either x or y:")
for acc in accs: 
    if re.search(r"^(x|y)", acc): 
        print("\t" + acc) 
#will print if it was x or y but ends with e 
print("starts with either x or y and ends with e:")
for acc in accs: 
    if re.search(r"^(x|y).*e$", acc): 
        print("\t" + acc) 
#will print anything with 3 or more numbers in a row 
print("contains three or more numbers in a row:")
for acc in accs: 
    if re.search(r"\d{3,}", acc): 
        print("\t" + acc) 
#will print if it ends with a d followed by an a, r or p 
print("ends with d followed by either a, r or p:")
for acc in accs: 
    if re.search(r"d[arp]$", acc): 
        print("\t" + acc)  
