from typing import List
from zene import zene


def main() -> None:

    zeneszamok: List[zene] = []
    with open('zene.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            zeneszamok.append(zene(sor))

    print(f'A lista {len(zeneszamok)} db zeneszámot tartalmaz.')

    db_1988: int = 0
    for db in zeneszamok:
        if db.kiadas_eve == 1988:
            db_1988 += 1
    print(f'Az 1988-ban {db_1988} db számot adtak ki')

    van_rock_1989: bool = False
    for vr in zeneszamok:
        if vr.kategoria == 'Rock 1980s':
            if vr.kiadas_eve == 1989:
                van_rock_1989 = True
    print(f'1989-ben kiadott rock szám {"Van" if van_rock_1989 else "Nincs"} a listában')

    gnr: List[str] = []
    for z in zeneszamok[1:]:
        if z.eloado == "Guns N' Roses":
            gnr.append(z.cim)
    print(f"A Guns N' Roses számának a címe: {gnr[0]}")

    leghosszabb: zene = zeneszamok[0]
    for zen in zeneszamok[1:]:
        if zen.hossz > leghosszabb.hossz:
            leghosszabb = zen
    print('A leghoszabb dal:')
    print(f'\tElőadója: {leghosszabb.eloado}')
    print(f'\tSzám címe:{leghosszabb.cim}')

    dance_1980s: List[str] = []
    for z1980 in zeneszamok[1:]:
        if z1980.kategoria == "Dance 1980s":
            dance_1980s.append(z1980.eloado)
            dance_1980s.append(': ')
            dance_1980s.append(z1980.cim)
            dance_1980s.append('\n')

    with open('dances_1980s.txt', 'w', encoding='utf-8') as file_ki:
        file_ki.writelines(dance_1980s)


if __name__ == "__main__":
    main()
