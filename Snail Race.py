def maurice_wins(m_snails, s_snails):
    s = 0
    m = 0
    if m_snails[0] > s_snails[2]:
        m = m + 1
    else:
        s = s + 1

    if m_snails[1] > s_snails[0]:
        m = m + 1
    else:
        s = s + 1

    if m_snails[2] > s_snails[1]:
        m = m + 1
    else:
        s = s + 1

    return True if m>s else False


print(maurice_wins([6, 8, 9], [7, 12, 14]))
