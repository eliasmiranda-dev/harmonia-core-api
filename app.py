from flask import Flask, jsonify

app = Flask(__name__)

NIVEIS = {
    "iniciante": {
        "descricao": "Fundamentos básicos da teoria musical.",
        "modulos": [
            "O que é música",
            "Notas musicais",
            "Ritmo e tempo"
        ]
    },
    "intermediario": {
        "descricao": "Construção e organização musical.",
        "modulos": [
            "Escalas maiores",
            "Escalas menores",
            "Campo harmônico",
            "Formação de acordes"
        ]
    },
    "avancado": {
        "descricao": "Harmonia aplicada e análise musical.",
        "modulos": [
            "Modulação",
            "Empréstimo modal",
            "Rearmonização"
        ]
    }
}
@app.route("/niveis")
def listar_niveis():
    lista = []

    for nome, dados in NIVEIS.items():
        lista.append({
            "nome": nome,
            "descricao": dados["descricao"]
        })

    return jsonify(lista)

@app.route("/niveis/<nivel>")
def detalhar_nivel(nivel):
    if nivel in NIVEIS:
        return jsonify(NIVEIS[nivel])
    else:
        return jsonify({"erro": "Nível não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)