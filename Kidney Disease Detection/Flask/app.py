from flask import flask,render_template,request
import numpy as np
import pickle

app = Flask(_name_) # initializing a falsk app
model = pickle.load(open('CKD.pkl''rb'))#loading the model



@app.route('/')#route to disply the home page
def home():
     return render_template('home.html')#rendering the home page

@app.route('/prediction',methods=['POST','GET'])
def prediction():
   return render_template('indexnew.html')
@app.route('/Home',methods=['POST','GET'])
def my_Home():
      return render_template('Home.html')
@app.route('/predict',methods=['POST'])
def predict():
     input_features = [float(x) for x in request.formm.values()]
     features_values = [np.array(input_features)]
features_name = ['blood_urea','bloo glucose random','anemia',
   'coronary_artery_disease','pus_cell','red_blood_cells', 
    'diabetesmellitus','pedal_edema']
df = pd.dataframe(features_values, columns=features_name)
output=model.predict(df)
      return render_template('result.html',prediction_text=output)

if_name_ =='_main_'
#running the app
app.run(debug=true)


