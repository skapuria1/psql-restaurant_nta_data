"""
Name: Sammyajit Kapuria
Email: sammyajit.kapuria87@myhunter.cuny.edu
09/20/2021

Resources: Used the example provided in the coursework as a reference to solve this problem,
along with the provided psql resources (https://pypi.org/project/pandasql/) and DS 100: Section 5.2 in the homework page. Also used
pandas.pydata.org as a reference as suggested by the TAs.
pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/03_subset_data.html
https://pypi.org/project/pandasql/
http://www.textbook.ds100.org/ch/05/sql_basics.html
Assignment 11
"""

import pandas as pd
import pandasql as psql

#Get input and output file names:

inFile1 = input('Enter input file name 1: ')
inFile2 = input('Enter input file name 2: ')
outFile = input('Enter output file name: ')


res = pd.read_csv(inFile1)
nta = pd.read_csv(inFile2)

'''
nta = pd.read_csv('nta.csv')
res = pd.read_csv('restaurants30July.csv')
'''

#Save the NTA column from the restaurant inspection table to the output file prefix+"1.csv"
a = 'SELECT NTA FROM res'
#Put the selected data in the DataFrame
one = psql.sqldf(a)
#print(one)
#Write the new dataframe to CSV:
one.to_csv(outFile + "1.csv",index=0)

#Save the count of unique NTAs in the restaurant health inspection table to the output file prefix+"2.csv"
b = 'SELECT count(distinct NTA) FROM res'
#Put the selected data in the DataFrame
two = psql.sqldf(b)
#print(two)
#Write the new dataframe to CSV:
two.to_csv(outFile + "2.csv",index=0)

#Save the NTA column and the count of the distinct restaurants from the restaurant inspection table to the output file prefix+"3.csv"
c = 'SELECT NTA,COUNT(DISTINCT(DBA)) AS "cnt_restaurants" FROM res GROUP BY NTA'
#Put the selected data in the DataFrame
three = psql.sqldf(c)
#print(three)
#Write the new dataframe to CSV:
three.to_csv(outFile + "3.csv",index=0)


#Save the number of rows in the NTA table and the number of unique NTAs in the NTA table to the output file prefix+"4.csv"
d = 'SELECT COUNT(NTA) AS "num_rows",COUNT(DISTINCT(NTA)) AS "num_ntas" FROM nta'
#Put the selected data in the DataFrame
four = psql.sqldf(d)
#print(four)
#Write the new dataframe to CSV:
four.to_csv(outFile + "4.csv",index=0)

#Save the restaurant name and its NTA which can be found via a LEFT JOIN of the restaurant inspection table and NTA table. Save the results to the output file prefix+"5.csv"
e = """
SELECT R.[NTA], NTA_Name
FROM res R
    LEFT JOIN nta N
    ON R.NTA = N.NTA
"""
#Put the selected data in the DataFrame
five = psql.sqldf(e)
#print(five)
#Write the new dataframe to CSV:
five.to_csv(outFile + "5.csv",index=0)


#Building on the result from 5) above, keep the LEFT JOIN as is, do one more level of aggregation, so that the end result contains 3 columns (unique NTA code, unique NTA description, and the count distinct restaurants as grouped by the first 2 columns). Save result to the output file prefix+"6.csv"
f = """
SELECT R.[NTA],[DBA] AS "NTA_Name",COUNT(DISTINCT(DBA)) AS num_restaurants
FROM res R
    LEFT JOIN nta N
    ON R.NTA = N.NTA
    GROUP BY R.[NTA],DBA
"""
#Put the selected data in the DataFrame
six = psql.sqldf(f)
#print(six)
#Write the new dataframe to CSV:
six.to_csv(outFile + "6.csv",index=0)
