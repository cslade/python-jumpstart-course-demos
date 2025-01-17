import journal


journal_entries = []

def main():
    header()
    run_event_loop()
    
    
def header():
    print("-----------------------", end:="\n")
    print("PERSONAL JOURNAL APP   ", end:="\n")
    print("-----------------------", end:="\n")
    
    
def run_event_loop():
    print("What do you want to do with your journal?")
    cmd = "EMPTY"
    journal_name = "default"
    journal_data = journal.load(journal_name) # [] # list()
    
    while cmd != 'x' and cmd:
        cmd =input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()
        
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print(f'Sorry not sure what you are doing with {cmd}')
            
    print('Done, goodbye. ')
    journal.save(journal_name, journal_data)
    
    

def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)
    # data.append(text)

# print("__file__ " + __file__)
# print("__name__ " + __name__)
    
if __name__ == '__main__':
    main()