reduction = 0

def reduction_prixPanier(panier):
    prixTotal = []
    global reduction
    for prod in panier:
        listQuantite = int(prod.get("quantity"))
        listPrix = prod.get("price")

        totalLigne = float(listPrix) * listQuantite
        prixTotal.append(totalLigne)

    prixTotal = sum(prixTotal)
    if type(prixTotal) != float:
        raise TypeError('Le montant doit être en type float.')
    elif type(prixTotal) < 0:
        raise TypeError('Le montant doit être positif.')
    elif type(listQuantite) < 0:
        raise TypeError('Les quantités doivent être positifs.')
    else:
        if (prixTotal >= 1000):
            prixTotal*80/100
            reduction = prixTotal*20/100
        elif (prixTotal >= 500 and prixTotal < 1000):
            prixTotal * 90 / 100
            reduction = prixTotal*10/100
        elif (prixTotal >= 250 and prixTotal < 500):
            prixTotal * 95 / 100
            reduction = prixTotal*5/100
        else:
            prixTotal
            reduction
        return prixTotal
