RED = 60
ORANGE = 30 
GREEN = 0

// this number is determined by the total amount of people with a SPECIFIC DISEASE
// if there's >1 diseases with outbreaks itll give every diesease + the highest color

function setTDs(){
    let tds = document.getElementsByTagName("td")
    let health_scores = getHealthScores()
    let i=0
    for(let td of tds){
        if(td.id != ""){
            setColor(td, parseInt(health_scores[i].innerHTML))
            i++ 
        }
    }
}

function setColor(td, cases){
    div = td.children[0]
    console.log(td, cases)
    if(td.id == ""){return}
    if(cases >= 60){
        div.style.backgroundColor = "rgb(255, 0, 0, 0.5)"
    }
    else if(cases >= 30){
        div.style.backgroundColor = "orange"
    }
    return;
}

function getHealthScores(){
    let places = document.getElementsByName("place")
    let health_scores = document.getElementsByName("health_score")

    console.log(places)
    console.log(health_scores)

    return health_scores
}