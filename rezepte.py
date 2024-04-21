import json

class Recipe:
    def __init__(self, name, main_ingredients, spices):
        self.name = name
        self.main_ingredients = main_ingredients
        self.spices = spices
try:
    def load_ingredients_and_spices(json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
except:
    print("Leider ist eines der Rezepte leer")
def can_cook_recipe(recipe, available_main_ingredients, available_spices):
    main_ingredients_present = [ingredient for ingredient in recipe.main_ingredients if ingredient in available_main_ingredients]
    spices_present = [spice for spice in recipe.spices if spice in available_spices]
    can_cook = len(main_ingredients_present) == len(recipe.main_ingredients) and len(spices_present) == len(recipe.spices)
    return can_cook, main_ingredients_present, spices_present
def main():
    # Rezepte definiert
    recipes = [
        Recipe("Rindfleisch mit Reis und Brokkoli", ["Rindfleisch", "Reis", "Brokkoli"], ["Salz", "Pfeffer", "Fischsauce", "Magi"]),
        Recipe("Schwarzbrot mit Butter und Salami", ["Schwarzbrot", "Butter", "Salami"], ["Salz", "Pfeffer"]),
        Recipe("Schwarzbrot mit Butter und Salami mit Käse", ["Schwarzbrot", "Butter", "Salami", "Käse"], ["Pfeffer", "Salz"]),
        Recipe("Schwarzbrot mit Butter und Wurst", ["Schwarzbrot", "Butter", "Wurst"], ["Pfeffer", "Salz"]),
        Recipe("Schwarzbrot mit Butter und Wurst mit Käse", ["Schwarzbrot", "Butter", "Wurst", "Käse"], ["Pfeffer", "Salz"]),
        Recipe("Schwarzbrot mit Butter und Käse", ["Schwarzbrot", "Butter", "Käse"], ["Pfeffer", "Salz"]),
        Recipe("Schwarzbrot mit Caviar und Butter", ["Schwarzbrot", "Caviar", "Butter"], ["Salz", "Pfeffer"]),
        Recipe("Schwarzbrot mit Caviar und Butter mit Käse", ["Schwarzbrot", "Caviar", "Butter", "Käse"], ["Salz", "Pfeffer"]),
        Recipe("Schwarzbrot mit Caviar und Butter mit Schinken", ["Schwarzbrot", "Caviar", "Butter", "Schinken"], ["Salz", "Pfeffer"]),
        Recipe("Schwarzbrot mit Caviar und Butter mit Schinken mit Käse", ["Schwarzbrot", "Caviar", "Butter", "Schinken", "Käse"], ["Salz", "Pfeffer"]),
        Recipe("Schwarzbrot mit Leberwurst und Butter", ["Schwarzbrot", "Leberwurst", "Butter"], ["Salz", "Pfeffer"]),
        Recipe("Toastbrot mit Butter und Salami Sandwich", ["Toastbrot", "Butter", "Salami"], ["Salz", "Pfeffer"]),
        Recipe("Toastbrot mit Butter und Salami Sandwich mit Käse", ["Toastbrot", "Butter", "Salami", "Käse"], ["Salz", "Pfeffer"]),
        Recipe("Toastbrot mit Butter und Wurst Sandwich", ["Toastbrot", "Butter", "Wurst"], ["Salz", "Pfeffer"]),
        Recipe("Toastbrot mit Butter und Wurst Sandwich mit Käse", ["Toastbrot", "Butter", "Wurst", "Käse"], ["Salz", "Pfeffer"]),
        Recipe("Toastbrot mit Butter und Käse Sandwich", ["Toastbrot", "Butter", "Käse"], ["Salz", "Pfeffer"]),
        Recipe("Toastbrot mit Hering Tomaten und Butter", ["Toastbrot", "Tomatenhering", "Butter"], ["Salz", "Pfeffer"]),
        Recipe("Bratreis mit Ei", ["Reis", "Ei", "OlivenÖl"], ["Salz", "Pfeffer", "Fischsauce", "Magi"]),
        Recipe("Hühnchen mit Reis und Brokkoli", ["Hühnchen", "Reis", "Brokkoli"], ["Curry", "Salz"]),
        Recipe("Ei mit Reis", ["Reis", "Ei"], ["Salz", "Pfeffer", "Fischsauce", "Magi"]),
        Recipe("Spaghetti mit Ketchup", ["Ketchup", "Nudeln", "Speckwürfel", "Ei"], ["Zimt", "Salz", "Pfeffer"]),
        Recipe("Spaghetti mit Tomatensauce ohne Fleisch aus der Verpackung", ["Nudeln mit Tomatensauce Verpackung"], ["Salz", "Pfeffer", "Rinderbrühe"]),
        Recipe("Ramen" , ["Ramen"], ["Salz", "Pfeffer", "Fischsauce", "Magi", "Ingwer", "Zwiebeln", "Knoblauch"]),
        Recipe("Reis mit Hühnerbrust", ["Reis", "Hühnerbrust"], ["Salz", "Pfeffer", "Fischsauce", "Magi", "Ingwer", "Zwiebeln", "Knoblauch", "Zucker"]),
        #sonstiges
        Recipe("Nudeln mit Pesto", ["Nudeln", "Pesto"], ["Salz", "Pfeffer", "OlivenÖl"]),
        Recipe("Nudeln mit Pesto und Hühnerbrust", ["Nudeln", "Pesto", "Hühnerbrust"], ["Salz", "Pfeffer", "OlivenÖl"]),
        Recipe("Omelett mit Hackfleisch", ["Ei", "Hackfleisch"], ["Salz", "Pfeffer", "Fischsauce", "Magi","Zwiebeln"]),
        Recipe("Tomaten mit Hackfleisch und Reis", ["Reis","Tomaten", "Hackfleisch"], ["Salz", "Pfeffer", "Fischsauce", "Magi","Zwiebeln", "Knoblauch", "Ingwer"]),
        Recipe("Bologenese", [ "Hackfleisch", "Tomatenglas", "Möhren", "Tomatenmark", "Käse" ], ["Rinderbrühe","Salz", "Pfeffer", "Fischsauce", "Magi","Zwiebeln", "Knoblauch", "Ingwer"]),
        #gesund
        Recipe("Joghurt", ["Joghurt"], [""]),
        Recipe("Joghurt mit Müsli", ["Joghurt", "Müsli"], [""]),
        Recipe("Joghurt mit Apfel", ["Joghurt", "Apfel"], [""]),
        Recipe("Joghurt mit Nektarine", ["Joghurt", "Nektarine"], [""]),
        Recipe("Lachs mit Reis", ["Lachs", "Reis"], ["Salz", "Pfeffer", "Magi", "Knoblauch"]),
        Recipe("Lachs mit Reis und Tomaten", ["Lachs", "Reis", "Tomaten"], ["Salz", "Pfeffer", "Magi", "Knoblauch"]),
        Recipe("Banane", ["Banane"], [""]),
        Recipe("Rinderfleisch mit Reis", ["Reis", "Rindfleisch"], ["Salz", "Pfeffer", "Fischsauce", "Magi", "Ingwer", "Zwiebeln", "Knoblauch", "Zucker"]),
        Recipe("Ramen mit Rindfleisch", ["Ramen", "Rindfleisch"], ["Salz", "Pfeffer", "Fischsauce", "Magi", "Ingwer", "Zwiebeln", "Knoblauch", "Zucker"]),
        Recipe("Ramen mit Ei", ["Ramen", "Ei"], ["Salz", "Pfeffer", "Fischsauce", "Magi", "Ingwer", "Zwiebeln", "Knoblauch", "Zucker"]),
        Recipe("Ramen mit Ei und Rindfleisch", ["Ramen", "Ei", "Rindfleisch"], ["Salz", "Pfeffer", "Fischsauce", "Magi", "Ingwer", "Zwiebeln", "Knoblauch", "Zucker"]),
        Recipe("Ramen mit Pilze und Reis", ["Ramen", "Pilze", "Reis"], ["Salz", "Pfeffer", "Fischsauce", "Magi", "Ingwer", "Zwiebeln", "Knoblauch", "Zucker"]),
        Recipe("Bratkartoffeln mit Speck", ["Bratkartoffeln", "Speck"], ["Salz", "Pfeffer", "Fischsauce", "Magi", "Ingwer", "Zwiebeln", "Knoblauch", "Zucker"]),
        Recipe("Bratkartoffeln mit Speck und Ei", ["Bratkartoffeln", "Speck", "Ei"], ["Salz", "Pfeffer", "Fischsauce", "Magi", "Ingwer", "Zwiebeln", "Knoblauch", "Zucker"]),
        #ungesund
        Recipe("Hot Dog, Wurst mit Brötchen", ["Hot Dog Brötchen", "Wurst", "Käse"], ["Ketchup", "Senf", "Mayonaise", "Salz", "Pfeffer", "Rostzwiebeln"]),
        Recipe("Eiersalat", ["Ei", "Schwarzbrot"], ["Salz", "Pfeffer", "Zwiebeln", "Knoblauch","Mayonaise", "Senf"]),
        Recipe("Eiersalat mit Toast", ["Ei", "Toastbrot"], ["Salz", "Pfeffer", "Zwiebeln", "Knoblauch","Mayonaise", "Senf"]),
        Recipe("Pancakes", ["Pancakes"], ["Ahornsirup", "Butter"]),
        Recipe("Garlic Noodles", ["Nudeln", "Knoblauch"], ["Salz", "Pfeffer", "Fischsauce", "Magi","Soysauce", "Knoblauch"]),
        Recipe("Garlic Noodles mit Hühnerbrust", ["Nudeln", "Knoblauch", "Hühnerbrust"], ["Salz", "Pfeffer", "Fischsauce", "Magi","Soysauce", "Knoblauch"]),
        Recipe("Garlic Noodles mit Hühnerbrust und Ei", ["Nudeln", "Knoblauch", "Hühnerbrust", "Ei"], ["Salz", "Pfeffer", "Fischsauce", "Magi","Soysauce", "Knoblauch"]),
        Recipe("Garlic Noddles mit Ei", ["Nudeln", "Knoblauch", "Ei"], ["Salz", "Pfeffer", "Fischsauce", "Magi","Soysauce", "Knoblauch"]),
        Recipe("Reis mit Schnitzel und Ei", ["Reis", "Schnitzel", "Ei"], ["Salz", "Pfeffer"]),
        #mexican
        Recipe("Taco mit Fleisch, Käse, Burgersauce und Salat", ["Taco", "Hackfleisch", "Käse", "Burgersauce", "Bergsalat"], ["Salz", "Pfeffer", "Fischsauce", "Magi", "Ingwer", "Zwiebeln", "Knoblauch"]),
        #japanisch
        Recipe("Sushirolls" , ["Reis", "Lachs", "Seetang"], ["Sojasauce", "Wasabi", "Ingwer", "Reisessig", "Zucker", "Salz", "Pfeffer"]),
        Recipe("Takoyaki", ["Takoyaki"], ["Lauchzwiebeln", "Mayonaise", "Okonomi Sauce"]),
        #obst
        Recipe("Apfel" , ["Apfel"], [""]),
        Recipe("Nektarine" , ["Nektarine"], [""]),
        # vietnamesisch
        Recipe("Reis mit Schweinebauch und Tomaten" , ["Reis", "Schweinebauch", "Tomaten"], ["Salz", "Pfeffer", "Fischsauce", "Magi", "Ingwer", "Zwiebeln", "Knoblauch"]),
        Recipe("Ramen fritiert" , ["Ramen", "Ei"], ["Salz", "Pfeffer", "Knoblauch", "Zwiebeln"]),
        Recipe("Schweinebauch Kross" , ["Schweinebauch"], ["Salz", "Pfeffer", "Knoblauch", "Zwiebeln"]),
        Recipe("Nudeln mit Pesto, Zuchini und Tomate" , ["Nudeln", "Zucchini", "Tomate", "Pesto"], ["Salz", "Pfeffer", "Knoblauch"]),
        Recipe("Weizenbrot ohne Ei" ,["Weizenmehl"] , ["Salz", "Zucker", "Wasser", "Hefe", "Salz", "Zucker", "Olivenöl"])
    ]
    available_main_ingredients = load_ingredients_and_spices('A:/Desktop/Scripts/Essen/hauptzutaten.json')
    available_spices = load_ingredients_and_spices('A:/Desktop/Scripts/Essen/gewürze.json')
    for recipe in recipes:
        can_cook, main_ingredients_present, spices_present = can_cook_recipe(recipe, available_main_ingredients, available_spices)
        if can_cook:
            print(f"Du kannst das Rezept '{recipe.name}' kochen.")
        else:
            print(f"Du kannst das Rezept '{recipe.name}' NICHT kochen, es fehlen Zutaten oder Gewürze.")
            print(f"{len(main_ingredients_present)} sind in Hauptzutaten drin und {len(spices_present)} sind in Gewürze drin.")
if __name__ == "__main__":
    main()