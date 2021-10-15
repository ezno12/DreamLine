import forms, routes, models

#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    forms.app.run(debug=True)