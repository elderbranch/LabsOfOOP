
class Employee:
    def __init__(self, name, position, base_salary, experience):
        self.name = name
        self.position = position
        self.base_salary = base_salary
        self.experience = experience

    def salary(self):
        return self.base_salary

    def introduce(self):
        return (
            f"Имя: {self.name}, должность: {self.position}, "
            f"стаж: {self.experience} лет, "
            f"зарплата: {self.salary():.2f} сом"
        )


class Manager(Employee):
    def __init__(self, name, base_salary, experience,
                 department, subordinates, bonus_percent):
        super().__init__(name, "Менеджер", base_salary, experience)
        self.department = department
        self.subordinates = subordinates
        self.bonus_percent = bonus_percent

    def salary(self):
        return self.base_salary * (1 + self.bonus_percent / 100)

    def introduce(self):
        return (
            f"{super().introduce()}, отдел: {self.department}, "
            f"подчинённых: {self.subordinates}, "
            f"бонус: {self.bonus_percent}%"
        )


class Developer(Employee):
    def __init__(self, name, base_salary, experience,
                 language, level):
        super().__init__(name, "Разработчик", base_salary, experience)
        self.language = language
        self.level = level.lower()

    def salary(self):
        bonuses = {"junior": 0, "middle": 30, "senior": 60}
        if self.level not in bonuses:
            raise ValueError("Уровень должен быть junior, middle или senior")
        return self.base_salary * (1 + bonuses[self.level] / 100)

    def introduce(self):
        return (
            f"{super().introduce()}, язык: {self.language}, "
            f"уровень: {self.level}"
        )


team = [
    Manager("Айбек", 80000, 8, "IT", 5, 20),
    Manager("Алина", 70000, 6, "Продажи", 3, 15),
    Developer("Бек", 50000, 2, "Python", "junior"),
    Developer("Данияр", 70000, 4, "Java", "middle"),
    Developer("Елена", 90000, 7, "Python", "senior"),
    Employee("Марат", "Тестировщик", 45000, 1)
]

salary_fund = 0

for employee in team:
    print(employee.introduce())
    salary_fund += employee.salary()

print(f"\nЗарплатный фонд: {salary_fund:,.2f} сом")






# Задание 2

class TourPackage:
    def __init__(self, name, country, days, base_price):
        self.name = name
        self.country = country
        self.days = days
        self.base_price = base_price

    def total_price(self, persons, month=7):
        return persons * self.base_price * (
            1 - self.season_discount(month) / 100
        )

    def season_discount(self, month):
        if month in (12, 1, 2):
            return 10
        if month in (3, 4, 10, 11):
            return 5
        return 0

    def describe(self):
        return f"{self.name}: {self.country}, {self.days} дней"


class BeachTour(TourPackage):
    def __init__(self, name, country, days, base_price,
                 resort, hotel, flight, food):
        super().__init__(name, country, days, base_price)
        self.resort = resort
        self.hotel = hotel
        self.flight = flight
        self.food = food

    def total_price(self, persons, month=7):
        hotel_cost = {"3*": 0, "4*": 10000, "5*": 25000}
        food_cost = {"BB": 0, "HB": 5000, "AI": 12000}
        flight_cost = 15000 if self.flight else 0

        per_person = (
            self.base_price
            + hotel_cost[self.hotel]
            + food_cost[self.food]
            + flight_cost
        )
        return persons * per_person * (
            1 - self.season_discount(month) / 100
        )

    def describe(self):
        return (
            f"{super().describe()}, курорт: {self.resort}, "
            f"отель: {self.hotel}, перелёт: {self.flight}, "
            f"питание: {self.food}"
        )


