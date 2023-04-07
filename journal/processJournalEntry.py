
def processJournalEntry(request):
    if request.method == "POST":
        print("Hello")
        return True
    else:
        return False