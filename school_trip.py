import webbrowser
from pywebio import start_server
from pywebio.input import input, select, slider, NUMBER
from pywebio.output import put_error, put_success, put_table

def school_trip():
    # Введення даних
    students = input("Кількість учнів:", type=NUMBER)
    teachers = input("Кількість вчителів:", type=NUMBER)
    transport = select("Оберіть транспорт:", ["🚌 Автобус", "🚆 Поїзд"])
    days = slider(label="Кількість днів:", min_value=0, max_value=10, value=1)

    # Перевірка помилок
    if students == 0:
        put_error("Помилка: кількість учнів не може бути 0")
        return

    # Загальна кількість людей
    total_people = students + teachers

    # Розрахунок транспорту
    transport_cost = 0
    buses_needed = 0
    if transport == "🚌 Автобус":
        buses_needed = -(-total_people // 40)  # округлення вгору
        transport_cost = buses_needed * 5000
    else:  # Поїзд
        transport_cost = total_people * 300

    # Розрахунок проживання
    accommodation_cost = 0
    if days > 0:
        accommodation_cost = total_people * 400 * days

    # Загальна сума
    total_cost = transport_cost + accommodation_cost

    # Знижка
    discount = 0
    if total_people > 30:
        discount = total_cost * 0.1
        total_cost -= discount

    # Вивід результатів у таблиці
    result_table = [
        ["Загальна кількість людей", total_people],
        ["Транспорт", transport],
    ]

    if transport == "🚌 Автобус":
        result_table.append(["Потрібно автобусів", buses_needed])

    result_table.extend([
        ["Вартість транспорту", f"{transport_cost} грн"],
        ["Вартість проживання", f"{accommodation_cost} грн" if days > 0 else "Без проживання"],
        ["Знижка", f"{int(discount)} грн" if discount > 0 else "Немає"],
        ["Загальна сума", f"{int(total_cost)} грн"]
    ])

    put_table(result_table)
    put_success("Розрахунок завершено!")

if __name__ == "__main__":
    port = 8080
    url = f"http://localhost:{port}/"
    # Відкрити браузер автоматично
    webbrowser.open(url)
    start_server(school_trip, port=port, debug=True)
