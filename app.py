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
        'format': 'bestaudio/best',
        'outtmpl': str(output_dir / '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': FFMPEG_CODEC,
            'preferredquality': FFMPEG_QUALITY,
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        audio_file = Path(ydl.prepare_filename(info_dict)).with_suffix(f".{FFMPEG_CODEC}")

    if audio_file.exists():
        return audio_file
    else:
        print(f"File {audio_file} does not exist. If the path contains spaces, please try again after surrounding the entire path with quotes \"\".")
        return None

# Función para separar el audio en componentes usando Demucs
def separate_audio_with_demucs(audio_file: Path):
    if audio_file.exists():
        command = [
            "demucs",
            "-n", DEMUCS_MODEL,
            "-d", DEMUCS_DEVICE,
            str(audio_file)
        ]
        subprocess.run(command, check=True)
        print("Separación completa. Archivos guardados en el directorio de descargas.")
    else:
        print(f"File {audio_file} does not exist. If the path contains spaces, please try again after surrounding the entire path with quotes \"\".")

# Ejemplo de uso
if __name__ == "__main__":
    url = input("Ingrese la URL del video de YouTube: ")
    audio_file = download_audio_from_youtube(url)
    if (audio_file):
        separate_audio_with_demucs(audio_file)