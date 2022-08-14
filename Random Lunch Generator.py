import random
print("What do you want to eat today?")

food_lists = {
    "pizza": ["Dominos",'Pizza Hut',"Little Caesars","Marco's",'Little Caesars',"Papa John's","jet's","Pizza in","Rocco's Pizza Shop","CiCi's Pizza","Godfather's Pizza"],
    "Sandwitches": ['Subway','Jersey Mikes','Penn Station','Firehouse Subs','The Sub Station','Magic Subs & Gyros',"Mr. Zub's Deli", 'Corral Sanwich Shop','Hanini Subs',"Jimmy John's"],
    "Mexican": ['Taco Bell','Funky Truckeria','Chipotle',"Tito's Mexican Grill",'Tres Potrillos','El Rancho',"Moe's Southwest Grill",'BOMBA Tacos','Qdoba','Casa Del Rio'],
    "Burgers": ['Wayback','The Rail','Five Guys',"Louie's Bar & Grille","Bob's Hamburg",'Swensons',"Rally's",'Skyway',"Hodge's Cafe","Wendy's",'Burger King',"McDonald's"],
    "Healthy": ['First Watch',"Ms. Julie's Kitchen",'Continental Cuisine',"Niko's Sandwich Board",'Poke Fresh','Zoup!',"Aladdin's Eatery","Beau's Grille",'Valley Cafe','CoreLife Eatery'],
    "Asian": ['China King','Imperial Wok','China Star','Platinum Dragon','Sushi Asia Gormet','China Express','New Ming Restaurant','House of Hunan','Sushi Katsu','Sakura','T J Sushi','Big Eye Japanese Cuisine & Sushi Bar','Hong Kong Buffet','Taste of Bankok','Hyde Out']}



category = random.choice(list(food_lists.keys()))
rest_list=random.choice(food_lists[category])
print("You will eat " + category)
print("At "+ rest_list)
