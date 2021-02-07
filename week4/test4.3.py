import datetime
amount_people = int(input('Enter number of competitor : '))
list_name = []
list_score = []
list_time = []
list_hit = []
for i in range (amount_people) :
    date = input('Please enter (name;score;time) : ')
    split_date = date.split(';')
    list_name.append(split_date[0])
    list_score.append(split_date[1])
    list_time.append(split_date[2])
    list_hit.append(float(list_score[i])/float(list_time[i]))

time = datetime.datetime.now()
timenew = time.strftime('%G-%m-%d %H:%M:%S')
print('\nShotgun ',time.strftime('%A'),'Training ',time.strftime('%Y'))
print(timenew)
print(" "+"-"*120+'\n{0:-<8}{1:-<13}{2:-<12}{3:-<20}{4:-<15}{5:-<20}{6}'.format('No','Points','Time','CompetitorName','Hit factor','State Points','State Percents\n'+'-'*120))
for k in range (amount_people) :
    j = k
    for j in range(amount_people) :
        if list_hit[k] > list_hit[j] :
            z,x,c,v = list_hit[k],list_name[k],list_score[k],list_time[k]
            list_hit[k],list_name[k],list_score[k],list_time[k] = list_hit[j],list_name[j],list_score[j],list_time[j]
            list_hit[j],list_name[j],list_score[j],list_time[j] = z,x,c,v

for i in range(amount_people) :
    stage_pt = (((list_hit[i])/(max(list_hit))*50))
    stage_per = (stage_pt/((max(list_hit)/(max(list_hit)))*50))*100
    print('{0: <8}{1: <13}{2: <12}{3: <20}{4: <15}{5: <20}{6}'.format(i+1,list_score[i],list_time[i],list_name[i],'%.4f'%list_hit[i],'%.4f'%stage_pt,'%.2f'%stage_per))
