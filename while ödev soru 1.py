satismiktari=500
satisfiyati=20
ciro=5000
i=0
while(ciro<=500000):
    ciro=(satismiktari*satisfiyati)+ciro
    satismiktari=satismiktari+200
    satisfiyati=satisfiyati+10
    i=i+1
print("500.000 den fazla kar ",i,". ayda tamamlanmıştır")
