import sqlite3
import pandas as pd

conn = sqlite3.connect('ghi.db')
conn.execute('''DROP TABLE IF EXISTS disease2010''')
conn.execute('''DROP TABLE IF EXISTS disease2013''')
conn.execute('''DROP TABLE IF EXISTS disease2015''')
conn.execute('''DROP TABLE IF EXISTS disbars''')
conn.execute('''DROP TABLE IF EXISTS distypes''')
conn.execute('''DROP TABLE IF EXISTS disbars2010B2015''')
conn.execute('''DROP TABLE IF EXISTS distypes2010B2015''')

conn.execute('''CREATE TABLE disease2013
             (disease text, distype text, impact real, daly real, need text, color text)''')

conn.execute('''CREATE TABLE disease2010
             (disease text, distype text, impact real, daly real, need text, color text)''')

conn.execute('''CREATE TABLE disease2015
             (disease text, distype text, impact real, daly real, need text, color text)''')

conn.execute('''CREATE TABLE disbars
            (disease text, color text, efficacy2010 real, efficacy2013 real, coverage2010 real, coverage2013 real, need2010 real, need2013 real)''')

conn.execute('''CREATE TABLE distypes
            (disease text,distype text, color text, efficacy2010 real, efficacy2013 real, coverage2010 real, coverage2013 real,position real)''')

conn.execute('''CREATE TABLE disbars2010B2015
            (disease text, color text, efficacy2010 real, efficacy2013 real, coverage2010 real, coverage2013 real, need2010 real, need2013 real)''')

conn.execute('''CREATE TABLE distypes2010B2015
            (disease text,distype text, color text, efficacy2010 real, efficacy2013 real, coverage2010 real, coverage2013 real,position real)''')



#datasrc = 'https://docs.google.com/spreadsheets/d/1IBfN_3f-dG65YbLWQbkXojUxs2PlQyo7l04Ubz9kLkU/pub?gid=1560508440&single=true&output=csv'
datasrc = 'ORS_GlobalBurdenDisease_2010_2013.csv'
df = pd.read_csv(datasrc, skiprows=1)
#datasrc2 = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQI7j2NartMCCF_N-OCkFqAyD67N9Q32yybE21x-zaRPrETsszdZep91dVVVSCjeXXbPjPfZVdE-odE/pub?gid=1560508440&single=true&output=csv'
datasrc2 = 'ORS_GlobalBurdenDisease_2010_2013.csv'
datasrc3 = 'ORS_GlobalBurdenDisease_2010B_2015.csv'
df2 = pd.read_csv(datasrc2, skiprows=1)
df_2010B_2015 = pd.read_csv(datasrc3, skiprows=1)

disease2010db = []
disease2013db = []
disease2015db = []

i = 0
for k in range(8,20):
    distypes = ['TB','TB','TB','Malaria','Malaria','HIV','Roundworm','Hookworm','Whipworm','Schistosomiasis','Onchoceriasis','LF']
    colors = ['#FFB31C','#FFB31C','#FFB31C','#0083CA','#0083CA','#EF3E2E','#003452','#86AAB9','#CAEEFD','#546675','#8A5575','#305516']
    dis = ['Drug Susceptable TB','MDR-TB','XDR-TB','p. falc Malaria','p. vivax Malaria','HIV','Roundworm','Hookworm','Whipworm','Schistosomiasis','Onchoceriasis','LF']
    color = colors[i]
    disease = dis[i]
    distype = distypes[i]
    temp = df.iloc[k,43]
    print(temp)
    temp1 = df.iloc[k,45]
    print(temp1)
    temp2 = df.iloc[k,46]
    print(temp2)
    if type(temp) != float and type(temp1)!=float and type(temp2)!=float:
        impact = float(temp.replace(',',''))
        daly = float(temp1.replace(',',''))
        need = float(temp2.replace(',',''))
        i += 1
        row = [disease,distype,impact,daly,need,color]
        disease2010db.append(row)
        conn.execute('insert into disease2010 values (?,?,?,?,?,?)', row)

