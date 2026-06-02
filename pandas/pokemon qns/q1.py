import pandas as pd
import numpy as np
data = {
    "Name": [
        "Bulbasaur",
        "Ivysaur",
        "Venusaur",
        "VenusaurMega Venusaur",
        "Charmander",
        "Charmeleon",
        "Charizard",
        "Squirtle",
        "Wartortle",
        "Blastoise",
        "Pikachu",
        "Raichu",
        "Gengar",
        "Dragonite",
        "Mewtwo"
    ],

    "Type 1": [
        "Grass",
        "Grass",
        "Grass",
        "Grass",
        "Fire",
        "Fire",
        "Fire",
        "Water",
        "Water",
        "Water",
        "Electric",
        "Electric",
        "Ghost",
        "Dragon",
        "Psychic"
    ],

    "Type 2": [
        "Poison",
        "Poison",
        "Poison",
        "Poison",
        None,
        None,
        "Flying",
        None,
        None,
        None,
        None,
        None,
        "Poison",
        "Flying",
        None
    ],

    "Total": [
        318, 405, 525, 625,
        309, 405, 534,
        314, 405, 530,
        320, 485, 500,
        600, 680
    ],

    "HP": [
        45, 60, 80, 80,
        39, 58, 78,
        44, 59, 79,
        35, 60, 60,
        91, 106
    ],

    "Attack": [
        49, 62, 82, 100,
        52, 64, 84,
        48, 63, 83,
        55, 90, 65,
        134, 110
    ],

    "Defense": [
        49, 63, 83, 123,
        43, 58, 78,
        65, 80, 100,
        40, 55, 60,
        95, 90
    ],

    "Sp. Atk": [
        65, 80, 100, 122,
        60, 80, 109,
        50, 65, 85,
        50, 90, 130,
        100, 154
    ],

    "Sp. Def": [
        65, 80, 100, 120,
        50, 65, 85,
        64, 80, 105,
        50, 80, 75,
        100, 90
    ],

    "Speed": [
        45, 60, 80, 80,
        65, 80, 100,
        43, 58, 78,
        90, 110, 110,
        80, 130
    ],

    "Generation": [
        1, 1, 1, 1,
        1, 1, 1,
        1, 1, 1,
        1, 1, 1,
        1, 1
    ],

    "Legendary": [
        False, True, False, False,
        False, False, False,
        False, False, True,
        False, False, False,
        False, True
    ],

    "Type3": [
        "Grass+Poison",
        "Grass+Poison",
        "Grass+Poison",
        "Grass+Poison",
        "Fire+nan",
        "Fire+nan",
        "Fire+Flying",
        "Water+nan",
        "Water+nan",
        "Water+nan",
        "Electric+nan",
        "Electric+nan",
        "Ghost+Poison",
        "Dragon+Flying",
        "Psychic+nan"
    ]
}
df=pd.DataFrame(data)
print(df,"\n")
print(df.groupby("Type 1")["Attack"].aggregate([np.min,np.median,np.mean]),"\n")
print(df.groupby("Type 1").aggregate({"Attack":[min,"median"], "Defense":np.mean}))