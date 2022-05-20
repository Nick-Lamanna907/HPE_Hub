from ._anvil_designer import MainPageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class MainPage(MainPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def btnUnitSummary_click(self, **event_args):
    open_form('UnitSummary')

  def btnStudyTips_click(self, **event_args):
    open_form('StudyTips')

  def btnMindfullness_click(self, **event_args):
   open_form('Mindfullness')

  def btnFlashcards_click(self, **event_args):
   open_form('Flashcards')




