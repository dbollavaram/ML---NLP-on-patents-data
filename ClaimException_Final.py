"""This code is to extract the following features from claims text data 
	1. Total number of claims 
	2. Number of dependent claims 
	3. Number of independent claims
	4. Length of first independent claim"""

"""
An example of claim will be as follows: 
1. A method of analyzing a claim in a patent or patent application, comprising:
		a. retrieving a patent claim which has been rendered into a format parsable by a computer program into a computer memory;
		b. parsing the claim into a set of discrete elements;
		c. categorizing each element in the set of elements according to a predetermined rule; and
		d. storing a set of categorized elements in a data store.
2. The method of claim 1, wherein:
		a. parsing further comprises at least one of (i) semantic indexing, (ii) latent semantic indexing, (iii) rules based parsing, or (iv) free form parsing.
3. The method of claim 1, wherein parsing further comprises:
		a. identifying each keyword set in each element, the keyword set comprising at least one of (i) a noun, (ii) an adjective and a noun, (iii) a verb, or (iv) an adverb and a verb.
4. The method of claim 1, claim 2 wherein:
		a. each keyword set further comprises a modifier to categorize the keyword set, the modifier comprising at least one of (i) a modifier identifying the keyword set as a necessary keyword set or (ii) a modifier identifying the keyword set as a non-necessary keyword set.
5. The method of claim 1, claim 2, claim 3, wherein:
		a. the stored set of categorized elements is stored an interrogatable database.
"""
"""  For the above example, the code will extract the following features:
	1. Total number of claims as 5
	2. Number of dependent claims as 4 (since claims 2, 3, 4, 5 reference other claims within them)
	3. Number of independent claims as 1 (since claim 1 does not reference any other claim)
	4. Length of first claim 
"""

#the above claim is present in following format in the files 
"""1. A method of analyzing a claim in a patent or patent application, comprising:a. retrieving a patent claim which has been rendered into a format parsable by a computer program into a computer memory;b. parsing the claim into a set of discrete elements; 
c. categorizing each element in the set of elements according to a predetermined rule; and d. storing a set of categorized elements in a data store. 2. The method of claim 1, wherein:a. parsing further comprises at least one of (i) semantic indexing, (ii) latent semantic indexing, 
(iii) rules based parsing, or (iv) free form parsing. 3. The method of claim 1, wherein parsing further comprises:a. identifying each keyword set in each element, the keyword set 
comprising at least one of (i) a noun, (ii) an adjective and a noun, (iii) a verb, or (iv) an adverb and a verb. 4. The method of claim 1, claim 2 wherein:a. each keyword set further comprises a modifier to categorize the keyword set, the modifier comprising at least one of (i) a modifier identifying the keyword set as a necessary keyword 
set or (ii) a modifier identifying the keyword set as a non-necessary keyword set. 5. The method of claim 1, claim 2, claim 3, wherein:a. the stored set of categorized elements is stored an interrogatable database.
"""

#The above format is just one of the multiple formats present in the file. 
#The code below is written to handle all such formats and also deal with exceptions i the file.

########## Claim exception data - Final code ##################################
import pandas as pd
import re
import timeit
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
start_time = timeit.default_timer()

#reading files 
file = pd.read_csv('C:/Users/saketha lakshmi/Documents/Capstone/Deepika/Data/file_pub1_claims_new_v2.csv')
print file.head()
#renaming the columns 
file.columns = [0,1,2,3,4,5,'Title','Claims', 'Abstract', 'total_claims', 'dependent_claims','total_length_firstclaim','nostop_length_firstclaim'] 
#print file.head()

"""function: find_between 
	Extracts the text of first claim 
	Paramaters:
		s : Entire claim
		first: the first index 
		last: the last index 
	Returns:
		The code returns the text present between the first and last index 
"""
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
		
"""function: find_between 
	Extracts the text of first claim 
	Paramaters:
		s : Entire claim
		first: the first index 
		last: the last index 
	Returns:
		The code returns the text present between the first and last index 
"""

def find_between_idx( s, first, last ):
    try:
        start = first
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

#This loop will run over all rows in dataset 
for i in range(0,100000):
	#checking if claims have 'cancelled word' in them
    s = re.findall(r'cancel|Cancel|CANCEL|Cancelled', file.loc[i,'Claims'], re.IGNORECASE)
    if len(s) >0:
