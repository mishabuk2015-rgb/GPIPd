# ============================================================
# Джерело: https://toyota.od.ua/stock/rav4-gibrid-3
# ============================================================



car = {
    "model": "Toyota RAV4 Гібрид Style",
    "price": 2_026_125,
    "engine_displacement_cm3": 2487,
    "max_mass_kg": 2135,
    "max_speed_kmh": 180,
    "fuel_consumption_per_100km": 4.8,

    "interior_features": [
        "Задній підлокітник",
        "Кермо оздоблене шкірою",
        "Оздоблення селектора КПП шкірою",
        "Стеля чорного кольору",
    ],

    "trunk": {
        "volume_l": 580,
        "volume_seats_folded_l": 1690,
    },
}



car["max_trailer_mass_braked_kg"] = 800


print("Назва авто:", car["model"])
print("Ціна:", car["price"], "грн")
print("Перша опція інтер'єру:", car["interior_features"][0])
print("Об'єм багажника зі складеними сидіннями:", car["trunk"]["volume_seats_folded_l"], "л")


car["insurance_payment"] = car["price"] * 0.005
print(f"Страховий платіж (0,5%): {car['insurance_payment']:.2f} грн")


distance_km      = 200
fuel_price_per_l = 93
fuel_needed      = car["fuel_consumption_per_100km"] * distance_km / 100
trip_cost        = fuel_needed * fuel_price_per_l
print(f"Вартість мандрівки на {distance_km} км: {trip_cost:.2f} грн")