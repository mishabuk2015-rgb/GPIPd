
car = {
    "model": "Toyota RAV4 Hybrid Style 2025",
    "price_uah": 2026125,
    "engine_capacity_l": 2.5,
    "curb_weight_kg": 1700,   # приблизно
    "max_speed_kmh": 180,
    "fuel_consumption_l_per_100km": 5.5,
    "interior_features": [
        "Smart Entry and Start",
        "Hands-free trunk opening",
        "Auto-dimming rearview mirror",
        "Driver seat lumbar support adjustment",
        "Power windows with auto function",
        "Child safety lock",
        "Heated windshield",
        "Parking assist with rear camera",
        "Split-folding rear seats 60:40",
        "Reversible trunk floor (carpet/plastic)",
        "Multimedia system with 10.5-inch display"
    ],
    "trunk": {
        "volume_l": 580,
        "volume_with_seats_folded_l": 1690
    },
    "max_trailer_weight_braked_kg": 2000,
    "insurance_payment_uah": None
}

# Отримання даних зі словника
print("Назва авто:", car["model"])
print("Ціна:", car["price_uah"], "грн")
print("Перша опція інтер'єру:", car["interior_features"][0])
print("Об'єм багажника зі складеними сидіннями:", car["trunk"]["volume_with_seats_folded_l"], "л")

# Розрахунок страхового платежу (0,5% від вартості авто)
insurance_payment = car["price_uah"] * 0.005
car["insurance_payment_uah"] = insurance_payment
print("Страховий платіж:", insurance_payment, "грн")

