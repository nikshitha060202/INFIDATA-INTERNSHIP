print("delete a list of keys")
student={"name":"arun","id":101,"branch":"cs","age":20,"gender":"male","city":"bangalore"}
print("before delete:",student)
# keys to remove from a dict
keys=["gender","city"]
for k in keys:
    student.pop(k)
print("after delete:",student)