import sqlite3
db = sqlite3.connect('database.db')
cur = db.cursor()


def initialize_database():
    try:
        file = open("sql_commands.sql", "r")
        command_string = ""
        for line in file.readlines():
            command_string += line
        cur.executescript(command_string)
    except sqlite3.OperationalError:
        print("Database exists, skip initialization")
    except Exception:
        print("No SQL file to be used for initialization") 


def main():
    initialize_database()
    user_input = -1
    while user_input != "0":
        print("\nMenu options:")
        print("1: Print database information")
        print("2: Insert information to the database")
        print("3: Delete information from the database")
        print("4: Update information in the database")
        print("5: Run query")
        print("0: Quit")
        user_input = input("What do you want to do? ")
        print(user_input)
        if user_input == "1":
            print_option()
        elif user_input == "2":
            insert_option()
        elif user_input == "3":
            delete_option()
        elif user_input == "4":
            update_option()
        elif user_input == "5":
            query_option()
        elif user_input == "0":
            print("Ending software...")
        else:
            print("Invalid input, try again.")
    db.close()
    return


# Main sub functions
def print_option():
    print("What do you want to print?")
    input_choice = input("1: Air Forces\n"
                         "2: Countries\n"
                         "3: Pilots\n"
                         "4: Jets\n")
    if input_choice == "1":
        print_air_forces()
    elif input_choice == "2":
        print_countries()
    elif input_choice == "3":
        print_pilots()
    elif input_choice == "4":
        print_jets()
    else:
        print("Invalid input, try again.")


def insert_option():
    print("What do you want to insert?")
    input_choice = input("1: Air Force\n"
                         "2: Country\n"
                         "3: Pilot\n"
                         "4: Jet\n")
    if input_choice == "1":
        insert_air_force()
    elif input_choice == "2":
        insert_country()
    elif input_choice == "3":
        insert_pilot()
    elif input_choice == "4":
        insert_jet()
    else:
        print("Invalid input, try again.")


def delete_option():
    print("What do you want to delete?")
    input_choice = input("1: Air Force\n"
                         "2: Country\n"
                         "3: Pilot\n"
                         "4: Jet\n")
    if input_choice == "1":
        delete_air_force()
    elif input_choice == "2":
        delete_country()
    elif input_choice == "3":
        delete_pilot()
    elif input_choice == "4":
        delete_jet()
    else:
        print("Invalid input, try again.")


def update_option():
    print("What do you want to update?")
    input_choice = input("1: Air Force\n"
                         "2: Country\n"
                         "3: Pilot\n"
                         "4: Jet\n")
    if input_choice == "1":
        update_air_force()
    elif input_choice == "2":
        update_country()
    elif input_choice == "3":
        update_pilot()
    elif input_choice == "4":
        update_jet()
    else:
        print("Invalid input, try again.")


def query_option():
    print("Which query you want to do")
    input_choice = input("1: Query 1\n"
                         "2: Query 2\n"
                         "3: Query 3\n"
                         "4: Query 4\n"
                         "5: Query 5\n"
                         "6: Query 6\n")
    if input_choice == "1":
        query1()
    elif input_choice == "2":
        query2()
    elif input_choice == "3":
        query3()
    elif input_choice == "4":
        query4()
    elif input_choice == "5":
        query5()
    elif input_choice == "6":
        query6()
    else:
        print("Invalid input, try again.")


# prints
def print_air_forces():
    cur.execute("SELECT * FROM AirForce")
    rows = cur.fetchall()
    print("AirForceID, Name, Size, CountryID")
    for row in rows:
        print(row)
    return


def print_pilots():
    cur.execute("SELECT * FROM Pilot")
    rows = cur.fetchall()
    print("PilotID, Name, Rank, ExperienceYears, AirForceID")
    for row in rows:
        print(row)
    return


def print_countries():
    cur.execute("SELECT * FROM Country")
    rows = cur.fetchall()
    print("CountryID, Name, Region")
    for row in rows:
        print(row)
    return


def print_jets():
    cur.execute("SELECT * FROM JetModel")
    rows = cur.fetchall()
    print("JetID, Name, IntroductionYear, MaxSpeed (km/h), Armament, ManufacturerID")
    for row in rows:
        print(row)
    return


# inserts
def insert_air_force():
    try:
        air_force = input("Air force's name: ")
        air_force_size = int(input("Air force's size: "))
        country_id = int(input("Country ID: "))
        cur.execute("INSERT INTO AirForce (Name, Size, CountryID) VALUES (?,?,?)",
                    (air_force, air_force_size, country_id))
        db.commit()
    except sqlite3.IntegrityError:
        print("Air force already exists in the database")
    except sqlite3.Error as e:
        print(f"Error inserting air force: {e}")
    return


