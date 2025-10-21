import subprocess
import csv
from datetime import datetime

def run_nslookup(record_type, domain):
    """Menjalankan nslookup untuk tipe record tertentu"""
    try:
        result = subprocess.run(
            ["nslookup", "-type=" + record_type, domain],
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"Error: {e}"

def parse_nslookup_output(output):
    """Menyaring hasil nslookup agar lebih mudah dibaca"""
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    filtered = [line for line in lines if not line.startswith("Server:") and not line.startswith("Address:")]
    return filtered

def save_to_csv(domain, data):
    """Menyimpan hasil lookup ke file CSV"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"dns_lookup_{domain.replace('.', '-')}_{timestamp}.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Record Type", "Result"])
        for record_type, result_lines in data.items():
            writer.writerow([record_type, " | ".join(result_lines)])
    print(f"\n✅ Hasil DNS lookup disimpan ke file: {filename}")

def main():
    domain = input("Masukkan nama domain (contoh: pcr.ac.id): ").strip()
    record_types = ["A", "MX", "NS", "CNAME", "AAAA"]
    all_results = {}

    print(f"\n🔍 Melakukan lookup DNS untuk {domain}...\n")

    for rtype in record_types:
        print(f"--- {rtype} Record ---")
        output = run_nslookup(rtype, domain)
        parsed = parse_nslookup_output(output)
        all_results[rtype] = parsed
        for line in parsed:
            print(line)
        print()

    save_to_csv(domain, all_results)
    print("\nSelesai ✅")

if __name__ == "__main__":
    main()
