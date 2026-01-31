import requests
import sys
import arg
import os
import json





"""                    sakura downloader
   you need to write here a
   url then it will download it
   if file downloaded search
   it ONLY in CURRENT directory
   also you can customize it
   Legal & Ethical Use
   This tool is a utility for automated file downloading. It is designed to simplify data collection, not to disrupt web services.
   The author is not responsible for any misuse or intentional server overload caused by this software
   
                          sys args
            - --blue  | setting interface as blue
            - --green | setting interface as green
            - --red   | setting interface as red
            - --help  | giving you help
            (maybe new commands soon)
   
   
   file get downloaded by request library
   you need to install it 
   also:
   	      - basic python libs
   	      - tkinter (if i update it (idk)
   if you need to get a FILE
   give a FILE url
   
                  if you need to use it as a lib
                         IMPORT THIS FILE 
                    then call the sakura(<url>)
                    
   if you need a core version
   just call it in code
                       "       end       "
"""
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "conf", "data.json")
print("only for legal use")

with open(file_path, "r") as f:
    pamparam = json.load(f)
if pamparam['browser'] == True:
    headers = {
        'User-Agent-downloader': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Referer': 'https://www.google.com'
    }
else:
    headers = {}
    
def sakura(url):
    try:
        filename = url.split('/')[-1]
        
        # message that we downloading it here
        print(f"[*] downloading {url}...")
        with requests.get(url, stream=True, headers=headers) as r:
            r.raise_for_status()
            # open the file and writing
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
                    sys.stdout.write("■")
        print("")
        # if everything ok this message will pop
        print(f"[+] file downloaded!!")
    except:
        # everything wrong
        print(f"[-] something wrong bro")

def sakura_core(url):
    
    
    """ a core version of func
        you can import this and call it
            - sakura_core(yoururl)
    """
    
    
    try:
        filename = url.split('/')[-1]
        

        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            # open the file and writing
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    except:
        # everything wrong
        sys.exit(1)  
	time.sleep(0.5)
	
""" the main TUI if I
    can call this TUI
"""

if __name__ == "__main__":
    	    """ prints interface """
    	    print ("===================================")
    	    print ('       sakura downloader')
    	    print ('  give me a url and i will load it')
    	    print ("===================================")
    	    url = input ('>>>')
    	    sakura(url)
print ("\033[0m")


    
