import wiringpi
import cv2

class Motors:
    A1 = 5
    B1 = 6
    A2 = 20
    B2 = 21
    PWM1 = 13
    PWM2 = 19

    def setup_motors(self):
        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(self.A1, 1)
        wiringpi.pinMode(self.A2, 1)
        wiringpi.pinMode(self.B1, 1)
        wiringpi.pinMode(self.B2, 1)
        wiringpi.softPwmCreate(self.PWM1, 1, 100)
        wiringpi.softPwmCreate(self.PWM2, 1, 100)

    def move_right_motor(self, forward, pwm):
        if forward:
            wiringpi.digitalWrite(self.A1, 1)
            wiringpi.digitalWrite(self.B1, 0)
        else:
            wiringpi.digitalWrite(self.A1, 0)
            wiringpi.digitalWrite(self.B1, 1)
        if 0 == pwm:
            wiringpi.digitalWrite(self.A1, 1)
            wiringpi.digitalWrite(self.B1, 1)
        else:
            wiringpi.softPwmWrite(self.PWM1, pwm)

    def move_left_motor(self, forward, pwm):
        if forward:
            wiringpi.digitalWrite(self.A2, 0)
            wiringpi.digitalWrite(self.B2, 1)
        else:
            wiringpi.digitalWrite(self.A2, 1)
            wiringpi.digitalWrite(self.B2, 0)
        if 0 == pwm:
            wiringpi.digitalWrite(self.A2, 1)
            wiringpi.digitalWrite(self.B2, 1)
        else:
            wiringpi.softPwmWrite(self.PWM2, pwm)

if (__name__ == '__main__'):
    img = cv2.imread('robot.jpg')
    cv2.imshow('Robot', img)

    motors = Motors()
    motors.setup_motors()
    pwm = 10

    while(True):
        key = cv2.waitKey(1) & 0xFF

        if key == 27: #exit
            motors.move_right_motor(True, 0)
            motors.move_left_motor(True, 0)
            quit()
        elif key == 119: #up
            motors.move_right_motor(True, pwm)
            motors.move_left_motor(True, pwm)
        elif key == 115: #down
            motors.move_right_motor(True, 0)
            motors.move_left_motor(True, 0)
        elif key == 97: #left
            motors.move_right_motor(True, pwm)
            motors.move_left_motor(True, 0)
        elif key == 100: #right
            motors.move_right_motor(True, 0)
            motors.move_left_motor(True, pwm)
        elif key == 45: #plus
            pwm = pwm + 1
            print(pwm)
        elif key == 48: #minus
            pwm = pwm - 1
            print(pwm)
