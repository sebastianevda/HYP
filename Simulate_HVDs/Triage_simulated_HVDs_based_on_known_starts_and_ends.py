list_filename = "Simulated_HVDs_10000_.txt"

output_filename = "Simulated_HVDs_10000_.txt.triaged.txt"

possible_ends_above_20 = ["16641","16681","41681","41691","41781","46681","61681","64168","69168","74168"]
possible_starts_above_20 = ["1568","1681","1757","1759","1781","1789","1791","1959"]


listofnames = open(list_filename)
withmatchedid = open(output_filename, "w")
infile = open(list_filename)
read = infile.read()
#cleaninfile = read.replace("\n","")
#rep = cleaninfile.replace (">","\n>")
splitrep = read.split("\n")

out = ""
count = 0
for entry in splitrep:
    #print (entry)
    if len(entry)>20:
        end = entry[len(entry)-6:len(entry)-1]
        start = entry[:4]
        #print (start)
        #print (end)
        if end in possible_ends_above_20:
            #print ("yes")
            #print (end)
            if start in possible_starts_above_20:
                #print ("yes")
                out = out + entry + "\n"
                count = count + 1
                #print (end)


#    else:
#        out = out + entry + "\n"
print (str(count)+" ok, out of "+str(len(splitrep)))
print ("done")
withmatchedid.write(out)
withmatchedid.close()
