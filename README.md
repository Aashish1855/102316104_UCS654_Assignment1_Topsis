# 102316104_UCS654_Assignment2_Topsis
This project implements the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method as a command-line Python program.


The script takes an input file (Excel/CSV), weights, impacts (+ or -), and an output file name. It first validates the inputs (file existence, numeric columns, correct number of weights and impacts). Then it normalizes the data, applies weights, calculates ideal best and worst values, computes TOPSIS scores, and assigns ranks (higher score = better rank). Finally, it saves the result with score and rank to the output file.


Usage:


python topsis.py data.xlsx 1,1,1,1,1 +,+,+,+,+ result.xlsx
