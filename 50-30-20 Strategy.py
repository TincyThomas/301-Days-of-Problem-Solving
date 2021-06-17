def fifty_thirty_twenty(ati):
    need = int(ati * (50 / 100))                                                  # percentage needs to be divided by 100 
    want = int(ati * (30 / 100))
    save = int(ati * (20 / 100))

    return {"Needs": need, "Wants": want, "Savings": save}                        # return in dictionary format


print(fifty_thirty_twenty(10000))                                                 # Function calling and printing
