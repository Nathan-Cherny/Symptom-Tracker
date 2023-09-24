"""
############## Are you diagnose with... corresponding numbers ##########
0 - disease is unknown
1 - Stomach Bug
2 - Covid
3 - Cold

################Dorm's corresponding number ###########
1-Kardon
2-Atlantic terminal
3-University village
4-White Hall
5-J&H
6-1940
7-conwell
8-Beech internation
9-The edge
10-Morgan
11-Oxford
12-1300
13-Temple Towers
"""

## Dummy Data ##
sym1 = [True, True, False, True, False, True, False, False, True, True, False, False, False, False, False, False]
sym2 = [True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, True]
sym3 = [False, True, False, False, True, True, False, False, True, False, False, False, False, False, False, False]
sym4 = [True, True, False, False, True, True, False, False, True, False, False, True, True, False, False, False]
stu1 = [1]
stu2 = [4]
stu3 = [10]







############
diseaseKnown = 0

schoolsickData = []

oneStomach = 0 
oneCovid = 0
oneCold = 0

twoStomach = 0 
twoCovid = 0
twoCold = 0

threeStomach = 0 
threeCovid = 0
threeCold = 0
    
fourStomach = 0 
fourCovid = 0
fourCold = 0

fiveStomach = 0 
fiveCovid = 0
fiveCold = 0

sixStomach = 0 
sixCovid = 0
sixCold = 0

sevenStomach = 0 
sevenCovid = 0
sevenCold = 0

eightStomach = 0 
eightCovid = 0
eightCold = 0

nineStomach = 0 
nineCovid = 0
nineCold = 0

tenStomach = 0 
tenCovid = 0
tenCold = 0

elevenStomach = 0 
elevenCovid = 0
elevenCold = 0

twelveStomach = 0 
twelveCovid = 0
twelveCold = 0

thirteenStomach = 0 
thirteenCovid = 0
thirteenCold = 0



#Calculates probability of each sickness based on symptoms, adds most likely sickness to list of cases
def surveySickness(stu, sym):

    coldValue = 0
    covidValue = 0
    stomachBugValue = 0

    cough = sym[0]
    fever = sym[1]
    chills = sym[2]
    breathing = sym[3]
    taste = sym[4]
    smell = sym[5]
    fatigue = sym[6]
    vomit = sym[7]
    nausea = sym[8]
    stomach = sym[9]
    diarrhea = sym[10]
    nose = sym[11]
    throat = sym[12]
    smoker = sym[13]
    drink = sym[14]
    nearSick = sym[15]

    symptomList = [cough, fever, chills, breathing, taste, smell, fatigue, vomit, nausea, stomach, diarrhea, nose, throat, smoker, drink, nearSick]

    stomachBugMultiplier = [0,0,0,0,0,0,1,0,1,2,2,0,0] ##Some symptoms count more than others

    covidMultiplier = [2,1,1,2,1,1,1,0,0,0,0,0,1]

    coldMultiplier = [1,1,0,0,0,0,0,0,0,0,0,2,1]

    
    if(diseaseKnown == 1):
        stomachBugValue = 1
    elif(diseaseKnown == 2):
        covidValue = 1
    elif(diseaseKnown == 3):
        coldValue = 1
    elif(diseaseKnown == 0): 
        
        for i in range(len(symptomList)-3): #Calculating confidence in user's illness
            stomachBugValue += stomachBugMultiplier[i]*symptomList[i]  
            covidValue += covidMultiplier[i]*symptomList[i]
            coldValue += coldMultiplier[i]*symptomList[i]
        stomachBugValue = stomachBugValue - (drink) 
        covidValue = covidValue - smoker - (drink) + (2*nearSick)
        coldValue = coldValue - (smoker) - (drink) + (2*nearSick)
        

        stomachBugValue = float(stomachBugValue/sum(stomachBugMultiplier))
        covidValue = float(covidValue/sum(covidMultiplier))
        coldValue = float(coldValue/sum(coldMultiplier))

        studentSickData = [] #each element is dorm, illness, confidence in illness

        if (stomachBugValue > coldValue) and (stomachBugValue > covidValue):
            stu.append("Stomach Bug")
            stu.append(stomachBugValue)
        
        elif (covidValue > coldValue) and (covidValue > stomachBugValue):
            stu.append("Covid")
            stu.append(covidValue)
        elif (coldValue > covidValue) and (coldValue > stomachBugValue):
            stu.append("Common Cold")
            stu.append(coldValue)
        else:
            stu.append("Inconclusive")
            values = [coldValue, covidValue, stomachBugValue]
            values.sort()
            stu.append(values[2])

    schoolsickData.append(stu)
    return(stu)
    

