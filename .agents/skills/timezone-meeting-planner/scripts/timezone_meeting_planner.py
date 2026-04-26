from datetime import datetime
from zoneinfo import ZoneInfo

WORK_START = 9
WORK_END = 17

def convert_meeting(date, time, source_tz, target_tzs):
    source_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
    source_datetime = source_datetime.replace(tzinfo=ZoneInfo(source_tz))

    results = []

    for tz in target_tzs:
        local_time = source_datetime.astimezone(ZoneInfo(tz))
        hour = local_time.hour

        if WORK_START <= hour < WORK_END:
            status = "Inside work hours"
        else:
            status = "Outside work hours"

        results.append({
            "time_zone": tz,
            "local_time": local_time.strftime("%Y-%m-%d %I:%M %p"),
            "status": status
        })

    return results


if __name__ == "__main__":
    # Example test run
    results = convert_meeting(
        "2026-04-30",
        "14:00",
        "America/New_York",
        ["America/Los_Angeles", "Europe/London", "Asia/Riyadh"]
    )

    for item in results:
        print(f"{item['time_zone']} | {item['local_time']} | {item['status']}")