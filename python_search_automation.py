import pyautogui
import random
import time

pyautogui.hotkey('winleft', 'r')
pyautogui.typewrite('msedge')
pyautogui.press('enter')
time.sleep(2)
# Focus on the address bar
pyautogui.hotkey('alt', 'd')

                

lst=["Rose Abdoo (born 1962)","Raymond Ablack (born 1989)","John Aboud (born 1973)","James Acaster (born 1985)","Jayde Adams (born 1984)",
     "Kev Adams (born 1991)","Pamela Adlon (born 1966)","James Adomian (born 1980)","Scott Adsit (born 1965)","Steve Agee (born 1969)",
     "Alex Agnew (born 1973)","Rubén Aguirre (1934–2016)","Dan Ahdoot (born 1981)","Caroline Aherne (1963-2016)","Ahmed Ahmed (born 1970)",
     "Sohail Ahmed (born 1963)","Franklyn Ajaye (born 1949)","Anna Akana (born 1989)","Malin Akerman (born 1978)","Nawaal Akram (born 1990)",
     "Nasser Al Qasabi (born 1963)","Joe Alaskey (1952–2016)","Carlos Alazraqui (born 1962)","Rory Albanese (born 1977)","Lou Albano (1933-2009)",
     "Eddie Albert (1906-2005)","Alan Alda (born 1936)","Jason Alexander (born 1959)","Ted Alexandro (born 1969)","Barbara Jo Allen (1906–1974)","Dave Allen (1936–2005)","Gracie Allen (1895–1964)","Leo Allen (born 1972)","Marty Allen (1922–2018)","Steve Allen (1921–2000)","Tim Allen (born 1953)","Woody Allen (born 1935)","Kirstie Alley (born 1951)","Kevin Allison (born 1970)","Stephanie Allynne (born 1986)","Cristela Alonzo (born 1979)","Jeff Altman (born 1951)","Brian Jordan Alvarez (born 1987)","The Amazing Johnathan (1958–2022)","Utkarsh Ambudkar (born 1983)","Robbie Amell (born 1988)","Mo Amer (born 1981)","John Amos (born 1939)","Megan Amram (born 1987)","Simon Amstell (born 1979)","Morey Amsterdam (1908–1996)","Andrea Anders (born 1975)","Siw Anita Andersen (born 1966)","Amy Anderson (born 1972)","Anthony Anderson (born 1970)","Blake Anderson (born 1984)","Harry Anderson (1952–2018)","James Anderson","Louie Anderson (1953–2022)","Wil Anderson (born 1974)","Eric André (born 1983)","Alex Anfanger (born 1985)","Michael Angarano (born 1987)","Lucia Aniello (born 1983)","Jennifer Aniston (born 1969)","Aziz Ansari (born 1983)","Ant (born 1967)","Dave Anthony (born 1967)","Craig Anton (born 1962)","Judd Apatow (born 1967)","Ingo Appelt (born 1967)","Christina Applegate (born 1971)","John Aprea (born 1941)","Carly Aquilino (born 1990)","Nicole Arbour (born 1985)","Lisa Arch (born 1971)","Rosco Arbuckle (1887–1933)","Geoffrey Arend (born 1978)","Lesley Arfin (born 1979)","Marcella Arguello (born 1985)","Fred Armisen (born 1966)","Alexander Armstrong (born 1970)","Desi Arnaz (1917-1986)","Will Arnett (born 1970)","David A. Arnold (1968–2022)","Tichina Arnold (born 1969)","Tom Arnold (born 1959)","David Arquette (born 1971)","Bea Arthur (1922–2009)","Aaron Aryanpur (born 1978)","Katie Aselton (born 1978)","Erica Ash (born 1977)","Lauren Ash (born 1983)","Arthu"]

for i in range(20):
    a=random.choice(lst)
    pyautogui.typewrite(a)# Type a string of text
    pyautogui.typewrite(["enter"])# Simulate pressing the Enter key
        
    time.sleep(1)# Wait for a moment
    pyautogui.hotkey('alt', 'd')


# Wait for a moment
# time.sleep(1)

# Drag the mouse to new coordinates (x, y)
# pyautogui.dragTo(200, 200, duration=1)


#               
x, y = pyautogui.position()

# Print the coordinates
print(f"Current coordinates: x={x}, y={y}")