#Calculates illness level of dorm (red/orange/green)
def getRiskData(): 
    global oneStomach
    global oneCovid 
    global oneCold 

    global twoStomach  
    global twoCovid 
    global twoCold 

    global threeStomach  
    global threeCovid 
    global threeCold 
        
    global fourStomach  
    global fourCovid 
    global fourCold 

    global fiveStomach 
    global fiveCovid 
    global fiveCold 

    global sixStomach  
    global sixCovid 
    global sixCold 

    global sevenStomach  
    global sevenCovid 
    global sevenCold 

    global eightStomach 
    global eightCovid 
    global eightCold 

    global nineStomach 
    global nineCovid 
    global nineCold 

    global tenStomach 
    global tenCovid 
    global tenCold 

    global elevenStomach 
    global elevenCovid 
    global elevenCold 

    global twelveStomach  
    global twelveCovid 
    global twelveCold 

    global thirteenStomach  
    global thirteenCovid 
    global thirteenCold 

   
    for student in schoolsickData:
        if student[0] == 1:
            if student[1] == "Stomach Bug":
                if student[2] > 0.3:
                    if student[2] >= 0.8: #More confident values count twice
                        oneStomach += 2
                    else:
                        oneStomach += 1
            elif student[1] == "Covid":
                if student[2] > 0.3:
                    if student[2] >= 0.8:
                        oneCovid += 2
                    else:
                        oneCovid += 1
            elif student[1] == "Common Cold":
                if student[2] > 0.3:
                    if student[2] >= 0.8:
                        oneCold += 2
                    else:
                        oneCold += 1
        ##################################################
        elif student[0] == 2:
                if student[1] == "Stomach Bug":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            twoStomach += 2
                        else:
                            twoStomach += 1
                elif student[1] == "Covid":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            twoCovid += 2
                        else:
                            twoCovid += 1
                elif student[1] == "Common Cold":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            twoCold += 2
                        else:
                            twoCold += 1
##################################################
        elif student[0] == 3: 
                if student[1] == "Stomach Bug":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            threeStomach += 2
                        else:
                            threeStomach += 1
                elif student[1] == "Covid":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            threeCovid += 2
                        else:
                            threeCovid += 1
                elif student[1] == "Common Cold":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            threeCold += 2
                        else:
                            threeCold += 1

##################################################
        elif student[0] == 4: 
                if student[1] == "Stomach Bug":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            fourStomach += 2
                        else:
                            fourStomach += 1
                elif student[1] == "Covid":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            fourCovid += 2
                        else:
                            fourCovid += 1
                elif student[1] == "Common Cold":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            fourCold += 2
                        else:
                            fourCold += 1         

##################################################
        elif student[0] == 5:  
                if student[1] == "Stomach Bug":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            fiveStomach += 2
                        else:
                            fiveStomach += 1
                elif student[1] == "Covid":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            fiveCovid += 2
                        else:
                            fiveCovid += 1
                elif student[1] == "Common Cold":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            fiveCold += 2
                        else:
                            fiveCold += 1       

##################################################
        elif student[0] == 6:   
                if student[1] == "Stomach Bug":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            sixStomach += 2
                        else:
                            sixStomach += 1
                elif student[1] == "Covid":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            sixCovid += 2
                        else:
                            sixCovid += 1
                elif student[1] == "Common Cold":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            sixCold += 2
                        else:
                            sixCold += 1     

