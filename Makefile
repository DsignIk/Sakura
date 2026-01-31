.PHONY: bstart clean

bstart:
    python sakura/src
clean:
    @echo "use this only in project main folder"
    find . -type d -name "__pycache__" -exec rm -rf {} +
    
