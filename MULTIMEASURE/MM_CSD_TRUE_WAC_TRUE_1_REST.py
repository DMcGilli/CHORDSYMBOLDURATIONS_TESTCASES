from music21 import *

theStreamMeta = metadata.Metadata()

def DoStreamLabel(theStream):
    """ This labels the tests for reference on visual output"""
    theStreamMeta.title = theTestTitle
    theStream.insert(0,theStreamMeta)

theChordList = ["A7", "D7","G7", "CM9", "Bmin7","E7#9"]
SymbolList = list(map(harmony.ChordSymbol, theChordList))


myStream = stream.Stream()

theTestTitle = "writeAsChord:TRUE \n CSDuration:TRUE \n 1 REST"

for x in SymbolList:
    harmony.realizeChordSymbolDurations(myStream)  # toggle as needed for behaviors
    x.writeAsChord = True #toggle as needed
    x.duration = duration.Duration("half")
    myStream.append(note.Rest(duration=duration.Duration("half")))
    myStream.append(x)
    # myStream.repeatAppend(note.Rest(duration=duration.Duration(4.0)),0)

DoStreamLabel(myStream)
myStream.show('musicxml.png')


#



