def hitung_kondisi_server(suhu: float, beban_cpu: int) -> str:
    """Fungsi dengan Type Hinting untuk mendeteksi kesehatan server."""
    if suhu > 75.0 or beban_cpu > 85:
        return "WARNING: Server Overheat/Overload!"
    return "STATUS: Server Aman."

# Test Drive fungsi
status_saat_ini = hitung_kondisi_server(72.5, 60)