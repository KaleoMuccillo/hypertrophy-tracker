from datetime import datetime

def check_peso(entrada):
    try:
        peso = float(entrada)
    except ValueError:
        return None
    if peso <= 0:
        return None
    return peso

def create_reg(peso):
    data = datetime.now().strftime("%d/%m/%y")
    return {"peso": peso, "data": data}

def show_history(pesos):
    if not pesos:
        print("Nenhum registro encontrado.")
        return
    for i, registro in enumerate(pesos, 1):
        print(f"{registro['data']}: {registro['peso']:.2f} kg")


def create_profile(profile):
    profile["nome"] = input("Digite seu nome: ")
    profile["idade"] = input("Digite sua idade: ")
    profile["sexo"] = input("Digite seu sexo (M/F): ")
    profile["email"] = input("Digite seu email: ")
    profile["telefone"] = input("Digite seu telefone: ")
    profile["altura"] = input("Digite sua altura (em cm): ")
    return profile

def edit_profile(profile):
    print("===== Editar Perfil =====")
    print("Deixe em branco para manter o valor atual.")
    
    nome = input(f"Nome ({profile.get('nome', '')}): ")
    if nome:
        profile["nome"] = nome

    idade = input(f"Idade ({profile.get('idade', '')}): ")
    if idade:
        profile["idade"] = idade

    sx = profile.get('sexo', '').strip().lower()
    if sx.startswith('m'):
        sx = 'Masculino'
    elif sx.startswith('f'):
        sx = 'Feminino'

    sexo = input(f"Sexo ({sx}): ")
    if sexo:
        profile["sexo"] = sexo

    email = input(f"Email ({profile.get('email', '')}): ")
    if email:
        profile["email"] = email

    telefone = input(f"Telefone ({profile.get('telefone', '')}): ")
    if telefone:
        profile["telefone"] = telefone

    altura = input(f"Altura ({profile.get('altura', '')} cm): ")
    if altura:
        profile["altura"] = altura

    return profile

def show_profile(profile):
    if not profile:
        print("Perfil vazio.")
        return
    print("===== Perfil do Usuário =====")
    print(f"Nome: {profile.get('nome', 'N/A')}")
    print(f"Idade: {profile.get('idade', 'N/A')}")
    sx = profile.get('sexo', '').strip().lower()
    if sx.startswith('m'):
        print("Sexo: Masculino")
    elif sx.startswith('f'):
        print("Sexo: Feminino")
    print(f"Email: {profile.get('email', 'N/A')}")
    print(f"Telefone: {profile.get('telefone', 'N/A')}")
    print(f"Altura: {profile.get('altura', 'N/A')} cm")

# ---------- estatisticas
def get_pesos(pesos):
    return [registro["peso"] for registro in pesos]

def prog_last(pesos):
    if len(pesos) < 2:
        print("Não há registros suficientes para calcular a progressão.")
        return
    
    ante = pesos[-2]["peso"]
    atual = pesos[-1]["peso"]
    dif = atual - ante
    
    if dif > 0:
        print(f"Progressão do anterior: +{dif:.2f} kg")
    elif dif < 0:
        print(f"Progressão do anterior: -{dif:.2f} kg")
    else:
        print("Sem progressão em relação ao último registro.")

def prog_first(pesos):
    if len(pesos) < 2:
        print("Não há registros suficientes para calcular a progressão.")
        return
    
    inicial = pesos[0]["peso"]
    atual = pesos[-1]["peso"]
    dif = atual - inicial
    
    if dif > 0:
        print(f"Progressão desde o início: +{dif:.2f} kg")
    elif dif < 0:
        print(f"Progressão desde o início: -{dif:.2f} kg")
    else:
        print("Sem progressão desde o início.")

def show_stats(pesos, profile):
    val = get_pesos(pesos)
    if not val:
        print("Nenhum registro disponível")
        return
    
    inicial = val[0]
    atual = val[-1]
    anterior = val[-2] if len(val) > 1 else None
    media = sum(val) / len(val)
    mini = min(val)
    maxi = max(val)

    print(f"Peso inicial: {inicial:.2f} kg")
    print(f"Peso atual: {atual:.2f} kg")
    if anterior is not None:
        print(f"Peso anterior: {anterior:.2f} kg")
    else:
        print("Não há peso anterior registrado.")
    print(f"Média dos pesos: {media:.2f} kg")
    print(f"Menor peso: {mini:.2f} kg")
    print(f"Maior peso: {maxi:.2f} kg")

    prog_first(pesos)
    prog_last(pesos)

    bmr = estimate_bmr(profile, pesos)
    if bmr is not None:
        print(f"Gasto Calórico estimado em repouso (BMR): {bmr:.2f} kcal/dia")

def estimate_bmr(profile, pesos):
    try:
        age = int(profile.get("idade", 0))
        height = float(profile.get("altura", 0))
        weight = float(pesos[-1].get("peso", 0))
    except ValueError:
        return None

    sex = profile.get("sexo", "").strip().lower()
    if sex.startswith("m"):
        return 10 * weight + 6.25 * height - 5 * age + 5
    return 10 * weight + 6.25 * height - 5 * age - 161