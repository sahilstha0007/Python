class Recipe:
    def __init__(self, name, cuisine, ingredient, rating):
        self.name= name
        self.cuisine= cuisine
        self.ingredient= ingredient
        self.rating= rating 

        def get_name (self):
            return self.name
        def get_cuisine (self):
            return self.cuisine
        def get_ingredient (self ):
            return self.ingredient
        def get_rating (self):
            return self.rating



        def set_name (self,name ):
            self.name = name
        def set_cuisine (self,cuisine ):
            self.cuisine = cuisine
        def set_name (self,ingredient):
            self.ingredient = ingredient
        def set_rating (self,rating):
            self.rating = rating

    def _str_(self):
        return f"{self.name} - Cuisine: {self.cuisine} , Ingredient: {self.ingredient}, Rating: {self.rating} "