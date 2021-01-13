

#/bin/bash/
#### EKRANA YAZDIRMA ####
clear
cp scifi.mp3 /sdcard
mpv /sdcard/scifi.mp3
clear
cd files
bash banner2.sh
printf "NUMARA SEÇ VE İNDİR"
echo    
printf "                                                   
             1= HAMMER                                     
	     2= TERMUXU ÖZELLEŞTİR                         
             3= SQLNMAP                                    
             4= RED_HAWK                                    
             5= SAYCHEESE(KAMERA HACK)                    
             6= PPHONEINFOGA                
	     7= LITTLE BROTHER(BILGI TOPLAMA)              
	     8=TH3INSPECTOR(BILGI TOPLAMA)                 





"
echo
echo
#### KULLANICI GİRDİSİ ####
read -e -p $'SEÇİM ====> : ' secim
#### KOŞULLAR ####
if [[ $secim == 1 ]];then
	git clone https://github.com/cyweb/hammer.git
	exit
elif [[ $secim == 2 ]];then
	git clone https://github.com/noob-hackers/T-LOAD
	exit

elif [[ $secim == 3 ]];then
	git clone https://github.com/Raven1965/sqlnmap.git
	exit
elif [[ $secim == 4 ]];then
	git clone https://github.com/Tuhinshubhra/RED_HAWK.git
	exit

elif [[ $secim == 5 ]];then
	pkg install wget
	pkg install openssh
	git clone https://github.com/thelinuxchoice/saycheese
	exit

elif [[ $secim == 6 ]];then
	git clone https://github.com/sundowndev/PhoneInfoga
	exit

elif [[ $secim == 7 ]];then
	git clone https://github.com/Lulz3xploit/LittleBrother
	exit

elif [[ $secim == 8 ]];then
	pkg install perl 
	git clone https://github.com/Moham3dRiahi/Th3inspector.git
	exit


else
	printf "HATALI SEÇİM"

fi	
