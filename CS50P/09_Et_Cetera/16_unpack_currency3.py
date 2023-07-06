def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts


coins = {"galleons":100, "sickles":50, "knuts":25}

# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
# to unpack dictionarys use --> **coins
print(total(**coins), "Knuts")