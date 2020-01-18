import sys
import numpy as np
import pandas as pd

""" Reads data file into one long list """
def fileToList(filename):
    with open(filename, mode='r') as f:
        line_list = f.readlines()
    
    intermediate_list = [line.split() for line in line_list]
    long_list = []

    for line in intermediate_list:
        long_list+=line

    return long_list

""" Turns long list from fileToList into nx76 matrix """
def reshapeList(in_list):
    try:
        assert(len(in_list)%76==0)
        out_list=[]
        num_rows = len(in_list)//76
        for row in range(num_rows):
            idx = row*76
            out_list.append(in_list[idx:idx+76])
        
    except AssertionError: #wrong format data
        print("Raw data not in correct format")
        sys.exit(1)

    return out_list

""" Harcoded column name and comments """
def getColumnComments():
    comment_dict = {3:"sex (1 = male; 0 = female)",
                    4:"chest pain location (1 = substernal; 0 = otherwise)",
                    5:"pain on exertion (1 = provoked by exertion; 0 = otherwise)",
                    6:"relief after resting (1 = relieved; 0 = otherwise)",
                    7:"sum of 4, 5, and 6",
                    8:"pain type (1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic)",
                    9:"resting blood pressure (in mm Hg on admission to the hospital)",
                    11:"serum cholestoral in mg/dl",
                    12:"I believe this is 1 = smoker; 0 = not a smoker",
                    13:"cigarettes per day",
                    14:"number of years as a smoker",
                    15:"fasting blood sugar > 120 mg/dl)  (1 = true; 0 = false)",
                    16:"1 = history of diabetes; 0 = no such history)",
                    17:"family history of coronary artery disease (1 = yes; 0 = no)",
                    18:"restecg: resting ecg results (0: normal, 1: having ST-T wave abnormality, 2: showing probable or definite left ventricular hypertrophy by Estes criteria)",
                    19:"month of exercise ECG reading",
                    20:"day of exercise ECG reading",
                    21:"year of exercise ECG reading",
                    22:"digitalis used during exercise ECG: 1 = yes; 0 = no",
                    23:"Beta blocker used during exercise ECG: 1 = yes; 0 = no",
                    24:"nitrates used during exercise ECG: 1 = yes; 0 = no",
                    25:"calcium channel blocker used during exercise ECG: 1 = yes; 0 = no",
                    26:"diuretic used used during exercise ECG: 1 = yes; 0 = no",
                    27:"exercise protocol (1 = Bruce, 2 = Kottus, 3 = McHenry, 4 = fast Balke, 5 = Balke, 6 = Noughton, 7 = bike 150 kpa min/min  (Not sure if 'kpa min/min' is what was written!), 8 = bike 125 kpa min/min, 9 = bike 100 kpa min/min, 10 = bike 75 kpa min/min, 11 = bike 50 kpa min/min, 12 = arm ergometer",
                    28:"duration of exercise test in minutes",
                    29:"time when ST measure depression was noted",                  
                    30:"mets achieved",
                    31:"maximum heart rate achieved",
                    32:"resting heart rate",
                    33:"peak exercise blood pressure (first of 2 parts)",
                    34:"peak exercise blood pressure (second of 2 parts)",
                    36:"resting blood pressure",
                    37:"exercise induced angina (1 = yes; 0 = no)",
                    38:"1 = yes; 0 = no",
                    39:"ST depression induced by exercise relative to rest",
                    40:"the slope of the peak exercise ST segment (1: upsloping, 2: flat, 3: downsloping)",
                    41:"height at rest",
                    42:"height at peak exercise",
                    43:"number of major vessels (0-3) colored by flouroscopy",
                    44:"irrelevant",
                    45:"irrelevant",
                    46:"rest radionucleide (sp?) ejection fraction",
                    47:"rest wall (sp?) motion abnormality (0: none, 1: mild or moderate, 2: moderate or severe, 3: akinesis or dyskmem (sp?))",
                    48:"exercise radinalid (sp?) ejection fraction",
                    49:"exerwm: exercise wall (sp?) motion",
                    50:"3 = normal; 6 = fixed defect; 7 = reversable defect",
                    51:"not used",
                    52:"not used",
                    53:"not used",
                    54:"month of cardiac cath (sp?)  (perhaps 'call')",
                    55:"day of cardiac cath (sp?)",
                    56:"year of cardiac cath (sp?)",
                    57:"diagnosis of heart disease (angiographic disease status) 0: < 50% diameter narrowing, 1: > 50% diameter narrowing (in any major vessel: attributes 59 through 68 are vessels)",
                    68:"not used",
                    69:"not used",
                    70:"not used",
                    71:"not used",
                    72:"not used",
                    73:"not used",
                    74:"not used",
                    75:"last name of patient"
    }
    
    return comment_dict


def getColumnLabels():
    label_dict = {0:"id",
                  1:"ccf",
                  2:"age",
                  3:"sex",
                  4:"painloc",
                  5:"painexer",
                  6:"relrest",
                  7:"pncaden", 
                  8:"cp",
                  9:"trestbps",
                  10:"htn",
                  11:"chol",
                  12:"smoke",
                  13:"cigs",
                  14:"years",
                  15:"fbs",
                  16:"dm",
                  17:"famhist",
                  18:"restecg",
                  19:"ekgmo",
                  20:"ekgday",
                  21:"ekgyr",
                  22:"dig",
                  23:"prop",
                  24:"nitr",
                  25:"pro",
                  26:"diuretic",
                  27:"proto",
                  28:"thaldur",
                  29:"thaltime",
                  30:"met",
                  31:"thalach",
                  32:"thalrest",
                  33:"tpeakbps",
                  34:"tpeakbpd",
                  35:"dummy",
                  36:"trestbpd",
                  37:"exang",
                  38:"xhypo",
                  39:"oldpeak",
                  40:"slope",
                  41:"rldv5",
                  42:"rldv5e",
                  43:"ca",
                  44:"restckm",
                  45:"exerckm",
                  46:"restef",
                  47:"restwm",
                  48:"exeref",
                  49:"exerwm",
                  50:"thal",
                  51:"thalsev",
                  52:"thalpul",
                  53:"earlobe",
                  54:"cmo",
                  55:"cday",
                  56:"cyr",
                  57:"num",
                  58:"lmt",
                  59:"ladprox",
                  60:"laddist",
                  61:"diag",
                  62:"cxmain",
                  63:"ramus",
                  64:"om1",
                  65:"om2",
                  66:"rcaprox",
                  67:"rcadist",
                  68:"lvx1",
                  69:"lvx2",
                  70:"lvx3",
                  71:"lvx4",
                  72:"lvf",
                  73:"cathef",
                  74:"junk",
                  75:"name",
                  }
    
    return label_dict


def usage():
    return "usage: data_cleaning input_file output_file"

if __name__=="__main__":
    if len(sys.argv) != 3:
        print(usage())
        sys.exit(0)
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        
        raw_data_list = fileToList(input_file)
        prepared_list = reshapeList(raw_data_list)
        dataframe = convertToDataframe(prepared_list)
        dataframe.to_csv(out_file)
        breakpoint()
        pass
    

