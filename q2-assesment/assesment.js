// **Ancestral Stories:** In many African cultures, the art of storytelling is passed
// down from generation to generation. Imagine you're creating an application that
// records these oral stories and translates them into different languages. The
// stories vary by length, moral lessons, and the age group they are intended for.
// Think about how you would model `Story`, `StoryTeller`, and `Translator`
// objects, and how inheritance might come into play if there are different types of
// stories or storytellers.

class StoryTeller{
    constructor(length,moralLessons,ageGroup){
        this.length=length
        this.moralLessons=moralLessons
        this.ageGroup=ageGroup
    }
    

}

// **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// methods.

// sudo code

// class Recipe
// subclasses Moroccan food





class Recipe {
    constructor(name,unique_ingredients,preparationTime,cooking_method,nutritional) {
        this.name=name
      this.unique_ingredients=unique_ingredients
      this.preparationTime=preparationTime
      this.cookingMethod=cooking_method
      this.nutritional=nutritional
    }
  
    displayRecipe() {
        return `:name ${this.name}`;
        return `:unique_ingredients ${this.unique_ingredients}`;
        return`: preparationTime${this.preparationTime}`;
        return`cooking_method: ${this.cooking_method}`;
        return `nutritional: ${this.nutritional}`;
      
    }
  }
  
  class MoroccanRecipe extends Recipe {
    constructor(name ) {
      super(name, 'Morocco', this.nutritional, preparationTime, cooking_method);
      
    }
  
    displayRecipe() {
      super.displayRecipe();
      return`Cooking time: ${this.cooking_method}`;
    }
  }
  
  class EthiopianRecipe extends Recipe {
    constructor(name,unique_ingredients,preparationTime,cooking_method,nutritional) {
      super(name, 'Ethiopia',unique_ingredients, preparationTime, cooking_method);
      
    }
  
  }
  
  class NigerianRecipe extends Recipe {
    constructor(name, ingredients, preparationTime, cooking_method,spicy) {
      super(name, 'Nigeria', ingredients, preparationTime, cookingMethod);
      this.spicy=spicy
     
    }
  
    displayRecipe() {
      super.displayRecipe();
      return`How the food is: ${this.spicy}`;
    }
  }

const recipe1=new Recipe("Tokyo","spicy","Noon","Boiled","healthy")
console.log(recipe1.displayRecipe())

const moroccanRecipe=new MoroccanRecipe()
  


// **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to

// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.




class WildlifePreservation{
    constructor( name, diet, typical_lifespan,migration_pattern){


    this.name = name
    this.diet = diet
    this.typical_lifespan = typical_lifespan
    this.migration_pattern=migration_pattern
}
}

class Predator extends WildlifePreservation{
    constructor( name, diet, typical_lifespan, hunting_method){
   
    this.hunting_method = hunting_method

    }
}
class Prey extends WildlifePreservation{
    constructor( name, diet, typical_lifespan, migration_pattern){
    
    this.migration_pattern = migration_pattern

}  
}
       