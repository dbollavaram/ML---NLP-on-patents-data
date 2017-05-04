#merging the final dataset of claims featues with cosine similairty index only 
import pandas as pd
file1 = pd.read_csv('Patent_Part1_similarity.csv')
file2 = pd.read_csv('Patent_Part2_similarity.csv')
file3 = pd.read_csv('UnPatent_similarity.csv')
print(file.head())
print(file.shape)

#dropping all unnecessary columns to decrease the file size 
file1.drop(['Claims','Abstract','Title'],axis = 1, inplace = True)
file2.drop(['Claims','Abstract','Title'],axis = 1, inplace = True)
file3.drop(['Claims','Abstract','Title'],axis = 1, inplace = True)

file_merged = pd.concat([file1,file2,file3],axis = 0)
file_merged.shape
file_merged.to_csv('file_merged_similarity.csv')