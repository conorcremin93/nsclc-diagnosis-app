# 🧠 NSCLC Diagnosis Classification App

## Overview

This project enables secure, offline classification of non-small cell lung cancer (NSCLC) from patient lab reports using local LLM inference. The app supports running different quantized versions of the **Mistral-7B-Instruct-v0.1** model via `llama-cpp-python` in a Trusted Research Environment (TRE).

---

## 🔍 Objective

Classify patient reports into the following categories:

- `Definite`
- `Likely`
- `Uncertain`
- `Unlikely`

Each result is accompanied by a one-sentence justification extracted directly from the model output.

---

## 📁 Directory Structure

nsclc_diagnosis_app/
│
├── data/ # Input Excel or CSV files with patient lab reports
├── models/
│ └── mistral-gguf/ # Contains quantized .gguf models (e.g., Q4_K_M)
├── notebooks/
│ ├── nsclc_classification_optimized.ipynb # Main notebook for classification
│ └── test_single_model_debug.py # Script for debugging single models
│
├── outputs/ # All output results (CSV, JSONL, XLSX)
├── setup/
│ ├── venv/ # Python virtual environment (excluded from version control)
│ └── requirements.txt # All Python packages required
├── README.md # You are here
├── Dockerfile # 🔧 Containerized build definition
└── .gitignore # Standard Python ignores

---

## 🐳 Docker Setup

```bash
# 1. Build the image
docker build -t nsclc-diagnosis .

# 2. Run the app in CLI mode
docker run --rm -v $(pwd):/app nsclc-diagnosis

# 3. (Optional) Start Jupyter Notebook
docker run -p 8888:8888 -v $(pwd):/app nsclc-diagnosis jupyter notebook --ip=0.0.0.0 --allow-root
```
---

## 🛠️ Installation & Setup

### 1. Create Environment

```bash
python -m venv setup/venv
source setup/venv/bin/activate        # Linux/macOS
.\setup\venv\Scripts\activate         # Windows
```
### 2. Install Packages (If not using Docker)

Install all required and optional packages from the ```bash requirements.txt```:
```bash
pip install -r requirements.txt
```

### 3. Download Model

Use Hugging Face CLI to download the model:
```bash
pip install huggingface_hub

huggingface-cli login   # Use a token with access to Mistral-7B-Instruct-v0.1
huggingface-cli download --resume-download \
  mistralai/Mistral-7B-Instruct-v0.1 \
  --local-dir ./models/mistral-gguf \
  --local-dir-use-symlinks False
```
Place .gguf files inside ```bash ./models/mistral-gguf/```.

---

## 📊 Usage

### Run the Notebook

Launch the Jupyter interface:
```bash
jupyter lab
```
Open ```bash ./notebooks/nsclc_classification_optimized.ipynb``` and run all cells. This will:

- Load reports from ```bash ./data/nsclc_patient_reports.xlsx```
- Chunk long reports to fit model context
- Run inference with Mistral GGUF model
- Parse structured JSON results
- Export predictions to:
   - ```bash ./outputs/nsclc_llm_results_chunked.csv```
   - ```bash ./outputs/nsclc_llm_results_chunked.xlsx```
   - ```bash ./outputs/nsclc_llm_results_chunked.jsonl```

### Example Output:
| PatientID | NSCLC\_Status | Justification                                                       |
| --------- | ------------- | ------------------------------------------------------------------- |
| P001      | Likely        | The presence of a 3.5cm mass and biopsy confirmation suggest NSCLC. |
| P002      | Uncertain     | Findings are inconclusive and further scans are required.           |

---

## ⚡ Performance
The notebook uses:
- Multithreading via ```bash ThreadPoolExecutor``` for faster batch processing
- Optimized prompt chunking with defined character limits
- Local inference via ```bash llama-cpp-python``` for TRE security

---

## 🔍 Troubleshooting
ParseError: The model did not return valid JSON. Check the prompt or temperature.

Long Reports: These are chunked automatically with results aggregated by certainty.

Token Limit: Keep chunks within 2k–4k characters depending on quantization level.

---

## ✅ Requirements
### Core
- llama-cpp-python
- pandas
- openpyxl
- tqdm

### Optional Enhancements
- nltk, scikit-learn, huggingface_hub, matplotlib, seaborn, spacy, scispacy

See requirements.txt for full details.

---

## 🔐 Secure Usage in TRE
- No internet connection is needed after model download
- No external APIs used
- Compatible with air-gapped systems

---

## 👤 Author
Dr. Conor Cremin, PhD
📧 ccremin@doh.gov.ae

---

## 🧪 Future Extensions
- Add model benchmarking between quantized variants
- Incorporate medical NER tools (e.g., medspacy) for preprocessing
- Expand classification to include NSCLC subtypes or staging

---