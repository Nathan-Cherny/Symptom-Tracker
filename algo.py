
from collections import Counter


"""
0 - disease is unknown
1 - Stomach Bug
2 - Covid
3 - Cold



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
diseaseKnown = 0

schoolsickData = []

riskRestaurants = []
restaurants = []

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

def surveySickness(): ##################### surveySickness()

    smoker = False
    drink = False
    nearSick = False

    coldValue = 0
    covidValue = 0
    stomachBugValue = 0

    cough = False
    fever = False
    chills = False
    breathing = False
    taste = False
    smell = False
    fatigue = False
    vomit = False
    nausea = False
    stomach = False
    diarrhea = False
    nose = False
    throat = False 

    symptomList = [cough, fever, chills, breathing, taste, smell, fatigue, vomit, nausea, stomach, diarrhea, nose, throat]

    stomachBugMultiplier = [0,0,0,0,0,0,1,0,1,2,2,0,0]

    covidMultiplier = [2,1,1,2,1,1,1,0,0,0,0,0,1]

    coldMultiplier = [1,1,0,0,0,0,0,0,0,0,0,2,1]

    
    if(diseaseKnown == 1):
        stomachBugValue = 1
    elif(diseaseKnown == 2):
        covidValue = 1
    elif(diseaseKnown == 3):
        coldValue = 1
    elif(diseaseKnown == 0): 
        
        for i in range(len(symptomList)):
            stomachBugValue += stomachBugMultiplier[i]*symptomList[i] - (drink) + (2*nearSick)
            covidValue += covidMultiplier[i]*symptomList[i] - (smoker) - (drink) + (2*nearSick)
            coldValue += coldMultiplier[i]*symptomList[i] - (smoker) - (drink) + (2*nearSick)
        

        stomachBugValue = float(stomachBugValue)
        covidValue = float(covidValue)
        coldValue = float(coldValue)

        stomachBugValue = float(stomachBugValue/sum(stomachBugMultiplier))
        covidValue = float(covidValue/sum(covidMultiplier))
        coldValue = float(coldValue/sum(coldMultiplier))

        print("Stomach: ", stomachBugValue)
        print("Cold: ", coldValue)
        print("Covid: ", covidValue)

        studentSickData = []

        if (stomachBugValue > coldValue) and (stomachBugValue > covidValue):
            studentSickData.append("Stomach Bug")
            studentSickData.append(stomachBugValue)
        
        elif (covidValue > coldValue) and (covidValue > stomachBugValue):
            studentSickData.append("Covid")
            studentSickData.append(covidValue)
        elif (coldValue > covidValue) and (coldValue > stomachBugValue):
            studentSickData.append("Common Cold")
            studentSickData.append(coldValue)
        else:
            studentSickData.append("Inconclusive")
            values = [coldValue, covidValue, stomachBugValue]
            values.sort()
            studentSickData.append(values[2])

    schoolsickData.append(studentSickData)


            



def getRiskRestaurant(): ################################ getRiskRestaurant

    count_dict = {}

    for res in restaurants:
        if res in count_dict:
            count_dict[res] += 1
        else:
            count_dict[res] = 1

    string_count_list = [(res, count) for res, count in count_dict.items()]

    for item in string_count_list:
        if(item[1] > 10):
            riskRestaurants.append(item)



#13 dorms, student[0] = dorm
#student[1] = disease
#student[2] = confidence level  
def getRiskArea(): ########################################### getRiskArea()

   
    for student in schoolsickData:
        if student[0] == 1:
            if student[1] == "Stomach Bug":
                if student[2] > 0.3:
                    if student[2] >= 0.8:
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


#0-30, 30-60, 60+
#n - dorm
def getRiskArea(n): ################################### getRiskArea
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
            
# n - dorm
def getDisease(n): ##################################################### getDisease(n)
    str = ""

    oneflag = False
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
    #surveySickness()
    #getRiskRestaurant()
    number = getRiskArea(12)
    print(number)
    numbertwo = getRiskArea(1)
    print(numbertwo)

    print(getDisease(2))


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


