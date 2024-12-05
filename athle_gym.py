from pyspark.sql import SparkSession
from pyspark.sql import functions
spark=SparkSession.builder.appName("gym").master("local[4]").getOrCreate()
path=r'C:\Users\CNAAR\OneDrive - Sopra Steria\Desktop\input_gym_complet.txt'
df=spark.read.text(path)
df.show(20)

longueur=df.select(functions.length("value"))
#print(longueur.first()[0])

for i in range(longueur.first()[0]):  #for i in range(5)
    df=df.withColumn("colonne_"+str(i+1),functions.col("value").substr(i+1,1))
df=df.drop("value")

colonnes = df.columns
for colonne in colonnes :
    print(df.groupBy(colonne).count().orderBy(functions.desc("count")).select(colonne).first()[colonne])

