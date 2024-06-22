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

nta = pd.read_csv('nta.csv')
res = pd.read_csv('restaurants30July.csv')

#
a = 'SELECT NTA FROM res'
#Put the selected data in the dr DataFrame
one = psql.sqldf(a)
#print(one)

#
b = 'SELECT COUNT(DISTINCT(NTA)) FROM res'
#Put the selected data in the dr DataFrame
two = psql.sqldf(b)
#print(two)

#
c = 'SELECT NTA,COUNT(DISTINCT(DBA)) FROM res GROUP BY NTA'
#Put the selected data in the dr DataFrame
three = psql.sqldf(c)
#print(three)

#
d = 'SELECT COUNT(NTA),COUNT(DISTINCT(NTA)) FROM nta'
#Put the selected data in the dr DataFrame
four = psql.sqldf(d)
#print(four)

#
#e = 'SELECT NTA FROM res LEFT JOIN "nta" ON res.NTA = nta.NTA;'
e = """
SELECT R.[NTA], NTA_Name
FROM res R
    LEFT JOIN nta N
    ON R.NTA = N.NTA
"""
#Put the selected data in the dr DataFrame
five = psql.sqldf(e)
print(five)

#GROUP BY R.[NTA],DBA    , DISTINCT(DBA), COUNT(DISTINCT(DBA))    DISTINCT(R.[NTA])
f = """
SELECT R.[NTA],[DBA],COUNT(DISTINCT(DBA))
FROM res R
    LEFT JOIN nta N
    ON R.NTA = N.NTA
    GROUP BY R.[NTA],DBA
"""
#Put the selected data in the dr DataFrame
six = psql.sqldf(f)
#print(six)
