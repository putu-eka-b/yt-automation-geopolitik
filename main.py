import os
import google.generativeai as genai
import asyncio
import edge_tts

# Ambil API Key dari Secrets
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

async def buat_konten():
    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        # Prompt khusus Bodet News
        prompt = "Buat skrip berita geopolitik viral hari ini untuk channel YouTube 'Bodet News'. Gaya tegas, 150 kata. Sertakan ide gambar 3D CGI."
        
        print("Bodet News: Meminta naskah...")
        response = model.generate_content(prompt)
        naskah = response.text
        
        # Simpan file di lokasi yang pasti terdeteksi
        with open("naskah_berita.txt", "w", encoding="utf-8") as f:
            f.write(naskah)
        print("File naskah tersimpan.")

        # Buat Suara
        print("Bodet News: Membuat suara...")
        VOICE = "id-ID-ArdiNeural"
        communicate = edge_tts.Communicate(naskah, VOICE)
        await communicate.save("audio_berita.mp3")
        print("File audio tersimpan.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(buat_konten())
