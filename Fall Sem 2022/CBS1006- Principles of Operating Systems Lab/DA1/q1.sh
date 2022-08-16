# Create a shell script program that uses a "for" loop to find the factorial of a given number.
echo "Registration Number: 21BBS0162"
echo "Name: Anuj Parihar"

echo "Enter a number: "
read num
fact=1
for i in `seq 1 $num`
do
fact=$((fact*i))
done
echo "Factorial of $num is $fact"