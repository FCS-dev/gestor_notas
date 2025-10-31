def promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


def nota_media(proms):
    return sum(proms) / 3


def alumnos_aprobados(notas):
    if notas:
        aprobados = [
            aprob["alumno"]
            for aprob in notas
            if (aprob["nota1"] + aprob["nota2"] + aprob["nota3"]) / 3 >= 5
        ]
    else:
        return []
    return aprobados


notas = [
    {"alumno": "Fernandito", "nota1": 8, "nota2": 7, "nota3": 6.5},
    {"alumno": "Josefina", "nota1": 8, "nota2": 8.5, "nota3": 5.5},
    {"alumno": "Arturito", "nota1": 5, "nota2": 4.5, "nota3": 5},
]

proms = []
print("Lista de Alumnos\n----------------\n")
for alumno in notas:
    print(f"Alumno  :{alumno['alumno']}")
    print(f"Nota 1  :{alumno['nota1']}")
    print(f"Nota 2  :{alumno['nota2']}")
    print(f"Nota 3  :{alumno['nota3']}")
    media = promedio(alumno["nota1"], alumno["nota2"], alumno["nota3"])
    proms.append(media)
    print(f"Promedio:{media:.2f}")
    print("---")
    # print("aprobado" if media >= 5 else "suspendido")
print("==========")
aprobados = alumnos_aprobados(notas)
print(f"Promedio gnral: {nota_media(proms):.2f}")
if aprobados:
    print("Aprobados:")
    for alumno in aprobados:
        print(f"\t{alumno}")