################################################### For Claims having 'Cancelled' word ###########################################################3
################### regex pattern finder to find total  number of claims ###############################
        p = re.findall(r' [0-9]+[0-9]*[0-9]*[0-9]*\. [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\: [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\- [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\) [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\)\- [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\)\. [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\. &| [0-9]+[0-9]*[0-9]*[0-9]*\.\- [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\/ [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\.\) &| [0-9]+[0-9]*[0-9]*[0-9]*\- &| [0-9]+[0-9]*[0-9]*[0-9]*\.\) &| [0-9]+[0-9]*[0-9]*[0-9]*\.\) [A-Za-z]',file.loc[i,'Claims'])
        p1 = re.findall(r' [0-9]+[0-9]*[0-9]*[0-9]*\. [A-Za-z]', file.loc[i,'Claims'])
        q = re.findall(r'[0-9]+[0-9]*[0-9]*[0-9]*\. [A-Za-z]|[0-9]+[0-9]*[0-9]*[0-9]*\: [A-Za-z]|[0-9]+[0-9]*[0-9]*[0-9]*\- [A-Za-z]|[0-9]+[0-9]*[0-9]*[0-9]*\) [A-Za-z]|[0-9]+[0-9]*[0-9]*[0-9]*\)\- [A-Za-z]|[0-9]+[0-9]*[0-9]*[0-9]*\)\. [A-Za-z]|[0-9]+[0-9]*[0-9]*[0-9]*\. &|[0-9]+[0-9]*[0-9]*[0-9]*\.\- [A-Za-z]|[0-9]+[0-9]*[0-9]*[0-9]*\/ [A-Za-z]|[0-9]+[0-9]*[0-9]*[0-9]*\.\) &|[0-9]+[0-9]*[0-9]*[0-9]*\- &|[0-9]+[0-9]*[0-9]*[0-9]*\.\) &|[0-9]+[0-9]*[0-9]*[0-9]*\.\) [A-Za-z]',file.loc[i,'Claims'])
        if len(p) and len(q) != 0:
            if p[0][1:] == q[0] | p[0] == q[0]:
                file.loc[i,'total_claims'] = len(p)
            else:
                file.loc[i,'total_claims'] = len(p) + 1
                print(i)
    ################### regex pattern finder to count the total number of dependent Claims ##################               
            file.loc[i,'dependent_claims'] = len(re.findall(r'(?: [0-9]+[0-9]*[0-9]*\. )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\: )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\- )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\) )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\)\- )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\)\. )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\. )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\)\.- )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\/ )(.*?)[Cc]laim',file.loc[i, 'Claims']))
        else:
            file.loc[i,'dependent_claims'] = 0
            file.loc[i,'total_claims'] = 1
   	
   	                    
    ########################## First Claim Length ####################
    #file.loc[i,'total_length_firstclaim'] = find_between( file.loc[i,'Claims'], p[0][:-2], p[1][:-2])      
        #uf only one claim is present 
		if len(p) == 0:
            length = 0
			#The claims are first converted to lowercase and punctuations are removed. The words which are of length > 2 are only considered 
            for j in re.sub("([^a-zA-Z])"," ",file.loc[i,'Claims']).lower().split():
                if len(j) > 2:
                    length = length + 1 
            file.loc[i,'total_length_firstclaim'] = length
            length = 0
			#the length of the claim without stop words is calculated 
            for j in re.sub("([^a-zA-Z])"," ",file.loc[i,'Claims']).lower().split():
                if len(j) > 2 and j not in stop:
                   length = length + 1 
            file.loc[i,'nostop_length_firstclaim'] = length
                
        else: #if more than one claim is present 
			#dealing with exceptions present in file 
            if p[0][1:] == q[0] | p[0] == q[0]:
                if len(p) == 1:
                    file.loc[i,'total_length_firstclaim'] = 'check'
                    file.loc[i,'nostop_length_firstclaim'] = 'check'
                else:
					#extracting first claim and dealing with exceptions
                    s= find_between( file.loc[i,'Claims'], p[0][:-2], p[1][:-2])
                    if len(s) == 0:
                       file.loc[i,'total_length_firstclaim'] = 'check'
                       file.loc[i,'nostop_length_firstclaim'] = 'check'
                    else:
                       length = 0 
                       for j in re.sub("([^a-zA-Z])"," ",s).lower().split(): #removes punctuations and symbols present in claim text 
                           if len(j) > 2:
                              length = length + 1 
                       file.loc[i,'total_length_firstclaim'] = length
                       length = 0
                       for j in re.sub("([^a-zA-Z])"," ",s).lower().split(): #removes stop words present 
                           if len(j) > 2 and j not in stop:
                              length = length + 1 
                       file.loc[i,'nostop_length_firstclaim'] = length
            else:
				#extracting the first claim and dealing with exceptions in file 
                 s = find_between( file.loc[i,'Claims'], q[0][:-2], q[1][:-2])
                 if len(s) == 0:
                    file.loc[i,'total_length_firstclaim'] = 'check'
                    file.loc[i,'nostop_length_firstclaim'] = 'check'
                 else:
                      length = 0
                      for j in re.sub("([^a-zA-Z])"," ",s).lower().split(): #removes punctuations and symbols present in claim text 
                          if len(j) > 2:
                             length = length + 1 
                      file.loc[i,'total_length_firstclaim'] = length
                      length = 0
                      for j in re.sub("([^a-zA-Z])"," ",s).lower().split(): #removes stop words present  
                          if len(j) > 2 and j not in stop:
                             length = length + 1 
                      file.loc[i,'nostop_length_firstclaim'] = length
                    
