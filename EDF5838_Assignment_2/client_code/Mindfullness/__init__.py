from ._anvil_designer import MindfullnessTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Mindfullness(MindfullnessTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def ddVideos_change(self, **event_args):
    if self.ddVideos.selected_value == 'Focus':
      self.ytMain.youtube_id = 'zSkFFW--Ma0'
    elif self.ddVideos.selected_value == 'Stress Relief':
      self.ytMain.youtube_id = 'z6X5oEIg6Ak'
    elif self.ddVideos.selected_value == 'Energy Boost':
      self.ytMain.youtube_id = 'kp_4OjtvH2k'
    elif self.ddVideos.selected_value == 'Sleep':
      self.ytMain.youtube_id = 'ft-vhYwHzxw'
    elif self.ddVideos.selected_value == 'Speedy Stress Relief':
      self.ytMain.youtube_id = 'c1Ndym-IsQg'   
    
  def btnBack_click(self, **event_args):
    open_form('MainPage')