##################################################
        elif student[0] == 7:    
                if student[1] == "Stomach Bug":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            sevenStomach += 2
                        else:
                            sevenStomach += 1
                elif student[1] == "Covid":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            sevenCovid += 2
                        else:
                            sevenCovid += 1
                elif student[1] == "Common Cold":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            sevenCold += 2
                        else:
                            sevenCold += 1      

##################################################
        elif student[0] == 8:     
                if student[1] == "Stomach Bug":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            eightStomach += 2
                        else:
                            eightStomach += 1
                elif student[1] == "Covid":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            eightCovid += 2
                        else:
                            eightCovid += 1
                elif student[1] == "Common Cold":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            eightCold += 2
                        else:
                            eightCold += 1         

##################################################
        elif student[0] == 9:      
                if student[1] == "Stomach Bug":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            nineStomach += 2
                        else:
                            nineStomach += 1
                elif student[1] == "Covid":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            nineCovid += 2
                        else:
                            nineCovid += 1
                elif student[1] == "Common Cold":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            nineCold += 2
                        else:
                            nineCold += 1    

##################################################
        elif student[0] == 10:       
                if student[1] == "Stomach Bug":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            tenStomach += 2
                        else:
                            tenStomach += 1
                elif student[1] == "Covid":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            tenCovid += 2
                        else:
                            tenCovid += 1
                elif student[1] == "Common Cold":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            tenCold += 2
                        else:
                            tenCold += 1 

##################################################
        elif student[0] == 11:        
                if student[1] == "Stomach Bug":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            elevenStomach += 2
                        else:
                            elevenStomach += 1
                elif student[1] == "Covid":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            elevenCovid += 2
                        else:
                            elevenCovid += 1
                elif student[1] == "Common Cold":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            elevenCold += 2
                        else:
                            elevenCold += 1 

##################################################
        elif student[0] == 12:         
                if student[1] == "Stomach Bug":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            twelveStomach += 2
                        else:
                            twelveStomach += 1
                elif student[1] == "Covid":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            twelveCovid += 2
                        else:
                            twelveCovid += 1
                elif student[1] == "Common Cold":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            twelveCold += 2
                        else:
                            twelveCold += 1 

##################################################
        elif student[0] == 13:          
                if student[1] == "Stomach Bug":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            thirteenStomach += 2
                        else:
                            thirteenStomach += 1
                elif student[1] == "Covid":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            thirteenCovid += 2
                        else:
                            thirteenCovid += 1
                elif student[1] == "Common Cold":
                    if student[2] > 0.3:
                        if student[2] >= 0.8:
                            thirteenCold += 2
                        else:
                            thirteenCold += 1



