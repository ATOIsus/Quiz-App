

import pickle

ques = ([ "Can you hear the sound behind you if you are travelling at the speed of sound ?", 
          "Yes", "No"],
                
        [ "What quantity is velocity ?", 
	  "Vector" , "Scalar" ,  "Both", "None"],

        ["Water flows through a horizontal pipe at a constant volumetric rate. At a location where the cross sectional area decreases, the velocity of the fluid :",
         "Increases",  "Decreases" , "Stays the same"],

        ["The word atom is from a Greek word meaning :",
         "Indivisible", "Small",  "Unseen",  "Visible"],

        ["Electric power is less expensive at night because :",
         "There is less demand at night.", "More hydroelectric generation is brought on line at night.", "Pollution control is less stringent at night.",
         "Power plants are more efficient at night."],

        ["Seawater (i.e. saltwater) freezes at :",
         "At a slightly lower temperature than fresh water." ,"The same temperature as fresh water.", "At a slightly higher temperature than fresh water." ,
         "Seawater does not freeze."],

        ["Nitrous oxide, commonly called laughing gas, has been a matter of concern to environmentalists recently because :",
         "It is a greenhouse gas.", "It is thought to cause cancer at low concentrations.", "It produces photochemical smog." , "None of the above"],

        ["Ozone in the upper atmosphere is produced from :",
         "Photochemical reactions", "Lightning", "Electrical appliances on Earth", "Model fractals"],

        ["The radioactive element most commonly detected in humans is :",
         "Potassium-40","Cobalt-60", "Iodine-131", "Plutonium-238"],

        ["Most commercial nuclear power plants worldwide are cooled by :",
         "Water", "Sodium", "Mercury", "Helium"],

        ["Spent fuel from a nuclear power plant cools down and loses most of its radioactivity through decay. In the first year, spent fuel loses about what percentage of its radioactivity ?",
         "80 percent", "50 percent", "10 percent", "100 percent"],

        ["What range of frequencies are usually referred to as audio frequencies for humans ?",
         "20 to 20,000 Hertz", "0 to 20 Hertz", "200 to 200,000 Hertz", "10,000 to 30,000 Hertz"],

        ["A device used to measure the amount of moisture in the atmosphere is called a :",
         "Hygrometer", "Hydrometer", "Anemometer", "Barometer"],

        ["The most suitable motor oil for use in a car in cold weather is :",
          "A low viscosity oil", "A high viscosity oil", "A medium viscosity oil "],

        ["The first animal launched into orbit was a :",
         "Dog", "Mouse", "Monkey", "Chimpanzee"],

        ["Thermal insulation is used to :",
         "Reduce the flow of heat." ,"Stop the flow of heat.", "Absorb heat.", "reverse the heat flow direction."],

        ["The most abundant organic molecule on the surface of the Earth is :",
         "Cellulose", "Chitin", "DNA", "Hemoglobin"],

        ["The sun makes up approximately what percent of matter in our solar system ?",
         "99%", "17%", "50%", "85%"],

        ["The image formed in a compound microscope is :",
         "Inverted", "Erect"],

        ["Which colour of light is deviated least : ",
         "Red", "Blue", "Green", "Orange"]
         )


file = open('Science.txt', 'ab')


pickle.dump(ques, file)
file.close()

