import sys
import pandas as pd

def usage():
    return "usage: aggregate_data input_file_1, ..., input_file_n output_file"


if __name__=="__main__":
    if len(sys.argv) > 1:
        input_files = sys.argv[1:-1]
        output_file = sys.argv[-1]

        df_list = [pd.read_csv(input_file) for input_file in input_files]
        dataframe = pd.concat(df_list)
        dataframe = dataframe.drop(dataframe.columns[0:2], axis=1) #COWBOY LINE
        dataframe.to_csv(output_file)
        
    else:
        print(usage())
        sys.exit(1)
        
    
        
    

