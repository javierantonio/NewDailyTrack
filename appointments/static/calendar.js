fetch('/appointments/calendar')
  .then((response) => response.json())
  .then((data) => {
    // Process the data and populate the Tui Calendar
    // For example, add events to the calendar
    // Sample code:
    const calendar = new tui.Calendar(document.getElementById('calendar'), {
      defaultView: 'week',
      taskView: true,
      scheduleView: true,
    });

    const schedules = data.map((event) => ({
      id: event.id,
      calendarId: '1',
      title: 'Scheduled Appointment',
      start: event.start,
      end: event.end,
    }));

    calendar.createSchedules(schedules);
  });
