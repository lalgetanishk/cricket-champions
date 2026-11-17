# Use Case Diagram — Cricket Champions 4.0

```mermaid
flowchart LR
    Player([Player])
    Game((Cricket Champions 4.0))

    UC1([Start match])
    UC2([Move batsman])
    UC3([Choose shot direction])
    UC4([Hit the ball])
    UC5([Pause or resume match])
    UC6([View score and wickets])
    UC7([View match result])
    UC8([Play again])

    Player --- UC1
    Player --- UC2
    Player --- UC3
    Player --- UC4
    Player --- UC5
    Player --- UC6
    Player --- UC7
    Player --- UC8

    UC1 --- Game
    UC2 --- Game
    UC3 --- Game
    UC4 --- Game
    UC5 --- Game
    UC6 --- Game
    UC7 --- Game
    UC8 --- Game
```

## Description
- The Player starts a match and controls the batsman.
- The Player can move left or right, select a shot direction, and attempt to hit the incoming ball.
- The game updates and displays runs, wickets, and overs.
- The Player can pause/resume the match and start another match after the result is displayed.
