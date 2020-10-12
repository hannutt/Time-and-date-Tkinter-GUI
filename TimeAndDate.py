#tuodaan ohjelassa käytettävät kirjastot.
from tkinter import* 
import time
import datetime
from tkinter.font import Font
import calendar
import requests
from bs4 import BeautifulSoup


#luodaan funktio, jolla toteutetaan kellon toiminta.
def clockFunc():
    #tallennetaan muuttujaan kellonaika muodossa tunnit,minuutit ja sekunnit.
    timeVar = time.strftime('%H:%M:%S')
    #näytetään kellonaika clock-nimisessä komponentissa.
    clock.config(text=timeVar)
    #after funktiolla päivitetään kellonaikaa jokaisen 1000 millisekunnin
    #jälkeen. arvo on annettu parametrina.
    clock.after(1000,clockFunc)

#luodaan funktio, jolla toteutaan tämänhetkinen päivämäärän näyttö.
def dateFunc():
    #tallennetaan muuttujaan tämänhetkinen päivämäärä
    timenow = datetime.datetime.now()
    #strftime metodilla muotoillaan tulos, niin että siitä näytetään
    #viikonpäivän nimi, päivämäärä, kuukausi ja vuosi.
    timenow = timenow.strftime('%a/%d/%m/%Y')
    date.config(text=timenow)

#luodaan funktio, jolla toteutetaan nimipäivän haku.
def nameFunc():
    #tehdään http-pyyntö parametrina  olevaan www-osoitteeseen. 
    page = requests.get('https://www.nimipaivat.fi')
    #otetaan html-parser moduuli käyttöön
    soup = BeautifulSoup(page.text, 'html.parser')
    #haetaan www-sivulta parametrina oleva html-taulukko
    nameday = soup.find(class_='table table-striped table-hover')
    #haetaan taulukosta kaikki span tagin sisällä olevat merkkijonot.
    namedays = nameday.find_all('span')
    #käydään merkkijonot for-silmukassa läpi, tallennetaan ne names muuttujaan
    #ja näytetään ne nameLabel-komponentissa.
    for nameday in namedays:
        names = nameday.text
    nameLabel.config(text = names)


#luodaan funktio, joka laskee kauanko kuluvaa vuotta on jäljellä.
def yearLeft():
    #tallennetaan muuttujaan kuluva vuosi.
    year = datetime.date.today().year
    #tallennetaan muuttujaan vuosi,kk ja pvm eli kuluvan vuoden viimeinen päivä.
    final = datetime.datetime(year,12,31)
    #tallennetaan muuttujaan tämänhetkinen vuosi,kuukausi ja päivä.
    now = datetime.datetime.today()
    now = datetime.datetime(now.year,now.month,now.day)
    #tallennetaan muuttujaan final ja now muuttujien erotus, eli montako päivää vuotta on jäljellä
    yearResult = final - now
    #näytetään tulos howMuchLeft komponentissa.
    howMuchLeft.config(text = yearResult.days)


#luodaan funktio joka näyttää meneillään olevan viikon viikkonumeron.
def week():
    #tallennetaan muuttujaan tämänhetkinen aika.
    weekVar = datetime.datetime.now()
    #muotoillaan tulos strftime metodilla siten, että näytetään tuloksesta vain viikkonumero.
    weekVar = weekVar.strftime('%W')
    weekresult.config(text = weekVar)

#luodaan funktio, jolla toteutetaan kalenteri.
def calendarFunc():
    #tallennetaan muuttujaan kuluva vuosi
    yearTime = datetime.date.today().year
    #tallennetaan muuttujaan kuluva kuukausi
    monthTime = datetime.date.today().month
    #annetaan kuluva vuosi ja kk parametrina calendar-funktiolle.
    cal = calendar.month(yearTime,monthTime)
    #näytetään kalenteri caLabel komponentissa.
    calLabel.config(text = cal)

#luodaan funktio, joka piilottaa kalenterin.
def calClose():
    calLabel.pack_forget()
    

root = Tk()
#luodaan alasvetovalikko
menubar = Menu(root)
calendarmenu = Menu(menubar)

#lisätään alasvetovalikkoon 2 tekstikomponenttia. command komennolla kerrotaan mikä funktio suoritetaan
#jos komponettia klikataan hiirellä.
calendarmenu.add_command(label = 'Open calendar', command = calendarFunc)
calendarmenu.add_command(label = 'Close calendar',command = calClose)
#Annetaan pudotusvalikolle nimi calendar. menu = calendar komennolla
#osoitetaan oudotusvalikko.
menubar.add_cascade(label = 'Calendar', menu = calendarmenu)

root.config(menu = menubar)
root.title('Time and date')
root.configure(background = 'gray60')

#luodaan frame-komponentit, joiden avulla asemoidaan muut komponentit. background komennolla annetaan
#komponenteille taustaväri.
frame1 = Frame()
frame1.configure(background = 'gray60')
frame2 = Frame()
frame2.configure(background = 'gray60')
frame3 = Frame()
frame3.configure(background = 'gray60')

frame4 = Frame()
frame4.configure(background = 'gray60')
frame5 = Frame()
frame5.configure(background = 'gray60')

#tallennetaan ohjelmassa käytettävät fontit muuttujiin.
labelfont = Font(family = 'Bradley Hand ITC')
titlefont = Font(family = 'Century Gothic', size = 10)

#label-komennolla luodaan teksti / tekstiä sisältävät komponentit, font komennolla kerrotaan niissä käytettävä fontti.
name = Label(root, text = 'Time and date',font = titlefont, background = 'gray60')
yearlefttxt = Label(frame3,text = 'Year left: ', font = titlefont, background = 'gray60')
clock = Label(frame2,bg='SkyBlue3',font = labelfont, relief = 'solid')

date = Label(frame1, bg ='SkyBlue3',font = labelfont)
today = Label(frame1, text = 'Today is: ', font = titlefont, background = 'gray60')
nameLabel = Label (frame5, bg = 'SkyBlue3',font = labelfont)

nametext = Label (frame5,text = 'Namedays: ',font = titlefont, bg = 'gray60')
timelabel = Label (frame2, text = 'Time is: ',font = titlefont, background = 'gray60') 

weeklabel = Label (frame4, text = 'Weeknumber is: ', font = titlefont,background = 'gray60')
weekresult = Label (frame4, bg = 'SkyBlue3', font = labelfont)
howMuchLeft = Label(frame3,font = labelfont, bg = 'SkyBlue3')

days = Label(frame3, text = 'Days', bg = 'SkyBlue3', font = labelfont)
calLabel = Label (root, bg = 'SkyBlue3', font = labelfont)



#kutsutaan funktioita.
clockFunc()
dateFunc()
nameFunc()
yearLeft()
week()

#pakataan komponentit, pady/padx komennoilla lisätään tyhjää tilaa komponenttien
#ympärille, side-komennolla kerrotaan komponentin sijoitussuunta.
name.pack()
frame1.pack()
today.pack(side=LEFT)
date.pack(side=RIGHT,pady=5)

frame5.pack()
nametext.pack(side=LEFT)
nameLabel.pack(side=RIGHT,pady=5)

frame4.pack()
weeklabel.pack(side=LEFT)
weekresult.pack(side=RIGHT)

frame2.pack()
timelabel.pack(side=LEFT)
clock.pack(side=RIGHT,pady=5)

frame3.pack()
yearlefttxt.pack(side=LEFT)
howMuchLeft.pack(side=LEFT,pady=5)

days.pack(side=RIGHT)
calLabel.pack()
mainloop()
    
