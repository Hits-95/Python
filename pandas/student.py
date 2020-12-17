import json
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import student_module as sm

# main method
if __name__ == "__main__":
    try:
        # Opening JSON file
        f = open('./pandas/data.json',)

        # read file
        data = json.load(f)

        # create array of objects..
        objs = [sm.Student() for i in range(len(data["students"]))]

        # calculate result and add into lists...
        rollno = []
        name = []
        city = []
        java = []
        php = []
        python = []
        nodejs = []
        total = []
        percentage = []
        _class = []

        for obj, d in zip(objs, data["students"]):
            obj.get_stud(d["rollno"], d["name"], d["city"],
                         d["marks"]["java"], d["marks"]["php"], d["marks"]["python"], d["marks"]["nodejs"])
            obj.cal_result()
            obj.find_cls()
            obj.display_stud()
            # insert data in list
            rollno.append(obj.rollno)
            name.append(obj.name)
            city.append(obj.city)
            java.append(obj.java)
            php.append(obj.php)
            python.append(obj.python)
            nodejs.append(obj.nodejs)
            total.append(obj.total)
            percentage.append(obj.percentage)
            _class.append(obj.cls)

        df = pd.DataFrame({
            "Rollno": rollno,
            "Name": name,
            "City": city,
            "Java": java,
            "Php": php,
            "Python": python,
            "Nodejs": nodejs,
            "Total": total,
            "Percentage": percentage,
            "Class": _class

        })

        writer = ExcelWriter(".//pandas//data.xlsx",  engine='xlsxwriter')

        df.to_excel(writer, 'Students', index=False)
        writer.save()

    except Exception as e:
        print(e)
    finally:
        # Closing file
        f.close()
