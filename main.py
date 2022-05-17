class Pracownik:
  def __init__(self, imie, wynagrodzenie):
      self.imie_pracownika = str(imie)
      self.wynagrodzenie_brutto = float(wynagrodzenie)
  
  def oblicz_netto(self) -> float:
    podstawa_wymiaru_skladek = float(self.wynagrodzenie_brutto)
    b = round(podstawa_wymiaru_skladek,2)
    a = b
    emerytalna = 0.0976 * b
    rentowa = 0.015 * b
    chorobowa = 0.0245 * b
    c = round(emerytalna,2) + round(rentowa,2) + round(chorobowa,2)
    d = round(b - c,2)
    e = round((d*0.09),2)
    f = round((d*0.0775),2)
    g = float(111.25)
    h = round(a - g - c,0)
    i = round((h*0.18),2) - float(46.33)
    j = round(i - f,0)
    k = round(a - c - e - j,2)
    return k
    
  def skladki_pracodawcy(self) -> float:
    podstawa_wymiaru_skladek = self.wynagrodzenie_brutto
    skladki_obciazajace_pracodawce = round(podstawa_wymiaru_skladek*0.0976,2) + round(podstawa_wymiaru_skladek*0.065,2) + round(podstawa_wymiaru_skladek*0.0193,2) + round(podstawa_wymiaru_skladek*0.0245,2) + round(podstawa_wymiaru_skladek*0.001,2)
    return skladki_obciazajace_pracodawce

  def koszt_pracodawcy(self) -> float:
    podstawa_wymiaru_skladek = self.wynagrodzenie_brutto
    skladki_obciazajace_pracodawce = round(podstawa_wymiaru_skladek*0.0976,2) + round(podstawa_wymiaru_skladek*0.065,2) + round(podstawa_wymiaru_skladek*0.0193,2) + round(podstawa_wymiaru_skladek*0.0245,2) + round(podstawa_wymiaru_skladek*0.001,2)
    koszt_pracodawcy = round(podstawa_wymiaru_skladek,2) + round(skladki_obciazajace_pracodawce,2)
    return koszt_pracodawcy



for index in range(0,i):
  dane_pracownika=input().replace('\r', '').replace('\n', '').split(" ")
  pracownik = Pracownik(dane_pracownika[0], dane_pracownika[1])
  tablica_pracownikow.append(dane_pracownika)

calkowity_koszt = 0

#printowanie wartości
for index in range(0,i):
  prac = Pracownik(tablica_pracownikow[index][0],tablica_pracownikow[index][1])
  calkowity_koszt += prac.koszt_pracodawcy()
  print(tablica_pracownikow[index][0] + " " + str(prac.oblicz_netto()) + " " + str(prac.skladki_pracodawcy()) + " " + str(prac.koszt_pracodawcy()))
print("%.2f"%calkowity_koszt)
