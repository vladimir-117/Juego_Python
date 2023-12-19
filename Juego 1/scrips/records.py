import csv

class Record:
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje

# funcion para caragr recors
def cargar_record():
    try:
        # Abre el cvs en modo lectura
        with open('records.csv', 'r') as archivo:
            # Create un CSV en modo lectura
            lectura = csv.reader(archivo)
            # lee los records del  CSV 
            records = []
            for row in lectura:
                nombre, puntaje = row
                record = Record(nombre, puntaje)
                records.append(record)
            
            # Ordenar los registros por puntaje de mayor a menor
            records.sort(key=lambda x: float(x.puntaje), reverse=True)
            
            # Devolver solo los primeros 5 registros
            return records[:5]
            
    except IOError:
        print("Error al cargar el récord")
        
# funcion para guardar records
def guardar_record(record):
    
    try:
        # Carga los registros existentes
        records = cargar_record()

        # Ordenar los registros por puntaje de mayor a menor
        records.sort(key=lambda r: int(r.puntaje), reverse=True)

        # Verificar si el nuevo récord es mejor que los existentes
        if int(record.puntaje) > int(records[-1].puntaje):
            # Reemplazar el récord más bajo
            records.pop()
            records.append(record)

            # Abrir el archivo CSV en modo escritura
            with open('records.csv', 'w', newline='') as archivo: # se da un apodo al achivo para facilidad de uso
                # Crear un objeto escritor CSV
                escribir = csv.writer(archivo)

                # Escribir todos los registros al archivo CSV
                for r in records:
                    escribir.writerow([r.nombre, r.puntaje])

            print("¡Récord guardado exitosamente!")
        else:
            print("El récord no supera a los 5 mejores registros. No se añadió.")

    except ValueError:
        print("Error al guardar el récord")