import subprocess 
from pathlib import Path 
from typing import Optional 
from yt_dlp import YoutubeDL 

DOWNLOAD_DIR = Path.home() / "Downloads" 
DOWNLOAD_DIR.mkdir(exist_ok=True) 

AUDIO_FORMATS = [".wav", ".mp3"] 
FFMPEG_CODEC = "wav" 
FFMPEG_QUALITY = "320"
DEMUCS_MODEL = "htdemucs" 
DEMUCS_DEVICE = "cpu"

# Función para descargar archivo wave de YouTube
def download_audio_from_youtube(url: str, output_dir: Path = DOWNLOAD_DIR) -> Optional[Path]: 
    ydl_opts = {
        "format": "bestaudio/best", 
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "postprocessors": [{ 
            "key": "FFmpegExtractAudio", 
            "preferredcodec": FFMPEG_CODEC, 
            "preferredquality": FFMPEG_QUALITY,
        }],
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            return output_dir / f"{info_dict['title']}.{FFMPEG_CODEC}"
    except Exception as e:
        print(f"Error al descargar el audio: {e}")
        return None

def enhance_audio_quality(file: Path):
    try:
        # Lógica para mejorar la calidad del audio
        pass
    except Exception as e:
        print(f"Error al mejorar la calidad del audio: {e}")

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
    except subprocess.CalledProcessError as e: # Capturamos errores
        print(f"Error al separar el audio: {e}")

def main():
    url = input("Ingrese la URL del video de YouTube: ").strip()
    if not url:
        print("La URL no puede estar vacía.")
        return

    audio_path = download_audio_from_youtube(url)
    if audio_path:
        separate_audio(audio_path)
    else:
        print("No se pudo descargar el audio.")

if __name__ == "__main__":
    main()