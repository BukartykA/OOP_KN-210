from flask import Flask
from jikanpy import Jikan

jikan = Jikan()
app = Flask(__name__)

# Отримуємо дані про аніме (наприклад, "Frieren")
j = jikan.anime(54595, extension='episodes')

@app.route('/')
def home():
    content = "<h1>Список епізодів:</h1>"
    for episode in j["data"]: 
        content += f"<p>Епізод {episode['mal_id']}: {episode['title']} — Оцінка: {episode['score']}</p>"
    return content

if __name__ == '__main__':
    app.run(debug=True)