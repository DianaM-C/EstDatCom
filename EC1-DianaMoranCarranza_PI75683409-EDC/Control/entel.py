def call(nume, dura, oper): #│ El parámetro número no es utilizado, pero
                            #│ se mantiene porque las indicaciones para
                            #│ elaborar el programa lo solicitan
    dura = round(dura,0)
    if oper == 3:
        cost = dura * 0.45
    else:
        if dura < 1:
            cost = 1
        elif dura >= 1 and dura < 5:
            cost = dura * 1.3
        else:
            cost = dura * 0.6
    return cost