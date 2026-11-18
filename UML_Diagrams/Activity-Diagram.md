# Activity Diagram — Cricket Champions 4.0 Match Flow

This diagram shows the main match workflow, including player input, ball processing, score updates, pause/resume, and the match-ending checks.

```mermaid
flowchart TD
    A((Start)) --> B[Display main menu]
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
    Q -- Yes --> R[Add wicket and completed ball]
    Q -- No --> S{Shot finished?}
    S -- No --> F
    S -- Yes --> T[Add completed ball]

    P --> U{Target reached, 3 wickets lost, or 12 balls completed?}
    R --> U
    T --> U
    U -- No --> E
    U -- Yes --> V[Display match result and best score]
    V --> W{Play again?}
    W -- Yes --> D
    W -- No --> X(((End)))

    classDef initial fill:#222,stroke:#222,color:#fff,stroke-width:2px;
    classDef final fill:#fff,stroke:#222,color:#222,stroke-width:3px;
    class A initial;
    class X final;
```

## Description

1. The game starts and displays the main menu.
2. When the player selects Play, the game initializes the match values.
3. The game repeatedly delivers a ball and reads the player's input.
4. The player may pause the game, move the batsman, change shot direction, or attempt a hit.
5. The game checks the hit and ball position, then updates the score or wicket/ball count as appropriate.
6. The match continues until the target is reached, three wickets are lost, or 12 balls are completed.
7. The result is displayed. The player can start another match or exit.

## Important UML notation

- **Filled circle:** Initial node (start).
- **Rounded rectangle:** Activity/action.
- **Diamond:** Decision or condition; outgoing paths are labelled Yes/No.
- **Arrow:** Control flow.
- **Bull's-eye symbol:** Activity final node (end).

> The diagram is a model of the match flow. Keep its conditions and transitions consistent with the actual Python game implementation.
