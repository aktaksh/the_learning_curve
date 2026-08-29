import re #Regex
'''
It helps you search, match, extract, replace, split and validate text
 based based patterns
'''
'''
#\d -> any digit from 0 to 9
#match() checks whether pattern occurs at the beginning of the string
text = "Python is easy"
result = re.match(r"Python",text)
print(result)

#search() -> search anywhere in the string
result = re.search(r"i",text)
print(result)

#findall() -> returns all matching values
text = "contact him at 123, 456 and 789"
result = re.findall(r"\d",text) #one or more digit
print(result)

text = "contact him at 123, 456 and 789"
result = re.findall(r"\d+",text) #one or more digit
print(result)

text = "abc123"
print(re.findall(r"\D",text))

text = "Python_1231"
print(re.findall(r"\w",text)) #word character

text = "Python_1231!@&"
print(re.findall(r"\W",text)) #word character

text = "Python is easy"
print(re.findall(r"\s",text)) #space, tab, new line

text = "apple, banana cat dog"
print(re.findall(r"[a-z]",text))


text = "apple, banana cat dog"
print(re.findall(r"[abc]",text))

text = "apple, banana cat64788 dog"
print(re.findall(r"[0-9]",text))

text = "apple, banana cat64788 dog"
print(re.findall(r"[^0-9]",text))

'''
'''
* -> 0 or more
+ -> 1 or more
? -> 0 or 1
{n} -> exactly n
{n,} -> At least n
{n,m} -> Between n amd m
'''
'''
text = "Hello@#$ Python!!!"
result = re.sub(r"[^a-zA-Z]","",text)
print(result)

text = """
Contact John: 766476476483
Contact Jack: 648764878
Contact Sam: 4687436874
"""
numbers = re.findall(r"\d+",text)
print(numbers)
'''

#fullmatch()
'''
#pathlib
create/directory paths
file exist or not
rename file
delete File
get file info
and more'''

'''
from pathlib import Path

#os.path.join("data","marks.txt") #with os
path = Path("data")/"Students"/"marks.txt"
path.parent.mkdir(parents=True,exist_ok=True)
path.touch()
print(path)


path.cwd() #current directory
path.home() #home directory
p = Path("data/student.txt")
p.exists() #check existence
p.name
p.stem
p.suffix
p.parent
p.mkdir()
p.touch()
p.read_text()
p.open("r")
p.write_text("hello")
p.unlink() #delete file
p.glob("*.txt")
p.stat().st_size
p.iterdir() #directory contents
'''


