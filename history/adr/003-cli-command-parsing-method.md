# ADR-003: CLI Command Parsing Method

## Status
Accepted

## Date
2025-12-04

## Context
The Todo Console App needs a method to parse user commands entered through the CLI interface. The parsing method must be lightweight, work with standard Python libraries (as per the constitution), and support the required commands (add, list, complete, update, delete, help). The approach should be simple for users to understand and easy for developers to extend and maintain.

## Decision
We will use Python's built-in `str.split()` method with basic string parsing to extract commands and arguments. This will involve:

1. Reading user input as a string
2. Using `str.split()` to separate the command from its arguments
3. Implementing a simple dispatch mechanism that routes to appropriate handler functions based on the command verb
4. Parsing arguments based on position and expected format

This approach keeps dependencies minimal, uses only standard Python libraries, and provides sufficient functionality for the console application.

## Alternatives Considered
1. **argparse module**: More complex than needed for a simple console app; designed for command-line arguments rather than interactive input
2. **Regular expressions**: Overkill for basic command parsing; would add unnecessary complexity
3. **Third-party CLI libraries**: Would violate constitution's dependency constraints requiring standard library only
4. **Custom recursive descent parser**: Excessively complex for the simple commands required

## Consequences

### Positive
- Lightweight implementation using only standard library
- Minimal dependencies, adhering to constitution requirements
- Simple to implement and understand
- Easy to extend with additional commands
- Low overhead in terms of resources and complexity

### Negative
- Less sophisticated error handling for malformed input
- Position-based argument parsing could be less flexible than advanced parsing methods
- Limited ability to handle complex argument structures
- May require manual validation for more complex command syntax in the future

## References
- plan.md: "Command Parsing Method" in Architecturally Significant Decisions section
- research.md: "Decision: Command Parsing Method"
- constitution.md: Technology Stack and Dependencies section