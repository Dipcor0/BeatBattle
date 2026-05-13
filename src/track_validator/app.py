from flask import Flask, request, jsonify

app = Flask(__name__)

# Список запрещённых слов (на английском)
BAD_WORDS = ["badword", "spam", "advertisement", "ad", "promo", "hate", "violence", "curse", "swear", "explicit"]


@app.route('/validate', methods=['POST'])
def validate():
    """Проверяет название трека на цензуру"""
    data = request.get_json()

    if not data or 'track_name' not in data:
        return jsonify({"valid": False, "reason": "No track name provided"}), 400

    track_name = data['track_name'].lower()

    for bad_word in BAD_WORDS:
        if bad_word in track_name:
            return jsonify({
                "valid": False,
                "reason": f"Track name contains forbidden word: '{bad_word}'"
            })

    return jsonify({"valid": True, "reason": ""})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)