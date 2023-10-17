from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from steppingStones.models import SteppingStone

import plotly.express as px
import pandas as pd

def summaries(request):
    data = SteppingStone.objects.all().order_by('-created_at')

    dataFrame = pd.DataFrame.from_records(data.values())
    dataFrame['created_at'] = pd.to_datetime(dataFrame['created_at'])
    value_counts = dataFrame['moodLevel'].value_counts().reset_index()
    value_counts.columns = ['value', 'count']


    area= px.area(value_counts, 
                  x= 'value',
                  y= "count",
                  title="Emoticards",
                 )    
    
    area.update_layout(
        xaxis_title='Moods',
        yaxis_title='Frequency',
        title_text='Mood Frequency',
    )

    area.update_xaxes(
        tickvals=[1,2,3,4,5],
        ticktext=['Terrible', 'Bad', 'Okay', 'Good', 'Awesome'])

    area.update_traces(
        fill='tozeroy',  # Fill below the curve
        line_shape='linear',  # Adjust the line shape
        line=dict(width=1),  # Adjust the line width
        hovertemplate='%{x}: %{y}',  # Tooltip format
    )

    
    line = px.line(x= [c.created_at for c in data],
                  y= [c.moodLevel for c in data],
                  title="Mood Fluctuations",
                  labels={'x': 'Date', 'y': 'Mood Levels'},
                  )
    
    line.update_layout(
        autosize = True,
    )
    
    
    areaChart = area.to_html()
    lineChart = line.to_html()

    context={'line':lineChart,'area': areaChart}
    return render(request, 'summaryCharts.html', context)