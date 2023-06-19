# Youtube MP3 Downloader

Esta es una aplicación de línea de comandos que te permite descargar el audio de videos de YouTube en formato MP3. Utiliza las bibliotecas `pytube` para descargar y `moviepy` convertir los archivos.

## Requisitos previos

- Python 3.10 o superior.

## Instalación de dependencias

1. Clona este repositorio y navega al directorio del proyecto.
2. Instala las dependencias del proyecto (recomendable hacerlo en un virutal enviroment):

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta la aplicación usando python con el siguiente comando:

   ```bash
   python main.py run
   ```

2. Sigue las instrucciones proporcionadas en la aplicación para ingresar el enlace del video de YouTube que deseas descargar como MP3.

3. El video se descargará y se convertirá a MP3. El archivo MP3 resultante se almacenará en el directorio de la aplicación.

## Construcción del ejecutable
Ejecuta el siguiente comando para crear el archivo ejecutable (.exe):

   ```bash
   python main.py build
   ```
Después de que se complete el proceso, encontrarás el archivo ejecutable en la carpeta dist.
