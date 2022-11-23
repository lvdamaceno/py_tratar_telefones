import pandas as pd

df = pd.read_csv('contatos.csv')
# removendo espaços dos telefones
df['FONE1'] = df['FONE1'].str.replace(" ","")
df['FONE2'] = df['FONE2'].str.replace(" ","")
# inserindo prefixo do país
df['FONE1'] = '+55' + df['FONE1'].astype(str)
df['FONE2'] = '+55' + df['FONE2'].astype(str)

df.to_csv('contatos_tratados.csv')

