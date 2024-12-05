from pyspark.sql import SparkSession

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    spark=SparkSession.builder.appName("SparkApp").master("local[4]").getOrCreate()
    numbers=[[1],[2],[3],[4],[5]]
    numbersDF=spark.createDataFrame(numbers,"Id:int")
    numbersDF.show()
    input("Press Enter to continue ... met fin à la SParkSession et donc à SparkUI")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
