!pip3 install spark
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q http://archive.apache.org/dist/spark/spark-2.3.1/spark-2.3.1-bin-hadoop2.7.tgz
!tar xf spark-2.3.1-bin-hadoop2.7.tgz
!pip install -q findspark
 
import os
os.environ["JAVA_HOME"]="/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"]="/content/spark-2.3.1-bin-hadoop2.7"
 
import findspark
findspark.init()
 
import pyspark
from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()
spark
