from flask import Flask, jsonify
from datetime import datetime
import math

app = Flask(__name__)

@app.route('/info', methods=['GET'])
def days_before_new_year():
    """
    Эндпоинт для получения количества дней до Нового года
    """
    # Получаем текущую дату и время
    current_date = datetime.now()
    
    # Создаем дату следующего Нового года
    next_year = current_date.year + 1
    new_year = datetime(next_year, 1, 1)
    
    # Вычисляем разницу в днях
    days_difference = (new_year - current_date).days
    
    return jsonify({
        "days_before_new_year": days_difference
    })

@app.route('/', methods=['GET'])
def home():
    """
    Главная страница с информацией о доступных эндпоинтах
    """
    return jsonify({
        "message": "API для подсчета дней до Нового года",
        "endpoints": {
            "/info": "GET - получить количество дней до Нового года"
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4200, debug=True)