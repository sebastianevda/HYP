list_filename = "HYP1_population.txt"
output_filename = "Output_number_homozyg_per_iteration.txt"


listofnames = open(list_filename)
withmatchedid = open(output_filename, "w")
infile = open(list_filename)
read = infile.read()
#cleaninfile = read.replace("\n","")
#rep = cleaninfile.replace (">","\n>")
splitrep = read.split("\n")

number_of_itterations = 1000000
number_of_j2s_per_iteration = 68
import random
counter = 0
outstring = ""
for x in range(number_of_itterations):
    for y in range(number_of_j2s_per_iteration):
        random143 = random.choices(splitrep, k=2)
        #print (random143)
        if random143[0] is random143[1]:
            #print ("same")
            counter = counter + 1
    outstring = outstring + str(number_of_j2s_per_iteration)+ "\t" + str(counter)+"\n"
    counter = 0
    if x == 100000:
        print ("100,000")
    if x == 1000000:
        print ("1,000,000")
    if x == 2000000:
        print ("2,000,000")
    if x == 3000000:
        print ("3,000,000")
    if x == 5000000:
        print ("5,000,000")
    if x == 8000000:
        print ("8,000,000")
    if x == 10000000:
        print ("10,000,000")

withmatchedid.write(outstring)
withmatchedid.close()
print ("done")
