let clientID = "aC07ml5HUZwqbhbZceukrPMFIDb_2rdmExYpCJ9f_O8";
let endpoint = `https://api.unsplash.com/photos/random/?client_id=${clientID}`;

let imageElement = document.querySelector("#unsplashImage");
let imageLink = document.querySelector("#imageLink");
let creator = document.querySelector("#creator");

function getBackground() {
    fetch(endpoint)
        .then(function (response) {
            return response.json();
        })
        .then(function (jsonData) {
            imageElement.style.background = `url("${jsonData.links.download}")`;
            console.log(jsonData);

            creator.innerText = jsonData.user.name;
            creator.setAttribute("href", jsonData.user.portfolio_url);
        })
        .catch(function (error) {
            console.log("Error:" + error);
        });
}

getBackground();

let dwp=document.querySelector('#dynamicwp');
dwp.addEventListener('click',getBackground);
