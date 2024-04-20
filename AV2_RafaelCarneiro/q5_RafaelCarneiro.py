import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(16)
iv = get_random_bytes(16)

def encrypt_password(password, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Converter a senha em bytes e preencher para um múltiplo de 16 bytes
    password_bytes = password.encode()
    padded_password = pad(password_bytes, 16)
    # Criptografar a senha
    encrypted_password = cipher.encrypt(padded_password)
    return encrypted_password

def decrypt_password(encrypted_password, key, iv):
    decipher = AES.new(key, AES.MODE_CBC, iv)
    # Descriptografar a senha
    decrypted_password = decipher.decrypt(encrypted_password)
    # Remover o preenchimento
    unpadded_password = unpad(decrypted_password, 16)
    # Decodificar de volta para uma string
    return unpadded_password.decode()

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

user_name_Logado = "UserLog"
user_pssw_Logado = "123456"

user_Fund = round(random.uniform(1, 5000), 2)

authenticate_lambda = lambda username, password: (
    lambda key, iv, user_name_Logado, user_pssw_Logado: "Login successful!"
    if username == user_name_Logado and AES.new(key, AES.MODE_CBC, iv).encrypt(pad(password.encode(), 16)) == user_pssw_Logado
    else "Login failed."
)(key, iv, user_name_Logado, user_pssw_Logado)

result = authenticate_lambda(user_name, user_pssw)
print(result)

runIt_ = lambda result: create_transaction(transaction_type()) if result == "Login successful!" else "Login failed. \n Try Again..."

result2(runIt_(result))
print(result2)
