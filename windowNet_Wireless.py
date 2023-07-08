import os
os.system('cls')

print('\n\n\n\n')
print("Wi-fi Hotspot Enabler")
print("revocoder")
print()

cmd='0'
while cmd != '3':
    print('1-start\n2-stop\n3-exit\n')
    cmd =input('Please enter your choice (1,2,3) : ')
    if cmd == '1':
        os.system("netsh wlan set hastednetwork mode=allow ssid=reovcoder key=faksldfjsdfj" )
        os.system("netsh wlan start hostednetwork")
    elif cmd == '2':
        os.system("netsh wlan stop hostednetwork")
    
    elif cmd == '3':
        exit()
    else:
        print("Wrong input, Please add 1,2,3")
    
        