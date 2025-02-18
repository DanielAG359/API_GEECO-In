from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import API.db as db

app = FastAPI()

# Modelo Pydantic para los ingresos
class Ingres(BaseModel):
    titol: str
    descripcio: str
    quantitat: float
    data: str  # Asumimos que la fecha está en formato YYYY-MM-DD

# Función auxiliar para obtener una conexión a la base de datos
def get_db_connection():
    return db.get_db_connection()

# Endpoint para crear un ingreso
@app.post("/ingresos/")
async def create_ingreso(ingreso: Ingres):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO ingressos (titol, descripcio, quantitat, data) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (ingreso.titol, ingreso.descripcio, ingreso.quantitat, ingreso.data))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Ingreso creado correctamente", "ingreso": ingreso}

# Endpoint para obtener todos los ingresos
@app.get("/ingresos/")
async def get_ingresos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM ingressos"
        cursor.execute(query)
        ingresos = cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"ingresos": ingresos}

# Endpoint para obtener un ingreso por ID (asumiendo que hay una columna 'id')
@app.get("/ingresos/{ingreso_id}")
async def get_ingreso(ingreso_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM ingressos WHERE id = %s"
        cursor.execute(query, (ingreso_id,))
        ingreso = cursor.fetchone()
        if not ingreso:
            raise HTTPException(status_code=404, detail="Ingreso no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"ingreso": ingreso}

# Endpoint para actualizar un ingreso por ID
@app.put("/ingresos/{ingreso_id}")
async def update_ingreso(ingreso_id: int, ingreso: Ingres):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = "UPDATE ingressos SET titol = %s, descripcio = %s, quantitat = %s, data = %s WHERE id = %s"
        cursor.execute(query, (ingreso.titol, ingreso.descripcio, ingreso.quantitat, ingreso.data, ingreso_id))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Ingreso no encontrado")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Ingreso actualizado correctamente", "ingreso": ingreso}

# Endpoint para eliminar un ingreso por ID
@app.delete("/ingresos/{ingreso_id}")
async def delete_ingreso(ingreso_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = "DELETE FROM ingressos WHERE id = %s"
        cursor.execute(query, (ingreso_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Ingreso no encontrado")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Ingreso eliminado correctamente"}

# Endpoint de bienvenida
@app.get("/")
async def read_root():
    return {"message": "Bienvenido a la API"}