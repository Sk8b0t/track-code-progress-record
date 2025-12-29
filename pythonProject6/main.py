import webbrowser

url = 'https://www.youtube.com'

# Open 100 tabs
for i in range(100):
    webbrowser.open_new_tab(url)
