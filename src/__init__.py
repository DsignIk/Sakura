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
