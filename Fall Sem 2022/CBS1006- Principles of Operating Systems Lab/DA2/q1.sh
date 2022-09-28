echo "Registration Number: 21BBS0162"
echo "Name: Anuj Parihar"
echo "Enter a number: "
read num
temp=$num
rev=0
while [ $num -gt 0 ]
do
a=`expr $num % 10`
num=`expr $num / 10`
rev=`expr $rev \* 10 + $a`
done
if [ $temp -eq $rev ]
then
echo "Number is palindrome"
else
echo "Number is not palindrome"
fi
