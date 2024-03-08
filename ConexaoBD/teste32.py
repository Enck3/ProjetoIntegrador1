import oracledb as cx_Oracle

username = 'BD150224531'
password = 'Cbfhy1'
hostname = '172.16.12.14'
port = '1521'


custo_produto= input("Digite o custo do produto:")

try:
    conn = cx_Oracle.connect(user=username, password=password, host = hostname, port=port)
    print("Conexão estabelecida com sucesso.")

    cur = conn.cursor()
    
    cur.execute("INSERT INTO TBL_PRODUTOS (custo_produto) VALUES (:1)",float()[(custo_produto)])
    
    

    conn.commit()
    print(f"nome produto {nome_produto} inserido com sucesso.")
    conn.commit()
    print(f"descrição produto {descricao_produto} inserido com sucesso.")
    conn.commit()
    print(f"custo produto {custo_produto} inserido com sucesso.")
    conn.commit()
    print(f"custo administrativo {custo_adm} inserido com sucesso.")
    conn.commit()
    print(f"comissao {comissao} inserido com sucesso.")
    conn.commit()
    print(f"impostos {Impostos} inserido com sucesso.")
    conn.commit()
    print(f"rentabilidade {Rentabilidade} inserido com sucesso.")
    conn.commit()
    print(f"nome autor {nome_autor} inserido com sucesso.")
    conn.commit()
    print(f"editora {editora} inserido com sucesso.")
    conn.commit()
    print(f"genero {genero} inserido com sucesso.")
    
    
except cx_Oracle.DatabaseError as e:
    print(f"Erro ao conectar ao Oracle DB: {e}")
finally:
    if 'conn' in locals():
        conn.close()
        print("Conexão fechada.")
