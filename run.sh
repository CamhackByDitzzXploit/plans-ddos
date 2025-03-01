#!/bin/sh

#warna
merah="\033[31;1m"
hijau="\033[32m"
biru="\033[33m"

pip install -r requirements.txt
clear
echo $biru"=========================================="
echo $biru"     Silahkan Login Untuk Menggunakan  "
echo $biru"=========================================="
echo
sleep 3
xdg-open https://youtube.com/@DitzzXploit
read -p "Enter Your Password: " pass
if [ $pass = DitzzXploit ]
then
echo $biru"Password Bener Anda Akan Di arahkan Ke Plans Kami"
sleep 5
echo "Tunggu Sebentar...."
echo
echo "Kami Akan mengarahkan Ke plans Anda"
echo
clear
echo
echo  $merah "+=================================+"
echo  $merah "| ( + ) Author: DitzzXploit  ( + )|"
echo  $merah "| ( + ) Youtube: DitzzXploit ( + )|"
echo  $merah "| ( + ) Script: Plans       ( + ) |"
echo  $merah "+=================================+"
echo
echo  $merah "1). DDOS TOOLS 1                  |"
echo  $merah "2). DDOS TOOLS 2                  |"
echo  $merah "3). DDOS TOOLS PROXY              |"
echo  $merah "4). AUTO DEFACER                  |"
echo  $merah "5). Spam Pairing ( Process )      |"
echo  $merah "6). SERVER CHECKER                |"
echo  $merah "7). Generator Username & Pass     |"
echo  $merah "8). DDOS TRAFIC                   |"
echo  $merah "9). Auto Xploit                   |"
echo  $merah "10). EXIT                         |"
echo
echo  $merah"+++++++++++++++++++++++++++++++++++|"
read -p "Pilih Menu Yang Tersedia: " dont

if [ $dont = 1 ]
then
python ddosSimple.py
fi

if [ $dont = 2 ]
then
python DDOStools.py
fi

if [ $dont = 3 ]
then
python ddos-proxy.py
fi

if [ $dont = 4 ]
then
python white-deface.py
fi

if [ $dont = 5 ]
then
echo "masih Prosess Bg"
fi

if [ $dont = 6 ]
then
python server-checker.py
fi

if [ $dont = 7 ]
then
python usnm-pas.py
fi

if [ $dont = 8 ]
then
python trafic.py
fi

if [ $dont = 9 ]
then
python AutoExploit.py
fi

if [ $dont = 10 ]
then
echo "Thanks To You"
exit
fi

else
echo "Password Salah"
fi
