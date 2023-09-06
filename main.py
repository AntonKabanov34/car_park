import sqlite3

class Owner:
    """Владелец автопарка"""
    # Сущность ВЛАДЕЛЕЦ АВТОПАРКА (АЙ ДИ ФИО ТЕЛЕФОН)
    def __init__(self, db_name):
        self.db_name = db_name
        pass

    def create_db(self):
        """Создает пустую DB"""
        with sqlite3.connect(self.db_name) as conn:
            print(f'Пустая БД с именем {self.db_name} была создана.')
            pass
    

    def create_table_owners(self):
        """Создает таблицу внутри full_name"""
        # owner_id,
        # last_name
        # first_name
        # second_name

        create_table_query = """
        CREATE TABLE IF NOT EXISTS owners (
            owner_id INTEGER PRIMARY KEY,
            last_name TEXT,
            first_name TEXT,
            second_name TEXT
        )
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(create_table_query)
            conn.commit()
        
        print(f'Таблица owners в БД {self.db_name} успешно создана')
        pass


    def create_table_owner_telephones(self):
        """Создает таблицу с номерами телефонов"""
        # id
        # owner_id
        # telephone

        create_table_query = """
        CREATE TABLE IF NOT EXISTS owner_telephones (
            id INTEGER PRIMARY KEY,
            owner_id INTEGER,
            telephone TEXT,
            FOREIGN KEY (owner_id) REFERENCES owners (owner_id)
        )
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(create_table_query)
            conn.commit()
        print(f'Таблица owner_telephones в БД {self.db_name} успешно создана.')
        pass

    def add_owner(self, last_name, first_name, second_name, telephone):
        """Добавляет данные ФИО и номера телефона в таблицы owners и owner_telephones"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            insert_owner_query = """
            INSERT INTO owners (last_name, first_name, second_name)
            VALUES (?, ?, ?)
            """
            cursor.execute(insert_owner_query, (last_name, first_name, second_name))

            # Получаем ID добавленного владельца
            owner_id = cursor.lastrowid

            insert_telephone_query = """
            INSERT INTO owner_telephones (owner_id, telephone)
            VALUES (?, ?)
            """
            cursor.execute(insert_telephone_query, (owner_id, telephone))
            conn.commit()

            print('Владелец успешно добавлен.')
            pass

        
    pass


class Car_park:
    """Автопарк"""
    # Сущность АВТОПАРК (АЙ-ДИ, АЙДИ Владельца, Наименование, кол-во автомобилей в парке)
    def create_table_car_parks(self):
        """Создает таблицу АВТОПАРКА"""
        # id
        # owner_id
        # car_park_name
        # auto_amount
        pass
    pass

class Driver:
    """Водитель"""
    # СУЩНОСТЬ ВОДИТЕЛЬ (ФИО, НОМЕР ВУ, Право на управление автомобилями)
    def create_table_drivers(self):
        # id
        # id driver
        # driver last_name
        # driver first_name
        # driver second_name
        # driving license
        # driving_cars
        pass
    pass

class Car:
    """Автомобиль"""
    # Сущность АВТОМОБИЛЬ (Марка, модель, год выпуска, госномер)
    def create_table_cars(self):
        """Создает таблицу АВТОМОБИЛИ"""
        # id
        # id car_park
        # brend
        # model
        # prod_year
        # number
        #
        #
        pass
    pass

class Route:
    """Маршрут"""
    # Сущность МАРШРУТ (ТОЧКА А, ТОЧКА Б)
    pass
pass

# Экземпляры:
db = Owner('testing.db')

# Вызовы:
# Создание таблиц влвдельца
db.create_db()
db.create_table_owners()
db.create_table_owner_telephones()

# Ввод данных
db.add_owner('Херов', 'Альберт', 'Епистафьевич', '+79999999999')