'''
n - dorm
gives level (green/orange/red) of dorm
1 - green
2 - orange
3 - red
'''
def getRiskLevel(n): ################################### getRiskArea
        oneRisk = 0
        twoRisk = 0
        threeRisk = 0
        fourRisk = 0
        fiveRisk = 0
        sixRisk = 0
        sevenRisk = 0
        eightRisk = 0
        nineRisk = 0
        tenRisk = 0
        elevenRisk = 0
        twelveRisk = 0
        thirteenRisk = 0

        if n == 1:
            if (oneCold > 60) or (oneCovid > 60) or (oneStomach > 60): 
                oneRisk = 3
            elif (oneCold > 30) or (oneCovid > 30) or (oneStomach > 30):
                oneRisk = 2
            else:
                oneRisk = 1
            return oneRisk

        elif n == 2:
            if (twoCold > 60) or (twoCovid > 60) or (twoStomach > 60):
                twoRisk = 3
            elif (twoCold > 30) or (twoCovid > 30) or (twoStomach > 30):
                twoRisk = 2
            else:
                twoRisk = 1
            return twoRisk

        elif n == 3:
            if (threeCold > 60) or (threeCovid > 60) or (threeStomach > 60):
                threeRisk = 3
            elif (threeCold > 30) or (threeCovid > 30) or (threeStomach > 30):
                threeRisk = 2
            else:
                threeRisk = 1
            return threeRisk

        elif n == 4:
            if (fourCold > 60) or (fourCovid > 60) or (fourStomach > 60):
                fourRisk = 3
            elif (fourCold > 30) or (fourCovid > 30) or (fourStomach > 30):
                fourRisk = 2
            else:
                fourRisk = 1
            return fourRisk

        elif n == 5:
            if (fiveCold > 60) or (fiveCovid > 60) or (fiveStomach > 60):
                fiveRisk = 3
            elif (fiveCold > 30) or (fiveCovid > 30) or (fiveStomach > 30):
                fiveRisk = 2
            else:
                fiveRisk = 1
            return fiveRisk


        elif n == 6:
            if (sixCold > 60) or (sixCovid > 60) or (sixStomach > 60):
                sixRisk = 3
            elif (sixCold > 30) or (sixCovid > 30) or (sixStomach > 30):
                sixRisk = 2
            else:
                sixRisk = 1
            return sixRisk

        elif n == 7:
            if (sevenCold > 60) or (sevenCovid > 60) or (sevenStomach > 60):
                sevenRisk = 3
            elif (sevenCold > 30) or (sevenCovid > 30) or (sevenStomach > 30):
                sevenRisk = 2
            else:
                sevenRisk = 1
            return sevenRisk

        elif n == 8: 
            if (eightCold > 60) or (eightCovid > 60) or (eightStomach > 60):
                eightRisk = 3
            elif (eightCold > 30) or (eightCovid > 30) or (eightStomach > 30):
                eightRisk = 2
            else:
                eightRisk = 1
            return eightRisk

        elif n == 9: 
            if (nineCold > 60) or (nineCovid > 60) or (nineStomach > 60):
                nineRisk = 3
            elif (nineCold > 30) or (nineCovid > 30) or (nineStomach > 30):
                nineRisk = 2
            else:
                nineRisk = 1
            return nineRisk

        elif n == 10: 
            if (tenCold > 60) or (tenCovid > 60) or (tenStomach > 60):
                tenRisk = 3
            elif (tenCold > 30) or (tenCovid > 30) or (tenStomach > 30):
                tenRisk = 2
            else:
                tenRisk = 1
            return tenRisk

        elif n == 11: 
            if (elevenCold > 60) or (elevenCovid > 60) or (elevenStomach > 60):
                elevenRisk = 3
            elif (elevenCold > 30) or (elevenCovid > 30) or (elevenStomach > 30):
                elevenRisk = 2
            else:
                elevenRisk = 1
            return elevenRisk

        elif n == 12: 
            if (twelveCold > 60) or (twelveCovid > 60) or (twelveStomach > 60):
                twelveRisk = 3
            elif (twelveCold > 30) or (twelveCovid > 30) or (twelveStomach > 30):
                twelveRisk = 2
            else:
                twelveRisk = 1
            return twelveRisk

        elif n == 13: 
            if (thirteenCold > 60) or (thirteenCovid > 60) or (thirteenStomach > 60):
                thirteenRisk = 3
            elif (thirteenCold > 30) or (thirteenCovid > 30) or (thirteenStomach > 30):
                thirteenRisk = 2
            else:
                thirteenRisk = 1
            return thirteenRisk
            
