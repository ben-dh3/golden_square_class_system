class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        # keep track of these for future calls of reading_chunk()
        self.words_per_chunk = 0
        self.iterator = 0

    def count_words(self):
        return len(self.contents.split(' '))

    def reading_time(self, wpm):
        number_of_words = len(self.contents.split(' '))
        return number_of_words/wpm

    def reading_chunk(self, wpm, minutes):
        # split contents into words
        split_string = self.contents.split(' ')
        # calculate no. words per chunk
        self.words_per_chunk = wpm * minutes
        # calculate no. chunks (words in content / words per chunk)
        number_of_chunks = int(len(split_string)/self.words_per_chunk)
        current_chunk = self.iterator * self.words_per_chunk
        # if all the content has been returned by previous calls, restart
        if self.iterator >= number_of_chunks:
            self.iterator = 0
            current_chunk = self.iterator * self.words_per_chunk
        # return the corresponding chunk   
        for i in range(self.iterator,number_of_chunks):
            # increment
            self.iterator+=1
            # join the split string after slicing at the current chunk
            return ' '.join(split_string[current_chunk:current_chunk+self.words_per_chunk])