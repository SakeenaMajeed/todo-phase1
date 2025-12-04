# ADR-001: Task ID Generation Strategy

## Status
Accepted

## Date
2025-12-04

## Context
The Todo Console App needs a strategy for generating unique identifiers for tasks. The system requires each task to have a unique ID during the application session, which will be used for referencing tasks in operations like update, complete, and delete. The ID generation strategy must be simple, efficient for in-memory storage, and user-friendly for a CLI interface.

## Decision
We will use auto-incrementing integer IDs starting from 1, managed by the TodoService. The service will track the last assigned ID and increment it for each new task. 

The implementation will:
- Use a simple integer counter that starts at 1
- Increment the counter for each new task created
- Store this counter as part of the TodoService state
- Ensure IDs remain unique within the application session

## Alternatives Considered
1. **UUIDs**: Would provide globally unique IDs but are complex to use in a CLI interface (long strings), making them less user-friendly
2. **Random integers**: Risk of collisions without sufficient management, requiring collision detection and retry logic
3. **Time-based IDs**: Unnecessarily complex for this use case, and could result in non-sequential IDs

## Consequences

### Positive
- Simple to implement and understand
- Efficient memory usage
- User-friendly for CLI interface (short, easy-to-remember IDs)
- Maintains natural ordering (newer tasks have higher IDs)

### Negative
- IDs are not globally unique across different application sessions
- IDs are tied to session lifetime and don't persist between runs
- Sequential nature might expose information about the number of tasks created

## References
- plan.md: "ID Generation Strategy" section
- research.md: "Decision: ID Generation Strategy"
- data-model.md: Task entity ID field specification