'''
n - dorm
gets most common disease(s) of dorm

'''
def getDisease(n): 
    str = ""

    oneflag = False  #Flags used to add "and" if theres more than 1 disease with over 30 cases at a dorm
    twoflag = False
    threeflag = False
    fourflag = False
    fiveflag = False
    sixflag = False
    sevenflag = False
    eightflag = False
    nineflag = False
    tenflag = False
    elevenflag = False
    twelveflag = False
    thirteenflag = False
    if n == 1:
        if oneCold > 30:
            str += "Common cold"
            oneflag = True
        if oneCovid > 30:
            if oneflag:
                str += " and "
            str += "Covid"

        if oneStomach > 30:
            if oneflag:
                str += " and "
            str += "Stomach Bug"
    
    elif n == 2:
        if twoCold > 30:
            str += "Common cold"
            twoflag = True
        if twoCovid > 30:
            if twoflag:
                str += " and "
            str += "Covid"

        if twoStomach > 30:
            if twoflag:
                str += " and "
            str += "Stomach Bug"

    elif n == 3:
        if threeCold > 30:
            str += "Common cold"
            threeflag = True
        if threeCovid > 30:
            if threeflag:
                str += " and "
            str += "Covid"

        if threeStomach > 30:
            if threeflag:
                str += " and "
            str += "Stomach Bug"

    elif n == 4:
        if fourCold > 30:
            str += "Common cold"
            fourflag = True
        if fourCovid > 30:
            if fourflag:
                str += " and "
            str += "Covid"

        if fourStomach > 30:
            if fourflag:
                str += " and "
            str += "Stomach Bug"

    elif n == 5:
        if fiveCold > 30:
            str += "Common cold"
            fiveflag = True
        if fiveCovid > 30:
            if fiveflag:
                str += " and "
            str += "Covid"

        if fiveStomach > 30:
            if fiveflag:
                str += " and "
            str += "Stomach Bug"

    elif n == 6:
        if sixCold > 30:
            str += "Common cold"
            sixflag = True
        if sixCovid > 30:
            if sixflag:
                str += " and "
            str += "Covid"

        if sixStomach > 30:
            if sixflag:
                str += " and "
            str += "Stomach Bug"

    elif n == 7:
        if sevenCold > 30:
            str += "Common cold"
            sevenflag = True
        if sevenCovid > 30:
            if sevenflag:
                str += " and "
            str += "Covid"

        if sevenStomach > 30:
            if sevenflag:
                str += " and "
            str += "Stomach Bug"

    elif n == 8:
        if eightCold > 30:
            str += "Common cold"
            eightflag = True
        if eightCovid > 30:
            if eightflag:
                str += " and "
            str += "Covid"

        if eightStomach > 30:
            if eightflag:
                str += " and "
            str += "Stomach Bug"

    elif n == 9:
        if nineCold > 30:
            str += "Common cold"
            nineflag = True
        if nineCovid > 30:
            if nineflag:
                str += " and "
            str += "Covid"

        if nineStomach > 30:
            if nineflag:
                str += " and "
            str += "Stomach Bug"

    elif n == 10:
        if tenCold > 30:
            str += "Common cold"
            tenflag = True
        if tenCovid > 30:
            if tenflag:
                str += " and "
            str += "Covid"

        if tenStomach > 30:
            if tenflag:
                str += " and "
            str += "Stomach Bug"

    elif n == 11:
        if elevenCold > 30:
            str += "Common cold"
            elevenflag = True
        if elevenCovid > 30:
            if elevenflag:
                str += " and "
            str += "Covid"

        if elevenStomach > 30:
            if elevenflag:
                str += " and "
            str += "Stomach Bug"

    elif n == 12:
        if twelveCold > 30:
            str += "Common cold"
            twelveflag = True
        if twelveCovid > 30:
            if twelveflag:
                str += " and "
            str += "Covid"

        if twelveStomach > 30:
            if twelveflag:
                str += " and "
            str += "Stomach Bug"

    elif n == 13:
        if thirteenCold > 30:
            str += "Common cold"
            thirteenflag = True
        if thirteenCovid > 30:
            if thirteenflag:
                str += " and "
            str += "Covid"

        if thirteenStomach > 30:
            if thirteenflag:
                str += " and "
            str += "Stomach Bug"
    return str
            

