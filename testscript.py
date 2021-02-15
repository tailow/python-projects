import random, math

# mitat (metriä)
leveys = 5.412
pituus = 10.2613
syvyys = 3.232

# kaakelin hinta (euroa)
hinta_per_m2 = 19

# säästöjä per kuukausi (euroa)
saastot_per_kk = 225

pinta_ala = (leveys * pituus) + 2 * (syvyys * pituus) + 2 * (syvyys * leveys)

print(str(format(pinta_ala, ".2f")), "m2")

hinta = pinta_ala * hinta_per_m2

print(str(format(hinta, ".2f")), "eur")

kuukaudet = math.ceil(hinta / saastot_per_kk)

print(str(kuukaudet), "kk")