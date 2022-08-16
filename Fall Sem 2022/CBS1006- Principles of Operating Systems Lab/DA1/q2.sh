# Print patterns
echo "Registration Number: 21BBS0162"
echo "Name: Anuj Parihar"
i=0
j=0
x=5
while [ $i -le 5 ]
do
    j=0     
    while [ $j -le 5 ]
    do
        if [ 5 -le `expr $i + $j` ]
        then
          echo -ne "$x"
        else
          echo -ne " "
        fi
        j=`expr $j + 1`
    done
    echo
              
    i=`expr $i + 1`
    x=`expr $x - 1`
done
