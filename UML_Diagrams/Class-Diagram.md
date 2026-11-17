# Class Diagram — Proposed Logical Design

> **Important:** This is a proposed object-oriented design model for the project. The current Python implementation is primarily procedural and uses functions and shared variables; these classes are conceptual responsibilities, not existing Python class declarations.

```mermaid
classDiagram
    class Game {
        +gameState
        +highScore
        +start()
        +run()
        +pause()
        +resume()
        +restart()
        +finish()
    }

    class Match {
        +score
        +wickets
        +balls
        +target
        +reset()
        +addRuns(runs)
        +addWicket()
        +isOver()
        +getResult()
    }

    class Player {
        +positionX
        +shotDirection
        +moveLeft()
        +moveRight()
        +selectShot(direction)
        +attemptHit()
    }

    class Ball {
        +positionX
        +positionY
        +speed
        +state
        +deliver()
        +update()
        +registerHit()
        +reset()
    }

    class Scoreboard {
        +displayScore()
        +displayWickets()
        +displayOvers()
        +displayTarget()
    }

    class GameUI {
        +showMenu()
        +showGameplay()
        +showPauseScreen()
        +showResult()
        +readInput()
    }

    class CelebrationEffect {
        +particles
        +timer
        +create()
        +update()
        +draw()
    }

    Game *-- Match : manages
    Game *-- GameUI : displays through
    Game o-- Player : controls
    Game o-- Ball : updates
    Game *-- Scoreboard : updates
    Game o-- CelebrationEffect : triggers
    Match ..> Scoreboard : provides match data
    Player ..> Ball : attempts to hit
    Ball ..> Match : reports delivery outcome
```

## Class responsibilities
- **Game:** coordinates the main loop and game states.
- **Match:** stores score, wickets, balls, target, and match result.
- **Player:** stores batsman position and selected shot direction.
- **Ball:** handles delivery movement and hit state.
- **Scoreboard:** presents current match statistics.
- **GameUI:** handles screens and player input.
- **CelebrationEffect:** manages visual effects after boundaries.
