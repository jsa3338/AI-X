# Flask 기본 구조 만들기

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template/index.html')

@app.route('/predict', methods=['POST'])
def predict():
    crop = request.form.get('crop')
    # 예측 로직 (임시로 고정값)
    prediction = f"{crop}의 예측 가격은 1000원입니다."
    return render_template('template/result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
