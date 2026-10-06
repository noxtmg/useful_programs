# Przykładowy Dokument Markdown

## Pierwsza Sekcja

To jest **bardzo ważny fragment**, który został pogrubiony, aby przyciągnąć uwagę czytelnika. Warto również zwrócić uwagę na *pochylony tekst*, podkreślający subtelniejsze akcenty w treści. Wstępny wzór matematyczny w tekście to $E = mc^2$.

## Druga Sekcja

W tej części przedstawiamy dodatkowe omówienie. Pamiętaj, że ten element był błędny, więc jest ~~przekreślony~~. Drugi wzór w tekście określa funkcję kwadratową $f(x) = ax^2 + bx + c$, a trzeci to równanie tożsamości Eulera $e^{i\pi} + 1 = 0$.

### Wzory Blokowe

Poniżej znajdują się trzy reprezentatywne wzory matematyczne wyświetlane jako osobne bloki:

$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$

$$\sum_{k=1}^{n} k = \frac{n(n+1)}{2}$$

$$A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

### Elementy Listy i Tabele

#### Lista Punktowana
* Pierwszy element listy
* Drugi element listy
* Trzeci element listy

#### Lista Numerowana
1. Krok pierwszy
2. Krok drugi
3. Krok trzeci

#### Checklist
- [x] Zadanie ukończone
- [ ] Zadanie w trakcie realizacji
- [ ] Zadanie do zrobienia

#### Tabela
| ID | Nazwa | Wartość |
| :--- | :--- | :---: |
| 1 | Element A | 100 |
| 2 | Element B | 250 |
| 3 | Element C | 400 |

### Kod i Narzędzia

Więcej informacji znajdziesz na stronie [Google Colab](http://colab.research.google.com).

```python
def powitanie(imie):
    print(f"Witaj, {imie}!")

powitanie("Świat")
```

![Wykres](wykres.png)