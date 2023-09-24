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

    for(let select of selects){
        console.log(select)
        postDict[String(select.name)] = select.value
    }

    for(let input of inputs){
        postDict[String(input.name)] = input.checked
    }

    return postDict
}

function postForm(){
    $.post("/report", getDictOfData())

}