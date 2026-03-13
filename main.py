import os
import google.generativeai as genai
import asyncio
import edge_tts

# Ambil API Key dari Secrets
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

async def buat_konten():
    # Prompt berita geopolitik
    prompt = "Buat skrip berita geopolitik dunia viral hari ini, durasi 1 menit, judul clickbait, dan prompt gambar 3D CGI sinematik."
    
    response = model.generate_content(prompt)
    naskah = response.text
    
    # Simpan naskah
    with open("naskah_berita.txt", "w") as f:
        f.write(naskah)

    # Buat Audio (Suara Indonesia Ardi)
    VOICE = "id-ID-ArdiNeural"
    communicate = edge_tts.Communicate(naskah[:500], VOICE)
    await communicate.save("audio_berita.mp3")

if __name__ == "__main__":
    asyncio.run(buat_konten())
