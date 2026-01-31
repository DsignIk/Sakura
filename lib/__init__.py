import tkinter as tk
root = tk.Tk()
root.withdraw() 

import requests 

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
    except:
        # everything wrong
        import error
        sys.exit(1)  
