# Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,
# Италия,США. РейнаТур – Англия,Япония,Канада,ЮАР. Радуга – США,Испания,Швеция,
# Австралия.
# Определить в каких турагенствах можно приобрести туры в Канаду, а в каких в США

voyage_set = {'Мексика', 'Канада', 'Израиль', 'Италия', 'США'}
reina_tour_set = {'Англия', 'Япония', 'Канада', 'ЮАР'}
raduga_set = {'США', 'Испания', 'Швеция', 'Австралия'}

tours_to_canada = set()
if 'Канада' in voyage_set:
    tours_to_canada.add('Вояж')
if 'Канада' in reina_tour_set:
    tours_to_canada.add('РейнаТур')
if 'Канада' in raduga_set:
        tours_to_canada.add('РейнаТур')

tours_to_usa = set()
if 'США' in voyage_set:
    tours_to_usa.add('Вояж')
if 'США' in raduga_set:
    tours_to_usa.add('Радуга')
if 'США' in reina_tour_set:
        tours_to_usa.add('Радуга')

print("Туры в Канаду:", tours_to_canada)
print("Туры в США:", tours_to_usa)