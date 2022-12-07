# this model file interacts with the DB
# handle all data related to the table 'dogs'
from mysqlconnection import connectToMySQL
DATABASE = "dogs_db"

class Dog:
    def __init__(self, data):
        self.id = data["id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.breed = data["breed"]
        self.name = data["name"]
        self.age = data["age"]
        self.color = data["color"]

    # ALL queries are classmethods
    # so that they have access to the class
    
    # ========= READ ALL ===========
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dogs;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        dog_instances = []
        if results:
            for row in results:
                this_dog = cls(row)
                dog_instances.append(this_dog)
            return dog_instances
        return []
    
    # ========== CREATE ===========
    @classmethod
    def create(cls, data):
        #! %()s is to protect form sql injection - var name 
        query = """
            INSERT INTO dogs (name, age, breed, color)
            VALUES (%(name)s, %(age)s, %(breed)s, %(color)s);
        """
        #! data must have the exact keys from the Form
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # ========== READ ONE ============
    @classmethod
    def get_one(cls, data):
        query = """
            SELECT * FROM dogs
            WHERE id=%(id)s;
        """
        #? SELECT is ALWAYS a LIST of dictionaries -  even if we only get 1
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False
        