i = 0
for k in range(8,20):
    distypes = ['TB','TB','TB','Malaria','Malaria','HIV','Roundworm','Hookworm','Whipworm','Schistosomiasis','Onchoceriasis','LF']
    colors = ['#FFB31C','#FFB31C','#FFB31C','#0083CA','#0083CA','#EF3E2E','#003452','#86AAB9','#CAEEFD','#546675','#8A5575','#305516']
    dis = ['Drug Susceptable TB','MDR-TB','XDR-TB','p. falc Malaria','p. vivax Malaria','HIV','Roundworm','Hookworm','Whipworm','Schistosomiasis','Onchoceriasis','LF']
    color = colors[i]
    disease = dis[i]
    distype = distypes[i]
    temp = df.iloc[k,94]
    temp1 = df.iloc[k,96]
    temp2 = df.iloc[k,97]
    print(temp)
    print(temp1)
    print(temp2)
    print(distype)
    print(disease)
    if type(temp) != float and type(temp1)!=float and type(temp2)!=float:
        impact = float(temp.replace(',',''))
        daly = float(temp1.replace(',',''))
        need = float(temp2.replace(',',''))
        i += 1
        row = [disease,distype,impact,daly,need,color]
        disease2013db.append(row)
        conn.execute('insert into disease2013 values (?,?,?,?,?,?)', row)
i = 0
for k in range(8,20):
    distypes = ['TB','TB','TB','Malaria','Malaria','HIV','Roundworm','Hookworm','Whipworm','Schistosomiasis','Onchoceriasis','LF']
    colors = ['#FFB31C','#FFB31C','#FFB31C','#0083CA','#0083CA','#EF3E2E','#003452','#86AAB9','#CAEEFD','#546675','#8A5575','#305516']
    dis = ['Drug Susceptable TB','MDR-TB','XDR-TB','p. falc Malaria','p. vivax Malaria','HIV','Roundworm','Hookworm','Whipworm','Schistosomiasis','Onchoceriasis','LF']
    color = colors[i]
    disease = dis[i]
    distype = distypes[i]
    temp = df_2010B_2015.iloc[k,94]
    temp1 = df_2010B_2015.iloc[k,96]
    temp2 = df_2010B_2015.iloc[k,97]
    print(temp)
    print(temp1)
    print(temp2)
    print(distype)
    print(disease)
    if type(temp) != float and type(temp1)!=float and type(temp2)!=float:
        impact = float(temp.replace(',',''))
        daly = float(temp1.replace(',',''))
        need = float(temp2.replace(',',''))
        i += 1
        row = [disease,distype,impact,daly,need,color]
        disease2013db.append(row)
        conn.execute('insert into disease2015 values (?,?,?,?,?,?)', row)

def stripdata(x,y):
    tmp = df.iloc[x,y]
    if tmp=="#DIV/0!" or tmp=="nan":
        return(0)
    if isinstance(tmp,float) == False:
        return(float(tmp.replace(',','').replace(' ','0').replace('%','')))
    else:
        return(0)

def stripdata3(x,y):
    tmp = df_2010B_2015.iloc[x,y]
    if tmp=="#DIV/0!" or tmp=="nan":
        return(0)
    if isinstance(tmp,float) == False:
        return(float(tmp.replace(',','').replace(' ','0').replace('%','')))
    else:
        return(0)

def stripdata2(x,y):
    tmp = df2.iloc[x,y]
    if tmp=="#DIV/0!" or tmp=="nan":
        return(0)
    if isinstance(tmp,float) == False:
        res = float(tmp.replace(',','').replace(' ','0').replace('%',''))
        if res > 10000:
            res = res * 0.00001
        #print(res)
        return (0.01*res)
    else:
        return(0)

disbars = []
j=0
for k in range(91, 100):
    colors = ['#FFB31C', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
              '#546675', '#8A5575', '#305516']
    diseasename = df.iloc[k,7]
    newdiseasename = df_2010B_2015.iloc[k,7]
    print(diseasename)
    color = colors[j]
    efficacy2010 = stripdata(k,8)
    efficacy2013 = stripdata(k,9)
    coverage2010 = stripdata(k,10)
    coverage2013 = stripdata(k,11)
    need2010 = stripdata(k,12)
    need2013 = stripdata(k,13)

    newefficacy2010 = stripdata3(k,8)
    newefficacy2013 = stripdata3(k,9)
    newcoverage2010 = stripdata3(k,10)
    newcoverage2013 = stripdata3(k,11)
    newneed2010 = stripdata3(k,12)
    newneed2013 = stripdata3(k,13)

    roww = [diseasename,color,efficacy2010,efficacy2013,coverage2010,coverage2013,need2010,need2013]
    newroww = [diseasename,color,newefficacy2010,newefficacy2013,newcoverage2010,newcoverage2013,newneed2010,newneed2013]
    print(roww)
    disbars.append(roww)
    j+=1
    conn.execute('insert into disbars values (?,?,?,?,?,?,?,?)', roww)
    print(newdiseasename)
    if(newdiseasename == 0):
        print("do nothing")
    else:
        conn.execute('insert into disbars2010B2015 values (?,?,?,?,?,?,?,?)', newroww)


