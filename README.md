# Rental Agreement Metadata Extraction System

## Project Overview

This project is an AI-powered metadata extraction system that automatically extracts structured information from rental agreement documents.

The system supports both editable DOCX files and scanned image documents (PNG, JPG, JPEG). Depending on the uploaded file type, the system either extracts text directly using python-docx or performs Optical Character Recognition (OCR) using PaddleOCR.

The extracted text is then processed by Google's Gemini Large Language Model (LLM), which identifies and extracts predefined metadata fields from the rental agreement.

The extracted metadata is displayed through a Streamlit dashboard and can be exported as JSON and CSV for further analysis and evaluation.

---

## Problem Statement

Rental agreements often exist in multiple formats and contain unstructured text. Manually extracting key information from these documents is time-consuming and error-prone.

The objective of this project is to automatically extract the following metadata fields:

- Agreement Value
- Agreement Start Date
- Agreement End Date
- Renewal Notice Period (Days)
- Party One (Landlord)
- Party Two (Tenant)

The solution must use an LLM-based extraction approach rather than rule-based methods.

---

## Solution Approach

The system follows a two-stage pipeline:

### Stage 1: Text Extraction

#### DOCX Documents

- Parsed using `python-docx`
- Text extracted directly from the document

#### Scanned Images

- Processed using `PaddleOCR`
- Image converted into machine-readable text

### Stage 2: Metadata Extraction

- Extracted text is passed to Google Gemini
- Prompt engineering is used to guide metadata extraction
- Gemini returns structured JSON containing required fields

---

## System Architecture

<p align="center">
  <img src="system_arch.png" width="800">
</p>

---

## Technology Stack

| Component            | Technology              |
| -------------------- | ----------------------- |
| Frontend             | Streamlit               |
| OCR Engine           | PaddleOCR               |
| Document Parsing     | python-docx             |
| LLM                  | Google Gemini 2.5 Flash |
| Data Processing      | Pandas                  |
| Evaluation           | Custom Recall Metrics   |
| Programming Language | Python                  |

---

## Project Structure

```text
metadata_extractor/

├── app.py
├── generate_predictions.py
├── evaluate.py
├── requirements.txt
├── README.md

├── src/
│   ├── document_processor.py
│   ├── docx_parser.py
│   ├── ocr_engine.py
│   ├── llm_extractor.py
│   ├── evaluator.py
│   ├── normalizer.py
│   ├── models.py
│   └── utils.py

├── data/
│   ├── train/
│   ├── test/
│   ├── train.csv
│   └── test.csv

├── predictions/
│   └── predictions.csv
```

---

## Metadata Fields Extracted

| Field                | Description                              |
| -------------------- | ---------------------------------------- |
| agreement_value      | Monthly rental amount                    |
| agreement_start_date | Agreement start date                     |
| agreement_end_date   | Agreement end date                       |
| renewal_notice_days  | Notice period before termination/renewal |
| party_one            | Landlord / Owner                         |
| party_two            | Tenant / Lessee                          |

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd metadata_extractor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Application

### Launch Streamlit Dashboard

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Generate Batch Predictions

```bash
python generate_predictions.py
```

Output:

```text
predictions/predictions.csv
```

---

## Evaluate Predictions

```bash
python evaluate.py
```

---

## Evaluation Methodology

The system is evaluated using **Field-Level Recall**.

### Recall Formula

```text
Recall = Correct Extractions / Total Ground Truth Records
```

Normalization is applied before comparison to ensure fair evaluation.

### Normalizations Performed

- Date Normalization
- Party Name Normalization
- Notice Period Normalization

---

## Experimental Results

| Field                 | Recall |
| --------------------- | ------ |
| Agreement Value       | 75%    |
| Agreement Start Date  | 100%   |
| Agreement End Date    | 75%    |
| Renewal Notice (Days) | 0%     |
| Party One             | 100%   |
| Party Two             | 75%    |

### Overall Recall

```text
75%
```

---

## Challenges Faced

### OCR Noise

Scanned agreements often contain noise, skew, and formatting inconsistencies that impact extraction quality.

### Multiple Monetary Values

Rental agreements frequently contain rent amounts, deposits, and advance payments. Distinguishing the actual rental value requires contextual understanding.

### Date Format Variations

Different agreements use varying date formats, requiring normalization before evaluation.

### Name Variations

Party names often include prefixes such as:

- Mr.
- Mrs.
- Sri

Normalization was implemented to improve matching accuracy.

### Renewal Notice Extraction

Distinguishing notice periods from rent increase percentages remains a challenging extraction task.

---

## Future Improvements

- Improved renewal notice extraction
- PDF document support
- Multi-page document handling
- Batch processing dashboard
- Multiple LLM provider support
- Docker deployment
- Precision and F1-score evaluation
- Human-in-the-loop verification

---

## Conclusion

This project demonstrates an end-to-end AI-powered document understanding pipeline combining OCR, document parsing, prompt engineering, and Large Language Models to automate metadata extraction from rental agreements.

The solution successfully processes both structured and scanned documents and produces machine-readable outputs suitable for downstream business workflows and analytics.
