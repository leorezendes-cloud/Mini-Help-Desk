#!/usr/bin/env python3   

from ast import If


def menu_option():
    print()
    print('Would you like to go back to the main menu?')
    print()
    print('1. Yes')
    print('2. No')
    menu_choice = input('Please enter the number of your answer: ')
    if menu_choice == '1':
        return True
    elif menu_choice == '2':
        return False
    else:
        print('Invalid choice. 1. = Yes, 2. = No, Please try again.')
        return menu_option()


    
def get_menu_choice(number_of_choices):
    try:
        choice_1 = int(input('Please enter the number to your problem: '))
    except ValueError:
        print(f'Your choice has to be a number between 1 and {number_of_choices}')
        return get_menu_choice(number_of_choices)
    if 1 <= choice_1 <= number_of_choices:
        return choice_1
    else:
        print(f'Your choice has to be a number between 1 and {number_of_choices}')
        return get_menu_choice(number_of_choices)


    
def get_choice(number_of_choices):
    try:
        choice = int(input('Please enter the number of your answer: '))
    except ValueError:
        print(f'Your choice has to be a number between 1 and {number_of_choices}')
        return get_choice(number_of_choices)
    if 1 <= choice <= number_of_choices:
        return choice
    else:
        print(f'Your choice has to be a number between 1 and {number_of_choices}')
        return get_choice(number_of_choices)


while True:
    print('\n')

    print(f'=====================================')
    print(f'=====================================')
    print(f'   Welcome to the Mini Help Desk ')  
    print(f'=====================================')
    print(f'=====================================')
    print('\n')
    print('What problem are you having today?')
    print()
    print('1. No Internet')
    print("2. Website won't load")
    print('3. Computer is slow')
    print()
    choice = get_menu_choice(3)

    match choice:
        case 1:
            print()
            print('Are you connected to wifi?')
            print()
            print('1. Yes')
            print('2. No')
            print()
            wifi_choice = get_choice(2)
            match wifi_choice:
                case 1:
                    print()
                    print('1.Do you have a valid IP address?')
                    print('2.Have you tried restarting your router?')
                    print('3.Can you ping your router?')
                    second_wifi_choice = get_choice(3)
                    match second_wifi_choice:
                        case 1:
                            print()
                            print('Check your network settings and make sure you have a valid IP address.')
                            print('Use command ipconfig to confirm.')
                            print('If you do not have a valid IP address, check your network settings and try to obtain a valid IP address.')
                            print()
                            if menu_option():
                                continue
                            else:
                                break
                        case 2:
                            print()
                            print('Try restarting your router and computer.')
                            print()
                            if menu_option():
                                continue
                            else:
                                print('Thank you for using the Mini Help Desk. Goodbye!')
                                break
                        case 3:
                            print()
                            print('Try pinging your router to check connectivity.')
                            print('Use command route -n get default to get the default gateway.')
                            print('Use command ping <router IP address>/<default gateway IP address> to check connectivity.')
                            print('If you cannot ping your router, the issue may be with your router or network settings.')
                            print()
                            if menu_option():
                                continue
                            else:
                                break
                case 2:
                    print()
                    print('Check if your ethernet cable is connected and router is powered on.')
                    print('If it is, try restarting your router and computer.')
                    print('If that does not work, contact your ISP for further assistance.')
                    print()
                    if menu_option():
                        continue
                    else:
                        print('Thank you for using the Mini Help Desk. Goodbye!')
                        break
        case 2:
            print()
            print('1. Is there a tcp connection established?')
            print('2. Is the website down for everyone or just you?')
            print('3. Have you tried clearing your browser cache?')
            print()
            website_choice = get_choice(3)
            match website_choice:
                case 1:
                    print()
                    print('Check tcp connection and ports using nc -vz <website> <port>')
                    print('If there is no tcp connection, the issue may be with your network settings or firewall.')
                    print('If there is a tcp connection, what is the response code? If it is 4xx or 5xx, the issue may be with the website itself.')
                    print()
                    if menu_option():
                        continue
                    else:
                        print('Thank you for using the Mini Help Desk. Goodbye!')
                        break
                case 2:
                    print()
                    print('Check if the website is down for everyone or just for you')
                    print('Test another website to see if it loads. If it does, the issue may be with the website itself.')
                    print('If it does not, try to ping 1.1.1.1')
                    print('If you can ping 1.1.1.1, the issue may be with your DNS settings.')
                    print('Use command nslookup <website> to check if the website resolves to an IP address.')
                    print('If it does not, the issue may be with your DNS settings or the website itself.')
                    print()
                    if menu_option():
                        continue
                    else:
                        print('Thank you for using the Mini Help Desk. Goodbye!')
                        break
                case 3:
                    print()
                    print('Try clearing your browser cache and cookies.')
                    print('If that does not work, try using a different browser or device to access the website.')
                    print('If the issue persists, contact the website administrator for further assistance.')
                    print()
                    if menu_option():
                        continue
                    else:
                        print('Thank you for using the Mini Help Desk. Goodbye!')
                        break
        case 3:
            print()
            print('Try restarting your computer and closing any unnecessary programs or browser tabs.')
            print('Check for malware or viruses using a reputable antivirus program.')
            print('Any software/hardware updates can cause strain on your computer especially if its not compatible with your system.')
            print('Check Activity Monitor/Task Manager to see if any processes are using a lot of resources.')
            print('Use commands like vmstat, df -h, to check for disk usage and memory usage.')
            print('If the issue persists, contact a computer technician for further assistance.')
            print()
            if menu_option():
                continue
            else:
                print('Thank you for using the Mini Help Desk. Goodbye!')
                break
                          
                          
                
