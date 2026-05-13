from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)


@app.route('/notify', methods=['POST'])
def notify():
    """Принимает уведомление об изменении рейтинга"""
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "Нет данных"}), 400

    track_id = data.get('track_id')
    new_rating = data.get('new_rating')
    old_rating = data.get('old_rating', 0)

    # Выводим в консоль (будет видно в docker logs)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] УВЕДОМЛЕНИЕ: Трек {track_id} | Рейтинг: {old_rating} → {new_rating}")

    return jsonify({
        "status": "ok",
        "message": "Уведомление получено",
        "timestamp": timestamp
    }), 200


@app.route('/health', methods=['GET'])
def health():
    """Проверка работоспособности"""
    return jsonify({"status": "ok", "service": "rating_notifier"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)