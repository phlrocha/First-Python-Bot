from getCEPInfo import findCEP
import pathlib
import pandas as pd
import os

folder_path = r"#puth your path here#"

files = [f for f in pathlib.Path(folder_path).iterdir() if f.is_file() and f.suffix ==".xlsx"]
for file in files:
    file_path = file
    print(file_path)

    sheet_name = "Planilha1"
    excel_data = pd.read_excel(file_path,sheet_name=sheet_name)

    excel_data[['ENDERECO','BAIRRO','CIDADE', 'ESTADO']] = excel_data['CEP'].apply(lambda cep: pd.Series(findCEP(cep)))
    excel_data.to_excel(file_path,sheet_name=sheet_name,index=False)



