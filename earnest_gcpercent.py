print("Enter a sequence of DNA bases (upper or lower case):")
dna=input() #prompts the user to enter a string of DNA bases

print("\nYour sequence is:")
print(dna) #outputs the DNA sequence

print("\nYour sequence length is:")
print(len(dna)) #outputs the sequence length

g_count=dna.count("g")+dna.count("G") #stores number of "G" and "g" occurrences in dna
c_count=dna.count("c")+dna.count("C") #stores number of "C" and "c" occurrences in dna
gc_total=g_count+c_count #stores the total number of Gs and Cs

print("\nYour sequence has " + str(gc_total) + " GCs (" + str(g_count) + " Gs and " +
str(c_count) + " Cs).") #reports the number of Gs and Cs

gc_percent=gc_total/len(dna)*100 #calculates the GC percent
gc_percent_rounded=round(gc_percent,2)  #rounds the percentage to 2 decimals

print("\nYour sequence's GC content is:")
print(str(gc_percent_rounded) + "%") #done!
