from lib.diary_entry import *
# unit tests
def test_count_words():
    diary_entry = DiaryEntry('title','contents')
    result = diary_entry.count_words()
    assert result == 1

def test_reading_time():
    # 10 word post
    diary_entry = DiaryEntry('title','Hello world here is an example post for this exercise')
    result = diary_entry.reading_time(2)
    assert result == 5

def test_reading_chunk():
    diary_entry = DiaryEntry('title','Hello world here is an example post for this exercise')
    first_chunk = diary_entry.reading_chunk(2,1)
    assert first_chunk == 'Hello world'
    second_chunk = diary_entry.reading_chunk(2,1)
    assert second_chunk == 'here is'
    diary_entry.reading_chunk(2,1)
    diary_entry.reading_chunk(2,1)
    diary_entry.reading_chunk(2,1)
    restart_chunk = diary_entry.reading_chunk(2,1)
    assert restart_chunk == 'Hello world'

    # Parameters:
    #   wpm: an integer representing the number of words the user can read
    #        per minute
    #   minutes: an integer representing the number of minutes the user has
    #            to read
    # Returns:
    #   A string representing a chunk of the contents that the user could
    #   read in the given number of minutes.
    # If called again, `reading_chunk` should return the next chunk,
    # skipping what has already been read, until the contents is fully read.
    # The next call after that it should restart from the beginning.