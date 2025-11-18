# 📘 Guía Completa de NumPy (Versión Detallada y Unificada)

Esta guía reúne **todo lo esencial de NumPy** en un solo archivo para estudiar rápido y tener como referencia.

---

# ⭐ 1. Introducción
NumPy (**Numerical Python**) es una librería fundamental para el cálculo numérico en Python. Ofrece:
- Arrays eficientes (más rápidos y compactos que listas)
- Operaciones vectorizadas sin bucles
- Herramientas estadísticas
- Álgebra lineal optimizada en C
- Funciones matemáticas avanzadas
- Manejo de datos multidimensionales

NumPy utiliza internamente memoria contigua en bloques, por lo que puede procesar datos de manera mucho más rápida que Python puro.

Para usarla:
```python
import numpy as np
```

---

# 🔢 2. Crear Arrays (Explicación Extendida)
### Desde listas
```python
arr = np.array([1, 2, 3])
```

### Bidimensional
```python
mat = np.array([[1,2,3],[4,5,6]])
```

### Rango
```python
np.arange(0, 10, 2)
```

### Linspace
```python
np.linspace(0, 1, 5)
```

### Arrays llenos
```python
np.zeros((3,3))
np.ones((2,4))
np.full((2,2), 7)
np.eye(3)
```

### Aleatorios
```python
np.random.rand(3,3)
np.random.randint(0, 10, (2,3))
```

---

# 📐 3. Atributos del Array (Detalles Técnicos)
```python
arr.ndim    # dimensiones
arr.shape   # filas y columnas
arr.size    # cantidad de elementos
arr.dtype   # tipo de dato
```

---

# ✂️ 4. Indexación y Slicing (Con Casos Especiales)
### Índices
```python
arr[0]
mat[1,2]
```

### Slicing
```python
mat[:,0]
mat[0,:]
mat[1:3, 0:2]
```

---

# 🔄 5. Operaciones Elementwise (Vectorización Completa)
```python
arr + 10
arr * 2
arr ** 2
arr1 + arr2
arr1 * arr2
```

---

# ➕ 6. Operaciones Estadísticas (Descriptivas y Avanzadas)
```python
arr.sum()
arr.mean()
arr.min()
arr.max()
arr.std()
arr.var()
```

Por filas/columnas:
```python
mat.sum(axis=0)
mat.sum(axis=1)
```

---

# 🧮 7. Álgebra Lineal (Linalg en Profundidad)
```python
np.dot(a, b)
a @ b
np.transpose(a)
np.linalg.inv(A)
np.linalg.det(A)
np.linalg.eig(A)
```

---

# 🔄 8. Cambiar Forma (Reshape, Ravel y Flatten)
```python
arr.reshape(3, 2)
arr.flatten()
```

---

# 🔍 9. Máscaras y Filtrado (Boolean Indexing Avanzado)
```python
arr[arr > 5]
mat[mat % 2 == 0]
```

---

# 🔗 10. Concatenación y Stacking (Ejes y Dimensiones)
```python
np.concatenate([a, b])
np.vstack((a, b))
np.hstack((a, b))
```

---

# 🧬 11. Copias y Vistas (View vs Copy a Detalle)
```python
b = arr       # referencia
c = arr.copy()  # copia real
```

---

# ⚡ 12. Tipos de Datos (Casting y Precisión)
```python
arr.astype(float)
arr.astype(int)
```

---

# 🎯 13. Funciones Útiles (Herramientas Prácticas Extendidas)
```python
np.unique(arr)
np.argmax(arr)
np.argmin(arr)
np.where(arr > 5)
np.clip(arr, 0, 10)
```

---

# ⚙️ 14. Matrices
```python
np.diag([1,2,3])
np.triu(A)
np.tril(A)
```

---

# 🧠 Resumen Final
- `np.array()` → crea arrays
- Todo opera **por elemento**
- `axis=0` columnas, `axis=1` filas
- `@` → multiplicación matricial
- `reshape`, `concatenate`, `flatten`
- Filtrado con: `arr[arr > cond]`

---

# 📘 Fin de la guía completa de NumPy
¿Quieres ahora una **hoja de ejercicios** con soluciones y nivel de examen?

