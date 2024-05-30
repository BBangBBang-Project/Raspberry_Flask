# 🍞 BBangBBang_Raspberry_Flask 🥐

> 2024 HSU Capstone AI를 활용한 키오스크와 스마트 빵 자판기 - BBangBBang 의 Flask Server입니다.

</br>

## ✔️ GUIDES

외부에서 라즈베리파이 서버에 잠금/해제 요청을 하면 연결된 GPIO 핀을 통해 모터를 제어합니다.
라즈베리파이의 linux 환경에서 실행하였습니다. 외부에서 라즈베리파이에 접근 가능하게 하기 위해 ngrok 명령어를 사용하여 해당 포트를 열어줍니다.
포트를 열어준 후에 플라스크 서버를 실행해줍니다.

```shell
$ngrok http —domain=raspberrypi.ngrok.io 5000
$python motor_flask.py
```

</br>

## ✏️ API

##### https://raspberrypi.ngrok.io/lock

- 서버에서의 잠금 요청을 받으면 해당 엔드포인트로 모터의 각도를 240도로 조절하여 잠금 설정

##### https://raspberrypi.ngrok.io/unlock

- 서버에서의 잠금 해제 요청을 받으면 해당 엔드포인트로 모터의 각도를 40도로 조절하여 잠금 해제 설정

</br>

## 🕗 VERSION

- Python 3.10.6
- Flask 2.3.2
