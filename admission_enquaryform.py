import ipywidgets as widgets
from IPython.display import display
name = widgets.Text(description='Name')
father = widgets.Text(description="Father's name")
gender = widgets.RadioButtons(options=['Male', 'Female'], description='Gender')
adhaar = widgets.Checkbox(description='Do you have Adhar card?')
pan = widgets.Checkbox(description='Do you have PAN card?')
drivinglicence = widgets.Checkbox(description='Do you have Driving Licence?')
course = widgets.Dropdown(options=['Course 1', 'Course 2', 'Course 3'], description='Course')
branch = widgets.Dropdown(options=['Branch 1', 'Branch 2', 'Branch 3'], description='Branch')
submitbutton = widgets.Button(description='Submit')
submitbutton.on_click(submitbutton)
items = [name, father, gender, adhaar, pan, drivinglicence, course, branch]
form = widgets.VBox(items)
display(form)
display(submitbutton)