import subprocess 
from pathlib import Path 
from typing import Optional 
from yt_dlp import YoutubeDL 
from pydub import AudioSegment 
import librosa 
import soundfile as sf 
import sys

DOWNLOAD_DIR = Path.home() / "Downloads" 
DOWNLOAD_DIR.mkdir(exist_ok=True) 

AUDIO_FORMATS = [".wav", ".mp3"] 
FFMPEG_CODEC = "wav" 
FFMPEG_QUALITY = "320"
DEMUCS_MODEL = "htdemucs" 
DEMUCS_DEVICE = "cpu"

def download_audio_from_youtube(url: str, output_dir: Path = DOWNLOAD_DIR) -> Optional[Path]: # Función para descargar audio de YouTube
    ydl_opts = {
        "format": "bestaudio/best", # Formato de audio
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"), # Plantilla de nombre de archivo
        "postprocessors": [{ # Postprocesadores
            "key": "FFmpegExtractAudio", # Extraer audio con FFmpeg
            "preferredcodec": FFMPEG_CODEC, # Códec preferido
            "preferredquality": FFMPEG_QUALITY, # Calidad preferida
        }],
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            return output_dir / f"{info_dict['title']}.{FFMPEG_CODEC}"
    except Exception as e:
        print(f"Error al descargar el audio: {e}")
        return None

def convert_to_wav(file_path: Path) -> Optional[Path]: # Función para convertir un archivo a WAV
    if file_path.suffix.lower() == ".wav":
        return file_path

    try:
        audio = AudioSegment.from_file(file_path)
        wav_path = file_path.with_suffix(".wav")
        audio.export(wav_path, format="wav")
        return wav_path
    except Exception as e:
        print(f"Error al convertir el archivo a WAV: {e}")
        return None

def select_local_audio_file() -> Optional[Path]: # Función para seleccionar un archivo de audio local
    file_path = input("Ingrese la ruta completa del archivo de audio local en formato WAV o MP3: ").strip().strip("'\"")
    file_path = Path(file_path)
    if file_path.is_file() and file_path.suffix.lower() in AUDIO_FORMATS:
        return convert_to_wav(file_path)
    print("Archivo no encontrado o formato inválido.")
    return None

def enhance_audio_quality(file_path: Path) -> None: # Función para mejorar la calidad del audio
    try:
        audio = AudioSegment.from_file(file_path)
        audio = audio.normalize() 
        audio = audio + 5
        audio.export(file_path, format="wav")
    except Exception as e:
        print(f"Error al mejorar la calidad del audio: {e}")

def smooth_audio(input_file: Path) -> None: # Función para suavizar el audio
    try:
        y, sr = librosa.load(input_file, sr=None)
        y = librosa.effects.harmonic(y, margin=8) 
        sf.write(input_file, y, sr)
    except Exception as e:
        print(f"Error al suavizar el audio: {e}")

def separate_audio(input_file: Path, output_dir: Path = DOWNLOAD_DIR): # Función para separar el audio
    print("Separando audio en componentes con Demucs...")
    command = [ 
        'demucs', 
        '--out', str(output_dir),
        '-d', DEMUCS_DEVICE,
        '-n', DEMUCS_MODEL,
        str(input_file)
    ]
    try: # Ejecutamos el comando en la terminal
        subprocess.run(command, check=True)
        print("Separación completa. Archivos guardados en el directorio de descargas.")
        for file in output_dir.glob(f"{DEMUCS_MODEL}/*/*.wav"): # Iteramos sobre los archivos separados
            enhance_audio_quality(file) # Mejoramos la calidad del audio
            smooth_audio(file) # Suavizamos el audio
    except subprocess.CalledProcessError as e: # Capturamos errores
        print(f"Error al separar el audio: {e}")

def main(): # Función principal
    while True:
        print("Bienvenido al separador de audio.")
        choice = input("Seleccione una opción:\n1. Descargar música desde YouTube\n2. Usar un archivo de audio local\n3. Salir\nIngrese 1, 2 o 3: ").strip()
        input_file = None
        try:
            if choice == "1":
                url = input("Ingrese la URL del video de YouTube: ").strip()
                input_file = download_audio_from_youtube(url)
                if not input_file:
                    print("Error al descargar el archivo de YouTube.")
                    continue
            elif choice == "2":
                input_file = select_local_audio_file()
                if not input_file:
                    print("Error al seleccionar el archivo local.")
                    continue
            elif choice == "3":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida.")
                continue

            split_choice = input("¿Desea dividir la canción? (s/n): ").strip().lower()
            if split_choice == 's':
                separate_audio(input_file)
                print("Proceso finalizado. ¡Disfruta de tus pistas separadas!")
            else:
                print("Operación completada sin dividir.")
        except KeyboardInterrupt:
            print("\nProceso interrumpido por el usuario.")
        finally:
            exit_choice = input("¿Desea realizar otra operación? (s/n): ").strip().lower()
            if exit_choice != 's':
                print("Saliendo del programa.")
                sys.exit(0)

if __name__ == "__main__": # Si el script se ejecuta directamente
    main() # Llamamos a la función principal