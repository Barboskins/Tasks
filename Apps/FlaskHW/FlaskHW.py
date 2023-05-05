"""1. Если вы еще не установили Flask, сделайте это сейчас. Это также установит werkzeug, jinja2 и, возможно,
другие пакеты.
2. Создайте скелет сайта с помощью веб-сервера Flask. Убедитесь, что сервер начинает свою работу по адресу Localhost
на стандартном порте 5000. Если ваш компьютер уже использует порт 5000 для чего-то еще, воспользуйтесь другим портом.
3. Добавьте функцию home() для обработки запросов к домашней странице. Пусть она возвращает строку It's alive!.
4. Создайте шаблон для jinja2, который называется home.html и содержит следующий контент:
<html>
<head>
<title>It's alive!</title>
<body>
I'm of course referring to {{thing}}, which is {{height}} feet tall and {{color}}.
</body>
</html>
5. Модифицируйте функцию home() вашего сервера, чтобы она использовала шаблон home.html. Передайте ей три
параметра для команды GET: thing, height и color."""

from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def start():
    return "It's alive!"
@app.route('/home')
def home():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['height'] = request.args.get('height')
    kwargs['color'] = request.args.get('color')
    return render_template('home.html', **kwargs)


app.run(port=5000, debug=True)