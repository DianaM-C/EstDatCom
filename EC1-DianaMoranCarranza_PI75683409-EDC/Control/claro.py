def call(nume, dura, oper): #│ El parámetro número no es utilizado, pero
                            #│ se mantiene porque las indicaciones para
                            #│ elaborar el programa lo solicitan
    dura = round(dura,0)
    if oper == 2:
        cost = dura * 0.6
    else:
        if dura < 1:
            cost = 1.3
        elif dura >= 1 and dura < 5:
            cost = dura * 1.1
        else:
            cost = dura * 0.5
    return cost