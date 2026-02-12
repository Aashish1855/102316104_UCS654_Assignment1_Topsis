import sys
import pandas as pd 
import numpy as np 
import os

def main():
    if(len(sys.argv)!=5):
        print("Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>")
        sys.exit(1)
    input_file=sys.argv[1]
    weights=sys.argv[2]
    impacts=sys.argv[3]
    output_file=sys.argv[4]
    if not os.path.exists(input_file):
        print("Error: file not found")
        sys.exit(1)
    try:
        data=pd.read_excel(input_file)
    except Exception:
        print("Error: Unable to open file")
        sys.exit(1)
    
    if(data.shape[1]<3):
        print("Error: input file must have 3 or more columns")
        sys.exit(1)
    for col in data.columns[1:]:
        if not pd.api.types.is_numeric_dtype(data[col]):
            print("Error: From 2nd to last columns must conatin numeric values only")
            sys.exit(1)
    weights=weights.split(',')
    impacts=impacts.split(',')
    if(len(weights)!=len(impacts) or len(weights)!=(data.shape[1]-1)):
        print("Error: Number weight is not equal to number of impacts")
        sys.exit(1)
    for impact in impacts:
        if impact not in["+","-"]:
            print("Error: Impacts must be '+' or '-'")
            sys.exit(1)
    try:
        weights=np.array(weights,dtype=float)
    except ValueError:
        print("Error: Weights mus be numeric and separted by comma")
        sys.exit(1)
    matrix=data.iloc[:,1:].values.astype(float)
    norm_matrix=matrix/np.sqrt((matrix**2).sum(axis=0))
    weighted_matrix=norm_matrix*weights
    ideal_best=[]
    ideal_worst=[]
    for i in range(len(impacts)):
        if(impacts[i]=="+"):
            ideal_best.append(np.max(weighted_matrix[:,i]))
            ideal_worst.append(np.min(weighted_matrix[:,i]))
        else:
            ideal_best.append(np.min(weighted_matrix[:,i]))
            ideal_worst.append(np.max(weighted_matrix[:,i]))
    ideal_best=np.array(ideal_best)
    ideal_worst=np.array(ideal_worst)
    s_best=np.sqrt(((weighted_matrix-ideal_best)**2).sum(axis=1))
    s_worst=np.sqrt(((weighted_matrix-ideal_worst)**2).sum(axis=1))

    score=s_worst/(s_best+s_worst)
    data['Topsis score']=score
    rank=data['Topsis score'].rank(ascending=False, method='max').astype(int).astype(int)
    data["Rank"]=rank

    data.to_excel(output_file,index=False)

    print("Done")
if __name__=="__main__":
    main()




    


