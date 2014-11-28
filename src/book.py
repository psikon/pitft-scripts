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

    def getPath(self):
      return self.path
      
    def get_num_chapter(self):
      return len(self.path)

    def get_chapter(self):
      return self.chapter

    def getTitle(self):
      return self.title
    
    def getArtist(self):
      return self.artist

    def getAlbum(self):
      return self.getAlbum

    def getChapterPlaytime(self):
      return self.chapterPlaytime
      
    def getTotalPlaytime(self):
      return self.totalPlaytime

    def getPosition(self):
      return self.position

    def setPosition(self, milliseconds):
      self.position = milliseconds

    def getCover(self):
      return self.cover