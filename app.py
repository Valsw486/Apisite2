from flask import Flask, render_template
import requests

app = Flask(__name__)  # исправлено с Flask(name)

# URL API для случайной цитаты
QUOTE_API_URL = 'https://api.quotable.io/random'

@app.route('/')
def index():
    try:
        # отключаем проверку SSL для обхода ошибки сертификата (только для разработки)
        response = requests.get(QUOTE_API_URL, timeout=5, verify=False)
        # Проверяем успешность запроса
        if response.status_code == 200:
            data = response.json()
            quote = data.get('content', 'Цитата не найдена')
            author = data.get('author', 'Неизвестен')
        else:
            print(f"Ошибка: получен статус {response.status_code}")
            quote = 'Не удалось получить цитату. Попробуйте позже.'
            author = ''
    except requests.RequestException as e:
        print(f"Исключение при запросе: {e}")
        quote = 'Не удалось получить цитату. Попробуйте позже.'
        author = ''
    return render_template('index.html', quote=quote, author=author)

if __name__ == '__main__':  # исправлено на правильное условие
    app.run(debug=True)