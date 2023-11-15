class Diary:
    def __init__(self):
        self = self
        self.entry_list = []

    def add(self, entry):
        self.entry_list.append(entry)

    def all(self):
        entries={}
        for entry in self.entry_list:
            entries[entry.title]=entry.contents
        return entries

    def count_words(self):
        total = 0
        for entry in self.entry_list:
            total += entry.count_words()
        return total

    def reading_time(self, wpm):
        total = 0
        for entry in self.entry_list:
            total += entry.count_words()
        return total/wpm

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # calculate words to read
        words_to_read = wpm * minutes
        # create a dictionary to update with the "best"
        entries = {'title':'','content':''}
        # create variable to track the current smallest diff
        current_smallest_diff=words_to_read
        # loop through entries in entry list
        for entry in self.entry_list:
            # find the difference between the length of the current entry and words to read
            current_diff = abs(words_to_read - entry.count_words())
            # if length of current entry <= words to read AND current diff <= smallest diff
            if entry.count_words() <= words_to_read and current_diff <= current_smallest_diff:
                # update smallest diff
                current_smallest_diff = current_diff
                # update entries dict
                entries['content'] = entry.contents
                entries['title'] = entry.title
        # return a string with the values of title and content
        return f"{entries['title']}: {entries['content']}"