# Instalación

Prerequisitos:
    - Python3
    - Git

1. Clonar el proyecto:
    ```
    $ cd /path/to/project
    $ git clone https://github.com/mmesas3699/LQN.git
    ```
2. Crear y activar entorno virtual
    ```
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```
3. Instalar dependecias:
    ```
    $ pip install -r requirements.txt
    ```
4. Ejecutar el servidor:
    ```
    $ cd starwars
    $ python manage.py runserver
    ```

# Probar el servicio
1. En un navegador ir a la dirección: http://localhost:8000/grapql

2. Puede ejecutar las siguientes queries y mutaciones:
```
# Characters

query allCharacters {
  characters {
    id,
    name
  }
}

query character{
  character(name: "Luke Skywalker"){
    id,
    name,
    movies {
      name
    }
  }
}

mutation createCharacter {
  createCharacter(name: "Darth Vader") {
    character {
      name
    }
  }
}

mutation updateCharacter {
  updateCharacter(id: 4, name: "luke skywalker"){
    character {
      id,
      name
    }
  }
}


mutation deleteCharacter {
  deleteCharacter(id: 4) {
    character {
      name
    }
  }
}


# Planets

query allPlanets{
  planets{
    id,
    name
  }
}

query planet {
  planet(name: "Sullust"){
    id,
    name,
    movies {
      name
    }
  }
}

mutation createPlanet {
  createPlanet(name: "Sullust"){
    planet{
      name
    }
  }
}

mutation updatePlanet {
  updatePlanet(id: 1, name: "sullust") {
    planet {
      id,
      name
    }
  }
}

mutation deletePlanet {
  deletePlanet(id: 2) {
    planet {
      name
    }
  }
}


# Movies

query allMovies {
  movies {
    id,
    name,
    year,
    directorName,
    characters {
      name
    },
    planets {
      name
    }
  }
}

query movie{
  movie(name: "Una nueva esperanza"){
    id,
    name,
    year,
    directorName,
    openingText,
    characters {
      name
    },
    planets {
      name
    }
  }
}

mutation createMovie{
  createMovie(
    name: "Una nueva esperanza",
    year: 1977,
    openingText: "Son tiempos de guerra civil, Naves rebeldes han atacado desde una base secreta y han obtenido su primera victoria contra el malvado Imperio Galáctico. Durante la batalla, espías rebeldes lograron robar los planos secretos del arma más extrema del Imperio, la ESTRELLA DE LA MUERTE, una estación espacial blindada con suficiente potencia para destruir un planeta entero. Perseguida por los siniestros agentes del Imperio, la Princesa Leia se dirige velozmente a casa en su nave espacial, mientras resguarda los planos que pueden salvar a su pueblo y restaurar la libertad en la galaxia…", 
    director: "George Lucas", 
    planets: [], 
    characters: []){
    movie {
      id,
      name
    }
  }
}

mutation addCharacters{
  addCharactersMovie(movieId: 2, characters: ["Luke Skywalker", "R2D2"]){
    movie {
      id,
      name,
      characters {
        name
      }
    }
  }
}

mutation addPlanets{
  addPlanetsMovie(movieId: 2, planets: ["Sullust"]) {
    movie {
      name,
      planets {
        name
      }
    }
  }
}

mutation deleteMovie{
  deleteMovie(movieId: 6){
    movie{
      id,
      name
    }
  }
}
```
