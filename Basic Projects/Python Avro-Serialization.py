from fastavro import writer
# The schema
schema = {"doc" : "Calculator",
         "name" : "Calv2.0",
         "type" : "record",
          "fields" : [{"name" : "User" , "type" : "string"},
                      {"name" : "Total", "type" : "float"}
          ]
}
# User inputs
name = input("Enter name:")
Totalsum = 0
for i in range(2):
    sums = float(input(f"Enter number of {i + 1} to be added:"))
    Totalsum += sums
record = [{"User" : name,
          "Total" : Totalsum
}]
# save and load
with open("Calculator.avro","wb") as out:
    writer(out,schema,record)
    
from fastavro import reader
with open("Calculator.avro","rb") as out:
    avro_reader = reader(out)
    for record in avro_reader:
        print(record)
