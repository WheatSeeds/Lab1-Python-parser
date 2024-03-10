import pandas as pd
import Parser

Parser.parse(6)

#Функция записи полученных значений в файл xlsx.
def record():
    df = pd.DataFrame.from_dict(Parser.dict)
    df.to_excel('./Lab1_result.xlsx', index=False)