class AdventureTour(TourPackage):
    def __init__(self, name, country, days, base_price,
                 route, fitness, equipment, guide):
        super().__init__(name, country, days, base_price)
        self.route = route
        self.fitness = fitness
        self.equipment = equipment
        self.guide = guide

    def total_price(self, persons, month=7):
        difficulty_cost = {"лёгкий": 0, "средний": 8000,
                           "сложный": 20000}
        guide_cost = 5000 if self.guide else 0

        per_person = (
            self.base_price
            + difficulty_cost[self.fitness]
            + guide_cost
        )
        return persons * per_person * (
            1 - self.season_discount(month) / 100
        )

    def describe(self):
        return (
            f"{super().describe()}, маршрут: {self.route}, "
            f"сложность: {self.fitness}, "
            f"снаряжение: {', '.join(self.equipment)}, "
            f"гид: {self.guide}"
        )


tours = [
    BeachTour("Море", "Турция", 7, 40000,
              "Анталья", "4*", True, "AI"),
    BeachTour("Острова", "Мальдивы", 8, 80000,
              "Мале", "5*", True, "HB"),
    BeachTour("Пляж", "Египет", 6, 35000,
              "Хургада", "3*", True, "BB"),
    AdventureTour("Треккинг", "Кыргызстан", 5, 15000,
                  "Ала-Арча", "средний",
                  ["палатка", "рюкзак"], True),
    AdventureTour("Восхождение", "Кыргызстан", 7, 30000,
                  "Ленинский пик", "сложный",
                  ["верёвка", "ледоруб"], True),
    AdventureTour("Прогулка", "Казахстан", 3, 10000,
                  "Чарынский каньон", "лёгкий",
                  ["вода", "треккинговая обувь"], False)
]

for tour in tours:
    print(tour.describe())
    print(f"Цена для 2 человек: {tour.total_price(2):,.2f} сом")
    print(f"Скидка в январе: {tour.season_discount(1)}%\n")


# Задание 3

class Appliance:
    def __init__(self, brand, power, price, energy_class):
        self.brand = brand
        self.power = power
        self.price = price
        self.energy_class = energy_class

    def spec(self):
        return (
            f"{self.brand}: {self.power} Вт, "
            f"{self.price} сом, класс {self.energy_class}"
        )

    def energy_cost(self, hours, rate):
        # Мощность переводится из ватт в киловатты
        return (self.power / 1000) * hours * rate

    def compare(self, other):
        if self.price < other.price:
            price_result = "дешевле"
        elif self.price > other.price:
            price_result = "дороже"
        else:
            price_result = "одинаковая цена"

        if self.power < other.power:
            power_result = "потребляет меньше мощности"
        elif self.power > other.power:
            power_result = "потребляет больше мощности"
        else:
            power_result = "одинаковая мощность"

        return (
            f"{self.brand} и {other.brand}: "
            f"{price_result}, {power_result}"
        )


class WashingMachine(Appliance):
    def __init__(self, brand, power, price, energy_class,
                 drum, modes, temperature):
        super().__init__(brand, power, price, energy_class)
        self.drum = drum
        self.modes = modes
        self.temperature = temperature

    def spec(self):
        return (
            f"{super().spec()}, барабан: {self.drum} кг, "
            f"режимы: {', '.join(self.modes)}, "
            f"температура: {self.temperature}°C"
        )


class Refrigerator(Appliance):
    def __init__(self, brand, power, price, energy_class,
                 volume, chambers, freezer_temperature):
        super().__init__(brand, power, price, energy_class)
        self.volume = volume
        self.chambers = chambers
        self.freezer_temperature = freezer_temperature

    def spec(self):
        return (
            f"{super().spec()}, объём: {self.volume} л, "
            f"камер: {self.chambers}, "
            f"морозилка: {self.freezer_temperature}°C"
        )


washer = WashingMachine(
    "LG", 2000, 45000, "A++",
    8, ["быстрая", "хлопок", "деликатная"], 40
)

fridge = Refrigerator(
    "Samsung", 150, 60000, "A+",
    350, 2, -18
)

print(washer.spec())
print(fridge.spec())

print("Стоимость электричества за 5 часов:")
print(f"Стиральная машина: {washer.energy_cost(5, 2.5):.2f} сом")
print(f"Холодильник: {fridge.energy_cost(5, 2.5):.2f} сом")

