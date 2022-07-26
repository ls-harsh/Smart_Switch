from subprocess import call
import speech_recognition as sr
import serial
import RPi.GPIO as GPIO
import os, time
r= sr.Recognizer()
led1=27
led2=26
led3=25
fan=24
text = {}
text1 = {}
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(fan, GPIO.OUT)
def listen1():
    with sr.Microphone(device_index = 1) as source:
               r.adjust_for_ambient_noise(source)
               print("Say Something");
               audio = r.listen(source)
               print("got it");
    return audio
def voice(audio1):
       try:
         text1 = r.recognize_google(audio1)
##         call('espeak '+text, shell=True)
         print ("you said: " + text1);
         return text1;
       except sr.UnknownValueError:
          call(["espeak", "-s140  -ven+18 -z" , "Google Speech Recognition could not understand"])
          print("Google Speech Recognition could not understand")
          return 0
       except sr.RequestError as e:
          print("Could not request results from Google")
          return 0
def main(text):
       audio1 = listen1()
       text = voice(audio1);
       if 'turn on light number 1' in text:
          GPIO.output(led1 , 1)
          call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching ON the Light number one"])
          print ("Turning light number one on");
       elif 'turn off light number 1' in text:
          GPIO.output(led1 , 0)
          call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching off the Light number one"])
          print ("Turning light number one Off");
       elif 'turn on light number 2' in text:
          GPIO.output(led2 , 1)
          call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching ON the Light number two"])
          print ("Turning light number two on");
       elif 'turn off light number 2' in text:
          GPIO.output(led2 , 0)
          call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching off the Light number two"])
          print ("Turning light number two Off");
       elif 'turn on light number 3' in text:
          GPIO.output(led3 , 1)
          call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching ON the Light number three"])
          print ("Turning light number three on");
       elif 'turn off light number 3' in text:
          GPIO.output(led3 , 0)
          call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching off the Lights number three"])
          print ("Turning light number three Off");
       elif 'turn on fan' in text:
          GPIO.output(fan , 1)
          call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching ON the fan"])
          print ("Turning fan on");
       elif 'turn off fan' in text:
          GPIO.output(fan , 0)
          call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching off the fan"])
          print ("Turning fan Off");
       elif 'turn on everything' in text:
          GPIO.output(led1 , 1)
          GPIO.output(led2 , 1)
          GPIO.output(led3 , 1)
          GPIO.output(fan , 1)
          call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching ON everything"])
          print ("Turning on everything");
       elif 'turn off everything' in text:
          GPIO.output(led1 , 0)
          GPIO.output(led2 , 0)
          GPIO.output(led3 , 0)
          GPIO.output(fan , 0)
          call(["espeak", "-s140  -ven+18 -z" , "okay  Sir, Switching off everything"])
          print ("Turning Off everything");
       text = {}
if __name__ == '__main__':
 while(1):
     audio1 = listen1()
     text = voice(audio1)
     if text == 'activate':
         text = {}
         call(["espeak", "-s140  -ven+18 -z" ," Okay Sir, waiting for your activation command"])
         main(text)
     else:
         call(["espeak", "-s140 -ven+18 -z" , " Please repeat activation code"])

