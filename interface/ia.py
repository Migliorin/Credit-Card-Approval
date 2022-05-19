import PySimpleGUI as sg
import pickle as pkl
import numpy as np


model = pkl.load(open("./model.pkl","rb"))

sg.theme('Topanga')      # Add some color to the window

# Very basic window.  Return values using auto numbered keys
size = (18, 1)
size_input = (25,1)

income_type = ['Working', 'Commercial associate', 'Pensioner', 'State servant', 'Student']
education_type = ['Secondary /secondary special', 'Higher education', 'Incomplete higher', 'Lower secondary', 'Academic degree']
family_status = ['Married', 'Single / not married', 'Civil marriage', 'Separated', 'Widow']
house_type = ['House / apartment', 'With parents', 'Municipal apartment', 'Rented apartment', 'Office apartment']
occupation = [
            'Security staff',
            'Sales staff',
            'Accountants',
            'Laborers', 
            'Managers',
            'Drivers',
            'Core Staff',
            'High skill tech staff',
            'Cleaning staff',
            'Private service staff',
            'Cooking staff',
            'Low-skill Laborers',
            'Medicine staff',
            'Secretaries',
            'Waiters/barmen staff',
            'HR staff',
            'Realty agents',
            'IT staff'
            
            ]

map_income_type = dict(zip(income_type,range(len(income_type))))
map_education_type = dict(zip(education_type,range(len(education_type))))
map_family_status = dict(zip(family_status,range(len(family_status))))
map_house_type = dict(zip(house_type,range(len(house_type))))
map_occupation = dict(zip(occupation,range(len(occupation))))



layout = [
    [sg.Text('Name', size=size), sg.InputText(size=size_input,key="--name-in--")],
    [sg.Text('CPF', size=size), sg.InputText(size=size_input,key="--cpf-in--")],
    [sg.Text('Gender',size=size) ,sg.Combo(['Masculine', 'Feminine'],key="--gender-in--",size=size)],
    [sg.Text('Own Car?',size=size), sg.Combo(['Yes', 'No'],size=size,key="--car-in--")],
    [sg.Text('Own Realty?',size=size), sg.Combo(['Yes', 'No'],size=size,key="--realty-in--")],
    [sg.Text('Number of childrens', size=size), sg.InputText(size=size_input,key="--childs-in--")],
    [sg.Text('Income Total', size=size), sg.InputText(size=size_input,key="--income-in--")],
    [
        sg.Text('Income Type', size=size),
        sg.Combo(income_type ,size=size,key="--income_type-in--")
    ],
    [
        sg.Text('Education Type', size=size),
        sg.Combo(education_type,size=size,key="--education_type-in--"),   
    ],
    [
        sg.Text('Family Status',size=size),
        sg.Combo(family_status,size=size,key="--family-in--")
        
    ],
    
    [
        sg.Text('Housing Type',size=size),
        sg.Combo(house_type,size=size,key="--housing_type-in--")
    ],
    [sg.Text('Phone',size=size) ,sg.Combo(['Yes', 'No'],key="--phone-in--",size=size)],
    [sg.Text('Work Phone',size=size) ,sg.Combo(['Yes', 'No'],key="--work_phone-in--",size=size)],
    [sg.Text('Mobile Phone',size=size) ,sg.Combo(['Yes', 'No'],key="--mobil_phone-in--",size=size)],
    [sg.Text('Email',size=size) ,sg.Combo(['Yes', 'No'],key="--email-in--",size=size)],
    [sg.Text('Days Birthday',size=size) ,sg.InputText(size=size_input,key="--days_birth-in--")],
    [sg.Text('Days Employed',size=size) ,sg.InputText(size=size_input,key="--days_emplo-in--")],
    [sg.Text('Fam. Members',size=size) ,sg.InputText(size=size_input,key="--fam_members-in--")],
    [
        sg.Text('Occupation',size=size) ,
        sg.Combo(occupation,size=size,key="--occupation-in--")
    ],


    [sg.Button("Send"), sg.Cancel()]
]

window = sg.Window('Client Credit Type Information', layout)
while(True):
    event, values = window.read()
    if((event == "Cancel") or (event == sg.WIN_CLOSED)):
        window.close()
        break
    else:
        val = np.array([
            0 if "M" in values["--gender-in--"] else 1,
            0 if "Y" in values["--car-in--"] else 1,
            0 if "Y" in values["--realty-in--"] else 1,
            0 if '' == values["--childs-in--"] else int(values["--childs-in--"]),
            0 if '' == values["--income-in--"] else float(values["--income-in--"]),
            0 if '' in values["--income_type-in--"] else map_income_type[values["--income_type-in--"]],
            0 if '' in values["--education_type-in--"] else map_education_type[values["--education_type-in--"]],
            0 if '' in values["--family-in--"] else map_family_status[values["--family-in--"]],
            0 if '' == values["--housing_type-in--"] else map_house_type[values["--housing_type-in--"]],
            0,
            0 if '' == values["--days_emplo-in--"] else int(values["--days_emplo-in--"]),
            0 if "Y" in values["--mobil_phone-in--"] else 1,
            0 if "Y" in values["--work_phone-in--"] else 1,
            0 if "Y" in values["--phone-in--"] else 1,
            0 if "Y" in values["--email-in--"] else 1,
            0 if '' == values["--fam_members-in--"] else int(values["--fam_members-in--"]),
            0 if '' in values["--occupation-in--"] else map_occupation[values["--occupation-in--"]],
            0
        ]).reshape(1, -1)
        sg.Popup(f"{'Bad' if model.predict(val)[0] == 0 else 'Good'} client")