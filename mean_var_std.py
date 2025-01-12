import numpy as np

rows=3
cols=3
matrix_size=rows*cols

def calculate():
#Take input from user
    Data=list(map(int,input(f"Enter {matrix_size} Elements SEPARATED BY SPACE:").split()))
#Validate the size of input
    if len(Data)!=matrix_size:
        print(" List must contain nine numbers: ")
    else:
        matrix=np.array(Data).reshape(rows,cols)
        print(matrix)
    Calculatons={
        'Mean':[matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()],
        'Variance':[matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()],
        'Standard deviation':[matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()],
        'Max':[matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()],
        'Min':[matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()],
        'Sum':[matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
                
    }
    return Calculatons
result=calculate()
print(f"Mean: {result['Mean']}")
print(f"Variance: {result['Variance']}")
print(f"Standard deviation: {result['Standard deviation']}")
print(f"Max: {result['Max']}")
print(f"Min: {result['Min']}")
print(f"Sum: {result['Sum']}")


       
    





