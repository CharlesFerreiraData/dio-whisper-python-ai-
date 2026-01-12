# dio-whisper-python-ai-
Projeto de assistente de voz integrando Whisper (STT), ChatGPT e gTTS (TTS)
# 🎙️ Assistente de Voz com IA: Whisper & Python

Este repositório documenta o funcionamento de um assistente de voz inteligente, desenvolvido como um desafio de projeto na DIO.

## 🏗️ Arquitetura da Solução
O sistema funciona como uma linha de montagem dividida em quatro etapas principais:

1. **Captura de Áudio**: O sistema grava a voz do usuário e gera um arquivo digital.
2. **Transcrição (Whisper)**: O modelo Whisper da OpenAI converte as ondas sonoras em texto escrito com alta precisão.
3. **Processamento (ChatGPT)**: O texto transcrito é enviado para a API do ChatGPT, que gera uma resposta lógica e contextual.
4. **Síntese de Voz (gTTS)**: A resposta em texto é convertida novamente em áudio através da biblioteca gTTS (Google Text-to-Speech) para que o usuário ouça a IA.

## 🛠️ Tecnologias Envolvidas
- **Python**: Linguagem de programação para integração.
- **OpenAI Whisper**: Tecnologia de Speech-to-Text.
- **OpenAI ChatGPT**: Modelo de linguagem para o "cérebro" do assistente.
- **gTTS**: Biblioteca para síntese de voz.
