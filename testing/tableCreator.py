def plasser_content(data, formatering):
    """Formaterer en celle: tall høyrejusteres (uten unødvendige desimaler
    hvis tallet er helt), tekst formateres som normalt."""
    try:
        tall = float(data)
        if tall % 1 == 0:
            tall = int(tall)
        return f'{str(tall):>{formatering}}'
    except (ValueError, TypeError):
        return f'{data:{formatering}}'


def bygg_linje(col_widths, venstre, horisontal, kryss, hoyre):
    """Bygger en horisontal linje (topp/bunn/midtlinje) for tabellen,
    gitt hjørne-/kryss-tegn og kolonnebredder."""
    linje = venstre
    for i, bredde in enumerate(col_widths):
        linje += horisontal * bredde
        linje += hoyre if i == len(col_widths) - 1 else kryss
    return linje + '\u000A'


def create_table(table_list, caption=False):
    """Lager en pen tekst-tabell fra en todimensjonal liste.

    Parametre:
        table_list: liste av rader, hver rad en liste av celleverdier.
                    Alle rader må ha samme lengde.
        caption:    hvis True, tegnes den første raden som en overskrift
                    med doble linjer.
    """
    if not table_list or not all(len(row) == len(table_list[0]) for row in table_list):
        raise ValueError("tableList kan ikke være tom, og alle rader må ha samme lengde")

    # Tegn for vanlige linjer
    left_upper_corner = '\u250C'
    horizontal_line = '\u2500'
    right_upper_corner = '\u2510'
    upper_t_cross = '\u252C'
    pole = '\u2502'
    left_t_cross = '\u251C'
    right_t_cross = '\u2524'
    mid_cross = '\u253C'
    left_lower_corner = '\u2514'
    right_lower_corner = '\u2518'
    lower_t_cross = '\u2534'

    # Tegn for overskrift (dobbel linje), brukes kun hvis caption=True
    left_upper_corner_caption = '\u2552'
    right_upper_corner_caption = '\u2555'
    horizontal_line_caption = '\u2550'
    left_t_cross_caption = '\u255E'
    right_t_cross_caption = '\u2561'
    upper_t_cross_caption = '\u2564'
    mid_cross_caption = '\u256A'

    # Analyser kolonnebredder
    table_col_widths = [0] * len(table_list[0])
    for row in table_list:
        for j, cell in enumerate(row):
            table_col_widths[j] = max(table_col_widths[j], len(str(cell)))

    if caption:
        top_line = bygg_linje(
            table_col_widths,
            left_upper_corner_caption, horizontal_line_caption,
            upper_t_cross_caption, right_upper_corner_caption
        )
        mid_line_caption = bygg_linje(
            table_col_widths,
            left_t_cross_caption, horizontal_line_caption,
            mid_cross_caption, right_t_cross_caption
        )
    else:
        top_line = bygg_linje(
            table_col_widths,
            left_upper_corner, horizontal_line,
            upper_t_cross, right_upper_corner
        )

    bottom_line = bygg_linje(
        table_col_widths,
        left_lower_corner, horizontal_line,
        lower_t_cross, right_lower_corner
    )
    mid_line = bygg_linje(
        table_col_widths,
        left_t_cross, horizontal_line,
        mid_cross, right_t_cross
    )

    # Bygg tabellen
    returnstring = top_line
    for i, row in enumerate(table_list):
        returnstring += pole
        for j, cell in enumerate(row):
            returnstring += plasser_content(cell, table_col_widths[j])
            returnstring += pole
        returnstring += '\u000A'

        if i == len(table_list) - 1:
            returnstring += bottom_line
        elif i == 0 and caption:
            returnstring += mid_line_caption
        else:
            returnstring += mid_line

    return returnstring


if __name__ == "__main__":
    # Eksempel
    tabell = [
        ["Norge", "Sverige", "Danmark", "Finland"],
        ["Oslo", "Stockholm", "København", "Helsinki"],
        ["NOK", "SEK", "DKK", "EUR"],
        [6.1, 12.0, 7.2, 4.9]
    ]

    print(create_table(tabell, True))
    #     ╒═════╤═════════╤══════════╤════════╕
    #     │Norge│Sverige  │Danmark   │Finland │
    #     ╞═════╪═════════╪══════════╪════════╡
    #     │Oslo │Stockholm│København │Helsinki│
    #     ├─────┼─────────┼──────────┼────────┤
    #     │NOK  │SEK      │DKK       │EUR     │
    #     ├─────┼─────────┼──────────┼────────┤
    #     │  6.1│     12.0│       7.2│     4.9│
    #     └─────┴─────────┴──────────┴────────┘
