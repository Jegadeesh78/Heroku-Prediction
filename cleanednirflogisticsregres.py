import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import pickle


data = pd.read_csv("cleanednirfdata.csv",encoding='latin1')
print(data.head(2))

#Nirf Rank for conditions applying:
m=[]
for x in data['NIRF rank']:
  if x==0:
    a=0
    m.append(a)
  if x >=1 and x <=30:
    v = 1
    m.append(v)
  elif x >=31 and x <=60:
    s=2
    m.append(s)   
  elif x>=61 and x<=90:
    d=3
    m.append(d)
  elif x>=91 and x<=120:
    f=4
    m.append(f)
  elif x>=121 and x<=150:
    g=5
    m.append(g)
    
data['NIRF rank1'] = m
#print(data['NIRF rank1'])    
    
#Campus area for conditions applying:
D=[]
for x in data['Campus Area']:
  if x >=0 and x <=500:
    v = 1
    D.append(v)
  elif x >=501 and x <=1000:
    s=2
    D.append(s)   
  elif x>=1001 and x<=1500:
    d=3
    D.append(d)
  elif x>=1501 and x<=2000:
    f=4
    D.append(f)
  elif x>=2001 and x<=2500:
    g=5
    D.append(g)
    
data['Campus Area1'] = D
#print(data['Campus Area1'])    

#BOys hostels for conditions applying:
A=[]
for x in data['No.of Boys Hostels']:
  if x >=0 and x <=5:
    v = 1
    A.append(v)
  elif x >=6 and x <=10:
    s=2
    A.append(s)   
  elif x>=11 and x<=15:
    d=3
    A.append(d)
  elif x>=16 and x<=20:
    f=4
    A.append(f)
    
data['No.of Boys Hostels1'] = A
#print(data['No.of Boys Hostels1'])   

#Girls hostels for conditions applying:
W=[]
for x in data['No. of Girls Hostels']:
  if x >=0 and x <=5:
    v = 1
    W.append(v)
  elif x >=6 and x <=10:
    s=2
    W.append(s)   
  elif x>=11 and x<=15:
    d=3
    W.append(d)
  elif x>=16 and x<=20:
    f=4
    W.append(f)  
data['No. of Girls Hostels1'] = W
#print(data['No. of Girls Hostels1'])   

#Faculty student Ratio for conditions applying:
R=[]
for x in data['Faculty Information_Faculty student Ratio']:
  if x >=0 and x <=701:
    v = 1
    R.append(v)
  elif x >=702 and x <=1101:
    s=2
    R.append(s)   
  elif x>=1102 and x<=1501:
    d=3
    R.append(d)
  elif x>=1502 and x<=2001:
    f=4
    R.append(f)  
data['Faculty Information_Faculty student Ratio1'] = R
#print(data['Faculty Information_Faculty student Ratio1'])   

#UG Placement Info_Placement Percentage for conditions applying:
Q=[]
for x in data['UG Placement Info_Placement Percentage']:
  if  x >=0 and x <=50:
    v = 1
    Q.append(v)
  elif x>=50.1 and x<=70.9:
    s=2
    Q.append(s)   
  elif x>=71.1 and x<=85.9:
    d=3
    Q.append(d)
  elif x>=86.1 and x<=100:
    f=4
    Q.append(f)
        
data['UG Placement Info_Placement Percentage1'] = Q
#print(data['UG Placement Info_Placement Percentage1'])  

#Median Salary_UG for conditions applying:
L=[]
for x in data['Median Salary_UG']:
  if  x >=100000 and x <=400000:
    v = 1
    L.append(v)
  elif x>=400001 and x<=800000:
    s=2
    L.append(s)   
  elif x>=800001 and x<=1200000:
    d=3
    L.append(d)
  elif x>=1200001 and x<=1600000:
    f=4
    L.append(f)
  elif x>=1600001 and x<=2000000:
    K=5
    L.append(K)      
data['Median Salary_UG1'] = L
#print(data['Median Salary_UG1'])  

#23 columns:
df=data[['NIRF rank1','State_values','District_values','Campus Area1','No.of Boys Hostels1','No. of Girls Hostels1','Faculty Information_Faculty student Ratio1','UG Placement Info_Placement Percentage1','Median Salary_UG1','Govt/Pvt_values','Closing Rank','UG Course List_values','Collegename_values']]
print("shape of data",df.shape)
 
#slicing the index value to train & test
X= df.iloc[:,0:12]
y= df.loc[:,['Collegename_values']]
 
#shape of X & y
print(X.shape)
print(y.shape)
 
#Split the train & test data   
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 30)      
 
#x_train & X_test to fit in PCA components
pca = PCA()
X_train = pca.fit_transform(X_train)
X_test =  pca.fit_transform(X_test)
#X = pca.fit_transform(X)
 
 
classifier = GradientBoostingRegressor()
classifier.fit(X_train, y_train)
#classifier.fit(X, y)
  
print('Accuracy',classifier.score(X_train, y_train))
print('Accuracy',classifier.score(X_test,y_test))
#print('Accuracy',classifier.score(X,y))
 
y_pred = classifier.predict(X_test)  
#y_pred = classifier.predict(X)  

print(y_pred)
print(y_test)
# load model into pickle file
#Model = pickle.dumps(classifier)
pickle.dump(classifier, open('GBRdemo.pkl','wb'))





