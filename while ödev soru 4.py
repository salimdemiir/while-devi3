calisan=50
yevmiye=90
aylikmesai=0
haftalikmaas=630
aylikmaas=0
while(aylikmesai<=22):
    haftalikmesai=int(input("haftalik mesai:"))
    aylikmesai=haftalikmesai*4
    haftalikmaas=haftalikmaas+(haftalikmesai*yevmiye*0.10)
    aylikmaas=aylikmaas+haftalikmaas*4
    print("aylık maaş:",aylikmaas)
else:
    print("aylik mesai 22 saatten fazla olamaz")
