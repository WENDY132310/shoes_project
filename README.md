# Shoes Project

Este proyecto es una aplicación para la gestión de producción y mantenimiento de máquinas, pensada para fábricas de zapatos o similares. Permite registrar, consultar, modificar y eliminar información sobre el mantenimiento de las máquinas, usando una interfaz gráfica sencilla.

## Características

- **Registro de máquinas:** Añade nombre, referencia y fechas de mantenimiento.
- **Visualización:** Muestra los registros en una tabla interactiva.
- **Búsqueda:** Permite buscar máquinas por nombre o referencia.
- **Modificación:** Edita la información de mantenimiento de cualquier máquina.
- **Eliminación:** Borra registros fácilmente, con confirmación.
- **Cálculo de días:** Calcula automáticamente los días restantes para el próximo mantenimiento.
- **Persistencia:** Guarda y lee los datos desde un archivo CSV.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/WENDY132310/shoes_project.git
   cd shoes_project
   ```
2. Instala las dependencias de Python (Tkinter está incluido en la mayoría de instalaciones de Python):
   ```bash
   pip install -r requirements.txt
   ```
   > Si no existe `requirements.txt`, las dependencias principales son:
   > - tkinter (interfaz gráfica)
   > - csv (módulo estándar para manejo de archivos CSV)
   > - datetime (módulo estándar para manejo de fechas)

3. Ejecuta la aplicación:
   ```bash
   python Produccion.py
   ```

## Uso

- Ingresa los datos de las máquinas en los campos correspondientes.
- Usa los botones para agregar, buscar, modificar o eliminar registros.
- Visualiza todos los registros en la tabla.
- El sistema calcula los días para el próximo mantenimiento automáticamente.

## Archivos principales

- `Produccion.py`: Lógica principal, interfaz gráfica, gestión de datos.
- `tarjeta.py`: Módulo auxiliar (por ejemplo, gestión de pagos o tarjetas).

## Estructura de datos

Los registros se almacenan en un archivo llamado `registro_mant.csv` con la siguiente estructura:
```
Nombre de máquina, Referencia, Fecha último mantenimiento, Fecha próximo mantenimiento
```

## Contribuciones

¡Las contribuciones son bienvenidas! Puedes abrir issues o pull requests para mejorar el proyecto.

## Licencia

Este proyecto está bajo la licencia MIT.

---

> Desarrollado por [WENDY132310](https://github.com/WENDY132310)
