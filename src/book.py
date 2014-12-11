class Book:
    '''class for storing all relevant facts about an audio book'''

    def __init__(self, path, title, artist, album, chapter, chapterPlaytime, 
      totalPlaytime, position, cover):
      self.path = path
      self.title = title
      self.artist = artist
      self.album = album
      self.chapter = chapter
      self.chapterPlaytime = chapterPlaytime
      self.totalPlaytime = totalPlaytime
      self.position = float(position)
      self.cover = cover

    def get_path(self):
      return self.path
      
    def get_num_chapter(self):
      return len(self.path)

    def get_chapter(self):
      return self.chapter

    def get_title(self):
      return self.title
    
    def get_artist(self):
      return self.artist

    def get_album(self):
      return self.getAlbum

    def get_chapter_playtime(self):
      return self.chapterPlaytime
      
    def get_total_playtime(self):
      return self.totalPlaytime

    def get_pos(self):
      return self.position

    def set_pos(self, milliseconds):
      self.position = milliseconds

    def get_cover(self):
      return self.cover