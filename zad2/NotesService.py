from NoteStorage import NoteStorage


class NoteService:
    def __init__(self):
        self.storage = NoteStorage()

    def add(self, note):
        return self.storage.add(note)

    def averageOf(self, name):
        allNotes = self.storage.getAllNotesOf(name)
        notesSum = 0
        for note in allNotes:
            notesSum += note.get_note()
        numOfNotes = len(allNotes)
        if numOfNotes == 0:
            return 0
        return notesSum / numOfNotes

    def clear(self):
        return self.storage.clear()
