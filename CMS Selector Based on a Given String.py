def cms_selector(lst, txt):
    a = []
    if txt == "":
        return lst
    for i in lst:
        if txt.upper() in i or txt.lower() in i:
            a = a + [i]
        else:
            continue
    return a
print(cms_selector(["WordPress", "Joomla", "Drupal"], ""))
