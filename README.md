# Configuración del Entorno Virtual en Linux

Este documento proporciona los pasos para configurar y usar un entorno virtual en Windows, instalar las dependencias necesarias y ejecutar una aplicación Python.

## Paso 1: Crear un Entorno Virtual

Abre la línea de comandos y navega al directorio donde deseas crear tu entorno virtual. Ejecuta el siguiente comando para crear un nuevo entorno virtual llamado `venv`:

```shell
python3 -m venv venv
```

Esto creará un nuevo directorio llamado venv en tu directorio actual, que contendrá el entorno virtual.

## Paso 2: Activar el Entorno Virtual
Para activar el entorno virtual en Windows, ejecuta el siguiente comando:

```shell
source venv/bin/activate
```

Verás que el prompt de tu línea de comandos cambia para mostrar el nombre del entorno virtual, indicando que está activo.

## Paso 3: Instalar Dependencias
Con el entorno virtual activo, puedes instalar las dependencias necesarias para tu proyecto. Si tienes un archivo requirements.txt, puedes instalar todas las dependencias listadas en él con el siguiente comando:

```shell
pip install -r requirements.txt
```

## Paso 4: Ejecutar la Aplicación
Finalmente, puedes ejecutar tu aplicación Python con el siguiente comando:

```shell
uvicorn app:app --reload
```

Asegúrate de que app.py esté en tu directorio actual o proporciona la ruta completa al archivo.

## Conclusión
Ahora tienes un entorno virtual configurado y activo en tu sistema Windows, has instalizado las dependencias necesarias y has ejecutado tu aplicación Python.