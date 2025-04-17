main.py

from modules.sherlock_runner import run_sherlock from modules.maigret_runner import run_maigret from modules.holehe_runner import run_holehe from modules.phoneinfoga_runner import run_phoneinfoga from modules.harvester_runner import run_theharvester from modules.ghunt_runner import run_ghunt from modules.social_analyzer_runner import run_social_analyzer

def main(): target = input("أدخل اسم المستخدم أو البريد الإلكتروني أو الرقم: ")

print("\n[1] Sherlock")
run_sherlock(target)

print("\n[2] Maigret")
run_maigret(target)

print("\n[3] Holehe")
run_holehe(target)

print("\n[4] PhoneInfoga")
run_phoneinfoga(target)

print("\n[5] theHarvester")
run_theharvester(target)

print("\n[6] GHunt")
run_ghunt(target)

print("\n[7] Social Analyzer")
run_social_analyzer(target)

if name == "main": main()

modules/sherlock_runner.py

import os

def run_sherlock(username): os.system(f"sherlock {username} --print-all")

modules/maigret_runner.py

import os

def run_maigret(username): os.system(f"maigret {username} -a")

modules/holehe_runner.py

import os

def run_holehe(email): os.system(f"holehe {email}")

modules/phoneinfoga_runner.py

import os

def run_phoneinfoga(phone): os.system(f"phoneinfoga scan -n {phone}")

modules/harvester_runner.py

import os

def run_theharvester(query): os.system(f"theHarvester -d {query} -b all")

modules/ghunt_runner.py

import os

def run_ghunt(email): os.system(f"python3 GHunt/ghunt.py email {email}")

modules/social_analyzer_runner.py

import os

def run_social_analyzer(target): os.system(f"python3 social-analyzer/analyze.py -u {target}")

