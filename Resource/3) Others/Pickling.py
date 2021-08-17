

import pickle

ques = (['When did Nepal join UN? ', ' 1955 ', '1984  ', ' 1948 ', ' 1976'],
       ['In which script is Nepali written? ', ' Devanagari ', ' Brahmi ', ' Kharoshti ', ' Urdu'],
       ['When was Tribhuvan University set up? ', ' 1959 ', ' 1952 ', ' 1944 ', ' 1937'],
       ['Who was Nepal’s king in 1911-1955? ', ' Tribhuvan ', ' Birendra ', ' Mahendra ', ' Devendra'],
       ['What is freedom of religion? ', 'You can practice any religion', ' or not practice a religion.   ',
        ' You must choose a religion. ', ' You can’t choose the time you practice your religion.  ',
        ' No one can practice a religion.'],
       ['Who is in charge of the executive branch? ', ' The President.  ', ' The Prime Minister. ',
        ' The Speaker of the House.  ', ' The Chief Justice.'],
       ['Who vetoes bills? ', ' The President ', ' The Vice President ', ' The Senate ',
        ' The House of Representatives'],
       ['We elect a President for how many years? ', ' Four (4).  ', ' Two (2).  ', ' Eight (8).  ', ' Ten (10).'],
       ['The idea of self-government is in the first three words of the Constitution. What are these words? ',
        ' We the People. ', ' Congress shall make. ', ' We the British. ', ' We the Colonists.'],
       ['What is the “rule of law”?  ', ' Everyone must follow the law. ',
        ' Government does not have to follow the law. ', ' All laws must be the same in every state. ',
        ' Everyone but the President must follow the law.'],
       ['How old do citizens have to be to vote for President? ', ' Eighteen (18) or older  ',
        ' Sixteen (16) or older.  ', ' Twenty-one (21) or older. ', ' Thirty-five (35) or older.'],
       ['What does the judicial branch do? ', ' All of the above. ', ' Reviews laws. ', ' Resolves disputes. ',
        ' Decides if a law goes against the Constitution.'],
       ['What is an amendment? ', ' An addition (to the Constitution). ', ' The Preamble to the Constitution. ',
        ' An introduction. ', ' The beginning of the Declaration of Independence.'],
       ['What is the supreme law of the land? ', ' The Constitution. ', ' The local law. ',
        ' The Emancipation Proclamation. ', ' The Declaration of Independence.'],
       ['What is one right or freedom granted by the First Amendment? ', ' Speech. ', ' To vote. ', ' To bear arms. ',
        ' Trial by jury.'], ['What did the Emancipation Proclamation do?  ', ' Freed slaves in most Southern states.  ',
                             ' Ended World War I. ', ' Gave women the right to vote. ',
                             ' Gave the United States independence from Great Britain.'],
       ['How many amendments does the Constitution have?  ', ' 27  ', ' 18 ', ' 25 ', ' 17  '],
       ['How many justices are on the Supreme Court? ', ' 9 ', ' 5 ', ' 12 ', ' 3'],
       ['What does the President’s Cabinet do? ', ' Advises the president ', ' Selects the Vice President ',
        ' Runs the government when the President travels ', ' Negotiates treaties with foreign nations'],
       ['Name one branch or part of the government. ', ' Legislative.  ', ' State government.  ', ' Parliament. ',
        ' United Nations.'])




file = open('Politics.txt', 'ab')


pickle.dump(ques, file)
file.close()

