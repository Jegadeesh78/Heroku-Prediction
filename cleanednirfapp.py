#import libraries
import numpy as np
from flask import Flask, render_template,request
import pickle


app = Flask(__name__)


model = pickle.load(open('GBRdemo.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    State = ['Tamil Nadu','Delhi','Maharashtra','West Bengal','Uttar Pradesh','Uttarakhand','Telangana','Madhya Pradesh','Odisha','Himachal Pradesh','Bihar','Gujarat','Kerala','Punjab','Rajasthan','Meghalaya','Tripura','Chhattisgarh','Goa','Assam','Nagaland','Sikkim','Arunachal Pradesh','Puducherry']
          
    return render_template("home.html",c=State)

@app.route('/hello', methods=['GET', 'POST'])
def hello(): 
    if request.method == "POST" :
        if request.json["inst_no"]:
            data = request.json["inst_no"]
            print(data)
            d=[]
            #e=[]
            #my_dict3={'Chennai':1,'South West Delhi':2,'Mumbai Suburban':3,'Paschim Bardhaman':4,'Kanpur':5,'Haridwar':6,'Sangareddy':7,'Indore':8,'Khordha':9,'Mandi':10,'Patna':11,'Gandhinagar':12,'Kozhikode':13,'Rupnagar':14,'Jodhpur':15,'Hamirpur':16,'East Khasi Hills':17,'West Tripura':18,'Raipur':19,'South Goa':20,'Kamrup Metropolitan':21,'Dimapur':22,'South Sikkim':23,'Papum Pare':24,'Karaikal':25}
            District = {
                'Tamil Nadu': ['Chennai'],
                'Delhi': ['South West Delhi'],                                                 
                'Maharashtra': ['Mumbai Suburban'],
                'West Bengal': ['Paschim Bardhaman'],
                'Uttar Pradesh': ['Kanpur'],                                                 
                'Uttarakhand': ['Haridwar'],
                'Telangana': ['Sangareddy'],
                'Madhya Pradesh': ['Indore'],                                                 
                'Odisha': ['Khordha'],
                'Himachal Pradesh': ['Mandi'],
                'Bihar': ['Patna'],                                                 
                'Gujarat': ['Gandhinagar'],
                'Kerala': ['Kozhikode'],
                'Punjab': ['Rupnagar'],                                                 
                'Rajasthan': ['Jodhpur'],
                'Meghalaya': ['East Khasi Hills'],
                'Tripura': ['West Tripura'],                                                 
                'Chhattisgarh': ['Raipur'],
                'Goa': ['South Goa'],
                'Assam': ['Kamrup Metropolitan'],                                                 
                'Nagaland': ['Dimapur'],
                'Sikkim': ['South Sikkim'],
                'Arunachal Pradesh': ['Papum Pare'],                                                 
                'Puducherry': ['Karaikal'],
                }
            search = data
            for key, value in District.items(): 
                if key == search:
                    for x in value:
                        d.append(x)
            d = str(d)[1:-1] 
            print(d)
            d=d.replace("'", "") 
            print(d)
            final ='<OPTION value="" disabled selected>SELECT</option>'
            attach ='<option value="{no}">{college}</option>'.format(no=d,college=d)
            final = final+'\n' + attach
            return final
    #return render_template("flaskdemo12.html",final=final)

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    if request.method == "POST":
        dictOfWords = {'Indian Institute of Technology Madras': 1.0, 'Indian Institute of Technology Delhi': 2.0, 'Indian Institute of Technology Bombay': 3.0, 'Indian Institute of Technology Kharagpur': 4.0, 'Indian Institute of Technology Kanpur': 5.0, 'Indian Institute of Technology Roorkee': 6.0, 'Indian Institute of Technology Hyderabad': 7.0, 'Indian Institute of Technology Indore': 8.0, 'Indian Institute of Technology Bhubaneswar': 9.0, 'Indian Institute of Technology Mandi': 10.0, 'Indian Institute of Technology Patna': 11.0, 'Indian Institute of Technology Gandhinagar': 12.0, 'National Institute of Technology Calicut': 13.0, 'Indian Institute of Technology Ropar': 14.0, 'National Institute of Technology Durgapur': 15.0, 'Indian Institute of Technology Jodhpur': 16.0, 'National Institute of Technology Hamirpur': 17.0, 'National Institute of Technology Meghalaya': 18.0, 'National Institute of Technology Agartala': 19.0, 'National Institute of Technology Raipur': 20.0, 'National Institute of Technology Goa': 21.0, 'National Institute of Technology Patna': 22.0, 'Indian Institute of Information Technology Guwahati': 23.0, 'National Institute of Technology Delhi': 24.0, 'National Institute of Technology Nagaland': 25.0, 'National Institute of Technology Sikkim': 26.0, 'National Institute of Technology Arunachal Pradesh': 27.0, 'National Institute of Technology Puducherry': 28.0, 'Indian Institute of Technology Guwahati': 29.0}
        my_dict2={'West Bengal':1,'Himachal Pradesh':2,'Chhattisgarh':3,'Kerala':4,'Delhi':5,'Bihar':6,'Tripura':7,'Maharashtra':8,'Uttarakhand':9,'Tamil Nadu':10,'Uttar Pradesh':11,'Assam':12,'Odisha':13,'Telangana':14,'Goa':15,'Puducherry':16,'Punjab':17,'Rajasthan':18,'Gujarat':19,'Arunachal Pradesh':20,'Meghalaya':21,'Nagaland':22,'Madhya Pradesh':23,'Sikkim':24}
        State = request.form.get("State")
        listOfKeys1 = [value  for (key, value) in my_dict2.items() if key ==State]
        listOfKeys1 = str(listOfKeys1)[1:-1]
        State1=float(listOfKeys1)
        my_dict3={'Chennai':1,'South West Delhi':2,'Mumbai Suburban':3,'Paschim Bardhaman':4,'Kanpur':5,'Haridwar':6,'Sangareddy':7,'Indore':8,'Khordha':9,'Mandi':10,'Patna':11,'Gandhinagar':12,'Kozhikode':13,'Rupnagar':14,'Jodhpur':15,'Hamirpur':16,'East Khasi Hills':17,'West Tripura':18,'Raipur':19,'South Goa':20,'Kamrup Metropolitan':21,'Dimapur':22,'South Sikkim':23,'Papum Pare':24,'Karaikal':25}
        District = request.form.get("District")
        listOfKeys2 = [value  for (key, value) in my_dict3.items() if key ==District]
        listOfKeys2 = str(listOfKeys2)[1:-1]
        District1=float(listOfKeys2)
        Rank = request.form.get("NIRF rank")
        Rank1=float(Rank)
        Area = request.form.get("Campus Area")
        Area1=float(Area)
        BHostels = request.form.get("Boys Hostels")
        BHostels1=float(BHostels)
        GHostels = request.form.get("Girls Hostels")
        GHostels1=float(GHostels)
        studentRatio = request.form.get("Faculty student Ratio")
        studentRatio1=float(studentRatio)
        UGPlacementPercentage = request.form.get("UG Placement Percentage")
        UGPlacementPercentage1=float(UGPlacementPercentage)
        MedianSalaryUG = request.form.get("Median Salary UG")
        MedianSalaryUG1=float(MedianSalaryUG)
        CollGovtPvt = request.form.get("Colleges Govt/Pvt")
        CollGovtPvt1=float(CollGovtPvt)
        JosaaRank = request.form.get("Josaa Rank")
        JosaaRank1=float(JosaaRank)
        UGCourseList = request.form.get("UG Course List")
        UGCourseList1=float(UGCourseList)
        int_features = [State1,District1,Rank1,Area1,BHostels1,GHostels1,studentRatio1,UGPlacementPercentage1,MedianSalaryUG1,CollGovtPvt1,JosaaRank1,UGCourseList1]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        print(prediction)
        output =round( prediction[0],2 )
    #print(output)
        output1 = round(output)
        print(output1)
    #split_num = str(output).split('.')
    #int_part = int(split_num[0])
   # print(int_part)
        listOfKeys = [key  for (key, value) in dictOfWords.items() if value ==output1]
        listOfKeys = str(listOfKeys)[1:-1]
        listOfKeys = listOfKeys.strip("''")
        print(listOfKeys)
    return render_template('home.html', prediction_text='predicted colleges is : {}'.format(listOfKeys))


if __name__ == "__main__":
    app.run(debug=True)
    