print(washer.compare(fridge))


# Задание 4


class Athlete:
    def __init__(self, name, age, country, awards=None):
        self.name = name
        self.age = age
        self.country = country
        self.awards = awards if awards is not None else []

    def achievement(self):
        return f"{self.name}: награды — {self.awards}"

    def add_medal(self, medal, year):
        self.awards.append({"medal": medal, "year": year})

    def medals_count(self):
        return len(self.awards)


class Swimmer(Athlete):
    def __init__(self, name, age, country, awards,
                 specialization, record, style):
        super().__init__(name, age, country, awards)
        self.specialization = specialization
        self.record = record
        self.style = style

    def avg_speed(self):
        return 100 / self.record if self.record > 0 else 0

    def achievement(self):
        return (
            f"{self.name}: плавание, стиль {self.style}, "
            f"рекорд 100 м — {self.record} сек"
        )


class Sprinter(Athlete):
    def __init__(self, name, age, country, awards,
                 distance, record, starts):
        super().__init__(name, age, country, awards)
        self.distance = distance
        self.record = record
        self.starts = starts

    def avg_speed(self):
        return self.distance / self.record if self.record > 0 else 0

    def achievement(self):
        return (
            f"{self.name}: спринт {self.distance} м, "
            f"рекорд — {self.record} сек, стартов: {self.starts}"
        )


athletes = [
    Swimmer("Иван", 22, "Кыргызстан",
            [{"medal": "золото", "year": 2025}],
            "100 м", 52.5, "вольный"),
    Swimmer("Анна", 20, "Россия", [], "100 м", 55.0, "брасс"),
    Swimmer("Данияр", 24, "Казахстан", [], "100 м", 54.0, "баттерфляй"),
    Sprinter("Алекс", 23, "США", [], 100, 10.5, 20),
    Sprinter("Марк", 21, "Ямайка", [], 200, 20.8, 15),
    Sprinter("Пётр", 25, "Кыргызстан", [], 100, 11.0, 12)
]

athletes[1].add_medal("серебро", 2024)

for athlete in athletes:
    print(athlete.achievement())
    print("Количество наград:", athlete.medals_count())
    print(f"Средняя скорость: {athlete.avg_speed():.2f} м/с\n")

fastest = min(
    athletes,
    key=lambda athlete: athlete.record
)
print("Лучший результат по времени:", fastest.name)


# Задание 5


class Property:
    def __init__(self, address, area, price, year_built):
        self.address = address
        self.area = area
        self.price = price
        self.year_built = year_built

    def price_per_sqm(self):
        return self.price / self.area if self.area > 0 else 0

    def is_affordable(self, budget):
        return self.price <= budget

    def age(self, current_year=2026):
        return current_year - self.year_built

    def describe(self):
        return (
            f"{self.address}: {self.area} м², "
            f"цена {self.price:,.0f} сом, "
            f"цена за м²: {self.price_per_sqm():,.0f} сом, "
            f"возраст: {self.age()} лет"
        )


class Apartment(Property):
    def __init__(self, address, area, price, year_built,
                 floor, rooms, balcony, property_type):
        super().__init__(address, area, price, year_built)
        self.floor = floor
        self.rooms = rooms
        self.balcony = balcony
        self.property_type = property_type

    def describe(self):
        return (
            f"Квартира. {super().describe()}, "
            f"этаж: {self.floor}, комнат: {self.rooms}, "
            f"балкон: {self.balcony}, тип: {self.property_type}"
        )


class House(Property):
    def __init__(self, address, area, price, year_built,
                 floors, land_area, material, garage):
        super().__init__(address, area, price, year_built)
        self.floors = floors
        self.land_area = land_area
        self.material = material
        self.garage = garage

    def describe(self):
        return (
            f"Дом. {super().describe()}, этажность: {self.floors}, "
            f"участок: {self.land_area} соток, "
            f"материал: {self.material}, гараж: {self.garage}"
        )


