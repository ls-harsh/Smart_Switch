import datetime
from posixpath import split
from typing import Text
import speech_recognition as sr
import pyttsx3
import os
import math
import cv2 as cv
import webbrowser
import pywhatkit
from time import sleep
from time import ctime
from selenium import webdriver
import wikipedia

user_name = os.getlogin()

engine =  pyttsx3.init('sapi5')	
voices= engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')

    elif hour>=12 and hour<16:
        speak('Good Afternoon')

    elif hour>=16 and hour<18:
        speak('Good Afternoon')

    else:
        speak('Good Night')

    speak(' Hi I am Lauren tell me what you need')

def pizza():
    driver = webdriver.Chrome("C:\\Users\\Govindaraju N\\OneDrive\\Desktop\\chromedriver.exe")

    driver.maximize_window()
    speak("Opening Dominos")

    driver.get("https://www.dominos.co.in/")
    sleep(2)

    speak("Getting ready to order")
    driver.find_element_by_link_text("ORDER ONLINE NOW").click()
    sleep(2)

    speak("Finding your location")
    driver.find_element_by_class_name("srch-cnt-srch-inpt").click()
    sleep(2)

    location = "GOVERNMENT S.K.S. "

    speak("Entering your location")
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/input'
    ).send_keys(location)
    sleep(10)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[1]/div[2]/span[2]'
    ).click()
    sleep(10)

    try:
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[2]').click()
        sleep(2)
    except:
        speak("Your location could not be found. Please try again later.")
        exit()

    speak("Logging in")

    phone_num = "9900336840 "

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(
        phone_num)
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input').click()
    sleep(2)

    speak("What is your O T P? ")
    sleep(3)

    otp_log = takeCommand()

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input').send_keys(
        otp_log)
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button/span').click()
    sleep(2)

    speak("Do you want me to order from your favorites?")
    query_fav = takeCommand()
    try:
        if "yes" in query_fav:
            try:
                driver.find_element_by_xpath(
                    '//*[@id="mn-lft"]/div[6]/div/div[6]/div/div/div[2]/div[3]/div/button/span').click()
                sleep(1)
            except:
                speak("The entered OTP is incorrect.")
                exit()

            speak("Adding your favorites to cart")

            speak("Do you want me to add extra cheese to your pizza?")
            ex_cheese = takeCommand()
            if "yes" in ex_cheese:
                speak("Extra cheese added")
                driver.find_element_by_xpath(
                    '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[2]/button').click()
            elif "no" in ex_cheese:
                driver.find_element_by_xpath(
                    '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()
            else:
                speak("I dont know that")
                driver.find_element_by_xpath(
                    '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()

            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[16]/div/div[1]/div/div/div[2]/div[2]/div/button').click()
            sleep(1)

            speak("Would you like to increase the qty?")
            qty = takeCommand()
            qty_pizza = 0
            qty_pepsi = 0
            if "yes" in qty:
                speak("Would you like to increase the quantity of pizza?")
                wh_qty = takeCommand()
                if "yes" in wh_qty:
                    speak("How many more pizzas would you like to add? ")
                    try:
                        qty_pizza = takeCommand()
                        qty_pizza = int(qty_pizza)
                        if qty_pizza > 0:
                            talk_piz = f"Adding {qty_pizza} more pizzas"
                            speak(talk_piz)
                            for i in range(qty_pizza):
                                driver.find_element_by_xpath(
                                    '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]').click()
                    except:
                        speak("I dont know that.")
                else:
                    pass

                speak("Would you like to increase the quantity of pepsi?")
                pep_qty = takeCommand()
                if "yes" in pep_qty:
                    speak("How many more pepsis would you like to add? ")
                    try:
                        qty_pepsi = takeCommand()
                        qty_pepsi = int(qty_pepsi)
                        if qty_pepsi > 0:
                            talk_pep = f"Adding {qty_pepsi} more pepsis"
                            speak(talk_pep)
                            for i in range(qty_pepsi):
                                driver.find_element_by_xpath(
                                    '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]').click()
                    except:
                        speak("I dont know that.")
                else:
                    pass

            elif "no" in qty:
                pass

            total_pizza = qty_pizza + 1
            total_pepsi = qty_pepsi + 1
            tell_num = f"This is your list of order. {total_pizza} Pizzas and {total_pepsi} Pepsis. Do you want to checkout?"
            speak(tell_num)
            check_order = takeCommand()
            if "yes" in check_order:
                speak("Checking out")
                driver.find_element_by_xpath(
                    '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button').click()
                sleep(1)
                total = driver.find_element_by_xpath(
                    '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[6]/span[2]/span')
                total_price = f'total price is {total.text}'
                speak(total_price)
                sleep(1)
            else:
                exit()

            speak("Placing your order")
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[8]/button').click()
            sleep(2)
            try:
                speak("Saving your location")
                driver.find_element_by_xpath(
                    '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/div[3]/div/div/input').click()
                sleep(2)
            except:
                speak("The store is currently offline.")
                exit()

            speak("Do you want to confirm your order?")
            confirm = takeCommand()
            if "yes" in confirm:
                speak("Placing your order")
                driver.find_element_by_xpath(
                    '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/button').click()
                sleep(2)
                speak("Your order is placed successfully. Wait for Dominos to deliver your order. Enjoy your day!")
            else:
                exit()

        else:
            exit()

    except OSError:
        print("Sorry some problem sir")

def amazon():
    driver = webdriver.Chrome("C:\\Users\\Govindaraju N\\OneDrive\\Desktop\\chromedriver.exe")
    speak("opening amazon")
    driver.get('https://www.amazon.in/')
    speak("signing in")
    driver.find_element_by_xpath('//*[@id="nav-link-accountList-nav-line-1"]').click()
    driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys("9900336840")
    driver.find_element_by_xpath('//*[@id="continue"]').click()
    driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys("Govindaraju@123")
    driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
    speak("successfully signed in")
    driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys("Gionee max mobile")
    speak("searching mobiles")
    driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]').click()

def restaurants():

    driver = webdriver.Chrome("C:\\Users\\Govindaraju N\\OneDrive\\Desktop\\chromedriver.exe")
    driver.get("https://www.google.co.in/maps/@13.0826883,77.4128187,15z")
    speak("finding restaurants near you")

    driver.find_element_by_xpath('//*[@id="searchboxinput"]').send_keys("Restaurants near me")
    driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]').click()
    speak("These are the restaurants near you")

