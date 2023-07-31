numberList = [1,2,3,4,5,6,7,8,9,0]
import random

list_of_all_pairs = ["-1","16","66","81","91","17","69","68","78","10","41","64","76","59","75","67","77","79","80","15","56","74","19","31","61","60","71","70","86","95","97","18","46","57","63","73","84","89","96","90"]
number = 10000
hyp = ""
for qq in range(number):

    previous = "-"
    stop = 0
    exists = 0

    for x in range(1,29):
        if stop == 0:
            list_filename = str(x)+"pos"
            listofnames = open(list_filename)
            infile = open(list_filename)
            read = infile.read()
            splitrep = read.split("\n")
            #print (splitrep)
            newlistofweights = [float(i) for i in splitrep]
            #iterativley select motif until we hit a possible pair
            while exists == 0:
                motif = (random.choices(numberList, weights=newlistofweights, k=1))
                #print (str(motif[0]))
                pair = previous + str(motif[0])
                #print (pair)
                previous = str(motif[0])
                if pair in list_of_all_pairs:
                    #print ("exists")
                    exists = 1
                    hyp = hyp + str(str(motif[0]))
            exists = 0    
                

            
            
            
            #print(random.choices(numberList, weights=newlistofweights, k=1))
            if "0" in str(motif[0]):
                stop = 1
                #print ("found zero")
    hyp = hyp + "\n"
#print (hyp)

print ("done")
withmatchedid = open("Simulated_HVDs_"+str(number)+"_.txt", "w")
withmatchedid.write(hyp)
withmatchedid.close()
