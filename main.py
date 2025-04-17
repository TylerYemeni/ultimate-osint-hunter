نقطة البداية للأداة

import argparse from modules import sherlock_runner, maigret_runner, phoneinfoga_runner from modules import holehe_runner, theharvester_runner, ghunt_runner from modules import social_analyzer_runner

def run_all(username=None, email=None, phone=None): if username: print("\n[+] Running Sherlock...") sherlock_runner.run(username)

print("\n[+] Running Maigret...")
    maigret_runner.run(username)

    print("\n[+] Running Social Analyzer...")
    social_analyzer_runner.run(username)

if email:
    print("\n[+] Running Holehe...")
    holehe_runner.run(email)

    print("\n[+] Running GHunt...")
    ghunt_runner.run(email)

if phone:
    print("\n[+] Running PhoneInfoga...")
    phoneinfoga_runner.run(phone)

print("\n[+] Running theHarvester...")
theharvester_runner.run(email=email, domain=username)

if name == "main": parser = argparse.ArgumentParser(description="Ultimate OSINT Hunter") parser.add_argument("--username", help="Username to investigate") parser.add_argument("--email", help="Email address to investigate") parser.add_argument("--phone", help="Phone number to investigate") args = parser.parse_args()

run_all(username=args.username, email=args.email, phone=args.phone)

