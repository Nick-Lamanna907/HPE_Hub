from ._anvil_designer import UnitSummaryTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class UnitSummary(UnitSummaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
          
  def btnU3O1_click(self, **event_args):
    self.resetter()
    self.btnU3O1.background = "#CB5A44"
    self.lblTopicQ.text = app_tables.unit_3_4_summary.get(code='U3O1')['topic']
    keyKnowl = app_tables.unit_3_4_summary.get(code='U3O1')['keyKnowledgeList']
    keySkill = app_tables.unit_3_4_summary.get(code='U3O1')['keySkillsList']
    self.lpChecklistL.add_component(Label(text='Key Knowledge', font_size=16, bold=True))
    self.lpChecklistR.add_component(Label(text='Key Skills', font_size=16, bold=True))
    for know in keyKnowl:
      self.lpChecklistL.add_component((CheckBox(checked=know[1],text=know[0])))
    for skill in keySkill:
      self.lpChecklistR.add_component((CheckBox(checked=skill[1],text=skill[0])))

  def btnU3O2_click(self, **event_args):
    self.resetter()
    self.btnU3O2.background = "#CB5A44"
    self.lblTopicQ.text = app_tables.unit_3_4_summary.get(code='U3O2')['topic']
    keyKnowl = app_tables.unit_3_4_summary.get(code='U3O2')['keyKnowledgeList']
    keySkill = app_tables.unit_3_4_summary.get(code='U3O2')['keySkillsList']
    self.lpChecklistL.add_component(Label(text='Key Knowledge', font_size=16, bold=True))
    self.lpChecklistR.add_component(Label(text='Key Skills', font_size=16, bold=True))
    for know in keyKnowl:
      self.lpChecklistL.add_component((CheckBox(checked=know[1],text=know[0])))
    for skill in keySkill:
      self.lpChecklistR.add_component((CheckBox(checked=skill[1],text=skill[0])))

  def btnU4O1_click(self, **event_args):
    self.resetter()
    self.btnU4O1.background = "#CB5A44"
    self.lblTopicQ.text = app_tables.unit_3_4_summary.get(code='U4O1')['topic']
    keyKnowl = app_tables.unit_3_4_summary.get(code='U4O1')['keyKnowledgeList']
    keySkill = app_tables.unit_3_4_summary.get(code='U4O1')['keySkillsList']
    self.lpChecklistL.add_component(Label(text='Key Knowledge', font_size=16, bold=True))
    self.lpChecklistR.add_component(Label(text='Key Skills', font_size=16, bold=True))
    for know in keyKnowl:
      self.lpChecklistL.add_component((CheckBox(checked=know[1],text=know[0])))
    for skill in keySkill:
      self.lpChecklistR.add_component((CheckBox(checked=skill[1],text=skill[0])))

  def btnU4O2_click(self, **event_args):
    self.resetter()
    self.btnU4O2.background = "#CB5A44"
    self.lblTopicQ.text = app_tables.unit_3_4_summary.get(code='U4O2')['topic']
    keyKnowl = app_tables.unit_3_4_summary.get(code='U4O2')['keyKnowledgeList']
    keySkill = app_tables.unit_3_4_summary.get(code='U4O2')['keySkillsList']
    self.lpChecklistL.add_component(Label(text='Key Knowledge', font_size=16, bold=True))
    self.lpChecklistR.add_component(Label(text='Key Skills', font_size=16, bold=True))
    for know in keyKnowl:
      self.lpChecklistL.add_component((CheckBox(checked=know[1],text=know[0])))
    for skill in keySkill:
      self.lpChecklistR.add_component((CheckBox(checked=skill[1],text=skill[0])))
      
  def resetter(self):
    buttons = [self.btnU3O1, self.btnU3O2, self.btnU4O1, self.btnU4O2]
    for button in buttons:
      button.background = "#FF7750"
    self.lpChecklistL.clear()
    self.lpChecklistR.clear()

  def btnBack_click(self, **event_args):
    open_form('MainPage')

def textToList(code, inn, out):
    text = app_tables.unit_3_4_summary.get(code=code)[inn].split(". ")
    megalist = []
    for point in text:
      megalist.append([point, False])
    app_tables.unit_3_4_summary.get(code=code)[out] = megalist
    



    
    
    
    
    