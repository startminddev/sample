README.md

Audio Splitter Tool

Este proyecto es una herramienta avanzada para procesar archivos de audio. Permite descargar música desde YouTube, convertir formatos de audio, mejorar la calidad del audio y separar las pistas de audio en componentes como voces, instrumental, batería, entre otros, utilizando el modelo Demucs.

Funcionalidades

	•	Descarga de música desde YouTube: Descarga y convierte automáticamente los archivos en formato WAV.
	•	Selección de archivos locales: Convierte automáticamente archivos en formatos MP3 o WAV a WAV.
	•	Mejora de calidad: Normaliza el volumen y aplica mejoras para una experiencia de audio más profesional.
	•	Separación de pistas: Usa Demucs para dividir el audio en múltiples componentes.
	•	Opciones interactivas: Interfaz basada en consola para elegir entre diferentes funcionalidades.

Requisitos

	•	Python 3.8 o superior
	•	FFmpeg instalado y accesible desde el sistema
	•	Demucs instalado (instrucciones aquí)
	•	Librerías Python necesarias:
	•	yt-dlp
	•	pydub
	•	librosa
	•	soundfile

Instalación

	1.	Clona este repositorio:

git clone https://github.com/tu-usuario/audio-splitter.git
cd audio-splitter


	2.	Instala las dependencias:

pip install -r requirements.txt


	3.	Asegúrate de que FFmpeg y Demucs están instalados y configurados en tu sistema.

Uso

Ejecuta el programa desde la terminal:

python audio_splitter.py

Sigue las instrucciones interactivas para:
	1.	Descargar música desde YouTube proporcionando una URL.
	2.	Seleccionar un archivo de audio local en formato WAV o MP3.
	3.	Mejorar la calidad del archivo de audio.
	4.	Dividir pistas utilizando Demucs.

Configuración

Variables clave

	•	DOWNLOAD_DIR: Directorio donde se guardan los archivos descargados y procesados. Por defecto, se usa el directorio de descargas del usuario.
	•	FFMPEG_CODEC: Formato de conversión de audio. Por defecto, wav.
	•	DEMUCS_MODEL: Modelo de separación de audio. Por defecto, htdemucs.
	•	DEMUCS_DEVICE: Dispositivo de procesamiento (cpu o cuda para GPU).

Notas

	1.	FFmpeg debe estar correctamente instalado y configurado en tu sistema para garantizar la conversión y exportación de audio.
	2.	Para aprovechar la aceleración por GPU, configura DEMUCS_DEVICE como cuda (requiere que tu sistema sea compatible con CUDA).

Contribuciones

Si deseas contribuir, por favor, crea un fork de este repositorio, realiza los cambios necesarios y envía un pull request. Todas las contribuciones son bienvenidas.

Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

¡Disfruta separando y procesando tu música! 🎵
