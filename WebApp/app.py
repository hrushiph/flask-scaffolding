from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/', methods=["POST","GET"])
def home():
    return render_template('index.html', random_data='random_data')

def getPrediction():
    print('Prediction analysis.')

@app.route('/getPrediction', methods=["GET","POST"])
def getPrediction():
    request_data = request.form.get('feedback')
    print(request_data)
    # ML Code
    
    data_decision = True   
    return render_template('result.html', data_decision=data_decision)                     

if __name__ == "__main__":
    app.run()