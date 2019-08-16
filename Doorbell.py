import time
import RPi.GPIO as g
import picamera as p
import pushbullet as c
ps=1
count=1
#push = c.Pushbullet("o.GK9TctIEenc2cMGmC3EHApJuNtpXyt3C")
g.setmode(g.BCM)
g.setup(2,g.IN)
cam = p.PiCamera()
a="img"
while 1:
        push = c.Pushbullet("o.GK9TctIEenc2cMGmC3EHApJuNtpXyt3C")

        name= str(time.time())
        cs=g.input(2)
        if((not ps) and cs):
                z=a+name+".jpg"
                cam.capture(z)
                push.push_note("Doorbell","Someone at the Main Door")
#               cam.close()
                with open(z,"rb") as pic:
                        file_data=push.upload_file(pic,"picture.jpg")
                push = push.push_file(**file_data)
                #cam.close()
                print(z)
                print("success")
        ps=cs
        time.sleep(0.05)
cam.close()

