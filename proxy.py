from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)

# ✅ 启用跨域，允许所有来源访问（可指定更安全的 origins）
CORS(app)

# 📌 主接口：代理请求塔罗 API
@app.route('/proxy/tarot', methods=['POST'])
def proxy_tarot():
    payload = request.json
    if not payload or 'spread' not in payload or 'cards' not in payload:
        return jsonify({'error': '缺少参数'}), 400

    api_key = 'FsF1CsVevk3N17w7oBkSydfSk'  # ✅ 替换为你的 key（勿公开分享）
    api_url = 'https://api.yuanfenju.com/index.php/v1/Zhanbu/taluospreads'

    form_data = {
        'api_key': 'RGAjSZiJ58854KUF8o8b08eio',
        'taluo_spreads': payload['spread'],
        'taluo_user_checked': payload['cards'],
        'lang': 'en-us'
    }

    try:
        response = requests.post(api_url, data=form_data)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 🧪 测试主页
@app.route('/')
def index():
    return '✅ 塔罗牌代理服务正在运行。'

# 🚀 入口点：用于 Render 部署绑定 0.0.0.0 和 PORT 环境变量
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

