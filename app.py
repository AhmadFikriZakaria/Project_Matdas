from flask import Flask, render_template, request

app = Flask(__name__)

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    panjang = int(request.form['panjang'])
    lebar = int(request.form['lebar'])
    pilihan = request.form['pilihan']

    if pilihan == '1':
        hasil = luas_persegi_panjang(panjang, lebar)
        proses = f'Proses: {panjang} * {lebar} = {hasil}'
    elif pilihan == '2':
        hasil = keliling_persegi_panjang(panjang, lebar)
        proses = f'Proses: 2 * ({panjang} + {lebar}) = {hasil}'
    else:
        luas = luas_persegi_panjang(panjang, lebar)
        keliling = keliling_persegi_panjang(panjang, lebar)
        proses = f'Luas: {panjang} * {lebar} = {luas}, Keliling: 2 * ({panjang} + {lebar}) = {keliling}'
        hasil = f'Luas: {luas}, Keliling: {keliling}'

    return render_template('index.html', hasil=hasil, proses=proses)

if __name__ == '__main__':
    app.run(debug=True)
