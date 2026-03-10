def is_pari(n):
    """Ritorna Vero se n è pari, Ritorna Falso se non lo è """
    
    risultato = False

    if n%2 == 0 :
        risultato = True 

    return risultato


"""
potevo fare risultato = True
            if n%2 != 0
            risultato False
"""
#########
main():
    numero = int(input("Dammi un numero: "))

    #print(type(numero))

    result = is_pari(numero)

    print(result)

main()

