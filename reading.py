def reading_status(title, current, total):
    prec = current // total *100
    return f'{title}: {current}/{total} pages read ({prec}% )'
reading_status("Dune", 120, 412)
