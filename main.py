import os
import google.generativeai as genai
import asyncio
import edge_tts

# Ambil API Key dari Secrets
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

async def buat_konten():
    try:
        # Gunakan model Flash terbaru yang punya akses informasi luas
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        # PROMPT ini menyuruh Gemini mencari berita terbaru
        prompt = (
            "Cari berita geopolitik internasional paling viral dan terbaru dalam 24 jam terakhir. "
            "Berdasarkan berita tersebut, buatkan skrip video pendek untuk channel YouTube 'Bodet News'. "
            "Gaya bahasa: Tegas, dramatis, dan informatif. "
            "Panjang: 150 kata. Sertakan judul yang clickbait tapi jujur."
        )
        
        print("Bodet News: Sedang riset berita terbaru lewat Gemini...")
        response = model.generate_content(prompt)
        naskah = response.text
        
        # Simpan naskah
        with open("naskah_berita.txt", "w", encoding="utf-8") as f:
            f.write(naskah)
        print("Riset selesai, naskah disimpan.")

        # Buat Suara
        print("Bodet News: Menghasilkan suara Ardi...")
        VOICE = "id-ID-ArdiNeural"
        communicate = edge_tts.Communicate(naskah, VOICE)
        await communicate.save("audio_berita.mp3")
        print("Suara berhasil dibuat!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(buat_konten())
