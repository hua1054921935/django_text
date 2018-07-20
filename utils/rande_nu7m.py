import random
# data=random.uniform(10,100)
# print(round(data,2))
# print(a)list1=[1,2,3]
# a=random.sample(list1,2)
sql="""INSERT INTO b_machine_monitoring(machine_id,cpu_use,memory_use,disk_use) VALUES(%s,%s,%s,%s)"""%(1,2,3,4)
print(sql)