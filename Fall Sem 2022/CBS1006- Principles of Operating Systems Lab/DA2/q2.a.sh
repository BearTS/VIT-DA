echo "Registration Number: 21BBS0162"
echo "Name: Anuj Parihar"
echo "Enter two numbers"
read a
read b
echo "Before swapping"
echo "a=$a"
echo "b=$b"
a=`expr $a + $b`
b=`expr $a - $b`
a=`expr $a - $b`
echo "After swapping"
echo "a=$a"
echo "b=$b"