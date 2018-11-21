print("Rock Paper Scissors")
p1w="Player 1 wins,, Congratulations"
p2w="Player 2 wins,, Congratulations"
t ="Its a tie"

p1=input('Enter one: Rock, Paper, Scissors !')
p2=input('Enter one: Rock, Paper, Scissors !')
if p1== 'Rock'and p2=='Scissors':
    result=p1w
elif p1=='Scissors' and p2=='Paper':
    result=p1w
elif p1=='Paper' and p2=='Rock':
    result=p1w
elif p2== 'Rock'and p1=='Scissors':
    result=p2w
elif p2=='Scissors' and p1=='Paper':
    result=p2w
elif p2=='Paper' and p1=='Rock':
    result=p2w
elif  p1==p2:
    result=t

print(result)
