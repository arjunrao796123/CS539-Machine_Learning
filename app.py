#Importing the required packages
from flask import Flask, render_template, request

import pandas as pd



import numpy as np

import warnings
warnings.filterwarnings('ignore')
from sklearn.linear_model import LogisticRegression


app = Flask(__name__)

#Routing to initial home page
@app.route('/')
def home():
    return render_template('home.html')
#Routing to page when Attribute Entry is selected
@app.route('/attribute_entry')
def attribute_entry():
    return render_template('attribute_entry.html')

#Obtaining values from attribute entry and processing them
@app.route('/yes', methods=['GET', 'POST'])
def yes():
    #Obtaining the values from HTML form
    
    ftp=request.form['FULL_TIME_POSITION']
    pwl=request.form['PW_WAGE_LEVEL']
    pws=request.form['PW_SOURCE']
    agc=request.form['AGENT_ATTORNEY_CITY_BIN']
    empn=request.form['EMPLOYER_NAME_BIN']
    emps=request.form['EMPLOYER_STATE_BIN']
    soc=request.form['SOC_REVISED_CODE']
    #print(h1bd,'\n',ftp,'\n',vd,'\n',pwl,'\n',pws,'\n',wup,'\n',amdp,'\n',newe,'\n',cpe,'\n',
          #are,'\n',ags,'\n',agc,'\n',empn,'\n',emps,'\n',empc,'\n',wss,'\n',wsc,'\n',soc,'\n',naics)
          
    
    #Initializing the one hot encoded columns to 0
    ftp_Y=0
    ftp_N=0
    
    empn_Bin1  = 0
    empn_Bin2  = 0
    empn_Bin3  = 0
    empn_Bin4  = 0
    empn_Bin5  = 0
    empn_Others  = 0
    
    
    agc_Bin1  = 0
    agc_Bin2  = 0
    agc_Bin3  = 0
    agc_Bin4  = 0
    agc_Bin5  = 0
    agc_None  = 0
    agc_Others  = 0
    pwl_LevelI  = 0
    pwl_LevelII  = 0
    pwl_LevelIII  = 0
    pwl_LevelIV  = 0
    soc_10  = 0
    soc_11  = 0
    soc_12  = 0
    soc_13  = 0
    soc_15  = 0
    soc_16  = 0
    soc_17  = 0
    soc_18  = 0
    soc_19  = 0
    soc_20  = 0
    soc_21  = 0
    soc_22  = 0
    soc_23  = 0
    soc_24  = 0
    soc_25  = 0
    soc_26  = 0
    soc_27  = 0
    soc_29  = 0
    soc_31  = 0
    soc_33  = 0
    soc_35  = 0
    soc_36  = 0
    soc_37  = 0
    soc_38  = 0
    soc_39  = 0
    soc_40  = 0
    soc_41  = 0
    soc_43  = 0
    soc_45  = 0
    soc_46  = 0
    soc_47  = 0
    soc_49  = 0
    soc_51  = 0
    soc_53  = 0
    soc_71  = 0
    soc_73  = 0
    soc_74  = 0
    soc_11  = 0
    soc_13  = 0
    soc_15  = 0
    soc_16  = 0
    soc_17  = 0
    soc_18  = 0
    soc_19  = 0
    soc_20  = 0
    soc_21  = 0
    soc_23  = 0
    soc_25  = 0
    soc_27  = 0
    soc_28  = 0
    soc_29  = 0
    soc_31  = 0
    soc_33  = 0
    soc_35  = 0
    soc_36  = 0
    soc_37  = 0
    soc_39  = 0
    soc_40  = 0
    soc_41  = 0
    soc_43  = 0
    soc_45  = 0
    soc_47  = 0
    soc_49  = 0
    soc_50  = 0
    soc_51  = 0
    soc_53  = 0
    soc_71  = 0
    soc_73  = 0
    soc_75  = 0
    soc_79  = 0
    soc_AC  = 0
    soc_AI  = 0
    soc_CO  = 0
    soc_EL  = 0
    soc_SO  = 0
    pws_CBA  = 0
    pws_DBA  = 0
    pws_OES  = 0
    pws_Other  = 0
    pws_SCA  = 0
    
    emps_Bin1  = 0
    emps_Bin2  = 0
    emps_Bin3  = 0
    emps_Bin4  = 0
    emps_Bin5  = 0
    emps_Bin6  = 0
    emps_Bin7  = 0
    emps_Others  = 0

    
    #Setting the value obtained from form to 1
    if ftp=='Y':
        ftp_Y=1
    if ftp=='N':
        ftp_N=1
    
    
    if empn =="Bin1":
        empn_Bin1=1
    if empn =="Bin2":
        empn_Bin2=1
    if empn =="Bin3":
        empn_Bin3=1
    if empn =="Bin4":
        empn_Bin4=1
    if empn =="Bin5":
        empn_Bin5=1
    if empn =="Others":
        empn_Others=1
    if agc =="Bin1":
        agc_Bin1=1
    if agc =="Bin2":
        agc_Bin2=1
    if agc =="Bin3":
        agc_Bin3=1
    if agc =="Bin4":
        agc_Bin4=1
    if agc =="Bin5":
        agc_Bin5=1
    if agc =="Others":
        agc_Others=1
    if agc =="None":
        agc_None=1
    
    if pwl =="Level I":
        pwl_LevelI =1
    if pwl =="Level II":
        pwl_LevelII =1
    if pwl =="Level III":
        pwl_LevelIII =1
    if pwl =="Level IV":
        pwl_LevelIV =1
        
    if soc == '10':
        soc_10 = 1
    if soc == '11':
        soc_11 = 1
    if soc == '12':
        soc_12 = 1
    if soc == '13':
        soc_13 = 1
    if soc == '14':
        soc_14 = 1
    if soc == '15':
        soc_15 = 1
    if soc == '16':
        soc_16 = 1
    if soc == '17':
        soc_17 = 1
    if soc == '18':
        soc_18 = 1
    if soc == '19':
        soc_19 = 1
    if soc == '20':
        soc_20 = 1
    if soc == '21':
        soc_21 = 1
    if soc == '22':
        soc_22 = 1
    if soc == '23':
        soc_23 = 1
    if soc == '24':
        soc_24 = 1
    if soc == '25':
        soc_25 = 1
    if soc == '26':
        soc_26 = 1
    if soc == '27':
        soc_27 = 1
    if soc == '28':
        soc_28 = 1
    if soc == '29':
        soc_29 = 1
    if soc == '30':
        soc_30 = 1
    if soc == '31':
        soc_31 = 1
    if soc == '32':
        soc_32 = 1
    if soc == '33':
        soc_33 = 1
    if soc == '34':
        soc_34 = 1
    if soc == '35':
        soc_35 = 1
    if soc == '36':
        soc_36 = 1
    if soc == '37':
        soc_37 = 1
    if soc == '38':
        soc_38 = 1
    if soc == '39':
        soc_39 = 1
    if soc == '40':
        soc_40 = 1
    if soc == '41':
        soc_41 = 1
    if soc == '42':
        soc_42 = 1
    if soc == '43':
        soc_43 = 1
    if soc == '44':
        soc_44 = 1
    if soc == '45':
        soc_45 = 1
    if soc == '46':
        soc_46 = 1
    if soc == '47':
        soc_47 = 1
    if soc == '48':
        soc_48 = 1
    if soc == '49':
        soc_49 = 1
    if soc == '50':
        soc_50 = 1
    if soc == '51':
        soc_51 = 1
    if soc == '52':
        soc_52 = 1
    if soc == '53':
        soc_53 = 1
    if soc == '54':
        soc_54 = 1
    if soc == '55':
        soc_55 = 1
    if soc == '56':
        soc_56 = 1
    if soc == '57':
        soc_57 = 1
    if soc == '58':
        soc_58 = 1
    if soc == '59':
        soc_59 = 1
    if soc == '60':
        soc_60 = 1
    if soc == '61':
        soc_61 = 1
    if soc == '62':
        soc_62 = 1
    if soc == '63':
        soc_63 = 1
    if soc == '64':
        soc_64 = 1
    if soc == '65':
        soc_65 = 1
    if soc == '66':
        soc_66 = 1
    if soc == '67':
        soc_67 = 1
    if soc == '68':
        soc_68 = 1
    if soc == '69':
        soc_69 = 1
    if soc == '70':
        soc_70 = 1
    if soc == '71':
        soc_71 = 1
    if soc == '72':
        soc_72 = 1
    if soc == '73':
        soc_73 = 1
    if soc == '74':
        soc_74 = 1
    if soc == '75':
        soc_75 = 1
    if soc == '76':
        soc_76 = 1
    if soc == '77':
        soc_77 = 1
    if soc == '78':
        soc_78 = 1
    if soc == '79':
        soc_79 = 1
    if soc == "AC":
        soc_AC=1
    if soc == "AI":
        soc_AI=1
    if soc == "CO":
        soc_CO=1
    if soc == "EL":
        soc_EL=1
    if soc == "SO":
        soc_SO=1
           
    if(pws=="CBA"):
       pws_CBA=1
    if(pws=="DBA"):
       pws_DBA=1
    if(pws=="OES"):
       pws_OES=1
    if(pws=="Other"):
       pws_Other=1
    if(pws=="SCA"):
       pws_SCA=1
    
    if(emps=="Bin1"):
       emps_Bin1=1
    if(emps=="Bin2"):
       emps_Bin2=1
    if(emps=="Bin3"):
       emps_Bin3=1
    if(emps=="Bin4"):
       emps_Bin4=1
    if(emps=="Bin5"):
       emps_Bin5=1
    if(emps=="Bin6"):
       emps_Bin6=1
    if(emps=="Bin7"):
       emps_Bin7=1  
    if(emps=="Others"):
       emps_Others=1
        
    #Training the data
    df=pd.read_csv('train.csv')
    
    train =df.drop(['Unnamed: 0','WORKSITE_STATE', 'WORKSITE_COUNTY_BIN',
       'AGENT_ATTORNEY_STATE_BIN', 'AMENDED_PETITION_BIN',
       'AGENT_REPRESENTING_EMPLOYER',
       'NEW_EMPLOYMENT_BIN', 'CHANGE_PREVIOUS_EMPLOYMENT_BIN'],axis=1)
    
    train = train.drop(train.iloc[:,1:5],axis=1)
    train=train.drop(['Target','WAGE_UNIT_OF_PAY'],axis=1)

    trainX =pd.get_dummies(train)
    #print(len(trainX.columns))
    
    trainY = df['Target']
    
    #trainX=trainX[["FULL_TIME_POSITION_N","FULL_TIME_POSITION_Y","EMPLOYER_NAME_BIN_Bin1","EMPLOYER_NAME_BIN_Bin2","EMPLOYER_NAME_BIN_Bin3","EMPLOYER_NAME_BIN_Bin4","EMPLOYER_NAME_BIN_Bin5","EMPLOYER_NAME_BIN_Others","AGENT_ATTORNEY_CITY_BIN_Bin1","AGENT_ATTORNEY_CITY_BIN_Bin2","AGENT_ATTORNEY_CITY_BIN_Bin3","AGENT_ATTORNEY_CITY_BIN_Bin4","AGENT_ATTORNEY_CITY_BIN_Bin5","AGENT_ATTORNEY_CITY_BIN_None","AGENT_ATTORNEY_CITY_BIN_Others","PW_WAGE_LEVEL_Level I","PW_WAGE_LEVEL_Level II","PW_WAGE_LEVEL_Level III","PW_WAGE_LEVEL_Level IV","SOC_REVISED_CODE_10","SOC_REVISED_CODE_11","SOC_REVISED_CODE_12","SOC_REVISED_CODE_13","SOC_REVISED_CODE_15","SOC_REVISED_CODE_16","SOC_REVISED_CODE_17","SOC_REVISED_CODE_18","SOC_REVISED_CODE_19","SOC_REVISED_CODE_20","SOC_REVISED_CODE_21","SOC_REVISED_CODE_22","SOC_REVISED_CODE_23","SOC_REVISED_CODE_24","SOC_REVISED_CODE_25","SOC_REVISED_CODE_26","SOC_REVISED_CODE_27","SOC_REVISED_CODE_29","SOC_REVISED_CODE_31","SOC_REVISED_CODE_33","SOC_REVISED_CODE_35","SOC_REVISED_CODE_36","SOC_REVISED_CODE_37","SOC_REVISED_CODE_38","SOC_REVISED_CODE_39","SOC_REVISED_CODE_40","SOC_REVISED_CODE_41","SOC_REVISED_CODE_43","SOC_REVISED_CODE_45","SOC_REVISED_CODE_46","SOC_REVISED_CODE_47","SOC_REVISED_CODE_49","SOC_REVISED_CODE_51","SOC_REVISED_CODE_53","SOC_REVISED_CODE_71","SOC_REVISED_CODE_73","SOC_REVISED_CODE_74","SOC_REVISED_CODE_11","SOC_REVISED_CODE_13","SOC_REVISED_CODE_15","SOC_REVISED_CODE_16","SOC_REVISED_CODE_17","SOC_REVISED_CODE_18","SOC_REVISED_CODE_19","SOC_REVISED_CODE_20","SOC_REVISED_CODE_21","SOC_REVISED_CODE_23","SOC_REVISED_CODE_25","SOC_REVISED_CODE_27","SOC_REVISED_CODE_28","SOC_REVISED_CODE_29","SOC_REVISED_CODE_31","SOC_REVISED_CODE_33","SOC_REVISED_CODE_35","SOC_REVISED_CODE_36","SOC_REVISED_CODE_37","SOC_REVISED_CODE_39","SOC_REVISED_CODE_40","SOC_REVISED_CODE_41","SOC_REVISED_CODE_43","SOC_REVISED_CODE_45","SOC_REVISED_CODE_47","SOC_REVISED_CODE_49","SOC_REVISED_CODE_50","SOC_REVISED_CODE_51","SOC_REVISED_CODE_53","SOC_REVISED_CODE_71","SOC_REVISED_CODE_73","SOC_REVISED_CODE_75","SOC_REVISED_CODE_79","SOC_REVISED_CODE_AC","SOC_REVISED_CODE_AI","SOC_REVISED_CODE_CO","SOC_REVISED_CODE_EL","SOC_REVISED_CODE_SO","PW_SOURCE_CBA","PW_SOURCE_DBA","PW_SOURCE_OES","PW_SOURCE_Other","PW_SOURCE_SCA","EMPLOYER_STATE_BIN_Bin1","EMPLOYER_STATE_BIN_Bin2","EMPLOYER_STATE_BIN_Bin3","EMPLOYER_STATE_BIN_Bin4","EMPLOYER_STATE_BIN_Bin5","EMPLOYER_STATE_BIN_Bin6","EMPLOYER_STATE_BIN_Bin7","EMPLOYER_STATE_BIN_Others"]]
    test_list=[empn_Bin1, empn_Bin2, empn_Bin3, empn_Bin4, empn_Bin5, empn_Others, agc_Bin1, agc_Bin2, agc_Bin3, agc_Bin4, agc_Bin5, agc_None, agc_Others, pwl_LevelI, pwl_LevelII, pwl_LevelIII, pwl_LevelIV, soc_10, soc_11, soc_12, soc_13, soc_15, soc_16, soc_17, soc_18, soc_19, soc_20, soc_21, soc_22, soc_23, soc_24, soc_25, soc_26, soc_27, soc_29, soc_31, soc_33, soc_35, soc_36, soc_37, soc_38, soc_39, soc_40, soc_41, soc_43, soc_45, soc_46, soc_47, soc_49, soc_51, soc_53, soc_71, soc_73, soc_74, soc_11, soc_13, soc_15, soc_16, soc_17, soc_18, soc_19, soc_20, soc_21, soc_23, soc_25, soc_27, soc_28, soc_29, soc_31, soc_33, soc_35, soc_36, soc_37, soc_39, soc_40, soc_41, soc_43, soc_45, soc_47, soc_49, soc_50, soc_51, soc_53, soc_71, soc_73, soc_75, soc_79, soc_AC, soc_AI, soc_CO, soc_EL, soc_SO, pws_CBA, pws_DBA, pws_OES, pws_Other, pws_SCA,  emps_Bin1, emps_Bin2, emps_Bin3, emps_Bin4, emps_Bin5, emps_Bin6, emps_Bin7, emps_Others,ftp_N,ftp_Y]
    #print(len(trainX.columns))
    #print(len(testdf.columns))
    testdf=pd.DataFrame([test_list])
    trainX=np.asarray(trainX)
    trainY=np.asarray(trainY)
    testX=np.asarray(testdf)
    lr=LogisticRegression(solver='lbfgs')
    lr.fit(trainX,trainY)
    THRESHOLD = 0.015
    yhat = np.where(lr.predict_proba(testX)[:,1] > THRESHOLD, 1, 0)
    ci=lr.predict_proba(testX).max()
    ci*=100
    ci=round(ci,2)
    if yhat==1:
        disp='DENIED'
        return render_template('yes.html',value=disp,value1=ci)
    else:
        disp='ACCEPTED'
        
        return render_template('yes.html',value=disp,value1=ci)


@app.route('/insights',methods=['GET'])
def insights():
    return render_template('insights.html')

if __name__ == '__main__':
    app.run()
