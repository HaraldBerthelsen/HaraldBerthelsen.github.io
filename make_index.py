from pathlib import Path
import glob
import sys

bands = sys.argv[1:]

print("""<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
""")


for band in bands:
    albums = glob.glob(f"{band}/*")
    for album in albums:

        print(f"""<div>
        <h3>{album}</h3>
        """)
        
        songs = glob.glob(f"{album}/*mp3")
        for song in sorted(songs):
            #print(song)
            print(f"""<audio controls src="{song}"></audio>
            <a href="{song}">{Path(song).stem}</a>
            <br/>
            """)
        print("</div>")


print("""    
  </body>
</html>
""")

        
            
 
             
            

