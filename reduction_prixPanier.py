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
        reduction = 0
    return prixTotal
