# Tangalin, Michael Jan R.
# 3BSIT-2(Online)
# OLA # 5

from statistics import mean


def studentGrade(name, math, english, science):
    grades = [float(math), float(english), float(science)]
    average = mean(grades)
    print("{0} \n\tMath = {1}, English = {2}, Science = {3} \n\tAverage is {4}."
          .format(name, math, english, science, round(average, 2)))


studentGrade("Eunice", 89, 88, 90)
studentGrade("James", 90, 95, 90)
studentGrade("John", 70, 100, 99)