if __name__ == "__main__":
    stu01 = surveySickness(stu1, sym1)
    stu02 = surveySickness(stu2, sym2)
    stu03 = surveySickness(stu3, sym3)
    stu04 = surveySickness(stu1, sym1)
    stu05 = surveySickness(stu2, sym4)
    stu06 = surveySickness(stu3, sym2)
    stu07 = surveySickness(stu1, sym2)
    stu08 = surveySickness(stu1, sym2)
    stu09 = surveySickness(stu2, sym4)
    stu010 = surveySickness(stu3, sym4)
    stu011 = surveySickness(stu1, sym2)
    stu012 = surveySickness(stu2, sym2)
    stu013 = surveySickness(stu3, sym2)
    stu014 = surveySickness(stu1, sym3)
    stu015 = surveySickness(stu2, sym3)
    stu1016 = surveySickness(stu3, sym4)
    stu17 = surveySickness(stu1, sym2)
    stu18 = surveySickness(stu2, sym2)
    stu19 = surveySickness(stu3, sym3)
    stu20 = surveySickness(stu1, sym4)
    stu21 = surveySickness(stu2, sym4)
    stu22 = surveySickness(stu3, sym4)
    stu23 = surveySickness(stu1, sym1)
    stu24 = surveySickness(stu2, sym1)
    stu25 = surveySickness(stu3, sym1)
    stu26 = surveySickness(stu2, sym2)
    stu27 = surveySickness(stu2, sym2)
    stu28 = surveySickness(stu3, sym1)
    stu29 = surveySickness(stu1, sym1)
    stu30 = surveySickness(stu2, sym2)
    stu31 = surveySickness(stu3, sym1)
    stu32 = surveySickness(stu1, sym1)
    stu33 = surveySickness(stu2, sym2)
    stu34 = surveySickness(stu3, sym1)
    stu35 = surveySickness(stu2, sym2)
    stu36 = surveySickness(stu2, sym2)
    stu37 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)
    stu38 = surveySickness(stu2, sym2)     
    getRiskData()
    x = getRiskLevel(4)
    print(x)
    print(fourCovid)
    str2 = getDisease(4)
    print(str2)
    



    #print(stu1)
    #getRiskRestaurant()
    #number = getRiskArea(12)
    #print(number)
    #numbertwo = getRiskArea(1)
    #print(numbertwo)
    #rint(getDisease(2))

########################## Dictionary ##################################
"""   
1-Kardon
2-Atlantic terminal
3-University village
4-White Hall
5-J&H
6-1940
7-conwell
8-Beech internation
9-The edge
10-Morgan
11-Oxford
12-1300
13-Temple Towers
"""
diction = {
    "KardonCovidCases": oneCovid,
    "KardonColdCases": oneCold,
    "KardonStomachCases": oneStomach,

    "AtlanticTerminalCovidCases": twoCovid,
    "AtlanticTerminalColdCases": twoCold,
    "AtlanticTerminalStomachCases": twoStomach,

    "UniversityVillageCovidCases": threeCovid,
    "UniversityVillageColdCases": threeCold,
    "UniversityVillageStomachCases": threeStomach,

    "WhiteHallCovidCases": fourCovid,
    "WhiteHallColdCases": fourCold,
    "WhiteHallStomachCases": fourStomach,

    "J&HCovidCases": fiveCovid,
    "J&HColdCases": fiveCold,
    "J&HStomachCases": fiveStomach,

    "1940CovidCases": sixCovid,
    "1940ColdCases": sixCold,
    "1940StomachCases": sixStomach,

    "ConwellCovidCases": sevenCovid,
    "ConwellColdCases": sevenCold,
    "ConwellStomachCases": sevenStomach,

    "BeechInternationalCovidCases": eightCovid,
    "BeechInternationalColdCases": eightCold,
    "BeechInternationalStomachCases": eightStomach,

    "TheEdgeCovidCases": nineCovid,
    "TheEdgeColdCases": nineCold,
    "TheEdgeStomachCases": nineStomach,

    "MorganCovidCases": tenCovid,
    "MorganColdCases": tenCold,
    "MorganStomachCases": tenStomach,

    "OxfordCovidCases": elevenCovid,
    "OxfordColdCases": elevenCold,
    "OxfordStomachCases": elevenStomach,

    "1300CovidCases": twelveCovid,
    "1300ColdCases": twelveCold,
    "1300StomachCases": twelveStomach,

    "TempleTowersCovidCases": thirteenCovid,
    "TempleTowersColdCases": thirteenCold,
    "TempleTowersStomachCases": thirteenStomach,
}

