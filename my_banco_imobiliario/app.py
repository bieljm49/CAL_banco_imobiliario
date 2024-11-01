from flask import Flask, render_template, request, redirect, url_for, session

#import os
#port = int(os.environ.get("PORT", 5000))
#app.run(host='0.0.0.0', port=port)

app = Flask(__name__)
app.secret_key = 'secreta123'  # chave de segurança da sessão

# Dados iniciais
jogadores = {
    'jogador1': {'saldo': 1500, 'historico': []},
    'jogador2': {'saldo': 1500, 'historico': []},
    'jogador3': {'saldo': 1500, 'historico': []},
    'jogador4': {'saldo': 1500, 'historico': []},
}

# Rota para cada jogador
@app.route('/<jogador>', methods=['GET', 'POST'])
def player(jogador):
    if jogador not in jogadores:
        return redirect(url_for('player', jogador='jogador1'))
    
    if request.method == 'POST':
        # Pega valor da transação e atualiza saldo
        valor = int(request.form.get('valor'))
        tipo = request.form.get('tipo')
        if tipo == 'adicionar':
            jogadores[jogador]['saldo'] += valor
        elif tipo == 'subtrair':
            jogadores[jogador]['saldo'] -= valor
        
        # Armazena no histórico
        jogadores[jogador]['historico'].append(f"{tipo.capitalize()} {valor}")
        
    return render_template(f"{jogador}.html", jogador=jogador, data=jogadores[jogador])

if __name__ == '__main__':
    app.run(debug=True)
