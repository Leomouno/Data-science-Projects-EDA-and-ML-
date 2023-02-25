import pandas as pd 
from pandas_profiling import ProfileReport
import numpy


df = pd.read_excel('Questionary-for-thesis-Responses.xlsx')
print(df)



profile = ProfileReport(df,variables=False,Interactions=True, Correlations=False, Missing_values=False, Sample=False)
profile.to_file(output_file="Questionary-for-thesis-Responses.html")


 
# Listing available correlation
correlations = profile.description_set["correlations"]
print(correlations.keys())


pearson_df = correlations["phi_k"]

# Actual correlation values
pearson_mat = pearson_df.values

print(pearson_mat)


pearson_df2 = correlations["cramers"]
pearson_mat2 = pearson_df2.values
print(pearson_mat2)

Array1 = numpy.array(pearson_mat)

 
# Displaying the array
print('Array:\n', Array1)
file = open("Phi_k with trancuation.txt", "w+")
 
# Saving the array in a text file
content = str(Array1)
file.write(content)
file.close()


Array2 = numpy.array(pearson_mat2)
 
# Displaying the array
print('Array:\n', Array2)
file = open("cramer with trancuation.txt", "w+")
 
# Saving the array in a text file
content1 = str(Array2)
file.write(content1)
file.close()
 
