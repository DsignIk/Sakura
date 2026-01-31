import tkinter as tk
root = tk.Tk()
root.withdraw() 

import requests 
import time
""" 
   if you need only a lib
   you can go here
   also:
       - its have messages
       - error
       - success
 
"""

print ("[*] sakura")

def sakura_core(url):
    
    
    """ a lib version
        of a sakura
    """
    
    
    try:
        filename = url.split('/')[-1]
        

        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            # open the file and writing
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
                    
            """ showing the message """
            
            import message
        time.sleep(0.5)
    except:
        # everything wrong
        import error
        time.sleep(0.5)
        sys.exit(1)  
