# ✅ API Vulnerability Findings Validator

# Deskripsi (🇮🇩 INDONESIA)
Take-home test dari Plexicus. 
Tujuannya adalah untuk memvalidasi hasil temuan kerentanan keamanan pada API yang diekspor dalam format SARIF (`findings.json`).

Terdapat tiga metode validasi yang tersedia:

1. **BDD (Behavior-Driven Development)** menggunakan `behave`, lengkap dengan laporan HTML.
2. **Skrip Python sederhana (`validator.py`)** untuk validasi langsung via terminal.
3. **Automation menggunakan Robot Framework** untuk pengujian otomatis berbasis keyword.

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

#### ✅ Opsi 3: Jalankan dengan Robot

1. Buat dan aktifkan virtual environment:

    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

2. Instal dependensi:

    ```bash
    pip install robotframework
    ```

3. Jalankan pengujian:

    ```bash
    robot robot/ValidateSARIFFindings.robot
    ```
---
---

# Description (🇬🇧 ENGLISH)

This project is a take-home test from Plexicus.  
The goal is to validate security vulnerability findings exported in SARIF format (`findings.json`) from an API scan.

There are three available validation methods:

1. **BDD (Behavior-Driven Development)** using `behave`, complete with HTML reporting.
2. **Simple Python script (`validator.py`)** for quick terminal-based validation.
3. **Automation using Robot Framework**, with keyword-driven testing.

---

### 🎯 What Is Being Validated?

- The `findings.json` file must contain exactly **6 findings**.
- There must be one **SQL Injection** finding with the following criteria:
  - `ruleId`: `php.lang.security.injection.tainted-sql-string.tainted-sql-string`
  - Level: `error`
  - Security severity: greater than 8.0
  - Issue owner: `tmalbos`
  - Related file: `index.php`
- All findings with `ruleId` related to `package.json` must be owned by **Jose**.

---

### 🧪 How to Run the Validation

#### ✅ Option 1: Run with `behave` (BDD)

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

If you prefer fast validation without BDD:

```bash
python validator.py
```

---

#### ✅ Option 3: Run with Robot Framework

1. Create and activate a virtual environment:

    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```

2. Install dependencies:

    ```bash
    pip install robotframework
    ```

3. Run the Robot Framework test suite:

    ```bash
    robot robot/ValidateSARIFFindings.robot
    ```