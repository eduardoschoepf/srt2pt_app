import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from googletrans import Translator

# Caminho do arquivo SRT na mesma pasta que o script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRT_FILE = os.path.join(SCRIPT_DIR, "legenda_original.srt")
TRANSLATED_FILE = SRT_FILE.replace(".srt", "_traduzido.srt")

translator = Translator()

class SRTTranslator(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == SRT_FILE:
            translate_srt()

def translate_srt():
    with open(SRT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    translated_lines = []
    for line in lines:
        if "-->" in line or line.strip().isdigit() or line.strip() == "":
            translated_lines.append(line)
        else:
            translated_text = translator.translate(line, src="en", dest="pt").text
            translated_lines.append(translated_text + "\n")

    with open(TRANSLATED_FILE, "w", encoding="utf-8") as f:
        f.writelines(translated_lines)

    print(f"Arquivo traduzido salvo em: {TRANSLATED_FILE}")

# Monitorar mudanças no arquivo
event_handler = SRTTranslator()
observer = Observer()
observer.schedule(event_handler, path=SCRIPT_DIR, recursive=False)
observer.start()

print("Monitorando o arquivo SRT para tradução...")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
