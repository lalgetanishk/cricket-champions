# Component Diagram — Cricket Champions 4.0

```mermaid
flowchart TB
    Player([Player])

    subgraph Application["Cricket Champions 4.0 Application"]
        UI["User Interface<br/>Menu, gameplay, pause and result screens"]
        Input["Input Handler<br/>Keyboard and pointer/touch input"]
        Engine["Game Controller / Main Loop"]
        Match["Match State<br/>Score, wickets, balls and target"]
        Ball["Ball and Shot Logic<br/>Delivery, movement and hit detection"]
        Render["Rendering System<br/>Stadium, players, ball and scoreboard"]
        Effects["Celebration Effects<br/>Particles and boundary messages"]
    end

    Player --> UI
    Player --> Input
    Input --> Engine
    UI <--> Engine
    Engine <--> Match
    Engine <--> Ball
    Engine --> Render
    Match --> Render
    Ball --> Render
    Engine --> Effects
    Effects --> Render
```

## Component description
- **User Interface:** displays the menu, gameplay, pause, and result screens.
- **Input Handler:** receives keyboard and pointer/touch controls.
- **Game Controller:** coordinates the game loop and state transitions.
- **Match State:** stores the score, wickets, balls, and target.
- **Ball and Shot Logic:** updates deliveries, detects hits, and determines outcomes.
- **Rendering System:** draws the stadium, players, ball, controls, and scoreboard.
- **Celebration Effects:** displays particle effects and boundary messages.