def insert_country():
    try:
        country = input("Country's name: ")
        region = input("Country's region: ")
        cur.execute("INSERT INTO Country (Name, Region) VALUES (?,?)", (country, region))
        db.commit()
    except sqlite3.IntegrityError:
        print("Country already exists in the database")
    except sqlite3.Error as e:
        print(f"Error inserting country: {e}")
    return


def insert_pilot():
    try:
        name = input("Pilot's name: ")
        rank = input("Pilot's rank: ")
        experience = int(input("Experience: "))
        air_force_id = int(input("AirForce ID: "))
        cur.execute("INSERT INTO Pilot (Name, Rank, ExperienceYears, AirForceID) VALUES (?,?,?,?)",
                    (name, rank, experience, air_force_id))
        db.commit()
    except sqlite3.IntegrityError:
        print("Pilot already exists in the database")
    except sqlite3.Error as e:
        print(f"Error inserting pilot: {e}")
    return


def insert_jet():
    try:
        jet = input("Jet's name: ")
        introduction = int(input("Jet's introduction year: "))
        max_speed = int(input("Jet's max speed (km/h): "))
        armament = input("Jet's armament: ")
        manufacturer_id = int(input("Manufacturer ID: "))
        cur.execute(
            "INSERT INTO JetModel (Name, IntroductionYear, MaxSpeed, Armament, ManufacturerID) VALUES (?,?,?,?,?)",
            (jet, introduction, max_speed, armament, manufacturer_id)
        )
        db.commit()
    except sqlite3.IntegrityError:
        print("Jet already exists in the database")
    except sqlite3.Error as e:
        print(f"Error inserting jet: {e}")
    return


# deletes
def delete_air_force():
    air_force = input("Air force's name: ")
    cur.execute("DELETE FROM AirForce WHERE Name = ?", (air_force,))
    db.commit()
    return


def delete_country():
    country = input("Country's name: ")
    cur.execute("DELETE FROM Country WHERE Name = ?", (country,))
    db.commit()
    return


def delete_pilot():
    pilot = input("Pilot's name: ")
    cur.execute("DELETE FROM Pilot WHERE Name = ?", (pilot,))
    db.commit()
    return


def delete_jet():
    jet = input("Jet's name: ")
    cur.execute("DELETE FROM JetModel WHERE Name = ?", (jet,))
    db.commit()
    return


# updates
def update_air_force():
    air_force_name = input("Air force's name: ")
    air_force_size = int(input("Air force's new size: "))
    cur.execute("UPDATE AirForce SET Size = ? WHERE Name = ?", (air_force_size, air_force_name))
    db.commit()
    return


def update_country():
    country_name = input("Country's name: ")
    region = input("Country's new region: ")
    cur.execute("UPDATE Country SET Region = ? WHERE Name = ?", (region, country_name))
    db.commit()
    return


def update_pilot():
    name = input("Pilot's name: ")
    rank = input("Pilot's new rank: ")
    experience = int(input("Pilot's current experience: "))
    cur.execute("UPDATE Pilot SET Rank = ?, ExperienceYears = ? WHERE Name = ?", (rank, experience, name))
    db.commit()
    return


def update_jet():
    jet = input("Jet's name: ")
    introduction = int(input("Jet's new introduction year: "))
    max_speed = int(input("Jet's new max speed: "))
    armament = input("Jet's new armament: ")
    cur.execute("UPDATE JetModel SET IntroductionYear = ?, MaxSpeed = ?, Armament = ? WHERE Name = ?",
                (introduction, max_speed, armament, jet))
    db.commit()
    return


# queries
def read_file(filename):
    with open(filename, "r") as sql_file:
        sql_script = sql_file.read()
    return sql_script


def query1():
    sql_script = read_file("query_1.sql")
    cur.execute(sql_script)
    rows = cur.fetchall()
    print("Model, Introduction Year, Max Speed")
    for row in rows:
        print(row)


def query2():
    sql_script = read_file("query_2.sql")
    cur.execute(sql_script)
    rows = cur.fetchall()
    print("ModelID, Model, Introduction Year, Max Speed, Armament, ManufacturerID")
    for row in rows:
        print(row)


def query3():
    sql_script = read_file("query_3.sql")
    cur.execute(sql_script)
    rows = cur.fetchall()
    print("Manufacturer, Model, Headquarter location")
    for row in rows:
        print(row)


def query4():
    sql_script = read_file("query_4.sql")
    cur.execute(sql_script)
    rows = cur.fetchall()
    print("Pilot, Air force, Country")
    for row in rows:
        print(row)


def query5():
    sql_script = read_file("query_5.sql")
    cur.execute(sql_script)
    rows = cur.fetchall()
    print("Model, Introduction Year, Max Speed")
    for row in rows:
        print(row)


def query6():
    sql_script = read_file("query_6.sql")
    cur.execute(sql_script)
    rows = cur.fetchall()
    print("Model, Air force")
    for row in rows:
        print(row)


# Main call
main()
