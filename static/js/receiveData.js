RED = 60
ORANGE = 30 
GREEN = 0

// this number is determined by the total amount of people with a SPECIFIC DISEASE
// if there's >1 diseases with outbreaks itll give every diesease + the highest color

function setTDs(){
    let tds = document.getElementsByTagName("td")

    for(td of tds){
        setColor(td, 3)
    }
}

function setColor(td, cases){
    div = td.children[0]
    if(td.id == ""){return}
    if(cases >= 60){
        div.style.backgroundColor = "rgb(255, 0, 0, 0.5)"
    }
    else if(cases >= 30){
        div.style.backgroundColor = "orange"
    }
    

}