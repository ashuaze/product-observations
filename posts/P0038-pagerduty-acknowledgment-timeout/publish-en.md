### 1/4

1/4 A checkout outage wakes the on-call engineer. They tap Acknowledge and the paging stops. That silence now means someone claimed the incident. It tells you nothing about whether checkout is back.

### 2/4

2/4 PagerDuty separates two waits. An escalation timeout can page the next responder if nobody acts. An acknowledgment timeout can bring an unresolved incident back after someone has claimed it. The second timer is off by default. https://docs.pagerduty.com/incident-management/services/configurable-service-settings

### 3/4

3/4 Compare two ways to handle the same outage: leave the incident with the person who claimed it, or page again after a defined wait. The first gives them room to work. The second catches a stalled response but can interrupt a repair that's going well.

### 4/4

4/4 Set the timer around when another person could help. Test two cases: the responder claims the incident and disappears, or stays on it through a slow recovery. Track time without an active responder and pages that add no help.
