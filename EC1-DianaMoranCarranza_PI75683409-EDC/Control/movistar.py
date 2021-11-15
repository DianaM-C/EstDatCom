def call(nume, dura, oper): #│ El parámetro número no es utilizado, pero
                            #│ se mantiene porque las indicaciones para
                            #│ elaborar el programa lo solicitan
    dura = round(dura,0)
    if oper == 1:
        cost = dura * 0.5
    else:
        if dura < 1:
            cost = 1.2
        elif dura >= 1 and dura < 5:
            cost = dura
        else:
            cost = dura * 0.8
    return cost