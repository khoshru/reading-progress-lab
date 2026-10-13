Reading Status
Small Python project that formats reading progress for a book.

reading_status(title, current, total) returns:

{title}: {current}/{total} pages read
Example:

from reading import reading_status

reading_status("Dune", 120, 412)
# "Dune: 120/412 pages read"
Project files
reading.py – contains reading_status()
test_reading.py – simple test for reading_status()
How to run the test
python test_reading.py
If the test passes, it prints:

worked