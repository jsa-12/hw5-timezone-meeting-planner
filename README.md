# Timezone Meeting Planner Skill

## What the skill does
This skill converts one meeting time into multiple time zones and checks whether each converted time falls inside normal work hours.

## Why I chose it
I chose this skill because time-zone conversion is a narrow task where code is genuinely useful. A language model can explain time zones, but Python is better for exact date and time conversion.

## How to use it
Run the Python script with a date, time, source time zone, and target time zones.

Example:

```bash
python3 .agents/skills/timezone-meeting-planner/scripts/timezone_meeting_planner.py
```bash
## What worked well
The skill is simple, reusable, and demonstrates a clear use of deterministic code. The Python script handles time zone conversion reliably, which is difficult to do consistently with a language model alone.

## Limitations
This skill uses a fixed example inside the script and does not yet accept dynamic user input. It also assumes standard 9 AM–5 PM work hours for all regions.
