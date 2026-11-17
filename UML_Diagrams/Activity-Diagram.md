# Activity Diagram — Match Flow

```mermaid
flowchart TD
    A([Start]) --> B[Display main menu]
    B --> C[Player selects Play]
    C --> D[Initialize score, wickets, balls and player position]
    D --> E[Deliver ball]
    E --> F[Read player input]
    F --> G{Pause requested?}
    G -- Yes --> H[Pause game]
    H --> I[Wait for resume]
    I --> F
    G -- No --> J{Move or change shot direction?}
    J -- Yes --> K[Update player position or shot direction]
    J -- No --> L{Attempt hit?}
    K --> L
    L -- Yes --> M{Ball in hitting range?}
    M -- Yes --> N[Calculate runs from timing]
    M -- No --> O[Continue ball movement]
    L -- No --> O
    N --> P[Update score and ball state]
    O --> Q{Ball passed batsman?}
    Q -- Yes --> R[Add wicket and ball]
    Q -- No --> S{Shot finished?}
    S -- No --> F
    S -- Yes --> T[Add completed ball]
    P --> U{Target reached or limit reached?}
    R --> U
    T --> U
    U -- No --> E
    U -- Yes --> V[Display match result and best score]
    V --> W{Play again?}
    W -- Yes --> D
    W -- No --> X([End])
```

## Description
The match begins from the menu. The game initializes the match values, repeatedly delivers a ball and reads player input. A successful hit adds runs based on timing. A missed delivery can add a wicket. The match ends when the target is reached, three wickets are lost, or 12 balls are completed.
