What Did I Do Here ? 

-Tracked myself using Haar Cascade algorithms. 
Why Did I do this  ?
-I want to use similar features in next project that will be scanner for detecting PCB traces. I want to do this device for using when making PCB. 

How do you do this experiment and what to know : 

-This project uses 2 library. Opencv and A servo library from Adafruit called ServoKit .

-Firstly , you should know your python version. it should be at least python3.8 because adafruit updates it's library and you can't download for old python version. 

sudo apt-get install software-properties-common

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt-get update

sudo apt-get install python3.8


-As second , you should keep updated your pip tool . It causes problems when downloading adafruit library. 

sudo pip3.8 install --upgrade pip

sudo python3 -m pip install --upgrade pip 

-Installing servokit library and some process 

sudo pip3 install adafruit-circuitpython-servokit 

-You should write your username instead of me (miki) 

sudo usermod -aG i2c miki 

sudo groupadd -f -r gpio 

sudo usermod -a -G gpio miki

sudo cp /lib/udev/rules.d/60-jetson-gpio-common.rules /etc/udev/rules.d/99-gpio.rules

sudo udevadm control --reload-rules && sudo udevadm trigger

-That was for servokit. let's download opencv package for python3.8 

python3.8 -m pip install opencv-python

-That is all ! you can run the script that I uploaded. 




