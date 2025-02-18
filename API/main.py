from fastapi import FastAPI, HTTPException
from db import get_db_connection
from models import Ingreso, Despesa

app = FastAPI()

# CRUD para Ingresos

# 1. Crear Ingreso (POST)
@app.post("/ingressos/")
def crear_ingreso(ingreso: Ingreso):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO ingressos (id, titol, descripcio, quantitat, data) VALUES (%s, %s, %s, %s, %s)",
            (ingreso.id, ingreso.titol, ingreso.descripcio, ingreso.quantitat, ingreso.data),
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Ingreso creat correctament"}

# 2. Obtenir Ingreso per ID (GET)
@app.get("/ingressos/{id}")
def obtenir_ingreso(id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ingressos WHERE id = %s", (id,))
    ingreso = cursor.fetchone()
    cursor.close()
    conn.close()
    if not ingreso:
        raise HTTPException(status_code=404, detail="Ingreso no trobat")
    return ingreso

# 3. Obtenir tots els Ingressos (GET)
@app.get("/ingressos/")
def obtenir_tots_ingressos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ingressos")
    ingressos = cursor.fetchall()
    cursor.close()
    conn.close()
    return ingressos

# 4. Modificar Ingreso (PUT)
@app.put("/ingressos/{id}")
def modificar_ingreso(id: int, ingreso: Ingreso):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE ingressos SET titol = %s, descripcio = %s, quantitat = %s, data = %s WHERE id = %s",
            (ingreso.titol, ingreso.descripcio, ingreso.quantitat, ingreso.data, id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Ingreso no trobat")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Ingreso actualitzat correctament"}

# 5. Eliminar Ingreso (DELETE)
@app.delete("/ingressos/{id}")
def eliminar_ingreso(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM ingressos WHERE id = %s", (id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Ingreso no trobat")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Ingreso eliminat correctament"}


# CRUD para Despesas

# 1. Crear Despesa (POST)
@app.post("/despeses/")
def crear_despesa(despesa: Despesa):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO despeses (id, titol, descripcio, quantitat, data) VALUES (%s, %s, %s, %s, %s)",
            (despesa.id, despesa.titol, despesa.descripcio, despesa.quantitat, despesa.data),
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Despesa creat correctament"}

# 2. Obtenir Despesa per ID (GET)
@app.get("/despeses/{id}")
def obtenir_despesa(id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM despeses WHERE id = %s", (id,))
    despesa = cursor.fetchone()
    cursor.close()
    conn.close()
    if not despesa:
        raise HTTPException(status_code=404, detail="Despesa no trobada")
    return despesa

# 3. Obtenir totes les Despeses (GET)
@app.get("/despeses/")
def obtenir_totes_despeses():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM despeses")
    despeses = cursor.fetchall()
    cursor.close()
    conn.close()
    return despeses

# 4. Modificar Despesa (PUT)
@app.put("/despeses/{id}")
def modificar_despesa(id: int, despesa: Despesa):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE despeses SET titol = %s, descripcio = %s, quantitat = %s, data = %s WHERE id = %s",
            (despesa.titol, despesa.descripcio, despesa.quantitat, despesa.data, id),
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Despesa no trobada")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Despesa actualitzada correctament"}

# 5. Eliminar Despesa (DELETE)
@app.delete("/despeses/{id}")
def eliminar_despesa(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM despeses WHERE id = %s", (id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Despesa no trobada")
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Despesa eliminada correctament"}
