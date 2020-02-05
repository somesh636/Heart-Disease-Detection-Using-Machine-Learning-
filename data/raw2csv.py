import sys
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
        #breakpoint()
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


""" Converts reshaped list to dataframe """
def convertToDataframe(prepared_list):
    column_dict = getColumnLabels()
    column_labels = [column_dict[i] for i in range(76)]
    dataframe = pd.DataFrame.from_records(prepared_list, columns=column_labels)
    return dataframe

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
    return "usage: raw2csv input_file output_file"

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
        dataframe.to_csv(output_file)
        
    

