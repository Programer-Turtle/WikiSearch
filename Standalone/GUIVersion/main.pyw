from bs4 import BeautifulSoup
import requests
from tkinter import *

def find_summary(soup):
    index = 0
    while True:
        try:
            text = soup.find_all('p')[index].get_text()
            if text != "" and len(text) > 100:
                return text
            else:
                index += 1
        except:
            return "To broad of a subject."

def GetWikiInfo(Article):
    # get URL
    page = requests.get(f"https://en.wikipedia.org/wiki/{Article}")

    #Scrapes Web
    soup = BeautifulSoup(page.content, 'html.parser')

    # Check if the article is not found
    not_found_message = "Wikipedia does not have an article with this exact name."
    if soup.find('b', string=not_found_message) or soup.find_all('p') == []:
        return "Article Not Found"
    else:
        return find_summary(soup)

def main():
    # SetUp
    window = Tk()
    window.title('Wiki Search')
    window.geometry('500x500')
    frame = Frame(window)
    entry = Entry(frame)
    custom_font = ("Helvetica", 10)
    label = Label(window, text='What would you like to learn about?', wraplength=400, font=custom_font)
    label.pack(padx=50, pady=30)

    # Input
    SearchButton = Button(frame, text='Search', command=lambda: label.configure(text=GetWikiInfo(entry.get())))
    SearchButton.pack(side=RIGHT, padx=5)
    entry.pack(side=LEFT)
    frame.pack(padx=20, pady=40)

    # Handle window close event
    window.protocol("WM_DELETE_WINDOW", window.destroy)

    window.mainloop()


if __name__ == "__main__":
    main()