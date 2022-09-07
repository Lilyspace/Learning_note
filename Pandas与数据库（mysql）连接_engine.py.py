import pymysql
import sqlalchemy as sac
import pandas as pd
engine = sac.create_engine("mysql+pymysql://root:Lily1234@localhost:3306/lily")
df = pd.read_sql_query('select * from babynames', engine)
df = df.set_index('ID')
df.info()
