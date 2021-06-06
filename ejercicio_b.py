


if __name__ == '__main__':
    pokemon_list = ['audino', 'bagon', 'baltoy', 'banette', 'bidoof',
    'braviary', 'bronzor', 'carracosta', 'charmeleon', 'cresselia',
    'croagunk', 'darmanitan', 'deino', 'emboar', 'emolga', 'exeggcute',
    'gabite', 'girafarig', 'gulpin', 'haxorus', 'heatmor', 'heatran', 
    'ivysaur', 'jellicent', 'jumpluff', 'kangaskhan', 'kricketune', 'landorus',
    'ledyba', 'loudred', 'lumineon', 'lunatone', 'machamp', 'magnezone',
    'mamoswine', 'nosepass', 'petilil', 'pidgeotto', 'pikachu', 'pinsir', 
    'poliwrath', 'poochyena', 'porygon2', 'porygonz', 'registeel', 'relicanth',
    'remoraid', 'rufflet', 'sableye', 'scolipede', 'scrafty', 'seaking',
    'sealeo', 'silcoon', 'simisear', 'snivy', 'snorlax', 'spoink', 'starly',
    'tirtouga', 'trapinch', 'treecko', 'tyrogue', 'vigoroth', 'vulpix',
    'wailord', 'wartortle', 'whismur', 'wingull', 'yamask']

    pokemon_total = len(pokemon_list)
    result = 0
    pokemon_result = []

    for pokemon in pokemon_list:
        current_position = pokemon_list.index(pokemon)
        next_position = current_position + 1
        
        if next_position > (pokemon_total - 1):
            break

        next_pokemon = pokemon_list[next_position]
        if next_pokemon[:1] == pokemon[-1]:
            result += 1
            pokemon_result.append(pokemon)
            pokemon_result.append(next_pokemon)

    print(result)
    print(pokemon_result)
