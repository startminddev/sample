# Separador de Audio

Esta aplicación te permite descargar música desde YouTube, optimizar la calidad del audio y separar automáticamente las pistas de sonido utilizando Demucs, todo a través de una URL.

## Requisitos

- Python 3.10
- yt-dlp
- Demucs

## Instalación

1. Instala python, git, pip y las dependencias necesarias con el siguiente comando (haz copiar y pegar en la terminal): 

    ```sh
    brew update && brew install python@3.10 && brew install git && python -m ensurepip --upgrade && brew install ffmpeg && pip install yt-dlp && pip install demucs
    ```

2. Clona este repositorio (Haz copiar y pegar en la terminal):

    ```sh
    git clone https://github.com/startminddev/sample.git
    cd sample
    ```

3. Ejecuta en la consola el script con:

```sh
python app.py
```