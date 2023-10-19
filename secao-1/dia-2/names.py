# Leitura de todos os arquivos
try:
    with open("names.txt", "r") as names:
        print(names.read())
except FileNotFoundError:
    print("Arquivo inexistente")
finally:
    # será sempre executado, independentemente de erro
    print("Fim da tentativa de ler o arquivo")


# filtro para pessoas reprovadas

recovery_students = []
with open("file.txt") as grades_file:
    for line in grades_file:
        student_grade = line
        student_grade = student_grade.split(" ")
        if int(student_grade[1]) < 6:
            recovery_students.append(student_grade[0] + "\n")


with open("recuStudents.txt", mode="w") as recu_students_file:
    print(recovery_students)
    recu_students_file.writelines(recovery_students)
