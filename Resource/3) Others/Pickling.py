

import pickle

ques = (['Which of the following is the set of positive integers? ', ' Infinite ', ' Subset ', ' Finite ', ' Empty'],
        ["Which of the following is union of {'1', '2', '5'} and {'1', '2', '6'} ? ", " {'1' , '2', '5', '6'} ", " {'1', '2', '6', '1'} ", " {'1', '2', '1', '2'} ", " {'1', '5', '6', '3'}"],
        ['Which of the following is complement of the set A? ', ' U – A  ', ' A – B ', ' A – U ', ' B – A'],
	['The relation between sets A', ' B', ' C as shown by venn diagram is ', ' C is subset of B and B is subset of A ', ' A is subset of B and B is subset of C ', ' C is not a subset of A and A is subset of B ', ' None of These'],
        ['Which of the following statement is false? ', ' (A U B)’ = A’ U B’  ', ' A X A = A ', ' A U A = A ', ' A – (B U C) = (A – B) U (A –C)'],
	['If a set contains 3 elements then the number of subsets are? ', ' 8 ', ' 6 ', ' 3 ', ' 12'],
        ['How many bytes are required to encode 2000 bits of data? ', ' 2 ', ' 8 ', ' 5 ', ' 32'],
	['Floor (2.4) + Ceil (2.9) is equal to ', ' 5 ', ' 1 ', ' 6.3 ', ' 7'],
        ['Which of the following is a collection of graph? ', ' Vertices and columns ', ' Row and column  ', ' Equation ', ' None of above'],
	['Which of the following is a error correcting code? ', ' Hamming code ', ' Error deducting code ', ' Gray code ', ' None of the above'],
	['The set of positive integers under the operation of ordinary multiplication is ', ' An Abelian group ', ' A group ', ' Not a group ', ' Not a monoid'],
        ['The number of eight-bit strings beginning with either 111 or 101 is - ', ' 64 ', ' 128 ', ' 256 ', ' 312'],
        ['Let A and B be two arbitrary events,  then ', ' P(AUB) not equal to P(A)+P(B) ', ' P(A X B) = P(A) X P (B) ', ' P(AUB) = P(A)+P(B) ', ' P(A/B) = P(A - B)+P(B)'],
	['The sum of square of the first n natural numbers is given by ', ' n(n+1)(2n+1)/6 ', ' n(n-1)/2(2n+1) ', ' n2(n+1)(2n+1)/6 ', ' None of these'],
	["The sequence '1 ', ' 1', ' 1', ' 1', ' 1' …. is ", ' Not absolutely summable ', ' Absolutely summable ', ' Can’t say ', ' None of These'],
        ["Which of the following is cardinality of the set A = {' 1', ' 2', ' 3', ' 4', ' 6}? ", ' 5 ', ' 9 ', ' 6 ', ' 3'],
        ['A matrix having many rows and one column is known as - ', ' Column matrix  ', ' Row matrix ', ' Diagonal matrix ', ' None of the above'],
        ['Which of the following sentence is a mistake? ', ' You ', ' The earth is round'],
	['Let A order (axb) and Border(cxd) be two matrices,  then if AB exists,  the order of AB is? ', ' axd ', ' bxc ', ' axb ', ' cxd'],
	['If determinant of a matrix A is Zero then ', ' A is a Singular matrix ', ' A is a non Singular matrix ', ' Can’t say ', ' None of These'])


file = open('Math.txt', 'ab')


pickle.dump(ques, file)
file.close()