#=====================================Jing-3/3/2-18============================================
i=1
j=0
mark=0
efficacy2010 = 0
efficacy2013 = 0
coverage2010 = 0
coverage2013 = 0
for k in [94,96,98,99,100,102]:
    colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
              '#546675', '#8A5575', '#305516']
    dismap =[2,3,1]
    position = [2,0,1]
    disease = ['Normal-TB','MDR-TB','XDR-TB']
    disetype='TB'
    m = dismap[mark]
    p = position[mark]
    color=colors[j%12]
    diseasename = disease[mark]
    efficacy2010 += stripdata(k,1)
    efficacy2013 += stripdata(k,2)
    coverage2010 += stripdata(k,3)
    coverage2013 += stripdata(k,5)

    newefficacy2010 += stripdata3(k,1)
    newefficacy2013 += stripdata3(k,2)
    newcoverage2010 += stripdata3(k,3)
    newcoverage2013 += stripdata3(k,5)
    print('==========efficacy2010=====')

    if i==m :
        efficacy2010 /= m
        efficacy2013 /= m
        coverage2010 /= m
        coverage2013 /= m

        newefficacy2010 /= m
        newefficacy2013 /= m
        newcoverage2010 /= m
        newcoverage2013 /= m

        i=0
        mark+=1
        roww = [diseasename,disetype,color,efficacy2010,efficacy2013,coverage2010,coverage2013,p]
        distypes.append(roww)

        newroww = [diseasename,disetype,color,newefficacy2010,newefficacy2013,newcoverage2010,newcoverage2013,p]

        print(roww)
        conn.execute('insert into distypes values (?,?,?,?,?,?,?,?)', roww)
        conn.execute('insert into distypes2010B2015 values (?,?,?,?,?,?,?,?)', newroww)
        efficacy2010 = 0
        efficacy2013 = 0
        coverage2010 = 0
        coverage2013 = 0

        newefficacy2010 = 0
        newefficacy2013 = 0
        newcoverage2010 = 0
        newcoverage2013 = 0

    j+=1
    i+=1
cur = conn.execute(' select * from distypes where distype=? ',('TB',))
data = cur.fetchall()

#print(data)
#print(data)
i=1
j=0
mark=0
efficacy2010 = 0
efficacy2013 = 0
coverage2010 = 0
coverage2013 = 0
for k in [111,104,105,106,107,108,109]:
    colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
              '#546675', '#8A5575', '#305516']
    dismap =[1,6]
    position = [0,1]
    disease = ['p. falc Malaria', 'p. vivax Malaria']
    disetype='Malaria'
    m = dismap[mark]
    p = position[mark]
    color=colors[j%12]
    diseasename = disease[mark]
    efficacy2010 += stripdata(k,1)
    efficacy2013 += stripdata(k,2)
    coverage2010 += stripdata(k,3)
    coverage2013 += stripdata(k,5)


    newefficacy2010 += stripdata3(k,1)
    newefficacy2013 += stripdata3(k,2)
    newcoverage2010 += stripdata3(k,3)
    newcoverage2013 += stripdata3(k,5)
    print('==========This is Malaria=====')

    if i==m :
        efficacy2010 /= m
        efficacy2013 /= m
        coverage2010 /= m
        coverage2013 /= m

        newefficacy2010 /= m
        newefficacy2013 /= m
        newcoverage2010 /= m
        newcoverage2013 /= m

        i=0
        mark+=1
        roww = [diseasename,disetype,color,efficacy2010,efficacy2013,coverage2010,coverage2013,p]
        distypes.append(roww)
        print(roww)
        newroww = [diseasename,disetype,color,newefficacy2010,newefficacy2013,newcoverage2010,newcoverage2013,p]
        conn.execute('insert into distypes values (?,?,?,?,?,?,?,?)', roww)
        conn.execute('insert into distypes2010B2015 values (?,?,?,?,?,?,?,?)', newroww)
        efficacy2010 = 0
        efficacy2013 = 0
        coverage2010 = 0
        coverage2013 = 0
        newefficacy2010 = 0
        newefficacy2013 = 0
        newcoverage2010 = 0
        newcoverage2013 = 0

    j+=1
    i+=1
cur = conn.execute(' select * from distypes where distype=? ',('Malaria',))
data = cur.fetchall()
print(data)

