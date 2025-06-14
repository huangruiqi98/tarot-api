from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy/tarot', methods=['POST'])
def proxy_tarot():
    payload = request.json
    form_data = {
        'api_key': 'RGAjSZiJ58854KUF8o8b08eio',
        'taluo_spreads': payload['spread'],
        'taluo_user_checked': payload['cards'],
        'lang': 'en-us'
    }

    try:
        res = requests.post(
            'https://api.yuanfenju.com/index.php/v1/Zhanbu/taluospreads',
            data=form_data,
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        return jsonify(res.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return '塔罗 API 代理已部署成功'
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render 会自动设置 PORT 变量
    app.run(host='0.0.0.0', port=port)
