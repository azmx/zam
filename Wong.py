#!/bin/bash
r="\033[31;1m"
y="\033[33;1m"
yl="\033[1;33m"
g="\033[0;32m"
gl="\033[32;1m"
b="\033[0;36m"
bl="\033[36;1m"
c="\033[36;1m"
p="\033[0;35m"
o="\033[0m"

cek():
command -v curl > /dev/null 2>&1 || { echo >&2 "curl belum terinstall ketik >> pkg install curl -y"; exit 1; }
command -v cowsay > /dev/null 2>&1 || { echo >&2 "cowsay belum terinstall ketik >> pkg install cowsay -y"; exit 1; }
command -v ruby > /dev/null 2>&1 || { echo >&2 "ruby belum terinstall ketik >> pkg install ruby -y dan >> gem install lolcat"; exit 1; }
}
mulai(){
echo ""
sleep 0.1
echo -e "             \033[90m~  ~  ~  \033[1;32m ┌∩┐(\033[1;31m◣_◢\033[1;32m)┌∩┐\033[90m   ~  ~  ~"
echo -e "\033[1;37m                  SPAM CALL VERSI(\033[1;32m2.0\033[1;37m)"
echo -e "\033[1;34m╔═══════════════════════════════════════════════════════╗"
echo -e "\033[1;34m║  \033[90m{\033[1;31m•\033[90m}  \033[1;37mAuthor    :   \033[1;36mFahmi Apz    \033[1;34m                     ║"
echo -e "\033[1;34m║\033[90m  {\033[1;31m•\033[90m} \033[1;37m Youtube   : \033[1;36m  Apmz Channel \033[1;34m                     ║"
echo -e "\033[1;34m║\033[90m  {\033[1;31m•\033[90m} \033[1;37m Github    :\033[1;32m   https://github.com/BangDanz  \033[1;34m     ║"
echo -e "\033[1;34m╚═══════════════════════════════════════════════════════╝"
echo -e "\033[1;37mMasukan Nomor Tanpa (0/62)"
sleep 0.1
echo -e "\033[1;37mMASUKAN NO TARGET \033[1;32m " ;read -p "=> " nomor
link="https://id.jagreward.com/member/verify-mobile/$nomor"
gas="curl -s $link"
sleep 0.1
echo -e "\e[1;37mMESSAGE\033[1;32m"
sleep 0.1
$gas
echo -e "${o}"
sleep 0.2
}
ulang(){
echo ""
echo -e "${o}Coba Lagi ?"
echo -e "${o}y${o}/${o}n${g}"
read -p "=> " ula
if [[ $ula == "y" ]]; then
u
elif [[ $ula == "n" ]]; then
exit
else
echo -e "${r}Pilih y/n  "
ulang
fi
}
u(){
mulai
ulang
}
i(){
cek
mulai
}
mulai
ulang