Transaction_Dataset = [["Sambhar", "Rice"], ["Sambhar", "Pasta"], ["Mayo", "Burger", "Cream"], ["Sambhar", "Rice"], ["Burger", "Chips"],
                       ["Sambhar", "Rice","Pasta","Chips"],["Burger", "Cream","Sambhar", "Rice"], ["Rice","Burger", "Cream"], ["Pasta","Burger", "Chips","Sambhar", "Rice"]]

items_purchased = ["Sambhar", "Rice","Pasta"]
supp = 2
item_list = set ()
Dict = {}

for trans in Transaction_Dataset:
    for prod in trans:
        item_list.add(prod)
        Dict[prod]=0

item_list = list(item_list)
for items in items_purchased:
    item_list.remove(items)

for products in item_list:
    for trans in Transaction_Dataset:
        Valid = True
        for items in items_purchased:
            if items not in trans:
                Valid = False
        if Valid:
            if products in trans:
                Dict[products]+=1

for product, freq in Dict.items():
    if freq >= supp:
        print("For combination of",items_purchased,product,"was also purchased")
