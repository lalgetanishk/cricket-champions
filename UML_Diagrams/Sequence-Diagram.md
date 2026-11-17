# Sequence Diagram — Playing a Match

```mermaid
sequenceDiagram
    actor Player
    participant UI as Game UI
    participant Controller as Game Controller
    participant Ball as Ball Logic
    participant Score as Score / Match State

    Player->>UI: Select Play Match
    UI->>Controller: Start new match
    Controller->>Score: Reset score, wickets and balls
    Controller->>Ball: Create first delivery
    Ball-->>Controller: Ball position and speed
    Controller-->>UI: Show gameplay screen

    loop Each frame while match is active
        Player->>UI: Move / choose direction / press Hit
        UI->>Controller: Send control input
        Controller->>Ball: Update ball position
        alt Hit attempted in valid range
            Controller->>Ball: Register hit
            Ball-->>Controller: Shot result and timing
            Controller->>Score: Add calculated runs
        else Ball passes the batsman
            Ball-->>Controller: Delivery missed
            Controller->>Score: Add wicket and ball
        end
        Controller->>Score: Check target and match limits
        Score-->>Controller: Continue or finish
        Controller-->>UI: Update scoreboard and screen
    end

    Controller-->>UI: Display final match result
    Player->>UI: Select Play Again
    UI->>Controller: Reset and start another match
```

## Description
This sequence shows how player input travels through the interface and game controller. Ball logic reports a hit or a missed delivery, the match state updates the score, and the controller decides whether gameplay continues or the result screen should appear.
