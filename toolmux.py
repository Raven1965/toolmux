#!/usr/bin/env python
# -*- coding: utf-8 -*-

import progressbar 

import time 

  

  
# Function to create  

def animated_marker(): 

      

    widgets = ['Başlıyoruz: ', progressbar.AnimatedMarker()] 

    bar = progressbar.ProgressBar(widgets=widgets).start() 

      

    for i in range(50): 

        time.sleep(0.1) 

        bar.update(i) 

          
# Driver's code 
animated_marker()





import os


os.system("clear")
os.system("figlet TOOLMUX")





print("""
Istediyin numarayı gir  ~~~~Made by Revan~~~~
_________________________________________________________________________________
1) python            5)python2	              9)sqlmap
2) php	             6)python3		     10)toollar
3)curl         	     7)nmap
4)pip güncelle       8)termux güncelle
_________________________________________________________________________________
""")

secim = input("Seçim ===> ")
	
if(secim=="1"):
	os.system("clear")
	os.system("pkg install python -y")

elif(secim=="2"):
	os.system("clear")
	os.system("pkg install php -y")
	
elif(secim=="3"):
	os.system("clear")
	os.system("pkg install curl -y")
	

elif(secim=="4"):
	os.system("clear")
	os.system("pip install --upgrade pip")
						
elif(secim=="5"):
	os.system("clear")
	os.system("pkg install python2 -y")
	
elif(secim=="6"):
	os.system("clear")
	os.system("pkg install python3 -y")
			
elif(secim=="7"):
	os.system("clear")
	os.system("pkg install nmap -y")

elif(secim=="8"):
	os.system("clear")
	os.system("pkg uptade && pkg upgrade")
		
																					
elif(secim=="9"):						
	os.system("clear")
	os.system("git clone https://github.com/sqlmapproject/sqlmap")
	
															
elif(secim=="10"):
	os.system("clear")
	os.system("figlet TOOLMUX")
	print('1)Ddos hammer' , '2)Termuxu özelleştir' , '3)Sqlnmap' , '4)Red_Hawk' , '5)saycheese(kamera hack)' , '6)scan(CCTV kamera hack)' , '7)HIDDENEYE(phishing)' , '8)AK47(bruteforce)' , '9)LittleBrother(bilgi topla)' , '10)Kali linux indir' , '11)Infect(kurbanın telin resetler)' , '12)Metasploit' , '13)Hydra(bruteforce)' , '14)TheFatRat(trojan kalide çalıştır)' , '15)vbug(virus oluşturucu)' '16)Th3inspector(bilgi topla numaradan)' , '17)PHONE INFOGA(numaradan bilgi toplar)' , '18)IMPULSE(Sms bomber)' , '19)Instaspam' , '20)Gametool(oyun)' , 'DAHA FAZLA TOOL EKLENICEK' , sep='\n')			   		
				   						   						   		
	secim2 = input("Seçim ===> ")
	
if(secim2=="1"):
	os.system("clear")
	os.system('git clone https://github.com/cyweb/hammer.git')
	


elif(secim2=="2"):
	os.system("clear")
	os.system("git clone https://github.com/noob-hackers/T-LOAD")			


elif(secim2=="3"):
	os.system('clear')
	os.system('git clone https://github.com/Raven1965/sqlnmap.git')
	
elif(secim2=='4'):
	os.system('clear')
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK.git')
	
			
elif(secim2=='5'):
	os.system("clear")
	os.system('pkg install wget')
	os.system('pkg install openssh')
	os.system('git clone https://github.com/thelinuxchoice/saycheese')				
	
elif(secim2=="6"):
		os.system('clear')
		os.system('pkg install python2')
		os.system('git clone https://github.com/kancotdiq/ipcs.git')
		
elif(secim2=="7"):
	os.system("clear")
	os.system('https://github.com/DarkSecDevelopers/HiddenEye-Legacy.git')
	os.system('pip install -r requirements.txt')	
	
elif(secim2=='8'):
	os.system('clear')
	os.system('pkg install python2')
	os.system('git clone https://github.com/nasirxo/AK47')
		
elif(secim2=="9"):
	os.system('clear')
	os.system('pkg install python3')
	os.system('git clone https://github.com/Lulz3xploit/LittleBrother')
		
elif(secim2=="10"):
	os.system('clear')
	os.system('pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-xfce.sh | bash')
		
elif(secim2=="11"):
	os.system("clear")
	os.system("pkg install python python2 -y && pip install lolcat && git clone https://github.com/noob-hackers/infect")		
	
elif(secim2=='12'):
	os.system("clear")
	os.system("pkg install wget && wget https://Auxilus.github.io/metasploit.sh")
		
elif(secim2=='13'):
	os.system('clear')
	os.system('pkg update && pkg upgrade -y && pkg install hydra && hydra -h')
		
elif(secim2=='14'):
	os.system('clear')
	os.system('git clone https://github.com/Screetsec/TheFatRat.git && chmod +x setup.sh && ./setup.sh')	

	
		
elif(secim2=='15'):
	os.system('clear')
	os.system('git clone https://github.com/Junior60/vbug && cd vbug && python2 vbug.py')	

elif(secim2=='16'):
		os.system('clear')
		os.system('pkg install perl && git clone https://github.com/Moham3dRiahi/Th3inspector && cd Th3inspector && chmod +x install.sh && ./install.sh')														
																
elif(secim2=='17'):
	   os.system('clear')
	   os.system('git clone https://github.com/sundowndev/PhoneInfoga')												
elif(secim2=='18'):
	os.system('clear')
	os.system('git clone https://github.com/LimerBoy/Impulse && pip install -r requirements.txt && python3 impulse.py')

elif(secim2=='19'):
	 os.system('clear')
	 os.system('https://github.com/tarik0/instaspam.git')																										
elif(secim2=='20'):
	os.system('clear')
	os.system('git clone https://github.com/mbest99/gametool && cd gametool && bash cok.sh')																											