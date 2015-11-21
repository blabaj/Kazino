skritoStevilo = 8
vnos = 0
konec = False
nadaljevanje = True
budget = int(raw_input("Vnesi koliko denarja zels porabiti. Za vsako igro je avtomat pobere 1\xe2\x82\xac: "))
while budget != 0 and konec != True:
    while (vnos != skritoStevilo and konec != True):
        budget = budget - 1
        vnos = int(raw_input("Vnesi skrito stevilo: "))
        if vnos == skritoStevilo:
            print ("Cestitke zadeli ste 20\xe2\x82\xac!")
            konec = True
            break
        elif vnos != skritoStevilo:
            print "Ni bilo zadetka"

        while nadaljevanje == True:
                if (budget > 0):
                    print "Imate se " + str(budget) + "\xe2\x82\xac"
                    nadaljuje = str(raw_input("Zelite nadaljevati (Da/Ne): ")).upper()
                    if nadaljuje == "NE":
                        print ("Vracamo vam preostanek denarja - " + str(budget) + "\xe2\x82\xac")
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

                print "Napacen ukaz! Ali zelis nadaljevati (Da/Ne)"