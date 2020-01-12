import speech_recognition as xx 
import playsound 
from gtts import gTTS 
import os 
from selenium import webdriver 

class Musicroot(object):
    
    def assistant_speaks(output): 
        global num 
        num = 1
        num += 1
        print("Croot : ", output) 
        toSpeak = gTTS(text = output, lang ='id', slow = False) 
        file = str(num)+".mp3"  
        toSpeak.save(file) 
        playsound.playsound(file, True) 
        os.remove(file) 



    def get_audio(): 
        rObject = xx.Recognizer() 
        audio = '' 
        with xx.Microphone() as source: 
            print("Bicara...") 
            audio = rObject.listen(source, phrase_time_limit = 5) 
            print("Stop.") 
        try: 

            text = rObject.recognize_google(audio, language ='id-ID') 
            print("Anda : ", text) 
            return text 

        except: 

            assistant_speaks("tidak jelas") 
            return 0

    


    if __name__ == "__main__": 
        
            assistant_speaks("Nama Anda Siapa ?") 
            name ='Manusia'
            name = get_audio() 
            assistant_speaks("Hallo, " + name + '.') 
            
            while(1): 

                assistant_speaks("Apa yang saya bisa bantu?") 
                text = get_audio().lower() 

                
                if "musik" in str(text) :
                    assistant_speaks("Ok , "+ name+' Membuka mundur alon-alon')
                    options = webdriver.ChromeOptions()
                    driver = webdriver.Chrome(chrome_options=options)
                    driver.get('https://www.youtube.com/watch?v=zCmHodTpt9I')
                    continue
                
                if "lyrics" in str(text) :
                    assistant_speaks("Ok , "+ name+' Membuka lyrics mundur alon-alon')
                    options = webdriver.ChromeOptions()
                    driver = webdriver.Chrome(chrome_options=options)
                    driver.get('https://www.google.com/search?safe=strict&hl=id&sxsrf=ACYBGNQDWNQ0tkOaPmxtoL29VOHZfKTEdw%3A1573181655017&source=hp&ei=1tjEXefEO4eEvQSLj4KwBQ&q=lirik+mundur+alon+alon&oq=l&gs_l=psy-ab.3.0.35i39l2j0i67j0l3j0i67j0i131j0i67l2.26634.26634..28264...0.0..0.705.875.0j1j6-1......0....1..gws-wiz.....10..35i362i39.oUYCZ9a37bg')
                    continue

                if "chrome" in str(text): 
                    assistant_speaks("Ok , "+ name+' Membuka google chrome')
                    os.startfile("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe") 
                    continue
                if "spotify" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka spotify')
                    os.startfile("C:/Users/innal/AppData/Roaming/Spotify/Spotify.exe") 
                    continue

                if "last" in str(text) :
                    assistant_speaks("Ok , "+ name+' Membuka last.fm')
                    options = webdriver.ChromeOptions()
                    driver = webdriver.Chrome(chrome_options=options)
                    driver.get('https://www.last.fm/')
                    driver.get('https://secure.last.fm/login')
                    driver.find_element_by_name('username').send_keys('muchamadinnalk@gmail.com')
                    driver.find_element_by_xpath('//*[@id="id_password"]').send_keys('samsung123!')
                    driver.get("https://www.last.fm/search")
                    driver.find_element_by_link_text('Search').send_keys("noah")
                    driver.find_element_by_class_name('search-submit').click()
                    driver.get('https://www.last.fm/music/Noah')
                    continue
                if "download" in str(text) :
                    assistant_speaks("Ok , "+ name+' Membuka last.fm')
                    options = webdriver.ChromeOptions()
                    driver = webdriver.Chrome(chrome_options=options)
                    driver.get("https://www.google.com/")
                    driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input").send_keys('download musik mp3')
                    driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div.A8SBwf > div.FPdoLc.tfB0Bf > center > input.gNO89b").click()
                    continue

                if "mundur" in str(text): 
                    assistant_speaks("Ok , "+ name+' membuka mundul alon-alon')
                    os.startfile("C:/Download/Compressed/Video/MUNDUR ALON ALON - ILUX ID (OFFICIAL VIDEO) - YouTube.mp4") 
                    continue
       
                if "djremix" in str(text): 
                    assistant_speaks("Ok , "+ name+' Membuka djremix')
                    os.startfile("C:/Download/Compressed/Video/DJ SLOW SALAH APA AKU REMIX 2019 (VERSI GAGAK) - YouTube.mkv")
                    continue
        
                if "pamer bojo" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka pamer bojo')
                    os.startfile("C:/Download/Compressed/Video/Nella Kharisma Pamer Bojo Versi Cendol Dawet - YouTube.mkv")
                    continue
                
                if "cendol dawet" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka cendol dawet')
                    os.startfile("C:/Download/Compressed/Video/videoplayback.mkv")
                    continue
       
                if "dj dimatamu" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka dj dimatamu')
                    os.startfile("C:/Download/Compressed\Video/DJ Dimatamu - Original Remix Terbaru Full Bass 2019 - YouTube.mkv")
                    continue
       
    
                if "kopi dangdut" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka kopi dangdut')
                    os.startfile("C:\\/Download/Compressed/Video/Fahmi Shahab - Kopi Dangdut [Official] - YouTube.mkv")
                    continue
       
    
                if "korban janji" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka korban janji')
                    os.startfile("C:/Download/Compressed/Video/GuyonWaton Official - Korban Janji (Official Music Video) - YouTube.mp4")       
                    continue
    
                if "medot janji" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka medot janji')
                    os.startfile("C:\Download\Compressed\Video\Lirik lagu Kartonyono Medot Janji - Denny Caknan - YouTube.mkv")
                    continue
       
                if "sayang" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka sayang')
                    os.startfile("C:/Download/Compressed/Video/Nella Kharisma - Sayang 2 [OFFICIAL] - YouTube.mkv")
                    continue
       
    
                if "lintang ati" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka lintang ati')
                    os.startfile("C:/Download/Compressed/Video/Nella Kharisma Pamer Bojo Versi Cendol Dawet - YouTube.mkv")
                    continue
       
    
                if "alon-alon" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka alon-alon')
                    os.startfile("C:/Download/Music/MUNDUR ALON ALON - ILUX ID (OFFICIAL VIDEO).mp3")
                    continue
       
    
                if "lil" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka lil nas x')
                    playsound.playsound('C:/Download/Music/Lil Nas X - Old Town Road (feat. Billy Ray Cyrus) Remix.mp3')
                    continue
       
    
                if "memori" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka memori')
                    playsound.playsound('C:/Download/Music/Maroon 5 - Memories.mp3')
                    continue
       
    
                if "senorita" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka senorita')
                    playsound.playsound('C:/Download/Music/Shawn Mendes, Camila Cabello - Señorita.mp3')
                    continue
       
    
                if "cendol" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka cendol dawet')
                    playsound.playsound('C:/Download/Music/Nella Kharisma Pamer Bojo Versi Cendol Dawet.mp3')
                    continue
       
                if "Lay-Lay" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka lay-lay')
                    playsound.playsound('C:/Download/Music/DJ LAY LAY LAY ( JOKER ) FULL BASS TERBARU 2019.mp3')
                    continue
                
                if "Tik-Tok" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka tik-tok')
                    playsound.playsound('C:/Download/Music/DJ Tik Tok Viral 2019Lagu Tik Tok Remix Terbaru 2019.mp3')
                    continue
                
                if "perfect" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka perfect')
                    playsound.playsound('C:/Download/Music/Ed Sheeran - Perfect (Official Music Video).mp3')
                    continue
                
                if "i love you" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka i love you')
                    playsound.playsound('C:/Download/Music/Stephanie Poetri - I Love You 3000 (Official Music Video).mp3')
                    continue

                if "dawet" in str(text):
                    assistant_speaks("Ok , "+ name+' Membuka cendol dawet')
                    playsound.playsound('C:/Download/Music/koplo Cendol Dawet .mp3')
                    continue

                if "keluar" in str(text) or "dadah" in str(text) or "udahan" in str(text): 
                    assistant_speaks("Ok dadah, "+ name+'.') 
                    break
