# Cricket Champions 4.0 — UML Diagrams

This folder contains the UML documentation for the Cricket Champions 4.0 project. Open each Markdown file on GitHub to view its rendered diagram.

## Diagrams
1. [Use Case Diagram](Use-Case-Diagram.md)
2. [Activity Diagram](Activity-Diagram.md)
3. [Sequence Diagram](Sequence-Diagram.md)
4. [Class Diagram — Proposed Logical Design](Class-Diagram.md)
5. [Component Diagram](Component-Diagram.md)

## Project overview
Cricket Champions 4.0 is a 2D batting game. The player starts a match, moves the batsman, selects a shot direction, times a hit, and tries to reach the target before losing three wickets or using the available 12 balls (two overs). The game tracks runs, wickets, balls, match state, and the best score.

## Modelling note
The current Python game is implemented mainly with functions and shared state rather than Python classes. Therefore, the class diagram is explicitly a **proposed logical/object-oriented design** of the same game responsibilities; it should not be mistaken for a claim that these classes already exist in the source code.

The diagrams use Mermaid syntax embedded in Markdown, which GitHub renders when these files are opened in the repository.
