import os
import torch
import symbolicregression
import glob
import pandas as pd
import time
import sympy as sp

model_path = "model.pt" 

if not os.path.isfile(model_path): 
    raise Exception("Model file not found")

if not torch.cuda.is_available():
    model = torch.load(model_path, map_location=torch.device('cpu'))
else:
    model = torch.load(model_path)
    model = model.cuda()

print(model.device)
print("Model successfully loaded!")

est = symbolicregression.model.SymbolicTransformerRegressor(
                        model=model,
                        max_input_points=200,
                        n_trees_to_refine=100,
                        rescale=True
                        )

path ="/root/csv_2feature"
all_files = glob.glob(os.path.join(path , "B*.csv"))

result_path = os.path.join("/root/.../", 'sp500_2feature.txt')

start_time = time.time()

with open(result_path, 'w') as f:
    for filename in all_files:
        file_start_time = time.time()
        df = pd.read_csv(filename)
        #x = df[['open', 'low','high','close','volume']].values
        x = df[['open', 'low']].values
        y = df['future_RV'].values
        est.fit(x, y)
        replace_ops = {"add": "+", "mul": "*", "sub": "-", "pow": "**", "inv": "1/"}
        model_str = est.retrieve_tree(with_infos=True)["relabed_predicted_tree"].infix()
        for op,replace_op in replace_ops.items():
            model_str = model_str.replace(op,replace_op)
        parsed_expr = sp.parse_expr(model_str)
        print(parsed_expr)
        
        f.write(f'Filename: {os.path.basename(filename)}\n')
        f.write(str(parsed_expr))
        f.write('\n')
        f.write(model_str)
        f.write('\n\n')
        file_end_time = time.time()
        print(f'Elapsed time for {os.path.basename(filename)}: {file_end_time - file_start_time} seconds')

end_time = time.time()
elapsed_time = end_time - start_time
print(f'Total elapsed time for all files: {elapsed_time} seconds')   






