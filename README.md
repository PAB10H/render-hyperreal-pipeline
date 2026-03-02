# 🎬 Render Hyperreal Pipeline

**Pipeline profissional para processamento sequencial de imagens de render arquitetônico com ChatGPT**

## 🎯 O Que Faz

✅ Lê imagens de `/input`  
✅ Envia para seu **GPT customizado** (análise técnica)  
✅ Gera **prompt hiper-realista** avançado  
✅ Gera imagem melhorada via **ChatGPT Go**  
✅ **Controle de qualidade** automático  
✅ **Comparação side-by-side** (original vs melhorado)  
✅ Salva **metadados em JSON**  
✅ Log detalhado em terminal  

---

## 📋 Requisitos

- Python 3.9+
- Links públicos dos seus chats (GPT customizado + ChatGPT Go)
- Dependências em `requirements.txt`

---

## 🚀 Instalação Rápida

### 1. Clonar repositório
```bash
git clone https://github.com/PAB10H/render-hyperreal-pipeline.git
cd render-hyperreal-pipeline
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Configurar ambiente
```bash
cp .env.example .env
# Editar .env com seus links
```

### 4. Criar estrutura de pastas
```bash
mkdir -p input output/processed output/comparisons
```

### 5. Adicionar imagens
Coloque suas imagens de render em `/input`

### 6. Rodar pipeline
```bash
python main.py
```

---

## 📁 Estrutura de Arquivos

```
render-hyperreal-pipeline/
├── main.py                 # Orquestração principal
├── gpt_analyzer.py        # Análise com GPT customizado
├── image_generator.py     # Geração via ChatGPT Go
├── quality_check.py       # Validação de qualidade
├── comparator.py          # Criação de comparações
├── requirements.txt       # Dependências Python
├── .env.example          # Template de configuração
├── README.md             # Este arquivo
├── input/                # Suas imagens (input)
├── output/
│   ├── processed/        # Imagens melhoradas
│   ├── comparisons/      # Comparações lado a lado
│   └── pipeline.log      # Log de execução
```

---

## ⚙️ Arquitetura

### Pipeline Sequencial (uma imagem por vez)

```
1. ANÁLISE
   ↓
2. GERAÇÃO DE PROMPT
   ↓
3. GERAÇÃO DE IMAGEM
   ↓
4. CONTROLE DE QUALIDADE
   ↓
5. COMPARAÇÃO LADO A LADO
   ↓
6. SALVAMENTO DE METADADOS
```

---

## 🔧 Configuração de Links

### Seu GPT Customizado
1. Crie um GPT customizado em https://chatgpt.com/gpts
2. Configure instruções para análise técnica de renders
3. Copie o link público (ex: `https://chatgpt.com/g/g-abc123...`)
4. Cole em `.env` como `GPT_ANALYZER_LINK`

### ChatGPT Go (Geração de Imagens)
1. Acesse https://chatgpt.com
2. Copie o link
3. Cole em `.env` como `CHATGPT_GO_LINK`

---

## 📊 Output

Cada imagem processada gera:

```
output/
├── processed/
│   ├── generated_20260302_150000.png      # Imagem melhorada
│   └── original_metadata.json             # Dados técnicos
└── comparisons/
    └── original_comparison.png            # Before/After
```

**Metadados JSON inclui:**
- Timestamp de processamento
- Análise técnica completa
- Resultado do controle de qualidade
- Prompt utilizado

---

## 🔥 Recursos Avançados

### Regeneração Automática
Se a qualidade não passar:
- Ajusta prompt automaticamente
- Regenera imagem
- Reavalia qualidade
- Máximo de tentativas: 3

### Logs Detalhados
```
✅ Pipeline inicializado
🖼️  PROCESSANDO: image1.png
📊 Realism Score: 7/10
[1/6] 🧠 Analisando imagem...
...
✨ IMAGEM PROCESSADA COM SUCESSO!
```

---

## 💡 Dicas

- **Primeira execução**: May levar tempo (Playwright precisa baixar navegador)
- **Imagens grandes**: Redimensiona automaticamente para 800x600
- **Múltiplas imagens**: Processa sequencialmente (não em paralelo)
- **Erros de conexão**: Verifica links nos `.env`

---

## 📝 Licença

MIT License - veja LICENSE.md

---

## 👤 Autor

**PAB10H** - 2026

---

**Pronto para uso! 🚀**