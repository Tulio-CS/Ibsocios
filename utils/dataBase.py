import sqlite3

class Database:
    def __init__(self, db_name="frota.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Cria todas as tabelas do banco de dados."""
        self.cursor.executescript("""
            CREATE TABLE IF NOT EXISTS motoristas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cnh TEXT UNIQUE NOT NULL
            );

            CREATE TABLE IF NOT EXISTS fornecedores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                contato TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS veiculos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                placa TEXT UNIQUE NOT NULL,
                modelo TEXT NOT NULL,
                ano INTEGER NOT NULL,
                motorista_id INTEGER,
                FOREIGN KEY (motorista_id) REFERENCES motoristas(id)
            );

            CREATE TABLE IF NOT EXISTS estoque (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                fornecedor_id INTEGER,
                FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
            );

            CREATE TABLE IF NOT EXISTS categorias_servico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS abastecimentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                veiculo_id INTEGER,
                litros REAL NOT NULL,
                valor_total REAL NOT NULL,
                data TEXT NOT NULL,
                FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
            );

            CREATE TABLE IF NOT EXISTS multas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                veiculo_id INTEGER,
                descricao TEXT NOT NULL,
                valor REAL NOT NULL,
                data TEXT NOT NULL,
                FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
            );

            CREATE TABLE IF NOT EXISTS contratos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fornecedor_id INTEGER,
                descricao TEXT NOT NULL,
                data_inicio TEXT NOT NULL,
                data_fim TEXT NOT NULL,
                FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
            );
        """)
        self.conn.commit()

    def execute(self, query, params=()):
        """Executa uma consulta SQL com parâmetros."""
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self, query, params=()):
        """Executa uma consulta SQL e retorna todos os resultados."""
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        """Fecha a conexão com o banco de dados."""
        self.conn.close()

# ==============================
# 🔹 CLASSES DOS OBJETOS
# ==============================

class Motorista:
    def __init__(self, db, nome, cnh):
        self.db = db
        self.nome = nome
        self.cnh = cnh

    def adicionar(self):
        self.db.execute("INSERT INTO motoristas (nome, cnh) VALUES (?, ?)", (self.nome, self.cnh))

    @staticmethod
    def listar(db):
        return db.fetchall("SELECT * FROM motoristas")

class Veiculo:
    def __init__(self, db, placa, modelo, ano, motorista_id=None):
        self.db = db
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.motorista_id = motorista_id

    def adicionar(self):
        self.db.execute("INSERT INTO veiculos (placa, modelo, ano, motorista_id) VALUES (?, ?, ?, ?)",
                        (self.placa, self.modelo, self.ano, self.motorista_id))

    @staticmethod
    def listar(db):
        return db.fetchall("SELECT * FROM veiculos")

    @staticmethod
    def remover(db, id_veiculo):
        db.execute("DELETE FROM veiculos WHERE id = ?", (id_veiculo,))

    @staticmethod
    def atualizar_motorista(db, id_veiculo, novo_motorista_id):
        db.execute("UPDATE veiculos SET motorista_id = ? WHERE id = ?", (novo_motorista_id, id_veiculo))

class Estoque:
    def __init__(self, db, nome, quantidade, fornecedor_id):
        self.db = db
        self.nome = nome
        self.quantidade = quantidade
        self.fornecedor_id = fornecedor_id

    def adicionar(self):
        self.db.execute("INSERT INTO estoque (nome, quantidade, fornecedor_id) VALUES (?, ?, ?)",
                        (self.nome, self.quantidade, self.fornecedor_id))

    @staticmethod
    def listar(db):
        return db.fetchall("SELECT * FROM estoque")

    @staticmethod
    def atualizar_quantidade(db, id_item, nova_quantidade):
        db.execute("UPDATE estoque SET quantidade = ? WHERE id = ?", (nova_quantidade, id_item))

class Multa:
    def __init__(self, db, veiculo_id, descricao, valor, data):
        self.db = db
        self.veiculo_id = veiculo_id
        self.descricao = descricao
        self.valor = valor
        self.data = data

    def adicionar(self):
        self.db.execute("INSERT INTO multas (veiculo_id, descricao, valor, data) VALUES (?, ?, ?, ?)",
                        (self.veiculo_id, self.descricao, self.valor, self.data))

    @staticmethod
    def listar(db):
        return db.fetchall("SELECT * FROM multas")

    @staticmethod
    def remover(db, id_multa):
        db.execute("DELETE FROM multas WHERE id = ?", (id_multa,))



if __name__ == "__main__":
    db = Database()

    # Criando objetos
    motorista1 = Motorista(db, "João Silva", "1234567890")
    motorista1.adicionar()

    veiculo1 = Veiculo(db, "ABC-1234", "Fiat Uno", 2015, motorista_id=1)
    veiculo1.adicionar()

    estoque1 = Estoque(db, "Óleo de Motor", 10, fornecedor_id=1)
    estoque1.adicionar()

    multa1 = Multa(db, 1, "Excesso de velocidade", 150.00, "2024-02-15")
    multa1.adicionar()

    # Listando os dados
    print("Motoristas:", Motorista.listar(db))
    print("Veículos:", Veiculo.listar(db))
    print("Estoque:", Estoque.listar(db))
    print("Multas:", Multa.listar(db))

    # Atualizando um motorista de um veículo
    Veiculo.atualizar_motorista(db, 1, 2)

    # Atualizando o estoque
    Estoque.atualizar_quantidade(db, 1, 15)

    # Removendo um veículo
    Veiculo.remover(db, 1)

    # Removendo uma multa
    Multa.remover(db, 1)

    db.close()
