reduction = 0

def reduction_prixPanier(panier):
    prixTotal = []
    global reduction
    for prod in panier: # Kevin Bonga, aide pour la boucle en WEBA
        listQuantite = int(prod.get("quantity"))
        listPrix = prod.get("price")

        if type(listQuantite) == int and type(listPrix) == float:
            totalLigne = float(listPrix) * listQuantite
            prixTotal.append(totalLigne)
        else:
            raise TypeError('La quantité doit être en int, les prix en float.')

    prixTotal = sum(prixTotal)

    if (prixTotal) and (listQuantite) and (listPrix) < 0:
        raise TypeError('Le montant doit être positif.')
    else:
        if (prixTotal >= 1000):
            prixTotal=prixTotal*80/100
            reduction = prixTotal*20/100
        elif (prixTotal >= 500 and prixTotal < 1000):
            prixTotal=prixTotal * 90 / 100
            reduction = prixTotal*10/100
        elif (prixTotal >= 250 and prixTotal < 500):
            prixTotal=prixTotal * 95 / 100
            reduction = prixTotal*5/100
        else:
            prixTotal
            reduction
        return prixTotal
