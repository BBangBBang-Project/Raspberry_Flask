from flask import Flask, request

import RPi.GPIO as GPIO

import time



app = Flask(__name__)



GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18, 50)

pwm.start(0)



def set_angle(angle):
	duty = angle / 18 + 2

    GPIO.output(18, True)

    pwm.ChangeDutyCycle(duty)

    time.sleep(1)

    GPIO.output(18, False)

    pwm.ChangeDutyCycle(0)

# 서보 모터 제어 함수

def control_servo(lock_or_unlock):

    if lock_or_unlock == 'lock':

        set_angle(240)

    elif lock_or_unlock == 'unlock':

        set_angle(40)



@app.route('/lock', methods=['POST'])

def lock():

    control_servo('lock')

    return 'Locked', 200

@app.route('/unlock', methods=['POST'])

def unlock():

    control_servo('unlock')

    return 'Unlocked', 200



if __name__ == '__main__':

    app.run(host='0.0.0.0')
