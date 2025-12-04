from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sozluk")
def sozluk():
    baslik =  "Sözlüğe hoşgeldiniz..!"
    sozluk= {
        "data1": "Open Resource Portal",
        "data2": "Open Education Portal"
    }
    return render_template("sozluk.html", data1=baslik, data2=sozluk, )

@app.route("/cv")
def ozgecmis():
    return render_template("cv.html")

@app.route('/eposta/<username>')
def show_user_profile(username):
    sozluk2= {
        "orcunmadran": "Orçun Madran - omadran@hacettepe.edu.tr",
        "hulusikentmen": "Hulusi Kentmen - hulusi@hacettepe.edu.tr"
    }
    goster = sozluk2.get(username, "User not found")
    return f'<b>Kullanıcı e-posta bilgileri:</b>  {goster}'

if __name__ == "__main__":
    app.run(debug=True)