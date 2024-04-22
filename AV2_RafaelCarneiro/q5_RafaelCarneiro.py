import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(16)
iv = get_random_bytes(16)

encrypted_passwords = []
usernames = []
store_data = []
results = []

def encrypt_password(password, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)

    password_bytes = password.encode()
    padded_password = pad(password_bytes, 16)

    encrypted_password = cipher.encrypt(padded_password)
    return encrypted_password

def decrypt_password(encrypted_password, key, iv):
    decipher = AES.new(key, AES.MODE_CBC, iv)

    decrypted_password = decipher.decrypt(encrypted_password)

    unpadded_password = unpad(decrypted_password, 16)

    return unpadded_password.decode()

def authenticate_user(password, key, iv, stored_encrypted_password):
    decipher = AES.new(key, AES.MODE_CBC, iv)

    decrypted_stored_password = decipher.decrypt(stored_encrypted_password)
    unpadded_stored_password = unpad(decrypted_stored_password, 16)

    input_password_bytes = password.encode()
    padded_input_password = pad(input_password_bytes, 16)

    return padded_input_password == unpadded_stored_password

def store_encrypted_password(username, encrypted_password):
    encrypted_passwords.append((username, encrypted_password))

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

    str_Choice = input("Confirm or Cancel the Transaction type ('Confirm' or 'Cancel'): ")

    return choices_from_user(str_Choice)

def credit(user_Fund, user_name):
    choices_from_user = lambda x : "Transaction Completed" if x == "Confirm" else "Close Transaction"

    print("Request Credit Account Details")
    print("----------------------------------------------")
    print("Provide Credit Account Details: " + "\nUsername: " + user_name + " // Credits: %.2f" % user_Fund)
    print("----------------------------------------------")

    str_Choice = lambda : input("Confirm or Cancel the Transaction type ('Confirm' or 'Cancel'): ")

    return choices_from_user(str_Choice())

create_transaction = lambda x : cash_Transaction(user_Fund) if x == "Cash" else (
    fund_Transfer(user_Fund, store_data[0]) if x == "Fund Transfer" else (
    credit(user_Fund, store_data[0]) if x == "Credit" else "Incorrect Value"))

def transaction_type():
    t_t = input("Enter transaction type (Cash, Fund Transfer, Credit): ")

    return t_t

print("Creating Transaction...!\n")

user_name = lambda : input("Please write down below your Username: ")
user_pssw = lambda : input("Please write down below your Password: ")

store_data[0] = user_name()
store_data[1] = user_pssw()

encrypted_password = encrypt_password(store_data[1], key, iv)
store_encrypted_password(store_data[0], encrypted_password)

user_name_Logado = lambda : "UserLog"
user_pssw_Logado = lambda : "123456"

user_Fund = round(random.uniform(1, 5000), 2)

result = lambda: authenticate_user(user_pssw_Logado(), key, iv, encrypted_passwords[0][1])

results[0] = result()

print(results[0])


runIt_ = lambda result: create_transaction(transaction_type()) if result == True else "Login failed. \n Try Again..."

result2 = lambda : runIt_(results[0])
print(result2())
