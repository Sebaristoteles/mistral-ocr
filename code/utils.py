def read_input_csv(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def write_output(output_data, output_path):
    import json
    with open(output_path, 'w') as f:
        json.dump(output_data, f, indent=4)