#variabile algoritmo
look_up_table = {}
for dato in dati:
    if dato.inc_y in look_up_table:
        look_up_table[dato.inc_y] = min([look_up_table[dato.inc_y] , dato.y])
    else:
        look_up_table[dato.inc_y] = dato.y

#algoritmo trova max
look_up_table_2 = {(dato.y + dato.inc_y):dato.x for dato in dati}
keys_look = list(look_up_table.keys())
keys_look.sort()
maggiori = keys_look[0:m.floor((len(keys_look)+1)/2-1)+1]
dato_min = min([look_up_table[magg]+magg for magg in maggiori])
coeff_max = dato_min / look_up_table_2[dato_min]
#algoritmo trova min
look_up_table_2 = {(dato.y - dato.inc_y):dato.x for dato in dati}
keys_look = list(look_up_table.keys())
keys_look.sort()
maggiori = keys_look[0:m.floor((len(keys_look)+1)/2-1)+1]
dato_min = min([abs(look_up_table[magg]-magg) for magg in maggiori])
coeff_min = dato_min / look_up_table_2[dato_min]
#retta di fit
coeff_fit = (coeff_max+coeff_min)/2




look_up_table = {dato.x+dato.inc_x: (dato.x , dato.inc_x , dato.y , dato.inc_y) for dato in dati}
look_keys = list(look_up_table.keys())
look_keys.sort(reverse=True)
min_key = look_up_table[look_keys[m.ceil((len(look_keys)+1)/2)]]
coeff_max = min_key[2]/min_key[0]
inc_coeff_max = (min_key[1]/min_key[0] + min_key[3]/min_key[2] ) * coeff_max
#algoritmo trova min
look_up_table = {dato.x-dato.inc_x: (dato.x , dato.inc_x , dato.y , dato.inc_y) for dato in dati}
look_keys = list(look_up_table.keys())
look_keys.sort()
min_key = look_up_table[look_keys[m.ceil((len(look_keys)+1)/2)]]
coeff_min = min_key[2]/min_key[0]
inc_coeff_min = (min_key[1]/min_key[0] + min_key[3]/min_key[2] ) * coeff_min
#retta di fit
coeff_fit = (coeff_max+coeff_min)/2