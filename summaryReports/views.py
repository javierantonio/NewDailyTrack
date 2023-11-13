from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from registration.models import Specialist, Profile

from steppingStones.models import SteppingStone
from appointments.models import Appointments
from patientDirectory.models import PatientList

import plotly.express as px
import pandas as pd

def summaries(request):
    mood_data = list()

    userProfile = Profile.objects.get(user=request.user)
    patients = PatientList.objects.filter(specialist = Specialist.objects.get(profile = userProfile))
    usersList = [person.patient for person in patients]
    
    if not usersList:
        return render(request, 'summaryEmptyPatient.html')

    for user in usersList:
        mood_data.extend(SteppingStone.objects.filter(patient = user).values())
        # print(mood_data)
    # Get data for mood levels
    # mood_data = SteppingStone.objects.all()
    mood_df = pd.DataFrame.from_records(mood_data)
    print(mood_df.columns)

    # Get data for appointment status
    appointment_data = Appointments.objects.all()
    appointment_df = pd.DataFrame.from_records(appointment_data.values())

    mood_value_counts = mood_df['moodLevel'].value_counts().reset_index()
    mood_value_counts.columns = ['value', 'count']

    area = px.area(mood_value_counts, 
                  x='value',
                  y='count',
                  title='Emoticards',
                 )    
    
    area.update_layout(
        xaxis_title='Moods',
        yaxis_title='Frequency',
        title_text='Mood Frequency',
    )

    area.update_xaxes(
        tickvals=[1, 2, 3, 4, 5],
        ticktext=['Terrible', 'Bad', 'Okay', 'Good', 'Awesome']
    )

    area.update_traces(
        fill='tozeroy',  # Fill below the curve
        line_shape='linear',  # Adjust the line shape
        line=dict(width=1),  # Adjust the line width
        hovertemplate='%{x}: %{y}',  # Tooltip format
    )

    print(mood_data)
    line = px.line(x=[c['created_at'] for c in mood_data],
                  y=[c['moodLevel'] for c in mood_data],
                  title='Mood Fluctuations',
                  labels={'x': 'Date', 'y': 'Mood Levels'},
    )
    
    line.update_layout(
        autosize=True,
    )

    # Create Donut chart for appointment status distribution
    appointment_status_counts = appointment_df['status'].value_counts().reset_index()
    appointment_status_counts.columns = ['Status', 'Count']
    donut = px.pie(appointment_status_counts, names='Status', title='Appointment Status Distribution', hole=0.4)
    donut.update_traces(textinfo='percent+label', pull=[0.1, 0.1, 0.1])
    donut.update_layout(showlegend=False)

    # Create a stacked bar chart for mood categories
    stacked_bar = px.bar(mood_value_counts, x='value', y='count', color='value',
                        title='Mood Categories Distribution',
                        labels={'value': 'Mood Category', 'count': 'Number of Patients'})

    stacked_bar.update_layout(barmode='stack')  # Set the bar mode to 'stack' for a stacked bar chart

    areaChart = area.to_html()
    lineChart = line.to_html()
    donutChart = donut.to_html()
    stackedBarChart = stacked_bar.to_html()

    context = {'line': lineChart, 'area': areaChart, 'donut': donutChart, 'stacked_bar': stackedBarChart}
    return render(request, 'summaryCharts.html', context)
