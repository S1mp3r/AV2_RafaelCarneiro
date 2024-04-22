import mysql.connector

db_connect = lambda host, user, password, database: mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

host = lambda: ""
user = lambda: ""
password = lambda: ""
database = lambda: ""

mydb = db_connect(host(), user(), password(), database())

#=================================================================================================================================================

create_table = lambda cursor, table_name, columns: cursor.execute(f"CREATE TABLE {table_name} ({', '.join(f'{col} {data_type}' for col, data_type in columns.items())})")

#=================================================================================================================================================

# Exemplo de uso:
# Vamos gerar comando INSERT para inserir dados na tabela USERS
# insert_user_columns = ["name", "country", "id_console"]
# insert_user_values = ["John", "USA", "1"]

# Gerar comando INSERT para inserir dados na tabela USERS
# insert_user_query = gen_insert_query("USERS", insert_user_columns, insert_user_values)

gen_insert_query = lambda table_name, columns, values: (
    f"INSERT INTO {table_name} ({', '.join(columns)}) " +
    f"VALUES ({', '.join('%s' for _ in values)})"
)

#=================================================================================================================================================

# Exemplo de uso:
# Vamos gerar comando DELETE para deletar dados da tabela USERS
# delete_user_condition = "id = '1'"

# Gerar comando DELETE para deletar dados da tabela USERS
# delete_user_query = gen_delete_query("USERS", delete_user_condition)

gen_delete_query = lambda table_name, condition: (
    f"DELETE FROM {table_name} WHERE {condition}"
)

#=================================================================================================================================================

# Exemplo de uso:
# Vamos gerar comando SELECT para obter dados da tabela USERS
# user_attributes = ["id", "name", "country"]
# user_alias = "u"

# # Gerar comando SELECT para obter dados da tabela USERS
# select_users_query = gen_select_query("USERS", user_alias, user_attributes)

gen_select_query = lambda table_name, table_alias, attributes: (
    f"SELECT {', '.join(f'{table_alias}.{attr}' for attr in attributes)} " +
    f"FROM {table_name} {table_alias}"
)

#=================================================================================================================================================

mycursor = mydb.cursor()

try:
    tables = lambda: {
        "USERS": {
            "id": "INT AUTO_INCREMENT PRIMARY KEY",
            "name": "VARCHAR(255)",
            "country": "VARCHAR(255)",
            "id_console": "VARCHAR(255)"
        },
        "VIDEOGAMES": {
            "id_console": "INT AUTO_INCREMENT PRIMARY KEY",
            "name": "VARCHAR(255)",
            "id_company": "VARCHAR(255)",
            "release_date": "DATE"
        },
        "GAMES": {
            "id_game": "INT AUTO_INCREMENT PRIMARY KEY",
            "title": "VARCHAR(255)",
            "genre": "VARCHAR(255)",
            "release_date": "DATE",
            "id_console": "INT",
            "FOREIGN KEY (id_console)": "REFERENCES VIDEOGAMES(id_console)"
        },
        "COMPANY": {
            "id_company": "INT AUTO_INCREMENT PRIMARY KEY",
            "name": "VARCHAR(255)",
            "country": "VARCHAR(255)"
        }
    }

    create_tables_lambda = lambda cursor, tables: [create_table(cursor, table_name, columns) for table_name, columns in tables.items()]

    create_tables_lambda(mycursor, tables())

#=================================================================================================================================================

    # Consulta SELECT para obter todos os dados da tabela USERS
    select_all_users_query = gen_select_query("USERS", "u", ["id", "name", "country", "id_console"])
    print("Consulta SELECT para todos os dados da tabela USERS:")
    print(select_all_users_query())

#=================================================================================================================================================

    # Dados para inserir na tabela USERS
    new_user_data = lambda: {"name": "Alice", "country": "Canada", "id_console": "2"}

    # Consulta INSERT para inserir novos dados na tabela USERS
    insert_user_query = lambda: gen_insert_query("USERS", list(new_user_data().keys()), list(new_user_data().values()))
    print("Consulta INSERT para inserir dados na tabela USERS:")
    print(insert_user_query())

#=================================================================================================================================================

    # Condição para deletar um registro da tabela USERS
    delete_user_condition = lambda: "id = '2'"  # Supondo que queremos deletar o usuário com id = 2

    # Consulta DELETE para deletar dados da tabela USERS com a condição especificada
    delete_user_query = lambda: gen_delete_query("USERS", delete_user_condition())
    print("Consulta DELETE para deletar dados da tabela USERS:")
    print(delete_user_query())

#=================================================================================================================================================

    mydb.commit()
finally:
    mydb.close()
