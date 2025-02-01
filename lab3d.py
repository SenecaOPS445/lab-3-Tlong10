#!/usr/bin/env python3

#Author ID: TLONG10

import os

command = "df -h | grep '/$' | awk '{print $4}'" #Varriable for command

def free_space():   
        result = os.popen(command).read().strip() #Function returning in utf-8 with newline chracter strip
        return result

if __name__ == "__main__":
    print(free_space())
