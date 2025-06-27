import json
import os

def load_findings(path):
    full_path = os.path.join("data", path)
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data['runs'][0]['results']
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ File tidak ditemukan: {full_path}")
    except Exception as e:
        raise RuntimeError(f"❌ Gagal memuat file: {e}")

def validate_findings(results):
    print("▶ Memulai proses validasi...")

    # 1. Jumlah findings harus 6
    assert len(results) == 6, f"❌ Jumlah temuan tidak sesuai (ditemukan {len(results)})."
    print("✅ Validasi jumlah temuan: 6")

    # 2. Validasi SQL Injection (ruleId tertentu)
    sql_rule_id = "php.lang.security.injection.tainted-sql-string.tainted-sql-string"
    sql_findings = [r for r in results if r['ruleId'] == sql_rule_id]
    assert sql_findings, "❌ Tidak ditemukan temuan dengan ruleId SQL Injection."
    sql = sql_findings[0]

    assert sql['level'] == "error", f"❌ Level tidak sesuai (ditemukan: {sql['level']})."
    print("✅ Level SQL Injection: error")

    severity = float(sql['properties'].get('security-severity', 0))
    assert severity > 8.0, f"❌ Severity tidak cukup tinggi (ditemukan: {severity})."
    print(f"✅ Security Severity SQL Injection: {severity} (> 8.0)")

    owner = sql['properties'].get('issue_owner')
    assert owner == "tmalbos", f"❌ Issue owner salah (ditemukan: {owner})."
    print("✅ Issue Owner SQL Injection: tmalbos")

    file_path = sql['locations'][0]['physicalLocation']['artifactLocation']['uri']
    assert "index.php" in file_path, f"❌ File tidak sesuai (ditemukan: {file_path})."
    print("✅ Lokasi file SQL Injection: index.php")

    # 3. Validasi semua findings dengan ruleId package.json harus dimiliki Jose
    npm_rule_id = "json.npm.security.package-dependencies-check.package-dependencies-check"
    npm_findings = [r for r in results if r['ruleId'] == npm_rule_id]
    assert npm_findings, "❌ Tidak ditemukan temuan terkait package.json"

    for i, finding in enumerate(npm_findings):
        owner = finding['properties'].get('issue_owner')
        assert owner == "Jose", f"❌ Issue owner pada finding #{i+1} bukan Jose (ditemukan: {owner})"
    print(f"✅ Semua {len(npm_findings)} temuan package.json dimiliki oleh Jose")

    print("\n🎉 Semua validasi berhasil!")

if __name__ == "__main__":
    findings = load_findings("findings.json")
    validate_findings(findings)