def local_files():
    file_split = query.split("open ")
    files = file_split[1]
    f1 = files.upper()
    f2 = files.lower()
    f3 = str.capitalize(files)
    a = files+".pdf"
    aa = f1+".pdf"
    ab = f2+".pdf"
    ac = f3+".pdf"
    b = files+".docx"
    ba = f1+".docx"
    bb = f2+".docx"
    bc = f3+".docx"
    c = files+".pptx"
    ca = f1+".pptx"
    cb = f2+".pptx"
    cc = f3+".pptx"
    speak("searching"+files)
    r = []

    for foldername,subfolders,filenames in os.walk('C:\\Users\\'+user_name):
        if files in subfolders:
            location=(foldername+'\\'+files)
            r.append(location)

        elif f1 in subfolders:
            location=(foldername+'\\'+f1)
            r.append(location)

        elif f2 in subfolders:
            location=(foldername+'\\'+f2)
            r.append(location)

        elif f3 in subfolders:
            location=(foldername+'\\'+f3)
            r.append(location)

        elif a in filenames and c in filenames:
            location=(foldername+'\\'+a)
            loc = (foldername+'\\'+c)
            r.append(location)
            r.append(loc)

        elif aa in filenames and ca in filenames:
            location=(foldername+'\\'+aa)
            loc = (foldername+'\\'+ca)
            r.append(location)
            r.append(loc)

        elif ab in filenames and cb in filenames:
            location=(foldername+'\\'+ab)
            loc = (foldername+'\\'+cb)
            r.append(location)
            r.append(loc)

        elif ac in filenames and cc in filenames:
            location=(foldername+'\\'+ab)
            loc = (foldername+'\\'+cc)
            r.append(location)
            r.append(loc)

        elif a in filenames and b in filenames:
            location=(foldername+'\\'+a)
            loc = (foldername+'\\'+b)
            r.append(location)
            r.append(loc)

        elif aa in filenames and ba in filenames:
            location=(foldername+'\\'+aa)
            loc = (foldername+'\\'+ba)
            r.append(location)
            r.append(loc)

        elif ab in filenames and bb in filenames:
            location=(foldername+'\\'+ab)
            loc = (foldername+'\\'+bb)
            r.append(location)
            r.append(loc)

        elif ac in filenames and bc in filenames:
            location=(foldername+'\\'+ab)
            loc = (foldername+'\\'+bc)
            r.append(location)
            r.append(loc)               

        elif a in filenames:
            location=(foldername+'\\'+a)
            r.append(location)

        elif files in filenames:
            location=(foldername+'\\'+files)
            r.append(location)

        elif aa in filenames:
            location=(foldername+'\\'+aa)
            r.append(location)

        elif ab in filenames:
            location=(foldername+'\\'+ab)
            r.append(location) 

        elif ac in filenames:
            location=(foldername+'\\'+ac)
            r.append(location)
            
    for i in range(len(r)):
        print(i+1 , end=" : ")
        print(r[i])

    try:
        if len(r)>1:
            # speak("select the file you want to open by its index")
            try:
                speak("enter the index of the file to open")
                index = input("Enter the index of the file to open : ")
                os.startfile(r[int(index)-1])
            except ValueError:
                # speak("sorry I did'nt get that")
                print("sorry I did'nt get that")

        elif len(r)==1:
            speak("opening"+files)
            os.startfile(r[0])

        else:
            print("file not found")

    except IndexError:
        print("file does'nt exist sir")
    print('')        


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print('listening....')
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print('Recognizing....')
        query = r.recognize_google(audio,language='en-in')
        print(f'user said: {query}\n')

    except Exception as e:
        #print(e)
        print('say that again please....')
        return 'None'
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing task 
        if 'open c drive' in query or 'open cd drive' in query:
            speak("opening C drive")
            os.startfile("c:")

        elif 'hello' in query:
            speak("hello vinay, Govindaraju, Abhishek, Harsh All the best for the presentation on me ")
            speak(" Namaste Naagesh sir and respected teachers present here")

        elif "open webcam" in query:
            speak("Opening webcam")
            cam = cv.VideoCapture(0)
            cv.namedWindow("test")
            img_counter = 0

            while True:
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    break
                cv.imshow("test", frame)
                k = cv.waitKey(1)
                if k%256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k%256 == 32:
                     # SPACE pressed
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    img_counter += 1

            cam.release()
            cv.destroyAllWindows()
            
        elif 'open whatsapp' in query:
            speak("Opening whatsapp ")
            whatsapp_dir='C:\\Users\\Govindaraju N\\OneDrive\\Desktop\\WhatsApp Desktop'
            os.startfile(whatsapp_dir)
            speak("Now you can text buddy")

        elif 'wikipedia' in query:
            speak('seraching wikipedia....')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)

        elif "open" in query:
            local_files()
            
        elif "what's the time" in query:
            time = ctime().split(" ")[3].split(":")[0:2]
            if time[0] == "00":
                hours = '12'
            else:
                hours = time[0]
            minutes = time[1]
            time = hours + " hours and " + minutes + "minutes"
            speak(time)

        elif "my gmail" in query:
            # search_term = query.split("for")[-1]
            url="https://mail.google.com/mail/u/0/#inbox"
            webbrowser.get().open(url)
            speak("here you can check your gmail")

        elif "tell me the weather report" in query:
            # search_term = voice_data.split("for")[-1]
            url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
            webbrowser.get().open(url)
            speak("Here is what I found for on google")

        elif "google" in query:
            search_term = query.split("google ")[1]
            url = "https://google.com/search?q=" + search_term
            webbrowser.get().open(url)
            speak("Here is what I found for" + search_term + "on google")

        elif "play music" in query:
            search_term= takeCommand().split("for")[-1]
            url="https://open.spotify.com/search/"+search_term
            webbrowser.get().open(url)
            speak("You are listening to"+ search_term +"enjoy sir")

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackover.com")

        elif "message nagesh"in query:
            speak("please say the message buddy")
            data4=takeCommand()
            print(data4)
            pywhatkit.sendwhatmsg_instantly("+91 9900371864",data4,wait_time=20,browser=None)
            speak("delivering your text")

        elif 'search files' in query or 'search file' in query:
            speak("tell the file name you want to search")
            file_name_1 = takeCommand()
            file_name_2= str.capitalize(file_name_1)
            file_name_3 = file_name_1.upper()
            speak("searching"+file_name_1)
            print("searching.......")

            location_list = []
            file_list = []

            for folderName,subfolders,filenames in os.walk('C:\\Users\\'+user_name):
                for files in filenames:
                    if files.startswith(file_name_1.lower()) or files.startswith(file_name_2) or files.startswith(file_name_3):
                        file_list.append(files)
                        location_1 = folderName + '\\'+files
                        location_list.append(location_1)

            for i in range(len(file_list)):
                    print(i+1 , end=" : ")
                    print(file_list[i])

            try:
                if len(location_list)>1:
                    speak("select the file you want to open by its index")
                    try:
                        index = input("Enter the index of the file to open : ")
                        os.startfile(location_list[int(index)-1])
                    except ValueError:
                        speak("sorry I did'nt get that")
                        print("sorry I did'nt get that")

                elif len(location_list)==1:
                    os.startfile(location_list[0])

                else:
                    print("file not found")

            except IndexError:
                print("file does'nt exist sir")

            print('')
                
        elif ' open video' in query or 'videos' in query:
            video_dir = 'C:\\Users\\'+user_name+'\\Videos'
            speak("Opening videos")
            videos=os.listdir(video_dir)

            for i in range(len(videos)):
                print(i+1 , end=" : ")
                print(videos[i])

            print("say the index of the video to play")
            speak("say the index of the video to play")
            # time.sleep(5)

            query_2 = input("Enter the index of the video to open : ")
            os.startfile(os.path.join(video_dir,videos[int(query_2)-1])) 
                
        elif 'open photos' in query or 'photos' in query:
            speak("Opening images")
            os.startfile("C:\\Users\\"+ user_name +"\\OneDrive\\Pictures")

        elif 'open desktop' in query or 'desktop' in query:
            speak("Opening Desktop")
            os.startfile("C:\\Users\\"+ user_name +"\\OneDrive\\Desktop")

        elif '+' in query:
            opr1=query.split(" ")
            sum =int(opr1[0])+int(opr1[2])
            speak("sum is")
            speak(sum)

        elif 'into' in query :
            opr2=query.split(" ")
            speak("product is")
            speak(int(opr2[0])*int(opr2[2]))
            
        elif 'divide' in query or 'by' in query:
            opr3=query.split(" ")
            speak("quotient is")
            speak(int(opr3[0])/int(opr3[2]))

        elif 'power' in query:
            opr4=query.split(" ")
            Value =int(opr4[0])**int(opr4[2])
            speak("answer is")
            speak(Value)
                      
        elif 'logarithm of ' in query or 'log of ' in query:
            data=query.split(" ")
            results=(math.log(int(data[2])))
            speak(results)

        elif "pizza" in query:
            pizza()

        elif "amazon" in query:
            amazon()

        elif "i am hungry" in query or "restaurants near me" in query:
            restaurants()

        elif "thank you" in query:
            speak("pleasure is mine")

        elif "who is your girlfriend" in query:
            speak("My Gf is Amazon Alexa and Siri I am maintaining two girlfriends") 

        elif 'close' in query or 'exit' in query or 'bye' in query:
            exit()
            

        



        


        

        



        

