import dbm.dumb

def init_db():
    db= dbm.open('Banco', 'c',)

# Adicionar registro

def Create(user: str, email: str):
    "Adiciona um novo registro"
    db= dbm.open('Banco', 'w',)
    if user in db:
        return f"User existente"
    else: 
        db[user] = email
        return f"User criado com sucesso"

# Consultar registro
def Read(user: str):
    "Consulta um registro"
    db= dbm.open('Banco', 'r',)
    if user in db:
        return f"User: {user}\n E-mail:{db[user].decode()}"
    else: 
        return f"User não cadastrado"

# Atualizar registro
def Update(user: str, email: str):
    "Alterar um registro"
    db= dbm.open('Banco', 'w',)
    if user in db:
        db[user] = email
        return f"User atualizado"
    else: 
        return f"User não cadastrado"

# Deletar Registro
def Delete(user: str):
    "Apagar registro"
    db= dbm.open('Banco', 'w',)
    if user in db:
        del db[user] 
        return f"User deletado"
    else: 
        return f"User não cadastrado"