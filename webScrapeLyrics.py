# This program web scrapes lyrics using input band name and song
#
# Copyright 2018, Eric Dawson, All rights reserved.

# Import modules
import requests
import bs4
import tkinter
import tkinter.filedialog

# Functions and Classes
        
def main():
    artist = input("Enter artist name: ")
    title = input("Enter song title: ")

    artist = artist.replace(" ", "-")
    title = title.replace(" ", "-")

    url = 'https://genius.com/' + artist + "-" + title + "-lyrics"

#    print(url)
#    url = 'https://www.lyrics.com/lyric/2326537/The+Cure/Jumping+Someone+Else%27s+Train'
    r = requests.get(url)
    r_html = r.text
    soup = bs4.BeautifulSoup(r_html, "html.parser")
    
    file_name = tkinter.filedialog.asksaveasfilename()
    with open(file_name, 'w') as f:
        f.write("")
        f.write("*****************************************\n")
        f.write("")
        for artist in soup.find_all(class_="header_with_cover_art-primary_info-primary_artist"):
            f.write(artist.text)
        f.write("\n")
        for title in soup.find_all(class_="header_with_cover_art-primary_info-title "):
            f.write(title.text)
        f.write("\n")
        f.write("*****************************************\n")
        f.write("")
        for lyrics in soup.find_all(class_="lyrics"):
            if lyrics:
                f.write(lyrics.text)
            else:
                f.write(lyrics.contents[0].strip())
        f.write("")

if __name__ == '__main__':
    import doctest
    doctest.testmod()


    # Run main program
    main()
