# Basic relations

# You are given two sets.
# Set A = {1,2,3,4,5,6}
# Set B = {2,3,4,5,6,7,8}

# How many elements are present A U B?
# Only enter the correct integer in the editor below. Do not include any extra spaces, tabs or newlines.

# Answer is 8

###########################################################################################################

# You are given two sets.
# Set A = {1,2,3,4,5,6}
# Set B = {2,3,4,5,6,7,8}

# How many elements are present A intersección B ?
# Only enter the correct integer in the answering box. Do not include any extra spaces, tabs or newlines.

#  Answer is 5

###########################################################################################################

# You are given two sets.
# Set A = {1,2,3,4,5,6}
# Set B = {2,3,4,5,6,7,8}

# How many elements are present in A - B?
# Only enter the correct integer in the answering box. Do not include any extra spaces, tabs or newlines.

#  Answer is 1

###########################################################################################################

# You are given two sets.
# Set A = {1,2,3,4,5,6}
# Set B = {2,3,4,5,6,7,8}

# What is the total number of ordered pairs present in the Cartesian Product A x B ? Only enter the correct integer in the answering box. Do not include any extra spaces, tabs or newlines.

# Answer is A x B = 6 * 7 = 42

###########################################################################################################

# Consider the following data table named Student.
# Student Name    Number  Sex  
# Ben             3412    M  
# Dan             1234    M  
# Nel             2341    F  
# What is the count of rows returned in the following relational selection? Number < 3000

# Answer is 2

###########################################################################################################

# Consider the following data table named Student.

# Name                Number  Sex  
# Nina                3412    F 
# Mike                1234    M  
# Nelson              2341    F  
# What is the count of attributes (columns) returned in the following projection? (name, number)Estudent

# Answer is 2

###########################################################################################################

# Consider the following data table named Student.

# Student Name        Number  Sex  
# Nina                3412    F 
# Mike                1234    M  
# Nelson              2341    F  
# Here is another data table named Teaching Assistants

# Subject     ID
# Physics     3412
# Chemistry   1111
# Mathematics 2341  
# What is the count of rows returned in the following join operation?
# Student ⊳⊲(Number=ID) Teaching Assistants

#  Answer is 2

###########################################################################################################

# Which is a join condition contains an equality operator?

# Answer is Equijoins (uniones equitativas)

###########################################################################################################

# In precedence of set operators the expression is evaluated from:

# Answer is Left to right

###########################################################################################################

# Using which language can a user request information from a database ?

# Answer is Query

###########################################################################################################

# Which one of the following is a procedural language ?

# Answer is Relational Algebra

###########################################################################################################

# The_____ operation allows the combining of two relations by merging pairs of tuples, one from each relation, into a single tuple.

# Answer is Join

###########################################################################################################

# The result which operation contains all pairs of tuples from the two relations, regardless of whether their attribute values match.

# Answer is Cartesian product

###########################################################################################################

# How many index architecture type classifications are there in MS SQL Server?

# Answer is 2: Clustered Index and Non-Clustered Index.

###########################################################################################################

# Which of the following statement is true about row locators in non-clustered indexes in MS SQL Server?

# Answer is: If the table has a clustered index, or the index is on an indexed view, the row locator is the clustered index key for the row.

###########################################################################################################

# Consider the following two designs to store the data using clustered indexes in MS SQL Server:
# In the first design, the fill factor is 20% and the total number of free rows per page are A.

# In the second design, the fill factor is 40% and the total number of free rows per page are B.

# Which the followings describes the relation between A and B:

# if total number rows in design of A = total number rows in design of B,
# A = 0.8x AND B = 0.6x
# then
# x = A/0.8 = B/0.6
# A = (B / 0.6)*0.8
# A = (0.8 / 0.6)* B
# A = 1.33B

# Answer is: A = 1.33B

###########################################################################################################

# The correct syntax for creating composite indexes in MS SQL Sever is:

# CREATE INDEX index_name
# ON table_name(column1, column2);

###########################################################################################################

# The following unnormalized table named PRODUCT is transformed to first normal form (1NF) by splitting it into two tables which have X and Y rows (such that X <Y) respectively. Both the tables have Z columns.

# *Product-ID*    *Colors*    *Price*
# 1               Red,Green   15.0
# 2               Blue        18.0
# 3               Yellow,Pink 2.5
# What are the values of X, Y, Z? Enter these integers, each on a new line, in the text-box below. Do not leave any leading or trailing spaces.

# Answer is: 3 5 2

###########################################################################################################

# A particular database is normalized to satisfy a particular level of normalization (either 1NF or 2NF or 3NF). One of the tables contains, among other fields, a column for the City and a column for the Zip Code. Assuming that there is a many-to-one mapping between the set of Zip Code(s) and City, we may conclude that the database is definitely NOT in xNF form. What is the integer x (1, 2, or 3)? Fill your answer in the text box below.

# Answer is: 3

