#while
#./all.py 0 36 255 255 255



a1="0"
a2=""
a3=""

b1=""
b2=""
b3=""

$i

while [ $i -lt 255 ]
do
a1=$[$i+1]


if [ $a1 -gt $b1 ]
$c1 = $a1 - $b1
#vois vaan määritellä onko tää erotus nega vai ei ja ottaa siitä positiivisen muunnoksen jos joo
#sit sitä muunnosta vois sen nega/posin perusteel laskea 0:aan tai nostaa 255:een.


if [ $c1 -gt 255 ]
then
c1=$[$c1+1]
fi

if [ $c1 -lt 0 ]
then
c1=$[$c1-1]
fi
