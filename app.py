from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('dicisiontree.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    

    if request.method == 'POST':
        
        
        Pclass=float(request.form['Pclass'])
        	
        Sex=float(request.form['Sex'])
                	
        Age=float(request.form['Age'])
        SibSp=float(request.form['SibSp'])
        Parch=float(request.form['Parch'])
        Fare=float(request.form['Fare'])

        input_data = (int(Pclass),int(Sex),int(Age),int(SibSp),int(Parch),int(Fare))
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        

        
        
        

        
        
        try:
        
            
            prediction = model.predict(input_data_reshaped)
        #     prediction_val=[intcr1,occ_2,occ_3,occ_4,occ_5,occ_6,occ_husb_2,occ_husb_3,occ_husb_4,occ_husb_5,occ_husb_6,rate_marriage1,age,yrs_married,children,religious1,educ1]    
        
        #     prediction_text=prediction[0]
        #     return render_template('index.html')
            
        #     result=True
        #     if int(prediction[0])==0:
        #         result=False
        #     else:
        #         pass
        

            if int(prediction[0])==0:
                return render_template('index.html',prediction_text="Dead")
            else:
                return render_template('index.html',prediction_text="Alive")
        except Exception as e:
            pass

            
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
