import time
import webbrowser

print ("Este programa iniciou as: " +time.ctime(10))

for x in range(0,3):
    time.sleep(10)
    #webbrowser.open(www.terra.com.br)
    print ("Estamos na iteracao %d" % (x))

