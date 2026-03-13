import os
import google.generativeai as genai
import asyncio
import edge_tts

# Ambil API Key dari Secrets GitHub
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

async def buat_konten():
    try:
        # Pakai model latest biar lancar
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        # Prompt khusus channel Bodet News
        prompt = (
            "Buat skrip berita geopolitik viral hari ini untuk channel YouTube 'Bodet News'. "
            "Gaya tegas dan informatif. Panjang 150 kata. "
            "Sertakan ide prompt gambar 3D CGI sinematik di akhir."
        )
        
        print("Bodet News: Memanggil Gemini...")
        response = model.generate_content(prompt)
        naskah = response.text
        
        with open("naskah_berita.txt", "w") as f:
            f.write(naskah)

        # Buat Suara Indonesia (Ardi)
        print("Bodet News: Membuat suara...")
        VOICE = "id-ID-ArdiNeural"
        communicate = edge_tts.Communicate(naskah, VOICE)
        await communicate.save("audio_berita.mp3")
        print("Berhasil! File Bodet News siap.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(buat_konten())
