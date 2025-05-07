import os
import uuid
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play
from elevenlabs import VoiceSettings

load_dotenv()

client = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

def text_to_speech_file(text: str) -> str:
    # Convertir texto a voz usando ElevenLabs API
    response = client.text_to_speech.convert(
        text=text,
        voice_id="knrPHWnBmmDHMoiMeP3l",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
        # Parámetros opcionales para personalizar la voz
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.75,
            style=0.0,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )

    # Generar un nombre de archivo único
    save_file_path = f"{uuid.uuid4()}.mp3"

    # Escribir el audio en un archivo
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: ¡El archivo de audio se guardó exitosamente!")

    # Devolver la ruta del archivo guardado
    return save_file_path

# Ejemplo de uso
if __name__ == "__main__":
    texto = "¡Parce, claro que sí! Aquí en Medellín, cualquier tiendita de la esquina tiene. Pero si querés algo más sabrosón, date una vuelta por El Poblado, ahí venden unos chocolates que hasta me hacen decir “¡ho ho ho, qué delicia!”"
    
    # Guardar el audio en un archivo
    archivo_audio = text_to_speech_file(texto)
    
    # Opcionalmente, reproducir el audio guardado
    with open(archivo_audio, "rb") as f:
        audio_data = f.read()
        play(audio_data)
