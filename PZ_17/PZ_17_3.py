
# 1
import os

folder_path = '../PZ_11'

os.chdir(folder_path)

files = os.listdir()

print("\nCписок всех файлов в каталоге PZ11:")
for file in files:
    if os.path.isfile(os.path.join(folder_path, file)):
        print(file)


# 2
os.chdir("..")
os.makedirs("test/test1")

os.replace(r"C:\Users\Acer\Documents\PycharmProjects\ИС-22\ProjectManakova\PZ_6\PZ_6_2.py", r"C:\Users\Acer\Documents\PycharmProjects\ИС-22\ProjectManakova\test\PZ_6_2.py")
os.replace(r"C:\Users\Acer\Documents\PycharmProjects\ИС-22\ProjectManakova\PZ_6\PZ_6_3.py", r"C:\Users\Acer\Documents\PycharmProjects\ИС-22\ProjectManakova\test\PZ_6_3.py")
os.replace(r"C:\Users\Acer\Documents\PycharmProjects\ИС-22\ProjectManakova\PZ_7\PZ_7_2.py", r"C:\Users\Acer\Documents\PycharmProjects\ИС-22\ProjectManakova\test\test1\test.txt")

folder_path = r"C:\Users\Acer\Documents\PycharmProjects\ИС-22\ProjectManakova\test"

files = os.listdir(folder_path)
print('\nРазмеры файлов в папке test:')

for file in files:
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        print(f"File: {file} | Size: {file_size} bytes")

# 3
os.chdir(r"C:\Users\Acer\Documents\PycharmProjects\ИС-22\ProjectManakova\PZ_11")
files = os.listdir()
shortest_file = min(files, key=len)
shortest_file_name = os.path.basename(shortest_file)
print(f"\n Файл с самым коротким именем в PZ11: {shortest_file_name}")

# 4
folder_path = r"C:\Users\Acer\Documents\PycharmProjects\ИС-22\ProjectManakova\reports"
os.chdir(folder_path)
os.startfile(r"C:\Users\Acer\Documents\PycharmProjects\ИС-22\ProjectManakova\reports\PZ-2.pdf")

# 5
file_path = r"C:\Users\Acer\Documents\PycharmProjects\ИС-22\ProjectManakova\test\test1\test.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("File not found.")