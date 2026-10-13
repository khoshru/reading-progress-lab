from reading import reading_status
def test_reading(title, current, total):
    prec = current // total *100
    assert reading_status(title, current, total) == f'{title} - progress: {current}/{total} pages ({prec}%)'
test_reading("Dune", 120, 412)
