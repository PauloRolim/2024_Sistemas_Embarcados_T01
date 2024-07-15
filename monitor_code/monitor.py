import RPi.GPIO as GPIO
import time
from flask import Flask, jsonify, render_template, request
import threading

# Configurações do GPIO
GPIO.setmode(GPIO.BCM)
SIGNAL_PIN = 17
LED_PIN = 27  # pino para controle da I1
LED_PIN22 = 22 # pino para controle da I2
GPIO.setup(SIGNAL_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN22, GPIO.OUT)

# Função para ler o sinal da placa
def read_signal():
    return GPIO.input(SIGNAL_PIN)

app = Flask(__name__)

# Variável global para armazenar o valor do sinal
signal_value = 0

def update_signal():
    global signal_value
    while True:
        signal_value = read_signal()
        time.sleep(1)  # Atualiza a cada segundo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signal')
def get_signal():
    return jsonify({'signal': signal_value})

@app.route('/led', methods=['POST'])
def control_led():
    data = request.json
    if data['state'] == 'on':
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
    return jsonify({'status': 'success'})

@app.route('/led2', methods=['POST'])
def control_i2():
    data = request.json
    if data['state'] == 'on':
        GPIO.output(LED_PIN22, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN22, GPIO.LOW)
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    # Iniciar o thread de atualização do sinal
    signal_thread = threading.Thread(target=update_signal)
    signal_thread.start()

    # Iniciar o servidor Flask
    app.run(host='0.0.0.0', port=5000)
