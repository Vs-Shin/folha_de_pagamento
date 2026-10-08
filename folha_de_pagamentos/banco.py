import sqlite3

def conectar():
    return sqlite3.connect("folha_de_pagamentos.db")

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS servidores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cargo TEXT NOT NULL,
            salario_base REAL NOT NULL,
            anos_servico INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def salvar_servidor(nome, cargo, salario_base, anos_servico):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO servidores (nome, cargo, salario_base, anos_servico)
        VALUES (?, ?, ?, ?)
    """, (nome, cargo, salario_base, anos_servico))
    conn.commit()
    conn.close()

def listar_servidores():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, cargo, salario_base, anos_servico FROM servidores")
    servidores = cursor.fetchall()
    conn.close()
    return servidores

def atualizar_servidor(id_servidor, novo_cargo, novo_salario, novos_anos):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE servidores
        SET cargo = ?, salario_base = ?, anos_servico = ?
        WHERE id = ?
    """, (novo_cargo, novo_salario, novos_anos, id_servidor))
    conn.commit()
    linhas_afetadas = cursor.rowcount
    conn.close()
    return linhas_afetadas > 0

def deletar_servidor(id_servidor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM servidores WHERE id = ?", (id_servidor,))
    conn.commit()
    linhas_afetadas = cursor.rowcount
    conn.close()
    return linhas_afetadas > 0
