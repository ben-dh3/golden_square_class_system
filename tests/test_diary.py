from lib.diary import *
from lib.diary_entry import *

# unit tests
def test_count_words():
    diary = Diary()
    diary_entry1 = DiaryEntry('title','contents')
    diary_entry2 = DiaryEntry('title','Hello world this is a post to test this exercise')
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.count_words()
    assert result == 11

def test_reading_time():
    diary = Diary()
    diary_entry1 = DiaryEntry('title','contents here')
    diary_entry2 = DiaryEntry('title','Hello world this is a post to test this exercise')
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.reading_time(3)
    assert result == 4

# integration tests
def test_diary_integration():
    diary = Diary()
    diary_entry = DiaryEntry('title','contents')
    diary.add(diary_entry)
    result = diary.all()
    assert result == {'title': 'contents'}


def test_find_best_entry():
    diary = Diary()
    diary_entry1 = DiaryEntry('title','contents')
    diary_entry2 = DiaryEntry('title','Hello world this is a post to test this exercise')
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    result = diary.find_best_entry_for_reading_time(2, 6)
    assert result == 'title: Hello world this is a post to test this exercise'
