# Proyecto Urban Grocers | Pruebas de API

## Descripción del proyecto

Proyecto de pruebas de API de Urban Grocers, enfocado en la validación de funcionalidades mediante pruebas manuales y automatizadas.

El proyecto comprende dos actividades:

- **Pruebas manuales:** diseño y ejecución de 104 casos de prueba funcionales para los requisitos KITS y Order and Go, documentados en Excel.
- **Pruebas automatizadas:** desarrollo de 9 pruebas con Python y Pytest para validar la creación de kits mediante solicitudes HTTP.

## Pruebas manuales de API

Se diseñaron y ejecutaron 104 casos de prueba basados en los requisitos y la documentación de la API.

- 43 casos correspondientes al requisito KITS.
- 61 casos correspondientes al requisito Order and Go.
- Documentación de pasos, datos de prueba, resultados esperados y obtenidos.
- Registro de incidencias y seguimiento mediante JIRA.

El archivo Excel con los casos de prueba se encuentra en la carpeta `documentacion/`.

[Consultar casos de prueba de API (Excel)](documentacion/casos-de-prueba-api.xlsx)

## Automatización de pruebas

Se desarrollaron 9 pruebas automatizadas para validar el comportamiento del endpoint de creación de kits.

Las pruebas contemplan diferentes escenarios:

- Longitud mínima y máxima del nombre.
- Nombre vacío.
- Caracteres especiales.
- Espacios y números.
- Parámetro obligatorio ausente.
- Tipo de dato incorrecto.

Se implementaron validaciones de respuestas HTTP 201 (creación exitosa) y 400 (solicitud incorrecta).

## Tecnologías y herramientas

- Python
- Pytest
- Requests
- Postman
- JIRA
- Git y GitHub
- PyCharm

## Estructura del repositorio

```text
qa-project-Urban-Grocers-app-es/
│
├── documentacion/
│   ├── README.md
│   └── casos-de-prueba-api.xlsx
│
├── .gitignore
├── README.md
├── configuration.py
├── create_kit_name_kit_test.py
├── data.py
└── sender_stand_request.py
```

## Ejecución de las pruebas automatizadas

1. Crear y activar un entorno virtual:

```bash
python -m venv .venv
```

En Windows:
```bash
.venv\Scripts\activate
```

2. Instalar las dependencias necesarias:

```bash
pip install pytest
```
3. Ejecutar las pruebas desde la terminal:

```bash
pytest
```


Objetivo del proyecto

Aplicar técnicas de pruebas de API manuales y automatizadas para validar el comportamiento de los servicios, identificar defectos y documentar los resultados obtenidos.
