# class Culture:
#     def __init__(self):





# **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.


class Recipe:
    def __init__(self, name,unique_ingredients,preparationTime,cooking_method,nutritional):
        
        self.unique_ingredients=unique_ingredients
        self.preparationTime=preparationTime
        self.cookingMethod=cooking_method
        self.nutritional=nutritional


        displayRecipe()

        return 'name ${self.name}'
        return 'unique_ingredients ${self.unique_ingredients}'
        return ' preparationTime${self.preparationTime}'
        return'cooking_method: ${self.cooking_method}'
        return 'nutritional: ${self.nutritional}'
      
        class MoroccanRecipe (Recipe)  :
           def __init__(name ) :
               super(name, 'Morocco', this.nutritional, preparationTime, cooking_method)
      
    
  
        displayRecipe() 
        super.displayRecipe()
        return'Cooking time: ${self.cooking_method}'
    
        
        class EthiopianRecipe(Recipe) :
            def __init__(self, name,unique_ingredients,preparationTime,cooking_method,nutritional):

                super(name, 'Ethiopia',unique_ingredients, preparationTime, cooking_method)
      
        class NigerianRecipe (Recipe)  :

            def __init__(name, ingredients, preparationTime, cooking_method,spicy) :
                super(name, 'Nigeria', ingredients, preparationTime, cookingMethod)
                this.spicy=spicy

        class EthiopianRecipe (Recipe)  :
            def__init__(name,unique_ingredients,preparationTime,cooking_method,nutritional)

            super(name, 'Ethiopia',unique_ingredients, preparationTime, cooking_method)
      

        class NigerianRecipe ( Recipe):
            def __init__(name, ingredients, preparationTime, cooking_method,spicy) :
             super(name, 'Nigeria', ingredients, preparationTime, cookingMethod)
            #  self.spicy spicy
     
    
  
        displayRecipe() 
        super.displayRecipe()
        return'How the food is: ${this.spicy}'
    
  

recipe1= Recipe("Tokyo","spicy","Noon","Boiled","healthy")

print(recipe1.displayRecipe())

moroccanRecipe= MoroccanRecipe()



# **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to

# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.

class WildlifePreservation:
    def __init__(self, name, diet, typical_lifespan,migration_pattern):
        self.name = name
        self.diet = diet
        self.typical_lifespan = typical_lifespan
        self.migration_pattern=migration_pattern


class Predator(WildlifePreservation):
    def __init__(self, name, diet, typical_lifespan, hunting_method):
        super().__init__(name, diet, typical_lifespan)
        self.hunting_method = hunting_method


class Prey(WildlifePreservation):
    def __init__(self, name, diet, typical_lifespan, migration_pattern):
        super().__init__(name, diet, typical_lifespan)
        self.migration_pattern = migration_pattern


wildlife=WildlifePreservation("Serengeti","predators","natural","high")
print( wildlife.pray())



# **African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.