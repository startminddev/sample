# Separador de Audio

Esta aplicación te permite descargar música desde YouTube, optimizar la calidad del audio y separar automáticamente las pistas de sonido utilizando Demucs, todo a través de una URL.

## Requisitos

- Python 3.10
- yt-dlp
- Demucs

## Instalación

1. Instala python y git con: 

    ```sh
    brew update && brew install python@3.10 && brew install git && python -m ensurepip --upgrade
    ```

2. Clona este repositorio:

    ```sh
    git clone https://github.com/startminddev/sample.git
    cd sample
    ```

3. Instala las dependencias:

    ```sh
    pip install -r requirements.txt
    ```

4. Instala Demucs siguiendo las instrucciones en su [repositorio oficial](https://github.com/facebookresearch/demucs).


## Uso

Ejecuta el script `server.py`:

```sh
python [server.py](http://_vscodecontentref_/2)
