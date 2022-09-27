#1. Zaimportuj pandas i wczytaj plik banklist.csv do ramki danych zwanej bankami.

import pandas as pd
banki = pd.read_csv("banklist.csv")

#2. Pokaż nagłówek ramki danych
print(banki.columns)

#3. Jakie są nazwy kolumn?
nazwy_kolumn = banki.columns.values
print(nazwy_kolumn)

#4. Ile stanów (ST) jest reprezentowanych w tym zestawie danych?

print("Unikalne stany:%s" %len(banki.ST.unique()))

#5. Przedstaw listę lub arraykę wszystkich stanów w zestawie danych.

print(banki.ST.unique())

#6. Jakie jest 5 stanów z największą liczbą upadków banków?

closed_banks_per_state = banki.iloc[:, [0,2]].groupby(by='ST').count()
print(closed_banks_per_state.sort_values(by=['Bank Name'], ascending=False).head())

#7. Jakie jest 5 najlepszych instytucji przejmujących (acquiring institutions)?
institutions = banki.iloc[:, [0,4]].groupby(by='Acquiring Institution').count()
print(institutions.sort_values(by=['Bank Name'], ascending=False).head(6))

# 8. Ile banków nabył State Bank of Texas? Ilu z nich było w Teksasie?

acq_by_tex = banki[banki['Acquiring Institution'] == 'State Bank of Texas']
print(acq_by_tex.groupby('Acquiring Institution')['Bank Name'].count())

acq_by_tex2 = banki[(banki['Acquiring Institution'] == 'State Bank of Texas') & (banki['ST'] == 'TX')]
print(acq_by_tex2.groupby('Acquiring Institution')['Bank Name'].count())

# 9. W jakim mieście w Kalifornii bank najczęściej ulega bankructwu?

closed_ca = banki[banki['ST'] == 'CA'].groupby('City')['City'].count()
closed_ca = closed_ca.sort_values(ascending=False)
print(closed_ca.head(1))
















