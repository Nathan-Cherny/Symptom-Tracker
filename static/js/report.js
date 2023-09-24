function notDiagnosed(){
    var notDiagnosed = document.getElementById("notDiagnosed").style.display = "block"
    //  var diagnosed = document.getElementById("diagnosed").style.display = "none"
    document.getElementById("hallQuestion").style.display = "block"
}

function diagnosed(){
    // var diagnosed = document.getElementById("diagnosed").style.display = "none"
    document.getElementById("hallQuestion").style.display = "block"
    document.getElementById("finalSubmit").style.display = "block"
    return;
}

function onDiagnosedSubmit(){
    let answer = document.getElementById("diagnosed").children[1].value 
    let isDiagnosed = answer != "I haven't been diagnosed with anything recently"
    document.getElementById("finalSubmit").style.display = "block"
    if(isDiagnosed){
        diagnosed()
    }
    else{
        notDiagnosed()
    }
}

function getDictOfData(){
    let selects = document.getElementsByTagName("select")
    let inputs = document.getElementsByTagName("input")
    
    let postDict = {}
    let symptoms = {}

    for(let select of selects){
        if(select.value == "I haven't been diagnosed with anything recently"){
            postDict[String(select.name)] = select.value
        }
        postDict[String(select.name)] = select.value
    }


    for(let input of inputs){
        symptoms[String(input.name)] = input.checked
    }

    delete symptoms.csrfmiddlewaretoken

    postDict['smoked'] = symptoms.smoke
    postDict['drank'] = symptoms.drink
    postDict['around_sick'] = symptoms.sick
    delete symptoms.smoke
    delete symptoms.drink
    delete symptoms.sick

    console.log(symptoms)
    postDict["symptoms"] = symptoms
    return postDict
}

function postForm(){
    $.post("/report", getDictOfData())

}