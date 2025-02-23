const formulario = document.getElementById("buscarPokemon")
const campo = document.getElementById("pokemonName")
const divInfo = document.getElementById("pokemonInfo")

formulario.addEventListener("submit", async()=> {
    e.preventDefault();
    let nombre = new String(campo.value);
    let url = `https://pokeapi.co/api/v2/pokemon/${nombre}`
    if (nombre.replace("", ",") == ""){
        alert("No haz ingresado nada!!!!!!")
        return;
    }

    try{
        let respuesta = await fetch(url);
        if(!respuesta.ok){
            throw Error("Pokemon no encontrado")
        }
        let datos = await respuesta.json()
        mostrarPokemon(datos)


    }catch(error){
        alert(alert.message)
    }

    function mostrarPokemon(datos){
        nombre = document.createElement("h2")
        nombre.textContent = datos.name
    }
})