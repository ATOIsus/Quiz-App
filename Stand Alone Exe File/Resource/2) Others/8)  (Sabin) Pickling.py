# Pickle the question into byte stream in a text file.
# 8 text files for 8 topic.
# Some errors occurred while using .JASON file.
# This is done after questions are converted into a list of lists.



import pickle
from tkinter import messagebox

try:

    ques = (['Binary coded decimal (BCD) numbers express each digit is a ', ' Nibble ', ' Byte ', ' Bit All of these'],
        ['ASCII code is an ', ' Alpha numeric code ', ' Cyclic code ', ' Numeric code ', ' Alphabet code'],
	['The decimal equivalent of binary number 0.0111 is ', ' 0.4375 ', ' 4.375 ', ' 0.5375 ', ' -0.4375'],
        ['The two’s complement in binary system is useful for expressing ', ' Negative numbers ', ' None of these ', ' Both positive and negative numbers ', ' Positive numbers'],
        ['The right most bit is the ____ and has the smallest positional weight. ', ' LSB', ' PSB ', ' MSB ', ' NSB'],
	['The speedup of a processor is estimated using which of the following parameters: ', ' Execution time in one and N processors', ' Cycles per instruction in one and N processors', ' None of the above', ' Throughput'],
        ['The general structure of the VON NEUMANN machine consists of ', " ' Main memory', ' arithmetic and logic unit', ' control unit' ", " 'Input / Output ' ", " ' Cores', ' ALU', ' CPU', ' devices ' ", " ' Pipeline', ' main memory', ' motherboard' "],
        ['Which type of topology is best suited for large businesses which must carefully control and coordinate the operation of distributed branch outlets? ', ' Hierarchical ', ' Star ', ' Ring ', ' Local area'],
        ['Which of the following transmission directions listed is not a legitimate channel? ', ' Double Duplex ', ' Simplex ', ' Half Duplex ', ' Full Duplex'],
        ['What kind of transmission medium is most appropriate to carry data in a computer network that is exposed to electrical interferences? ', ' Optical fiber ', ' Unshielded twisted pair ', ' Coaxial cable ', ' Microwave'],
        ['The maximum length (in bytes) of an IPv4 datagram is? ', ' 65535 ', ' 512 ', ' 1024 ', ' 32'],
        ['The IP network 192.168.50.0 is to be divided into 10 equal sized subnets. Which of the following subnet masks can be used for the above requirement? ', ' 255.255.255.0 ', ' 255.255.255 ', ' 255.255.0.0 ', ' 255.0.0.0'],
        ['The length of an IPv6 address is? ', ' 128 bits ', ' 256 bits ', ' 32 bits ', ' 64 bits'],
	['Which of the following address belongs class A? ', ' 121.12.12.248 ', ' 129.12.12.248 ', ' 130.12.12.248 ', ' 128.12.12.248'],
	['Which of the following IP addresses can be used as a loop-back addresses? ', ' 127.0.0.1 ', ' 255.255.255.255 ', ' 0.255.255.255 ', ' 0.0.0.0'],
	['What IP address class allocates 8 bits for the host identification part? ', ' Class C ', ' Class D ', ' Class A ', ' Class B'],
	['How many versions available of IP? ', ' 4 version ', ' 2 version ', ' 1 version ', ' 6 version'],
	['TCP/IP model does not have ______ layer but OSI model have this layer. ', ' Session layer ', ' Transport layer ', ' Application layer ', ' Network layer'],
	['Transmission control protocol ___________ ', ' All of the mentioned ', ' Is a connection-oriented protocol ', ' Uses a three way handshake to establish a connection ', ' Receives data from application as a single stream'],
        ['Which of the following are transport layer protocols used in networking? ', ' TCP and UDP ', ' UDP and HTTP ', ' TCP and FTP ', ' HTTP and FTP'])


    file = open('Architecture.txt', 'ab')  # Creates a new text file: Architecture.txt.
    pickle.dump(ques, file)        # Pickling the ques tuple into byte steam to the Architecture.txt file.
    file.close()


except BaseException as er:
    messagebox.showerror("Error", str(type(er))[6:-1] + " : " + str(er))