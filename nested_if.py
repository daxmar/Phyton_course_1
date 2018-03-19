wage = 1000
family = True
own_house = True

if wage > 1500:
    print "wage is above standart"
    if family:
        print "Must have insurrance to future retire"
    else:
        print "Must not have inssurance"

    if own_house:
        print "Pay the House Tax"
    else:
        print "not Pay the house tax"
else:
    print "wage is bellow standart"
