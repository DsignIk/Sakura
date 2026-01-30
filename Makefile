bstart:
    python sakura/src
clean:
    @echo "use this only in project main folder"
    rm -rf __pycache__
    cd src
    rm -rf __pycache__
    cd scen
    rm -rf __pycache__
    cd ..
    cd ..
    