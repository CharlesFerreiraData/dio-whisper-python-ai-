import openai
from gtts import gTTS
import os

# 1. Simulação de Transcrição com Whisper
# O Whisper "ouviria" o arquivo de áudio e transformaria em texto
pergunta_usuario = "O que é Deep Learning?" 

# 2. Envio para o ChatGPT
# Resposta gerada pela IA
resposta_ai = "Deep Learning é um subcampo do Machine Learning baseado em redes neurais."

# 3. Conversão de Texto para Voz (gTTS)
audio_resposta = gTTS(text=resposta_ai, lang='pt')
audio_resposta.save("resposta.mp3")

# 4. "Fala" (Reproduz o áudio)
os.system("start resposta.mp3")
