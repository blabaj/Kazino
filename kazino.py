# -*- coding: utf-8 -*-
skritoStevilo = 8
vnos = 0
konec = False
nadaljevanje = True
budget = int(raw_input("Vnesi koliko denarja želš porabiti. Za vsako igro avtomat pobere 1\xe2\x82\xac: "))
while budget != 0 and konec != True:
    while (vnos != skritoStevilo and konec != True):
        budget = budget - 1
        vnos = int(raw_input("Vnesi skrito število: "))
        if vnos == skritoStevilo:
            print ("Čestitke zadeli ste 20\xe2\x82\xac!")
            konec = True
            break
        elif vnos != skritoStevilo:
            print "Ni bilo zadetka"

        while nadaljevanje == True:
                if (budget > 0):
                    print "Imate še " + str(budget) + "\xe2\x82\xac"
                    nadaljuje = str(raw_input("Želite nadaljevati (Da/Ne): ")).upper()
                    if nadaljuje == "NE":
                        print ("Vračamo vam preostanek denarja: " + str(budget) + "\xe2\x82\xac")
                        print ("Nasvidenje")
                        nadaljevanje = False
                        konec = True
                        break
                    elif nadaljuje == "DA":
                        break

                elif budget == 0:
                    print "Porabili ste denar! Lep dan se naprej!"
                    nadaljevanje = False
                    konec = True
                    break

                print "Napačen ukaz! Ali želiš nadaljevati (Da/Ne)"
