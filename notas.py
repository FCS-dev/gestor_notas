def promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


def nota_media(proms):
    return sum(proms) / 3


notas = [
    {"alumno": "Fernandito", "nota1": 8, "nota2": 7, "nota3": 6.5},
    {"alumno": "Josefina", "nota1": 8, "nota2": 8.5, "nota3": 5.5},
    {"alumno": "Arturito", "nota1": 5, "nota2": 4.5, "nota3": 5},
]

proms = []
for alumno in notas:
    print(f"Alumno  :{alumno['alumno']}")
    print(f"Nota 1  :{alumno['nota1']}")
    print(f"Nota 2  :{alumno['nota2']}")
    print(f"Nota 3  :{alumno['nota3']}")
    media = promedio(alumno["nota1"], alumno["nota2"], alumno["nota3"])
    proms.append(media)
    print(f"Promedio:{media:.2f}")
    print("aprobado" if media >= 5 else "suspendido")
print(f"\nPromedio gnral: {nota_media(proms):.2f}")
