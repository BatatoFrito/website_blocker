'''

This program blocks websites

'''

from pathlib import Path
import os
import sys

def clear():
    return os.system('cls')

def pause():
    return os.system('pause')

def close():
    clear()
    return sys.exit()

class Website_Blocker:
    def __init__(self, hosts: Path, redirect: str) -> None:
        self.hosts = hosts
        self.redirect = redirect
        self.menu_choices = {('B', 'BLOCK', '[B]lock a website'): self.block,
                ('U', 'UNBLOCK', '[U]nblock a website'): self.unblock,
                ('C', 'CLOSE', '[C]lose the website blocker'): close}

    # Blocks a website
    def block(self):
        clear()

        # Asks for website to block
        blocked_website = input('Write the name of the website you would like to block: ')
        clear()

        # Not allow specific urls
        if not blocked_website or blocked_website == 'localhost':
            print("Not an allowed URL...\n")
            pause()
            clear()
            return

        # Saves the blocked website
        confirmation = input('Are you sure you want to block this website? (Y/N): ').upper()
        if confirmation.startswith('Y'):
            with open(self.hosts, 'a+') as f:
                f.write(f'\n{redirect} {blocked_website}')
        clear()

    # Unblocks a blocked website
    def unblock(self):
        clear()

        # Asks for website to be unblocked
        unblocked_website = input('Write the name of the website you would like to unblock: ')
        clear()

        # Not allow specific urls
        if not unblocked_website or unblocked_website == 'localhost':
            print("Not an allowed URL...\n")
            pause()
            clear()
            return

        # Unblocks the website
        confirmation = input('Are you sure you want to delete this contact? (Y/N): ').upper()
        if confirmation.startswith('Y'):
            clear()
            with open(self.hosts, 'r') as f:
                f.seek(0)
                hosts_text = f.read()
            
            # Looks for website in hosts file
            if f'{redirect} {unblocked_website}' in hosts_text:
                hosts_text = hosts_text.replace(f'{redirect} {unblocked_website}', '')
                with open(self.hosts, 'w+') as f:
                    f.seek(0)
                    f.write(hosts_text)
            else:
                print('URL not in hosts file...\n')
                pause()
        clear()
    
    # Brings up a menu to use the website blocker
    def menu(self):
        clear()
        while True:
            choices_str = ''
            for choice in self.menu_choices.keys():
                choices_str += f'{choice[-1]} | '
            choices_str = choices_str[:-3]
            print(f'What would you like to do?\n\n{choices_str}\n')
            choice_selected = input().upper()

            for choice in self.menu_choices.keys():
                if choice_selected in choice:
                    self.menu_choices[choice]()

if __name__ == '__main__':
    # This program requires administrative permissions
    HOSTS_FILE = 'C:\\Windows\\system32\\drivers\\etc\\hosts'
    redirect = '127.0.0.1'

    blocker = Website_Blocker(HOSTS_FILE, redirect)
    blocker.menu()