from pprint import pprint

students_db = {1:{"name": "alice", "age": 20, "department": "agric"}}
def start():
	print("i am back to executing start function")
	while True:
		print("""
			1. Add Student
			2. Delete Student
			3. Update record
			4. Get Student
			5. Display all student record
			6. Search Student by Name
			7. Count Student
			8. Filter By Age
			>>""")
		user_choice = int(input("choice:\n>>> "))
		if user_choice == 1:
			add_student()
		elif user_choice == 2:
			delete_student()
		elif user_choice == 3:
			update_student()
		elif user_choice == 4:
			get_student()
		elif user_choice == 5:
			display_students_db()
		elif user_choice == 6:
			search_student_by_name()
		elif user_choice == 7:
			count_students()
		elif user_choice == 8:
			filter_by_age()
		else:
			print("Good bye!")
			break
def add_student():
	print("I am back to add function")
	name = input("Student Name:\n>> ")
	age = int(input("Student Age:\n>> "))
	department = input("Student Department:\n>> ")
	key = len(students_db) + 1
	students_db[key] = {"name": name, "age": age, "department": department}
	pprint(students_db)

def delete_student():
	print("I am back to Delete function")
	student_id = int(input("Student Id to be deleted:\n>> "))
	if student_id in students_db:
		del students_db[student_id]
		print(f"Student with user id:{student_id} has been deleted successfully")
	else:
		print("STudent ID not found")

def update_student():
	print("I am back to updating function")
	student_id = int(input("Student id to be upadated:\n>> "))
	if student_id in students_db:
		print(students_db[student_id])
		
		print("""
		1. name
		2. age
		3. department >>""")

		item = input("Enter Item key to be update:\n>> ")
		if item in students_db[student_id].keys():
			new_value = input("Enter new value:\n>>")
			students_db[student_id].update({item: new_value})
			print(students_db)
		else:
			print("Item does not exist")
	else:
		print("User id does not exist")
def get_student():
	print("I am back to get function")
	student_id = int(input("Student id to be displayed:\n>> "))
	if student_id in students_db:
		print(f"Students name is: {students_db[student_id]['name']},\nStudent Age: {students_db[student_id]['age']},\nStudent Department: {students_db[student_id]['department']}")
	else:
		print("Student Record not found")

def display_students_db():
	print("I am back to display function")
	pprint(students_db)

def search_student_by_name():
	print("I am back to search function")
	search_name = input("Student name to search:\n>> ")
	for student, details in students_db.items():
		if search_name == details["name"]:
			print(f"{student}: {details}")	
		elif search_name != details["name"]:
			flag = True
			continue
			
def count_students():
	print("I am back to count function")
	no_student = 0
	for student in students_db:
		no_student += 1
	print(f"The number of students is: {no_student}")


def filter_by_age():
	student_age = int(input("Enter minimum Age:\n>>> "))
	for student, details in students_db.items():
		if details["age"] > student_age:
			print(f"{student}: {details}")
		else:
			continue
			
start()
