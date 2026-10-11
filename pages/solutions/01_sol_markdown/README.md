# Leonhard Euler – Geniusz Matematyki

## Biografia i osiągnięcia

**Leonhard Euler** był szwajcarskim matematykiem i fizykiem, który wniósł ogromny wkład w rozwój wielu dziedzin nauki, takich jak rachunek różniczkowy i całkowy, teoria grafów oraz analiza matematyczna. Uważany jest za *jednego z najwybitniejszych matematyków* w historii. Często błędnie przypisuje się mu stworzenie liczb zespolonych, ale w rzeczywistości ~~nie uciekał się do prostych rozwiązań~~, lecz uporządkował i sformalizował ich teorię.

Wzór Eulera dla wielościanów wyraża się jako $V - E + F = 2$, gdzie $V$ to liczba wierzchołków, $E$ krawędzi, a $F$ ścian. Słynna tożsamość $e^{i\pi} + 1 = 0$ łączy w jednym równaniu pięć najważniejszych stałych matematycznych. Ponadto wzór $e^{ix} = \cos(x) + i\sin(x)$ wiąże funkcje wykładnicze z trygonometrycznymi.

Poniżej przedstawiono trzy kluczowe wzory:

$$e^{i\pi} + 1 = 0$$

$$V - E + F = 2$$

$$\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$$

## Wybrane zagadnienia i notacja

Euler wprowadził m.in. oznaczenie funkcji $f(x)$, stałą $e$ oraz symbol jednostki urojonej $i$.

### Ważne pojęcia
* Teoria grafów (problem mostów królewieckich)
* Liczby pierwsze i hipoteza Riemanna
* Mechanika płynów i ciała sztywnego

### Chronologia życia
1. 1707 – Narodziny w Bazylei
2. 1727 – Przeprowadzka do Petersburga
3. 1783 – Śmierć w Petersburgu

### Zadania do wykonania
- [x] Przeczytać biografię Eulera
- [ ] Przeanalizować dowód na wzór Eulera
- [ ] Uruchomić skrypt w Colabie

### Podsumowanie wkładu naukowego

| Dziedzina | Główny wkład | Notacja / Odkrycie |
| :--- | :--- | :--- |
| Analiza | Rachunek różniczkowy | $e$, $f(x)$ |
| Geometria | Tożsamość Eulera | $e^{i\pi} + 1 = 0$ |
| Teoria grafów | Problem mostów królewieckich | Grafy eulerowskie |

Więcej interaktywnych obliczeń znajdziesz na stronie [Google Colab](http://colab.research.google.com).

```python
import numpy as np

# Przybliżenie wartości e za pomocą ciągu (1 + 1/n)^n
n = 1000000
e_approx = (1 + 1/n)**n
print(f"Przybliżona wartość e: {e_approx}")
```
![Wykres](wykres.png)