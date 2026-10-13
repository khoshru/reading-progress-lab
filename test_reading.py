from reading import reading_status
def test_reading(title, current, total):
    assert reading_status(title, current, total) == f'{title} - progress: {current}/{total} pages'
test_reading("Dune", 120, 412)