properties = [
    Apartment("Бишкек, ул. А", 60, 6000000, 2020,
              5, 2, True, "новостройка"),
    Apartment("Бишкек, ул. Б", 45, 3600000, 2010,
              3, 2, False, "вторичка"),
    Apartment("Бишкек, ул. В", 80, 8000000, 2024,
              8, 3, True, "новостройка"),
    House("Бишкек, ул. Г", 120, 9000000, 2015,
          2, 6, "кирпич", True),
    House("Бишкек, ул. Д", 90, 5000000, 2005,
          1, 5, "газобетон", False)
]

for prop in properties:
    print(prop.describe())
    print("Бюджет 5 млн:", prop.is_affordable(5000000))

best = min(properties, key=lambda prop: prop.price_per_sqm())

print("\nЛучшее соотношение цена/площадь:")
print(best.describe())


# Задание 6


class Food:
    def __init__(self, name, calories, protein, fat, carbs, price_per_kg):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.price_per_kg = price_per_kg

    def label(self):
        return (
            f"{self.name}\n"
            f"Калорийность: {self.calories} ккал на 100 г\n"
            f"Белки: {self.protein} г\n"
            f"Жиры: {self.fat} г\n"
            f"Углеводы: {self.carbs} г\n"
            f"Цена: {self.price_per_kg} сом/кг"
        )

    def calories_per_serving(self, serving_g):
        return self.calories * serving_g / 100


class Dairy(Food):
    def __init__(self, name, calories, protein, fat, carbs,
                 price_per_kg, fat_percent, shelf_life, dairy_type):
        super().__init__(
            name, calories, protein, fat, carbs, price_per_kg
        )
        self.fat_percent = fat_percent
        self.shelf_life = shelf_life
        self.dairy_type = dairy_type

    def is_fresh(self, days):
        return 0 <= days < self.shelf_life


class Bakery(Food):
    def __init__(self, name, calories, protein, fat, carbs,
                 price_per_kg, ingredients, weight, bakery_type):
        super().__init__(
            name, calories, protein, fat, carbs, price_per_kg
        )
        self.ingredients = ingredients
        self.weight = weight
        self.bakery_type = bakery_type


milk = Dairy(
    "Молоко", 60, 3.0, 3.2, 4.7, 100,
    3.2, 7, "молоко"
)

bread = Bakery(
    "Хлеб", 250, 8.0, 3.0, 49.0, 80,
    ["мука", "вода", "дрожжи", "соль"], 500, "хлеб"
)

print(milk.label())
print("Свежий на 3-й день:", milk.is_fresh(3))
print("Свежий на 8-й день:", milk.is_fresh(8))
print("Калории в 200 г молока:", milk.calories_per_serving(200))

print("\n", bread.label())
print("Состав:", ", ".join(bread.ingredients))
print("Вес:", bread.weight, "г")
print("Калории в 100 г хлеба:", bread.calories_per_serving(100))


# Задание 7

class Instrument:
    def __init__(self, name, country, year, instrument_type):
        self.name = name
        self.country = country
        self.year = year
        self.instrument_type = instrument_type

    def play(self):
        return f"{self.name} издаёт музыку."

    def tune(self):
        return f"{self.name} настроен."

    def describe(self):
        return (
            f"{self.name}, страна: {self.country}, "
            f"год создания: {self.year}, "
            f"тип: {self.instrument_type}"
        )


class StringInstrument(Instrument):
    def __init__(self, name, country, year, strings,
                 soundboard, playing_type):
        super().__init__(name, country, year, "струнный")
        self.strings = strings
        self.soundboard = soundboard
        self.playing_type = playing_type

    def play(self):
        return f"{self.name} звучит при {self.playing_type} игре."

    def describe(self):
        return (
            f"{super().describe()}, струн: {self.strings}, "
            f"дека: {self.soundboard}, "
            f"способ игры: {self.playing_type}"
        )


