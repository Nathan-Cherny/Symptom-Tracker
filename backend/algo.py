







def surveySickness():

    coldValue = 0
    covidValue = 0
    stomachBugValue = 0

    cough = False
    fever = False
    chills = False
    breathing = False
    taste = False
    smell = False
    fatigue = True
    vomit = False
    nausea = False
    stomach = False
    diarrhea = True
    nose = True
    throat = False 

    symptomList = [cough, fever, chills, breathing, taste, smell, fatigue, vomit, nausea, stomach, diarrhea, nose, throat]

    stomachBugSymptoms = [vomit, nausea, stomach, diarrhea, fatigue]
    covidSymptoms = [fever, chills, breathing, taste, smell, fatigue]
    coldSymptoms = [nose, throat, cough]

    diseaseList = [coldSymptoms, covidSymptoms, stomachBugSymptoms]

    
    for symptom in coldSymptoms:
        coldValue += symptom
    
    for symptom in covidSymptoms:
        covidValue += symptom


    for symptom in stomachBugSymptoms:
        stomachBugValue += symptom
        


    print("Stomach: ", stomachBugValue)
    print("Cold: ", coldValue)
    print("Covid: ", covidValue)

            

def BMICalc():
    weight1 = input("Weight (pounds): ")
    weight = float(weight1)
    height1 = input("Height (inches): ")
    height = float(height1)
    bmi = (weight*703)/(height*height) 
    bmiStr = "{:.2f}".format(bmi)
    print(bmiStr)

def findRestaurant():
    restaurants = []
    restaurants.append(input("Where have you eaten in the past 24 hours?"))
    


if __name__ == "__main__":
    #BMICalc()
    surveySickness()




    