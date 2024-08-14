from datetime import datetime
import speech_recognition as sr
import pyttsx3 
import webbrowser
import wikipedia
import wolframalpha

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
activationWords = ['computer', 'hey computer']

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

appId = 'J3LGLE-2LQU99E4XL'
wolframClient = wolframalpha.Client(appId)

def speak(text, rate=120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    listener = sr.Recognizer()
    print('Listening for a command')
    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try: 
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en_gb')
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('I did not quite catch that')
        speak('I did not quite catch that')
        print(exception)
        return 'None'
    
    return query

def search_wikipedia(query=''):
    searchResults = wikipedia.search(query)
    if not searchResults:
        print('No Wikipedia result')
        return 'No result received'
    try: 
        wikiPage = wikipedia.page(searchResults[0])
    except wikipedia.DisambiguationError as error:
        wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    return wikiSummary

def listOrDict(var):
    if isinstance(var, list):
        return var[0]['plaintext']
    else:
        return var['plaintext']

def search_wolframAlpha(query=''):
    response = wolframClient.query(query)
    if response['@success'] == 'false':
        return 'Could not compute'
    
    result = ''
    pod0 = response['pod'][0]
    pod1 = response['pod'][1]

    if ('result' in pod1['@title'].lower()) or (pod1.get('@primary', 'false') == 'true') or ('definition' in pod1['@title'].lower()):
        result = listOrDict(pod1['subpod'])
        return result.split('(')[0]
    else: 
        question = listOrDict(pod0['subpod'])
        return question.split('(')[0]

if __name__ == '__main__':
    speak('All systems nominal.')

    while True:
        query = parseCommand().lower().split()
        if any(word in query for word in activationWords):
            query = [word for word in query if word not in activationWords]

            if query[0] == 'say':
                if 'hello' in query:
                    speak('Greetings, all.')
                else: 
                    query.pop(0)
                    speech = ' '.join(query)
                    speak(speech)

            elif query[0] == 'go' and query[1] == 'to':
                speak('Opening...')
                query = ' '.join(query[2:])
                webbrowser.get('chrome').open_new(query)

            elif query[0] == 'wikipedia':
                query = ' '.join(query[1:])
                speak('Querying the universal databank.')
                speak(search_wikipedia(query))
                
            elif query[0] in ['compute', 'computer']:
                query = ' '.join(query[1:])
                speak('Computing')
                try: 
                    result = search_wolframAlpha(query)
                    speak(result)
                except:
                    speak('Unable to compute.')

            elif query[0] == 'log':
                speak('Ready to record your note')
                newNote = parseCommand().lower()
                now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                try:
                    with open(f'note_{now}.txt', 'w') as newFile:
                        newFile.write(newNote)
                    speak('Note written')
                except Exception as e:
                    speak('Failed to write note.')
                    print(e)

            elif query[0] == 'help':
                help_message = "Available commands are: say, go to, wikipedia, compute, log, exit."
                speak(help_message)

            elif query[0] == 'exit':
                speak('Goodbye')
                break
