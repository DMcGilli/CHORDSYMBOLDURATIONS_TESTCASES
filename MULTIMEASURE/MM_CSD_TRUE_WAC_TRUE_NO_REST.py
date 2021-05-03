from music21 import *

theStreamMeta = metadata.Metadata()
myStream = stream.Stream()

def DoStreamLabel(theStream):
    """ This labels the tests for reference on visual output"""
    theStreamMeta.title = theTestTitle
    theStream.insert(0,theStreamMeta)

theChordList = ["A7", "D7","G7", "CM9", "Bmin7","E7#9"]
SymbolList = list(map(harmony.ChordSymbol, theChordList))

theTestTitle = "writeAsChord:TRUE \n CSDuration:TRUE \n NO REST"

for x in SymbolList:
    x.duration = duration.Duration("half")
    harmony.realizeChordSymbolDurations(myStream)  # toggle as needed for behaviors
    x.writeAsChord = True  # toggle as needed
    myStream.append(x)

DoStreamLabel(myStream)
myStream.show('musicxml.png')


#



