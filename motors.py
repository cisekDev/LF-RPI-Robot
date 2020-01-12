import wiringpi
import cv2

A1 = 5
B1 = 6
A2 = 20
B2 = 21
PWM1 = 13
PWM2 = 19

if (__name__ == '__main__'):
    wiringpi.wiringPiSetupGpio()
    img = cv2.imread('robot.jpg')
    cv2.imshow('Robot', img)

    wiringpi.pinMode(A1, 1)
    wiringpi.pinMode(B1, 1)
    wiringpi.pinMode(A2, 1)
    wiringpi.pinMode(B2, 1)
    wiringpi.softPwmCreate(PWM1, 1, 100)
    wiringpi.softPwmCreate(PWM2, 1, 100)
    pwm = 10
    wiringpi.softPwmWrite(PWM1, pwm)
    wiringpi.softPwmWrite(PWM2, pwm)

    while(True):
        key = cv2.waitKey(1) & 0xFF



        if key == 27: #exit
            print("exit")
            wiringpi.digitalWrite(A1, 1)
            wiringpi.digitalWrite(B1, 1)
            wiringpi.digitalWrite(A2, 1)
            wiringpi.digitalWrite(B2, 1)
            quit()
        elif key == 119: #up
            wiringpi.digitalWrite(A1, 1)
            wiringpi.digitalWrite(B1, 0)
            wiringpi.digitalWrite(A2, 0)
            wiringpi.digitalWrite(B2, 1)
        elif key == 115: #down
            wiringpi.digitalWrite(A1, 1)
            wiringpi.digitalWrite(B1, 1)
            wiringpi.digitalWrite(A2, 1)
            wiringpi.digitalWrite(B2, 1)
        elif key == 97: #left
            wiringpi.digitalWrite(A1, 1)
            wiringpi.digitalWrite(B1, 0)
            wiringpi.digitalWrite(A2, 1)
            wiringpi.digitalWrite(B2, 1)
        elif key == 100: #right
            wiringpi.digitalWrite(A1, 1)
            wiringpi.digitalWrite(B1, 1)
            wiringpi.digitalWrite(A2, 0)
            wiringpi.digitalWrite(B2, 1)
        elif key == 45: #plus
            pwm = pwm + 1
            wiringpi.softPwmWrite(PWM1, pwm)
            wiringpi.softPwmWrite(PWM2, pwm)
        elif key == 48: #minus
            pwm = pwm - 1
            wiringpi.softPwmWrite(PWM1, pwm)
            wiringpi.softPwmWrite(PWM2, pwm)
