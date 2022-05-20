from ._anvil_designer import StudyTipsTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class StudyTips(StudyTipsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def btnBack_click(self, **event_args):
    open_form('MainPage')