######################################################### Patents which donot have 'Cancelled' word within them ##################################################
    else:
		#extracts the total number of claims present 
         p = re.findall(r' [0-9]+[0-9]*[0-9]*[0-9]*\. [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\: [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\- [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\) [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\)\- [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\)\. [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\. &| [0-9]+[0-9]*[0-9]*[0-9]*\.\- [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\/ [A-Za-z]| [0-9]+[0-9]*[0-9]*[0-9]*\.\) &| [0-9]+[0-9]*[0-9]*[0-9]*\- &| [0-9]+[0-9]*[0-9]*[0-9]*\.\) &| [0-9]+[0-9]*[0-9]*[0-9]*\.\) [A-Za-z]',file.loc[i,'Claims'])
 
        #q = re.findall(r'[0-9]+[0-9]*[0-9]*[0-9]*\. [A-Za-z]|[0-9]+[0-9]*[0-9]*[0-9]*\: [A-Za-z]|[0-9]+[0-9]*[0-9]*[0-9]*\- [A-Za-z]|[0-9]+[0-9]*[0-9]*[0-9]*\) [A-Za-z]|[0-9]+[0-9]*[0-9]*[0-9]*\)\- [A-Za-z]|[0-9]+[0-9]*[0-9]*[0-9]*\)\. [A-Za-z]|[0-9]+[0-9]*[0-9]*[0-9]*\. &|[0-9]+[0-9]*[0-9]*[0-9]*\.\- [A-Za-z]|[0-9]+[0-9]*[0-9]*[0-9]*\/ [A-Za-z]',file.loc[i,'Claims'])
         if len(p) != 0:
            file.loc[i,'total_claims'] = len(p)+1
            print(i)
    ################### Dependent Claims ##################               
            #finds the total number of dependent claims 
			file.loc[i,'dependent_claims'] = len(re.findall(r'(?: [0-9]+[0-9]*[0-9]*\. )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\: )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\- )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\) )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\)\- )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\)\. )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\. )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\)\.- )(.*?)[Cc]laim|(?: [0-9]+[0-9]*[0-9]*\/ )(.*?)[Cc]laim',file.loc[i, 'Claims']))
         else:
            file.loc[i,'total_claims'] = 1
            file.loc[i,'dependent_claims'] = 0        
    ########################## First Claim Length ####################
    #file.loc[i,'total_length_firstclaim'] = find_between( file.loc[i,'Claims'], p[0][:-2], p[1][:-2])      
         #if only one claim is present 
		 if len(p) == 0:
            length = 0
            for j in re.sub("([^a-zA-Z])"," ",file.loc[i,'Claims']).lower().split(): #removes punctuations and converts uppercase to lowercase 
                if len(j) > 2:
                    length = length + 1 
            file.loc[i,'total_length_firstclaim'] = length
            length = 0
            for j in re.sub("([^a-zA-Z])"," ",file.loc[i,'Claims']).lower().split(): #removes stop words present 
                if len(j) > 2 and j not in stop:
                    length = length + 1 
            file.loc[i,'nostop_length_firstclaim'] = length
                
         else: #if more than one claim is present 
             s= find_between_idx( file.loc[i,'Claims'], 0, p[0][:-2]) #dealing with exceptions in file 
             if len(s) == 0:
                file.loc[i,'total_length_firstclaim'] = 'check'
                file.loc[i,'nostop_length_firstclaim'] = 'check'
             else:
                  length = 0
                  for j in re.sub("([^a-zA-Z])"," ",s).lower().split(): #removes punctuations and converts uppercase to lowercase 
                      if len(j) > 2:
                         length = length + 1 
                  file.loc[i,'total_length_firstclaim'] = length
                  length = 0
                  for j in re.sub("([^a-zA-Z])"," ",s).lower().split():  #removes stop words present  
                      if len(j) > 2 and j not in stop:
                         length = length + 1 
                  file.loc[i,'nostop_length_firstclaim'] = length

file.to_csv("C:/Users/saketha lakshmi/Documents/Capstone/Deepika/Output/op10_Al1.csv")

  
#sorting the file based on total number of claims    
file1 = file.sort(columns= 'total_claims', ascending = True)                  
len(file1[file.total_claims <= 1])               

############## To separate out total claims 1 or more ####################
file1 = file[file.total_claims <= 1]
file1.to_csv("C:/Users/deeps/Documents/Capstone/Output/op2_claim1.csv")
file2 = file[file.total_claims > 1]
file.to_csv("C:/Users/deeps/Documents/Capstone/Output/op2_claims_rest.csv")      


                
            
          
 
        


