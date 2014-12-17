class Book:
    '''class for storing all relevant informations for playing a audio book and
    show informations in the interfaces. The seperated chapter of audio books are
    stored together for ensure an unbroken playback'''

    def __init__(self, path, title, artist, album, chapter, chapter_playtime, 
      total_playtime, position, cover):
      self.path = path
      self.title = title
      self.artist = artist
      self.album = album
      self.chapter = chapter
      self.chapter_playtime = chapter_playtime
      self.total_playtime = total_playtime
      self.position = float(position)
      self.cover = cover

    def get_path(self):
      ''' return an array with all paths for the seperated chapter'''
      return self.path
      
    def get_num_chapter(self):
      ''' count the number of chapters in the path array '''
      return len(self.path)

    def get_chapter(self):
      ''' get actual played chapter '''
      return self.chapter

    def get_title(self):
      ''' get title of the book '''
      return self.title
    
    def get_artist(self):
      ''' get artist of the book '''
      return self.artist

    def get_album(self):
      ''' if contained in id3 tags return the album name '''
      return self.getAlbum

    def get_chapter_playtime(self):
      ''' get playtime of actual chapter '''
      return self.chapter_playtime
      
    def get_total_playtime(self):
      ''' sum the playtime of every chapters of a book '''
      return self.total_playtime

    def get_pos(self):
      ''' get actual position in chapter '''
      return self.position

    def set_pos(self, milliseconds):
      ''' set position to value ''' 
      self.position = milliseconds

    def get_cover(self):
      ''' return the path to the cover image '''
      return self.cover