# # Python writing files (.txt .json .csv)

# # import json
# import csv

# # worker = {
# #     "name": "Ali",
# #     "age": 30,
# #     "job": "developer"
# # }

# workers = [["Name", "Age", "Job"],
#            ["Ali", 19, "developer"],
#            ["Andrew", 24, "developer"],
#            ["Ali", 21, "developer"]
#            ]

# file_path = '/Users/anvarjonsheraliev/Desktop/PYTHON/file-detection/writing-reading-files/main2.txt'

# # txt_data = "I like palov and manti!🤩🫥🇺🇿 12"
# employees = ["Anvarjon", "Adhamjon", "Alex", "Andrew"]
# # file_path = "/Users/anvarjonsheraliev/Desktop/output.txt"
# # file_path = '/Users/anvarjonsheraliev/Desktop/PYTHON/file-detection/writing-reading-files/main2.txt'

# try: 
#     # with open(file_path, "w") as file:
#     # csv
#     with open(file_path, "w", newline="") as file:
    
#         # file.write("\n" + txt_data)
#         # for employee in employees:
#         #     file.write(employee + "\n")

#         # json
#         # json.dump(worker, file, indent=4)
#         # print(f"json file '{file_path}' was created")

#         # csv
#         writer = csv.writer(file)
#         for row in workers:
#             writer.writerow(row)
#         print(f"csv file '{file_path}' was created")


#         # print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")



# ///////////===========----  PYTHON READING FILES -----=============//////////

# import json
import csv

# file_path = '/Users/anvarjonsheraliev/Desktop/PYTHON/file-detection/writing-reading-files/main2.txt'
# file_path = '/Users/anvarjonsheraliev/Desktop/PYTHON/file-detection/writing-reading-files/workers.json'
file_path = '/Users/anvarjonsheraliev/Desktop/PYTHON/file-detection/writing-reading-files/main2.csv'



try: 
    with open(file_path, "r") as file:
        # json
        # content = json.load(file)

        # csv
        content = csv.reader(file)
        for line in content:
            print(line[0])

        # content = file.read()
        print(content)
except FileExistsError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")
