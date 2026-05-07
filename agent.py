import json
import os
from datetime import date
from typing import List
from pydantic import BaseModel
from openai import OpenAI

# 1. Define the Schema using Pydantic for Structured Outputs
class AgendaItem(BaseModel):
    topic: str
    time_minutes: int
    owner: str
    outcome: str

class MeetingAgenda(BaseModel):
    meeting_title: str
    objective: str
    total_duration_minutes: int
    agenda: List[AgendaItem]

# Initialize Client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a Meeting Agenda Generator Agent.
Your job is to generate a clear, time-boxed meeting agenda based on the user's input.

Rules:
- The sum of 'time_minutes' must equal the total duration provided or requested.
- Focus strictly on the meeting objective.
- Identify specific decision points for 'outcome' fields.
"""

def read_input(path="meeting.txt"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Error: {path} not found. Creating a dummy input file.")
        with open(path, "w", encoding="utf-8") as f:
            f.write("Project Kickoff meeting for 'Apollo'. 60 minutes. Need to define roles and timeline.")
        return "Project Kickoff meeting for 'Apollo'. 60 minutes."

def generate_agenda(meeting_text: str) -> MeetingAgenda:
    try:
        # Using beta.chat.completions.parse for native Pydantic support
        response = client.beta.chat.completions.parse(
            model="gpt-4o-mini",  # Corrected model name
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": meeting_text}
            ],
            response_format=MeetingAgenda,
            temperature=0.3
        )
        return response.choices[0].message.parsed
    except Exception as e:
        print(f"API Error: {e}")
        raise

def save_outputs(data: MeetingAgenda):
    # Save as JSON
    with open("agenda.json", "w", encoding="utf-8") as f:
        f.write(data.model_dump_json(indent=2))

    # Save as Human-Readable Text
    with open("agenda.txt", "w", encoding="utf-8") as f:
        f.write(f"Meeting Agenda ({date.today()})\n")
        f.write("=" * 45 + "\n\n")
        f.write(f"Title: {data.meeting_title}\n")
        f.write(f"Objective: {data.objective}\n")
        f.write(f"Duration: {data.total_duration_minutes} minutes\n\n")

        for i, item in enumerate(data.agenda, 1):
            f.write(f"{i}. {item.topic} ({item.time_minutes} min)\n")
            f.write(f"   Owner: {item.owner}\n")
            f.write(f"   Outcome: {item.outcome}\n\n")

def main():
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set.")
        return

    meeting_text = read_input()
    print("Generating agenda...")
    
    agenda = generate_agenda(meeting_text)
    save_outputs(agenda)
    
    print("-" * 20)
    print(f"SUCCESS: 'agenda.json' and 'agenda.txt' have been updated.")
    print(f"Title: {agenda.meeting_title}")
    print("-" * 20)

if __name__ == "__main__":
    main()