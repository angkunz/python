class nisit :
    def __init__(self,namelastname,clas,sex,department,province) :
        self.namelastname = namelastname
        self.clas = clas
        self.sex = sex
        self.department = department
        self.province = province

    def shownisit(self) :
        print(30*'-'+'แนะนำตัว'+30*'-')
        sex = self.sex
        sex.lower
        if sex == 'ชาย'or 'men' :
            print('สวัสดีครับ ผมชื่อ',self.namelastname+'  นักศึกษาชั้นปีที่ '+self.clas+'  สาขา '+self.department+'  มาจากจังหวัด '+self.province)
        else :
            print('สวัสดีค่ะ ดิฉันชื่อ',self.namelastname+'  นักศึกษาชั้นปีที่ '+self.clas+'  สาขา '+self.department+'  มาจากจังหวัด '+self.province)

date = []
nisitt = input('ชื่อ-นามสกุล,ชั้นปี,เพศ,สาขาวิชา,จังหวัด : ')
split_nisitt = nisitt.split(',')
date.append(split_nisitt[0])
date.append(split_nisitt[1])
date.append(split_nisitt[2])
date.append(split_nisitt[3])
date.append(split_nisitt[4])


x = nisit(date[0],date[1],date[2],date[3],date[4])
x.shownisit()
