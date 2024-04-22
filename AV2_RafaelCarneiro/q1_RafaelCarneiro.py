import random

def cash_Transaction(user_Fund):
    print("Receive Cash")

    user_Fund += float(input("Digite a quantia desejada: "))
    str(user_Fund)
    print("\n\n\n\n\n\nPrinting Payment Receipt: " + "%.2f" % user_Fund)

    return("Transaction Completed")

def fund_Transfer(user_Fund, user_name):
    choices_from_user = lambda x : "Transaction Completed" if x == "Confirm" else "Close Transaction"
    print("----------------------------------------------")
    print("Provide Bank Deposit Details: " + "\nUsername: " + user_name + " // Credits:%.2f" % user_Fund)
    print("----------------------------------------------")

    str_Choice = lambda: input("Confirm or Cancel the Transaction type ('Confirm' or 'Cancel'): ")

    return choices_from_user(str_Choice())

def credit(user_Fund, user_name):
    choices_from_user = lambda x : "Transaction Completed" if x == "Confirm" else "Close Transaction"

    print("Request Credit Account Details")
    print("----------------------------------------------")
    print("Provide Credit Account Details: " + "\nUsername: " + user_name + " // Credits: %.2f" % user_Fund)
    print("----------------------------------------------")

    str_Choice = lambda: input("Confirm or Cancel the Transaction type ('Confirm' or 'Cancel'): ")

    return choices_from_user(str_Choice())

create_transaction = lambda x : cash_Transaction(user_Fund()) if x == "Cash" else (
    fund_Transfer(user_Fund(), datas[0]) if x == "Fund Transfer" else (
    credit(user_Fund(), datas[0]) if x == "Credit" else "Incorrect Value"))

print("Creating Transaction...!\n")

user_name = input("Please write down below your Username: ")
user_pssw = input("Please write down below your Password: ")

datas[0] = user_name()
datas[1] = user_pssw()

user_name_Logado = lambda: "UserLog"
user_pssw_Logado = lambda: "PassLog"

user_Fund = round(random.uniform(1, 5000), 2)

transaction_type = lambda: input("Enter transaction type (Cash, Fund Transfer, Credit): ")

result = lambda: create_transaction(transaction_type())
print(result())