class WindInstrument(Instrument):
    def __init__(self, name, country, year, note_range,
                 material, wind_type):
        super().__init__(name, country, year, "духовой")
        self.note_range = note_range
        self.material = material
        self.wind_type = wind_type

    def play(self):
        return f"{self.name} звучит при вдувании воздуха."

    def describe(self):
        return (
            f"{super().describe()}, диапазон: {self.note_range}, "
            f"материал: {self.material}, "
            f"вид: {self.wind_type}"
        )


orchestra = [
    StringInstrument("Скрипка", "Италия", 1550,
                     4, "ель", "смычковой"),
    StringInstrument("Гитара", "Испания", 1850,
                     6, "кедр", "щипковой"),
    StringInstrument("Арфа", "Ирландия", 1800,
                     47, "дерево", "щипковой"),
    WindInstrument("Труба", "Германия", 1500,
                   "фа#3–ре6", "металл", "медный"),
    WindInstrument("Флейта", "Германия", 1600,
                   "до4–до7", "дерево", "деревянный"),
    WindInstrument("Кларнет", "Германия", 1700,
                   "ми3–соль6", "дерево", "деревянный")
]

print("ОРКЕСТР\n")

for instrument in orchestra:
    print(instrument.describe())
    print(instrument.play())
    print(instrument.tune())
    print()


# Задание 8

class Mountain:
    def __init__(self, name, height, country, first_ascent):
        self.name = name
        self.height = height
        self.country = country
        self.first_ascent = first_ascent

    def describe(self):
        return (
            f"{self.name}: высота {self.height} м, "
            f"страна: {self.country}, "
            f"первое восхождение: {self.first_ascent}"
        )

    def is_highaltitude(self):
        return self.height > 5000

    def climbing_difficulty(self):
        return "Не определена"


class Peak(Mountain):
    def __init__(self, name, height, country, first_ascent,
                 difficulty, route_type, route_length):
        super().__init__(name, height, country, first_ascent)
        if not 1 <= difficulty <= 5:
            raise ValueError("Сложность должна быть от 1 до 5")

        self.difficulty = difficulty
        self.route_type = route_type
        self.route_length = route_length

    def climbing_difficulty(self):
        levels = {
            1: "Очень лёгкая",
            2: "Лёгкая",
            3: "Средняя",
            4: "Сложная",
            5: "Очень сложная"
        }
        return levels[self.difficulty]

    def describe(self):
        return (
            f"{super().describe()}, маршрут: {self.route_type}, "
            f"длина: {self.route_length} км, "
            f"сложность: {self.climbing_difficulty()}"
        )


class Volcano(Mountain):
    def __init__(self, name, height, country, first_ascent,
                 status, last_eruption, crater_diameter):
        super().__init__(name, height, country, first_ascent)
        self.status = status
        self.last_eruption = last_eruption
        self.crater_diameter = crater_diameter

    def describe(self):
        return (
            f"{super().describe()}, статус: {self.status}, "
            f"последнее извержение: {self.last_eruption}, "
            f"диаметр кратера: {self.crater_diameter} м"
        )


mountains = [
    Peak("Пик Ленина", 7134, "Кыргызстан", 1928,
         4, "ледовый", 20),
    Peak("Пик Победы", 7439, "Кыргызстан", 1956,
         5, "смешанный", 25),
    Peak("Хан-Тенгри", 7010, "Кыргызстан", 1931,
         5, "скальный", 18),
    Volcano("Этна", 3357, "Италия", 500,
            "активный", 2025, 500),
    Volcano("Фудзияма", 3776, "Япония", 663,
            "спящий", 1707, 800),
    Volcano("Килиманджаро", 5895, "Танзания", 1889,
            "спящий", 0, 2500)
]

for mountain in mountains:
    print(mountain.describe())
    print("Высокогорная:", mountain.is_highaltitude())
    print("Сложность восхождения:", mountain.climbing_difficulty())
    print()
