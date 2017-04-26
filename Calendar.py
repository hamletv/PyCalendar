'''Calendar that user can interact with from command line. User will be able to view calendar; add event to calendar; update existing event; delete existing event.'''
from time import sleep, strftime

USERS_NAME = raw_input('Max Powers')

calendar = {}

def welcome(): # welcome to calendar function
    print 'Welcome to your calendar %s' % (USERS_NAME)
    print 'The calendar is opening, please wait'
    sleep(1)
    print 'Today is: ' + strftime('%A %B %d, %Y') #full weekday name / Month day / Year
    print 'The current time is: ' + strftime('%H:%M:%S')
    sleep(1)
    print 'What would you like to do?'
	
def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = raw_input('Enter what you\'d like to do? Enter A to Add, U to Update, V to View, D to Delete, X to Edit:')
        user_choice = user_choice.upper()
    if user_choice == 'V':
        if len(calendar.keys()) < 1:
            print 'The calendar is empty.'
		else:
			print calendar
    elif user_choice == 'U':
        date = raw_input('What date?')
        update = raw_input('Enter the update:')
	    calendar[date] = update
        print 'Your update has been added!'
        print calendar
    elif user_choice == 'A':
        event = raw_input('Enter event:')
        date = raw_input('Enter date (MM/DD/YYYY):')
        if (len(date) > 10) or int(date[6:]) < int(strftime('%Y')):
            print 'An invalid date was entered.'
            try_again = raw_input('Try Again? Y for Yes, N for No:')
            try_again = try_again.upper()
        	if try_again == 'Y':
            	continue
        	else:
            	start = False
        else:
            calendar[date] = event
            print 'Your event has been added!'
            print calendar
    elif user_choice == 'D':
        if len(calendar.keys()) < 1:
            print 'The calendar is empty.'
        else:
            event = raw_input('What event?')
            for date in calendar.keys():
                if event == calendar[date]:
                    del(calendar[date])
                    print 'The event has been deleted.'
                    print calendar
                else:
                    print 'An incorrect event was specified.'
    elif user_choice == 'X':
        start = False
    else:
        print 'Invalid command entered. Goodbye.'
        exit()

start_calendar()
