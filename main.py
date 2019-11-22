import speech_recognition as sr 
import playsound 
from gtts import gTTS 
import os 
import wolframalpha 
from selenium import webdriver 


num = 1
def assistant_speaks(output): 
	global num 

	# num to rename every audio file 
	# with different name to remove ambiguity 
	num += 1
	print("Croot : ", output) 

	toSpeak = gTTS(text = output, lang ='en', slow = False) 
	# saving the audio file given by google text to speech 
	file = str(num)+".mp3"  
	toSpeak.save(file) 
	
	# playsound package is used to play the same file. 
	playsound.playsound(file, True) 
	os.remove(file) 



def get_audio(): 

	rObject = sr.Recognizer() 
	audio = '' 

	with sr.Microphone() as source: 
		print("Speak...") 
		
		# recording the audio using speech recognition 
		audio = rObject.listen(source, phrase_time_limit = 5) 
	print("Stop.") # limit 5 secs 

	try: 

		text = rObject.recognize_google(audio, language ='en-US') 
		print("You : ", text) 
		return text 

	except: 

		assistant_speaks("Could not understand your audio, PLease try again !") 
		return 0



# Driver Code 
if __name__ == "__main__": 
	assistant_speaks("What's your name, Human?") 
	name ='Human'
	name = get_audio() 
	assistant_speaks("Hello, " + name + '.') 
	
	while(1): 

		assistant_speaks("What can i do for you?") 
		text = get_audio().lower() 

		
		if "music" in str(text) :
			assistant_speaks("Ok , "+ name+' opening mundur alon-alon')
			options = webdriver.ChromeOptions()
			driver = webdriver.Chrome(chrome_options=options)
			driver.get('https://www.youtube.com/watch?v=zCmHodTpt9I')
			continue
		
		if "lyrics" in str(text) :
			assistant_speaks("Ok , "+ name+' opening lyrics mundur alon-alon')
			options = webdriver.ChromeOptions()
			driver = webdriver.Chrome(chrome_options=options)
			driver.get('https://www.google.com/search?safe=strict&hl=id&sxsrf=ACYBGNQDWNQ0tkOaPmxtoL29VOHZfKTEdw%3A1573181655017&source=hp&ei=1tjEXefEO4eEvQSLj4KwBQ&q=lirik+mundur+alon+alon&oq=l&gs_l=psy-ab.3.0.35i39l2j0i67j0l3j0i67j0i131j0i67l2.26634.26634..28264...0.0..0.705.875.0j1j6-1......0....1..gws-wiz.....10..35i362i39.oUYCZ9a37bg')
			continue

		if "chrome" in str(text): 
			assistant_speaks("Ok , "+ name+' opening google chrome')
			os.startfile("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe") 
			continue
		if "spotify" in str(text):
			assistant_speaks("Ok , "+ name+' opening spotify')
			os.startfile("C:/Users/innal/AppData/Roaming/Spotify/Spotify.exe") 
			continue

		if "last" in str(text) :
			assistant_speaks("Ok , "+ name+' opening lyrics mundur alon-alon')
			options = webdriver.ChromeOptions()
			driver = webdriver.Chrome(chrome_options=options)
			driver.get('https://www.last.fm/')
			driver.get('https://secure.last.fm/login')
			driver.find_element_by_name('username').send_keys('muchamadinnalk@gmail.com')
			driver.find_element_by_name('password').send_keys('samsung123!')
			driver.get("https://www.last.fm/search")
			driver.find_element_by_class_name('search-field').send_keys("noah")
			driver.find_element_by_class_name('search-submit').click()
			driver.get('https://www.last.fm/music/Noah')
			continue

		if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
			assistant_speaks("Ok bye, "+ name+'.') 
			break

		# calling process text to process the query 
		#process_text(text) 
