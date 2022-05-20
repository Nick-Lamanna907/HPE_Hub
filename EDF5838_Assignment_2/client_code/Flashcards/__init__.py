from ._anvil_designer import FlashcardsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from random import *

listOfWords = []

class Flashcards(FlashcardsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    global listOfWords 
    listOfWords = getWords()
    self.loadCard(True)

  def btnCheck_click(self, **event_args):
    if self.btnCheck.text == 'Next':
      self.loadCard(False)
    else:
      self.loadCard(True)
    
  def loadCard(self, new):
    if new == True:
      word = listOfWords[randint(0,len(listOfWords)-1)]
      self.lblFlashcard.text = "\n\n\n" + word + "\n\n\n"
      self.btnCheck.text = 'Next'
    else:
      word = str(self.lblFlashcard.text).strip("\n")
      definition = app_tables.flashcards.get(Word=word)['Definition']
      self.lblFlashcard.text = "\n\n\n" + definition + "\n\n\n"
      self.btnCheck.text = 'Check'

  def btnNewPair_click(self, **event_args):
    if self.tbWord.text != '' and self.tbDef.text != '':
      app_tables.flashcards.add_row(Word=self.tbWord.text, Definition=self.tbDef.text)
      global listOfWords 
      listOfWords = getWords()
      self.tbWord.text = ''
      self.tbDef.text = ''
 
def getWords(): 
    allRows = app_tables.flashcards.search()
    words = []
    for row in allRows:
      words.append(row['Word'])
    return words