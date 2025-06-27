# ✅ API Vulnerability Findings Validator

# Deskripsi (🇮🇩 INDONESIA)
Take-home test dari Plexicus. 
Tujuannya adalah untuk memvalidasi hasil temuan kerentanan keamanan pada API yang diekspor dalam format SARIF (`findings.json`).

Terdapat dua metode validasi yang tersedia:

1. **BDD (Behavior-Driven Development)** menggunakan `behave`, lengkap dengan laporan HTML.
2. **Skrip Python sederhana (`validator.py`)** untuk validasi langsung via terminal.

---

### 🎯 Validasi yang Diperiksa

- File `findings.json` harus berisi tepat **6 temuan**.
- Harus ada satu temuan terkait **SQL Injection** dengan kriteria:
  - `ruleId`: `php.lang.security.injection.tainted-sql-string.tainted-sql-string`
  - Level: `error`
  - Security severity: di atas 8.0
  - Pemilik isu: `tmalbos`
  - Berkas terkait: `index.php`
- Semua temuan dengan `ruleId` yang berkaitan dengan `package.json` harus dimiliki oleh **Jose**.

---

### 🧪 Cara Menjalankan Validasi

#### ✅ Opsi 1: Jalankan dengan `behave` (BDD)

1. Buat dan aktifkan virtual environment:

    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

2. Instal dependensi:

    ```bash
    pip install behave behave-html-formatter
    ```

3. Jalankan pengujian:

    ```bash
    behave
    ```

4. (Opsional) Buat laporan HTML:

    ```bash
    behave -f behave_html_formatter:HTMLFormatter -o report.html
    start report.html
    ```

---

#### ✅ Opsi 2: Jalankan Skrip Python Langsung

Jika ingin validasi cepat tanpa BDD, cukup jalankan:

```bash
python validator.py
```

---
---
## Description (🇬🇧 ENGLISH)

Take-home test project from Plexicus.  
The goal is to validate the exported API security vulnerability findings in SARIF format (`findings.json`).

This project provides two validation methods:

1. **BDD (Behavior-Driven Development)** using `behave`, with HTML report output.
2. **Simple Python script (`validator.py`)** for direct validation from terminal.

---

### 🎯 Validation Rules

- The `findings.json` file must contain exactly **6 findings**.
- There must be one **SQL Injection** finding with the following criteria:
  - `ruleId`: `php.lang.security.injection.tainted-sql-string.tainted-sql-string`
  - Level: `error`
  - Security severity: greater than 8.0
  - Issue owner: `tmalbos`
  - Related file: `index.php`
- All findings with a `ruleId` related to `package.json` must be owned by **Jose**.

---

### 🧪 How to Run the Validation

#### ✅ Option 1: Use `behave` (BDD)

1. Create and activate a virtual environment:

    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

2. Install dependencies:

    ```bash
    pip install behave behave-html-formatter
    ```

3. Run the tests:

    ```bash
    behave
    ```

4. (Optional) Generate HTML report:

    ```bash
    behave -f behave_html_formatter:HTMLFormatter -o report.html
    start report.html
    ```

---

#### ✅ Option 2: Run Python Script Directly

If you prefer a quicker validation without BDD:

```bash
python validator.py
```