i=1
j=0
mark=0
efficacy2010 = 0
efficacy2013 = 0
coverage2010 = 0
coverage2013 = 0
for k in [148,149,150,151,152,153]:
    colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
              '#546675', '#8A5575', '#305516']
    #dismap =[2,3,1]
    position = [5,4,3,2,1,0]
    disease = ['Alb', 'Mbd', 'Ivm + Alb', 'Dec + Alb', 'Pzq + Alb', 'Pzq + Mbd']
    disetype='Hookworm'
    p = position[mark]
    color=colors[j%12]
    diseasename = disease[mark]
    efficacy2010 += stripdata(k,1)
    efficacy2013 += stripdata(k,2)
    coverage2010 += stripdata(k,3)
    coverage2013 += stripdata(k,5)

    newefficacy2010 += stripdata3(k,1)
    newefficacy2013 += stripdata3(k,2)
    newcoverage2010 += stripdata3(k,3)
    newcoverage2013 += stripdata3(k,5)
    print('==========This is Hookworm=====')
    i=0
    roww = [diseasename,disetype,color,efficacy2010,efficacy2013,coverage2010,coverage2013,p]
    distypes.append(roww)
    print(roww)
    newroww = [diseasename,disetype,color,newefficacy2010,newefficacy2013,newcoverage2010,newcoverage2013,p]
    conn.execute('insert into distypes values (?,?,?,?,?,?,?,?)', roww)
    conn.execute('insert into distypes2010B2015 values (?,?,?,?,?,?,?,?)', roww)
    efficacy2010 = 0
    efficacy2013 = 0
    coverage2010 = 0
    coverage2013 = 0
    newefficacy2010 = 0
    newefficacy2013 = 0
    newcoverage2010 = 0
    newcoverage2013 = 0
    mark+=1
    j+=1
cur = conn.execute(' select * from distypes where distype=? ',('Hookworm',))
data = cur.fetchall()
print(data)

i=1
j=0
mark=0
for k in [155,156,157,158,159,160]:
    colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
              '#546675', '#8A5575', '#305516']
    #dismap =[2,3,1]
    position = [5,4,3,2,1,0]
    disease = ['Alb', 'Mbd', 'Ivm + Alb', 'Dec + Alb', 'Pzq + Alb', 'Pzq + Mbd']
    disetype='Whipworm'
    p = position[mark]
    color=colors[j%12]
    diseasename = disease[mark]
    efficacy2010 += stripdata(k,1)
    efficacy2013 += stripdata(k,2)
    coverage2010 += stripdata(k,3)
    coverage2013 += stripdata(k,5)
    print('==========This is Whipworm=====')
    newefficacy2010 += stripdata3(k,1)
    newefficacy2013 += stripdata3(k,2)
    newcoverage2010 += stripdata3(k,3)
    newcoverage2013 += stripdata3(k,5)
    i=0
    roww = [diseasename,disetype,color,efficacy2010,efficacy2013,coverage2010,coverage2013,p]
    distypes.append(roww)
    print(roww)
    newroww = [diseasename,disetype,color,efficacy2010,efficacy2013,coverage2010,coverage2013,p]
    conn.execute('insert into distypes values (?,?,?,?,?,?,?,?)', roww)
    conn.execute('insert into distypes2010B2015 values (?,?,?,?,?,?,?,?)', newroww)
    efficacy2010 = 0
    efficacy2013 = 0
    coverage2010 = 0
    coverage2013 = 0
    newefficacy2010 = 0
    newefficacy2013 = 0
    newcoverage2010 = 0
    newcoverage2013 = 0
    mark+=1
    j+=1
cur = conn.execute(' select * from distypes where distype=? ',('Whipworm',))
data = cur.fetchall()
print(data)

i=1
j=0
mark=0
for k in [162,163,164,165,166,167]:
    colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
              '#546675', '#8A5575', '#305516']
    #dismap =[2,3,1]
    position = [5,4,3,2,1,0]
    disease = ['Ivm + Alb', 'Dec + Alb', 'Pzq', 'Ivm', 'Dec', 'Alb']
    disetype='Schistosomiasis'
    p = position[mark]
    color=colors[j%12]
    diseasename = disease[mark]
    efficacy2010 += stripdata(k,1)
    efficacy2013 += stripdata(k,2)
    coverage2010 += stripdata(k,3)
    coverage2013 += stripdata(k,5)
    print('==========This is Schistosomiasis=====')
    newefficacy2010 += stripdata3(k,1)
    newefficacy2013 += stripdata3(k,2)
    newcoverage2010 += stripdata3(k,3)
    newcoverage2013 += stripdata3(k,5)
    i=0
    roww = [diseasename,disetype,color,efficacy2010,efficacy2013,coverage2010,coverage2013,p]
    distypes.append(roww)
    print(roww)
    newroww = [diseasename,disetype,color,newefficacy2010,newefficacy2013,newcoverage2010,newcoverage2013,p]
    conn.execute('insert into distypes values (?,?,?,?,?,?,?,?)', roww)
    conn.execute('insert into distypes2010B2015 values (?,?,?,?,?,?,?,?)', newroww)
    efficacy2010 = 0
    efficacy2013 = 0
    coverage2010 = 0
    coverage2013 = 0
    newefficacy2010 = 0
    newefficacy2013 = 0
    newcoverage2010 = 0
    newcoverage2013 = 0
    mark+=1
    j+=1
