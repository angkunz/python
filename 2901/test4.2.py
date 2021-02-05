import os
dictionary  = {
    'cat':'n.\t\tแมว',
    'dog':'n.\t\tสุนัข',
    'run':'v.\t\tวิ่ง',
    'sad':'adv.\t\tเศร้าใจ',
    'fly':'v.\t\tบิน',
}

def menu():
    global choice
    print('พจนานุกรม\n1) เพิ่มคำศัพท์\n2) แสดงคำศัพท์\n3) ลบคำศัพท์\n4) ออกจากโปรแกรม\n')
    choice = input('Input Choice : ')

def add():
    word = input('เพิ่มคำศัพท์ :\t')
    tword = input('( n. , v. , adj. , adv.) : ')
    mean = input('ความหมาย :\t')
    dictionary[word] = tword+'\t\t'+mean
    print('เพื่มคำศัพท์เรียบร้อยแล้ว')

def show():
    print('\tคำศัพท์ทั้งหมด\n{0:<15}{1:<16}{2}'.format('คำศัพท์','ประเภท','ความหมาย'))
    for i in dictionary:
        print('{}{:<11}{}'.format(i,'',dictionary[i]))

def delete():
    dword = input('พิมพ์คำศัพท์ที่ต้องการลบ: ')
    yesno = input('ต้องการลบ {} ใช่หรือไม่ (y/n) : '.format(dword))
    if yesno == 'y':
        del dictionary[dword]
        print('ลบ'+dword+'เรียบร้อยแล้ว')

while True:
    menu()
    if choice == '1':
        add()
    elif choice == '2':
        show()
    elif choice == '3':
        delete()
    else:
        yesno2=input('ต้องการออกจากโปรแกรมใช่หรือไม่ y/n : ')
        if yesno2 == 'y':
            break
        elif yesno2 == 'n':
            continue