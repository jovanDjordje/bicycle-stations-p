## Oslo Bysykkel
Bare en enkel app basert på Bysykkel API, som gir en oversikt over sykkelstasjoner i Oslo med
stasjonsnavn, kapasitet, antall sykler og dokker tilgjengelig.
### Requirements:
1.   Python
2. Bibliotek: [Requests](http://docs.python-requests.org/en/master/)
3. Bibliotek: [pandas](http://pandas.pydata.org/docs/)
4. Bibliotek: [tkinter](https://tkdocs.com/)
5. Bibliotek: [pandastable](https://pandastable.readthedocs.io/en/latest/)
### Installasjon:
- install requests:   ```python -m pip install requests```
- install pandas:     ```python -m pip install pandas```
- install tkinter     ```python -m pip install tkinter```
- install pandastable ```python -m pip pip install pandastable```
### Bruk:
Etter installasjon, naviger til filen BysykkelApp.py og kjør følgende kommando for å kjøre appen: \
```python BysykkelApp.py```
Hvis alt går bra, vil programmet åpne et gui-vindu der resultatene vil vises. \ 
GUI-biblioteket som brukes til å vise resultatene, gir kolonnesortering ved å dobbeltklikke på 
kolonneoverskriften. \
![Skjermskudd TABLE](https://github.com/jovanDjordje/bicycle-stations-p/master/table.jpg?raw=true)

### Noen refleksjoner:
Jeg valgte å systemavslutte appen i try/exception in fetch_data-metoden. 
Dette virker som en akseptabel løsning i denne sammenhengen siden appen 
er en standalone app og ikke brukes av noen annen app. 
Med dette i tankene anses det som en god praksis.

