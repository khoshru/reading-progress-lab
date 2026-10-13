def reading_status(title, current, total):
    prec = current // total *100
    return f'{title} - progress: {current}/{total} pages ({prec}%)'
reading_status("Dune", 120, 412)
