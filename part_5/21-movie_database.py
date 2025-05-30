# Write your solution here

def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    database_dict = {}
    database_dict["name"] = name
    database_dict["director"] = director
    database_dict["year"] = year
    database_dict["runtime"] = runtime
    database.append(database_dict)
    

if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)