cur = conn.execute(' select * from distypes where distype=? ',('Schistosomiasis',))
data = cur.fetchall()
print(data)


i=1
j=0
mark=0
for k in [169,170,171,172]:
    colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
              '#546675', '#8A5575', '#305516']
    #dismap =[2,3,1]
    position = [3,2,1,0]
    disease = ['Nodulectomy', 'Suramin', 'Ivm', 'Dec']
    disetype='Onchoceriasis'
    p = position[mark]
    color=colors[j%12]
    diseasename = disease[mark]
    efficacy2010 += stripdata(k,1)
    efficacy2013 += stripdata(k,2)
    coverage2010 += stripdata(k,3)
    coverage2013 += stripdata(k,5)

    newefficacy2010 += stripdata3(k,1)
    newefficacy2013 += stripdata3(k,2)
    newcoverage2010 += stripdata3(k,3)
    newcoverage2013 += stripdata3(k,5)
    print('==========This is Onchoceriasis=====')
    i=0
    roww = [diseasename,disetype,color,efficacy2010,efficacy2013,coverage2010,coverage2013,p]
    distypes.append(roww)
    print(roww)
    newroww = [diseasename,disetype,color,efficacy2010,efficacy2013,coverage2010,coverage2013,p]
    conn.execute('insert into distypes values (?,?,?,?,?,?,?,?)', roww)
    conn.execute('insert into distypes2010B2015 values (?,?,?,?,?,?,?,?)', newroww)
    efficacy2010 = 0
    efficacy2013 = 0
    coverage2010 = 0
    coverage2013 = 0
    newefficacy2010 = 0
    newefficacy2013 = 0
    newcoverage2010 = 0
    newcoverage2013 = 0
    mark+=1
    j+=1
cur = conn.execute(' select * from distypes where distype=? ',('Onchoceriasis',))
data = cur.fetchall()
print(data)

i=1
j=0
mark=0
for k in [174,175,176]:
    colors = ['#FFB31C', '#FFB31C', '#FFB31C', '#0083CA', '#0083CA', '#EF3E2E', '#003452', '#86AAB9', '#CAEEFD',
              '#546675', '#8A5575', '#305516']
    #dismap =[2,3,1]
    position = [2,1,0]
    disease = ['Dec', 'Dec + Alb', 'Ivm + Alb']
    disetype='LF'
    p = position[mark]
    color=colors[j%12]
    diseasename = disease[mark]
    efficacy2010 += stripdata(k,1)
    efficacy2013 += stripdata(k,2)
    coverage2010 += stripdata(k,3)
    coverage2013 += stripdata(k,5)
    print('==========This is LF=====')
    newefficacy2010 += stripdata3(k,1)
    newefficacy2013 += stripdata3(k,2)
    newcoverage2010 += stripdata3(k,3)
    newcoverage2013 += stripdata3(k,5)
    i=0
    roww = [diseasename,disetype,color,efficacy2010,efficacy2013,coverage2010,coverage2013,p]
    distypes.append(roww)
    print(roww)
    newroww = [diseasename,disetype,color,newefficacy2010,newefficacy2013,newcoverage2010,newcoverage2013,p]
    conn.execute('insert into distypes values (?,?,?,?,?,?,?,?)', roww)
    conn.execute('insert into distypes2010B2015 values (?,?,?,?,?,?,?,?)', newroww)
    efficacy2010 = 0
    efficacy2013 = 0
    coverage2010 = 0
    coverage2013 = 0
    newefficacy2010 = 0
    newefficacy2013 = 0
    newcoverage2010 = 0
    newcoverage2013 = 0
    mark+=1
    j+=1
cur = conn.execute(' select * from distypes where distype=? ',('LF',))
data = cur.fetchall()

conn.commit()
print("Database operation complete")
