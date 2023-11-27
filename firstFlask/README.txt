1. python -m venv myvenv
2. myvenv\Scripts\activate
3. pip install flask
4. python -c "import flask; print(flask.__version__)" - выведет версию flask

5. создаем app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", h1 = "Главная страница")


@app.route("/about")
def get_page_about():
    return render_template("about.html", h1 = "О приложении")

if __name__ == "__main__":
    app.run(debug=True)

7. cоздаем папку static и templates
8. в templates создаем шаблоны страниц: base.html index.html about.html
6. python app.py - запуск сервера
7. просмотр в браузере веб-приложения
http://127.0.0.1:5000/
http://127.0.0.1:5000/about
8. создаем static для статичных файлов, например, css для style.css