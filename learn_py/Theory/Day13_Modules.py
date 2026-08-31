# concurrent.futures-> used to execute multiple tasks consurrently
#import concurrent.futures
'''
Provides 2 main executors:
 1) ThreadPoolExecutor -> For Threads
   a) File operators
   b) Download file
   c) API Calls
      .. more
 2) ProcessPoolExecutor -> for processes
  a) Mathematical calculations
  b) Image processing
  c) Large data processing
  d) CPU Algorithms
    .. more
'''


from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time
import random
'''
1) Read student data from files/I-O -> ThreadPoolExecutor
2) Calculte total,percentage, grade -> CPU-BOUND -> ProcessPoolExecutor
3) Save the processed result -> file/database -> I-O 0> ThreadPoolExecutor
'''
#PART 1: I/O 
def read_student(student_id):
    print(f"Reading dta for student {student_id}")
    time.sleep(2)
   
    marks= [
        random.randint(40,100),
        random.randint(40,100),
        random.randint(40,100),
        random.randint(40,100),
        random.randint(40,100)
    ]
    return {
        "id":student_id,
        "marks":marks
    }

#PART 2 CALCULATIONS CPU-BOUND
def calculate_result(student):
    student_id = student["id"]
    marks = student["marks"]
    print(f"Calculating result for student {student_id}")

    #CPU-intesive calculation
    total=0
    for i in range(5_000_000):
        total+=i%10
    total_marks = sum(marks)
    percentage = total_marks/len(marks)
    if percentage>=90:
        grade ="A"
    elif percentage>=80:
        grade = "B"
    elif percentage >=70:
        grade = "C"
    else:
        grade="F"
    return {
        "id": student_id,
        "marks":marks,
        "total":total_marks,
        "percentage":percentage,
        "grade":grade
    }

#PART 3: I/O BOUND
def save_result(result):
    student_id = result["id"]
    print(f"Saving result for Student {student_id}")
    time.sleep(2)
    filename = f"student_{student_id}.txt"
    with open(filename,"w") as file:
        file.write(f"Student ID: {student_id}\n")
        file.write(f"Marks: {result['marks']}\n")
        file.write(f"Total: {result['total']}\n")
        file.write(f"Percentage: {result['percentage']}\n")
        file.write(f"Grade: {result['grade']}\n")

    return f"Student {student_id} saved successfully!"

###MAIN PROGRAM
if __name__ == "__main__":
    student_ids = [101,102,103,104,105]
    #READ STUDENT DATA
    print("\n STEP 1: READING STUDENT DATA\n")
    with ThreadPoolExecutor(max_workers=5) as executor:
        students = list(
            executor.map(read_student,student_ids)
        )
    print("\n All student data has been read.")

    #CALCULATING RESULT
    print("\nSTEP2: CALCULATING RESULT\n")
    with ProcessPoolExecutor(max_workers=4) as executor:
      results=list(
          executor.map(calculate_result,students)
          )
    print("\nAll result calculated.")

    #SAVING RESULT
    print("\n STEP 3: SAVING RESULTS\n")
    with ThreadPoolExecutor(max_workers=5) as executor:
        messages=list(
            executor.map(save_result,results)
        )
    print("\n FINAL OUTPUT\n")

    for message in messages:
        print(message)
