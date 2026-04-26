---
name: timezone-meeting-planner
description: Converts a proposed meeting time into multiple time zones and flags whether each time is inside normal work hours. Use when scheduling meetings across locations.
---

# Timezone Meeting Planner

## When to use
Use this skill when a user gives a meeting time and wants to compare it across different time zones.

## When not to use
Do not use this skill for general calendar management or creating calendar invites.

## Expected inputs
- Meeting date (YYYY-MM-DD)
- Meeting time (HH:MM)
- Original time zone (e.g., America/New_York)
- Target time zones (list)

## Steps
1. Ask for any missing date, time, or time zones.
2. Run the Python script in `scripts/timezone_meeting_planner.py`.
3. Convert the time into each target time zone.
4. Check if each time falls within 9 AM–5 PM.
5. Return the results.

## Expected output
A table showing:
- Time zone
- Converted local time
- Work hours status (Inside/Outside)

## Limitations
- Does not create calendar events
- Uses fixed 9 AM–5 PM work hours