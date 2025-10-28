# social_engineering_standalone.py
import json
from datetime import datetime

class SocialEngineeringSimulator:
    def __init__(self):
        self.scenarios = self.load_scenarios()
        self.current_session = None
    
    def load_scenarios(self):
        return {
            "1": {
                "name": "Email Phishing Attack",
                "description": "Identify suspicious emails and avoid falling for phishing attempts",
                "steps": [
                    {
                        "message": "You receive an email from 'security@yourbank.com' saying:\n'URGENT: Your account has been compromised! Click here to verify your identity: http://fake-bank-security.com'\n\nWhat do you do?",
                        "choices": [
                            {"text": "Click the link to verify", "risk": "High", "feedback": "Never click links in suspicious emails. Always visit websites directly."},
                            {"text": "Check the sender's email address", "risk": "Low", "feedback": "Good! Always verify sender addresses."},
                            {"text": "Forward to bank's security team", "risk": "Low", "feedback": "Excellent! Forward suspicious emails to legitimate security teams."}
                        ]
                    },
                    {
                        "message": "The email asks for your password and Social Security Number to 'verify your account'.",
                        "choices": [
                            {"text": "Provide the information", "risk": "High", "feedback": "Never provide sensitive information via email links."},
                            {"text": "Ignore and delete the email", "risk": "Low", "feedback": "Good choice! When in doubt, delete suspicious emails."},
                            {"text": "Contact bank directly", "risk": "Low", "feedback": "Perfect! Always use verified contact methods."}
                        ]
                    }
                ]
            },
            "2": {
                "name": "Fake Tech Support Scam", 
                "description": "Recognize and handle fake tech support calls",
                "steps": [
                    {
                        "message": "You receive a call: 'Hello, I'm from Microsoft. We've detected viruses on your computer.'",
                        "choices": [
                            {"text": "Follow their instructions", "risk": "High", "feedback": "Legitimate companies don't make unsolicited support calls."},
                            {"text": "Ask for verification", "risk": "Medium", "feedback": "Be careful - scammers often provide fake information."},
                            {"text": "Hang up immediately", "risk": "Low", "feedback": "Correct! Unsolicited tech support calls are almost always scams."}
                        ]
                    },
                    {
                        "message": "The caller says: 'I need remote access to your computer to fix the viruses immediately!'",
                        "choices": [
                            {"text": "Give them remote access", "risk": "High", "feedback": "Never give remote access to unsolicited callers!"},
                            {"text": "Say you'll call Microsoft directly", "risk": "Low", "feedback": "Smart! Always use official contact numbers."},
                            {"text": "Ask for a callback number", "risk": "Medium", "feedback": "Better to hang up and call the official support line."}
                        ]
                    }
                ]
            },
            "3": {
                "name": "Impersonation via Chat or Call",
                "description": "Handle impersonation attempts through phone calls and messaging",
                "steps": [
                    {
                        "message": "You get a call from 'IT Support': 'We need to verify your login credentials for system maintenance. Can you provide your username and password?'",
                        "choices": [
                            {"text": "Provide your credentials", "risk": "High", "feedback": "Never share login credentials over the phone!"},
                            {"text": "Ask for ID and call back main IT line", "risk": "Low", "feedback": "Excellent! Always verify through official channels."},
                            {"text": "Transfer to your manager", "risk": "Medium", "feedback": "Good, but better to contact IT directly."}
                        ]
                    },
                    {
                        "message": "A WhatsApp message from 'your boss': 'Urgent! Need you to buy gift cards for client meeting. Send codes to my personal email.'",
                        "choices": [
                            {"text": "Buy and send gift cards", "risk": "High", "feedback": "This is a common impersonation scam!"},
                            {"text": "Call boss's official number to verify", "risk": "Low", "feedback": "Perfect! Always verify unusual requests."},
                            {"text": "Ask why they need gift cards", "risk": "Medium", "feedback": "Good to question, but still verify officially."}
                        ]
                    },
                    {
                        "message": "Call from 'HR': 'We're processing bonuses and need your bank details for direct deposit verification.'",
                        "choices": [
                            {"text": "Provide bank account details", "risk": "High", "feedback": "Never share financial info on unsolicited calls!"},
                            {"text": "Visit HR in person", "risk": "Low", "feedback": "Excellent! In-person verification is safest."},
                            {"text": "Ask for official HR email", "risk": "Low", "feedback": "Good approach using official channels."}
                        ]
                    }
                ]
            }
        }

    def start_session(self):
        self.current_session = {
            'start_time': datetime.now(),
            'choices': [],
            'score': 100
        }
        print("=== Social Engineering Awareness Simulator ===")
        print("Welcome! This simulator will help you recognize social engineering attacks.")
        return True
    
    def show_scenarios(self):
        print("\nAvailable Scenarios:")
        for key, scenario in self.scenarios.items():
            print(f"{key}. {scenario['name']} - {scenario['description']}")
    
    def run_scenario(self, scenario_id):
        if scenario_id not in self.scenarios:
            print("Invalid scenario selection.")
            return
        
        scenario = self.scenarios[scenario_id]
        print(f"\n=== {scenario['name']} ===")
        print(scenario['description'])
        print("-" * 50)
        
        for step in scenario['steps']:
            print(f"\n{step['message']}\n")
            
            # Show choices
            for i, choice in enumerate(step['choices'], 1):
                print(f"{i}. {choice['text']}")
            
            # Get user choice
            while True:
                try:
                    user_choice = int(input("\nEnter your choice (1-3): ")) - 1
                    if 0 <= user_choice < len(step['choices']):
                        break
                    else:
                        print("Invalid choice. Please enter 1, 2, or 3.")
                except ValueError:
                    print("Please enter a valid number.")
            
            selected_choice = step['choices'][user_choice]
            
            # Show feedback
            print(f"\n=== FEEDBACK ===")
            risk_color = {
                "High": "RED",
                "Medium": "YELLOW", 
                "Low": "GREEN"
            }[selected_choice['risk']]
            print(f"Risk Level: {risk_color}")
            print(f"Feedback: {selected_choice['feedback']}")
            
            # Update score
            risk_penalty = {"Low": 0, "Medium": 10, "High": 25}[selected_choice['risk']]
            self.current_session['score'] = max(0, self.current_session['score'] - risk_penalty)
            self.current_session['choices'].append(selected_choice)
            
            print(f"Current Score: {self.current_session['score']}%")
            input("\nPress Enter to continue...")
    
    def show_results(self):
        print("\n" + "="*50)
        print("TRAINING COMPLETE!")
        print(f"Final Score: {self.current_session['score']}%")
        print("="*50)
        
        if self.current_session['score'] >= 80:
            print("🎉 Excellent! You have strong security awareness.")
        elif self.current_session['score'] >= 60:
            print("👍 Good! You have basic security awareness but can improve.")
        else:
            print("⚠️ Be careful! You need to improve your security awareness.")
        
        print("\nKey Lessons Learned:")
        high_risk_choices = [c for c in self.current_session['choices'] if c['risk'] != "Low"]
        if high_risk_choices:
            for choice in high_risk_choices:
                print(f"- {choice['feedback']}")
        else:
            print("- You made safe choices throughout the simulation!")

def main():
    simulator = SocialEngineeringSimulator()
    
    while True:
        simulator.start_session()
        simulator.show_scenarios()
        
        try:
            scenario_choice = input("\nSelect a scenario (1-3) or 'q' to quit: ")
            if scenario_choice.lower() == 'q':
                break
            
            if scenario_choice not in ['1', '2', '3']:
                print("Please select 1, 2, or 3")
                continue
            
            simulator.run_scenario(scenario_choice)
            simulator.show_results()
            
            continue_choice = input("\nWould you like to try another scenario? (y/n): ")
            if continue_choice.lower() != 'y':
                break
                
        except KeyboardInterrupt:
            print("\n\nThank you for using the Social Engineering Simulator!")
            break

if __name__ == "__main__":
    main()
