const API = "https://pokeapi.co/api/v2/pokemon/"


let searchInput = document.querySelector("#search-input")
let searchbtn = document.querySelector("#search-btn")
let image = document.querySelector("#poke-image")
let info = document.querySelector("#poke-data")




searchbtn.addEventListener("click", async function(){
    // console.log(searchInput.value)

    let res = await axios.get(API + searchInput.value)
    let data = res.data
    image.src = data.sprites.front_default

    

    info.innerText = Object.keys(data)
    console.log(data)
})