# Tradutor Automático de Legendas (SRT)

Este script monitora alterações em um arquivo de legenda `.srt` e automaticamente traduz seu conteúdo de inglês para português utilizando o Google Translate. O arquivo traduzido é salvo com um novo nome, acrescido de `_traduzido` no final.

## Funcionalidades

- Monitoramento contínuo de alterações no arquivo de legenda original.
- Tradução automática de todas as linhas de texto (exceto os tempos e identificadores de linha) do inglês para o português.
- Salvamento do arquivo traduzido com um novo nome (ex: `legenda_original_traduzido.srt`).

## Requisitos

- Python 3.x
- Bibliotecas: `watchdog`, `googletrans==4.0.0-rc1`

## Instalação

1. **Clone este repositório** ou faça o download do código.
2. **Instale as dependências** usando o `pip`:

   ```bash
   pip install watchdog googletrans==4.0.0-rc1
