# Pickle the question into byte stream in a text file.
# 8 text files for 8 topic.
# Some errors occurred while using .JASON file.
# This is done after questions are converted into a list of lists.



import pickle
from tkinter import messagebox

try:

    ques = (['Which of the following countries are associated most closely with Lassi? ', ' India and Pakistan  ', ' Sweden and Denmark ', ' Belgium and France  ', ' USA and Canada'],
     ['What is a mistake? ', ' You  ', ' The world ', ' The prince ', ' The god'],
     ['With which of the following leaders would you associate the Mongol Empire? ', ' Genghis Khan  ', ' Saladin ', ' Attila the Hun ', ' Alexander the Great'],
     ['Against which country did Britain fight the 19th century Opium Wars? ', ' China  ', ' Germany ', ' Russia ', ' France'],
     ['What was the codename for Nazi Germanys invasion of the Soviet Union in 1941? ', ' Barbarossa  ', ' Charlemagne ', ' Napoleon ', ' Attila'],
     ['Which country, also known as Land Of The Morning Calm, is known as Hanguk by its inhabitants? ', ' South Korea ', ' Haiti ', ' Vietnam ', ' Kenya'],
     ['In which district is Fungfung waterfall? ', ' Nuwakot ', ' Chitwan ', ' Khotang ', ' Lamjung'],
     ['How many Heritages of Nepal is listed in the World Heritage Site? ', ' 10 ', ' 2 ', ' 9 ', ' 7'],
     ['How much percentage of Nepal’s total land is cultivated for Farming? ', ' 17.97%  ', ' 19.23% ', ' 1% ', ' 45% '],
     ['How many business ways have been opened by Nepal and India? ', ' 27 ', ' 21 ', ' 54 ', ' 3'],
     ['How many years did the Gopal dynasty rule in Nepal? ', ' 521 ', ' 435 ', ' 69 ', ' 511'],
     ['Who is the first martyr of Nepal? ', ' Lakhan Thapa  ', ' Shukraraj Shastri ', ' Dashrath Chand ', ' Gangalal Shrestha'],
     ['How many states are there in Nepal at present? ', ' 7 ', ' 4 ', ' 6 ', ' 9'],
     ['Which is the largest province of Nepal in terms of population? ', ' Province 3 ', ' Province 5 ', ' Province 1 ', ' Province 4'],
     ['In which province is Kathmandu in? ', ' Province 3 ', ' Province 5 ', ' Province 8 ', ' Province 6'],
     ['Which is the tallest mountain in the world? ', ' Mt. Everest ', ' Mt. Lhotse ', ' K2 ', ' Mt. Makalu'],
     ['Which is the world’s smallest country? ', ' Vatican City  ', ' Monaco ', ' Nauru ', ' Tuvalu'],
     ['Which planet is closest to Planet Earth? ', ' Venus ', ' Earth  ', ' Mars ', ' Mercury'],
     ['On which day of the year is the Sun closest to the Earth? ', ' January 4th  ', ' December 19 ', ' August 8 ', ' November 2'],
     ['Which country produces maximum aluminium in the world? ', ' China ', ' USA ', ' Chile ', ' Nauru'])


    file = open('GK.txt', 'ab')  # Creates a new text file: Math.txt.
    pickle.dump(ques, file)        # Pickling the ques tuple into byte steam to the Math.txt file.
    file.close()


except BaseException as er:
    messagebox.showerror("Error", str(type(er))[6:-1] + " : " + str(er))