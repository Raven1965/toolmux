#!/bin/bash
#http://www.network-science.de/ascii/
#cyberlarge
if [[ $1 == site ]];then
	echo
	echo
	echo
	printf "

	SİTE \e[31m>\e[32m http://www.network-science.de/ascii\e[0m

	YAZI FONTU \e[31m>\e[32m CYBERLARGE\e[0m

	ADJUSTMENT \e[31m>\e[32m LEFT \e[31m=\e[32m CENTER\e[0m
	"
	echo
	echo
	echo
	exit
fi

#################### GÜNLER ####################

pazartesi=$(date |grep -o Mon)
sali=$(date |grep -o Tue)
carsamba=$(date |grep -o Wed)
persembe=$(date |grep -o Thu)
cuma=$(date |grep -o Fri)
cumartesi=$(date |grep -o Sat)
pazar=$(date |grep -o Sun)

#################### GÜNLERE GÖRE RENKLER ####################

if [[ $pazartesi == Mon ]];then
	renk1='\e[0m'

elif [[ $sali == Tue ]];then
	renk1='\e[0m'
	
elif [[ $carsamba == Wed ]];then
	renk1='\e[0m'
	
elif [[ $persembe == Thu ]];then
	renk1='\e[0m'
	
elif [[ $cuma == Fri ]];then
	renk1='\e[0m'
	
elif [[ $cumartesi == Sat ]];then
	renk1='\e[31m'
	
elif [[ $pazar == Sun ]];then
	renk1='\e[33m'
	
fi

#################### BANNER ####################

printf "
$renk1
'########::'#######:::'#######::'##:::::::'##::::'##:'##::::'##:'##::::'##:
... ##..::'##.... ##:'##.... ##: ##::::::: ###::'###: ##:::: ##:. ##::'##::
::: ##:::: ##:::: ##: ##:::: ##: ##::::::: ####'####: ##:::: ##::. ##'##:::
::: ##:::: ##:::: ##: ##:::: ##: ##::::::: ## ### ##: ##:::: ##:::. ###::::
::: ##:::: ##:::: ##: ##:::: ##: ##::::::: ##. #: ##: ##:::: ##::: ## ##:::
::: ##:::: ##:::: ##: ##:::: ##: ##::::::: ##:.:: ##: ##:::: ##:: ##:. ##::
::: ##::::. #######::. #######:: ########: ##:::: ##:. #######:: ##:::. ##:
:::..::::::.......::::.......:::........::..:::::..:::.......:::..:::::..::







\e[0m
"
