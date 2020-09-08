
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
<<<<<<< HEAD

ledPin = 11
buttonPin = 12

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

=======

ledPin = 11
buttonPin = 12

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

>>>>>>> 66b1d68514af7d00b8988361032ef9eb3f59eb93
while True:
  buttonState = GPIO.input(buttonPin)
  if buttonState == False:
    GPIO.output(ledPin, GPIO.HIGH)
  else:
<<<<<<< HEAD
    GPIO.output(ledPin, GPIO.LOW)
=======
    GPIO.output(ledPin, GPIO.LOW)
>>>>>>> 66b1d68514af7d00b8988361032ef9eb3f59eb93
