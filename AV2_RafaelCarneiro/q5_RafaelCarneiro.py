import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(16)
iv = get_random_bytes(16)

encrypted_passwords = []
usernames = []

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

def authenticate_user(password, key, iv, stored_password):
    decipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_input_password = encrypt_password(password, key, iv)

    decrypted_stored_password = decipher.decrypt(stored_password)
    unpadded_stored_password = unpad(decrypted_stored_password, 16)

    return encrypted_input_password == unpadded_stored_password

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

    str_Choice = input("Confirm or Cancel the Transaction type ('Confirm' or 'Cancel'): ")

    return choices_from_user(str_Choice)

create_transaction = lambda x : cash_Transaction(user_Fund) if x == "Cash" else (
    fund_Transfer(user_Fund, user_name) if x == "Fund Transfer" else (
    credit(user_Fund, user_name) if x == "Credit" else "Incorrect Value"))

def transaction_type():
    t_t = input("Enter transaction type (Cash, Fund Transfer, Credit): ")

    return t_t

print("Creating Transaction...!\n")

user_name = input("Please write down below your Username: ")
user_pssw = input("Please write down below your Password: ")

encrypted_password = encrypt_password(user_pssw, key, iv)
store_encrypted_password(user_name, encrypted_password)

user_name_Logado = "UserLog"
user_pssw_Logado = "123456"

user_Fund = round(random.uniform(1, 5000), 2)

result = authenticate_user(user_pssw, key, iv, encrypted_passwords[0][1])
print(result)

runIt_ = lambda result: create_transaction(transaction_type()) if result == True else "Login failed. \n Try Again..."

result2= runIt_(result)
print(result2)
