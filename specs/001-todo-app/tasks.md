---

description: "Task list for Todo Console App implementation"
---

# Tasks: Todo Console App

**Input**: Design documents from `/specs/001-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are required based on the testing strategy in the plan and constitution requirements.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan with src/ directory
- [X] T002 Initialize Python project with requirements file (pytest dependency)
- [ ] T003 [P] Configure linting and formatting tools (flake8, black)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create custom exceptions module in src/lib/exceptions.py
- [X] T005 Create Task entity model with validation in src/models/task.py
- [X] T006 [P] Create TodoService with in-memory storage in src/services/todo_service.py
- [ ] T007 Create basic CLI structure in src/cli/todo_cli.py
- [ ] T008 Configure error handling and logging infrastructure

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Tasks to List (Priority: P1) 🎯 MVP

**Goal**: Ability to add new tasks to the todo list with a required title and optional description

**Independent Test**: Can be fully tested by adding a task via the console interface and verifying the task appears in the list with a unique ID and 'incomplete' status.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T009 [P] [US1] Unit test for adding task with title in tests/unit/test_todo_service.py
- [X] T010 [P] [US1] Unit test for adding task with title and description in tests/unit/test_todo_service.py
- [X] T011 [P] [US1] Unit test for adding task with empty title (should fail) in tests/unit/test_todo_service.py

### Implementation for User Story 1

- [X] T012 [P] [US1] Implement Task creation with validation in src/models/task.py
- [X] T013 [US1] Implement add_task method in TodoService in src/services/todo_service.py
- [ ] T014 [US1] Implement add command in CLI interface in src/cli/todo_cli.py
- [ ] T015 [US1] Add type hints and docstrings to Task model following Google style
- [ ] T016 [US1] Add type hints and docstrings to TodoService add functionality
- [ ] T017 [US1] Add type hints and docstrings to CLI add command
- [ ] T018 [US1] Test adding tasks to list functionality end-to-end

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Display all tasks in the list with their ID, status, title, and description

**Independent Test**: Can be fully tested by adding several tasks and then viewing the complete list with all tasks showing their status, title, and ID.

### Tests for User Story 2 ⚠️

- [X] T019 [P] [US2] Unit test for listing all tasks in tests/unit/test_todo_service.py
- [X] T020 [P] [US2] Unit test for listing empty task list in tests/unit/test_todo_service.py
- [X] T021 [P] [US2] Unit test for listing tasks with mixed completion status in tests/unit/test_todo_service.py

### Implementation for User Story 2

- [X] T022 [P] [US2] Implement list_tasks method in TodoService in src/services/todo_service.py
- [X] T023 [US2] Implement list command in CLI interface in src/cli/todo_cli.py
- [ ] T024 [US2] Implement proper output formatting for task list
- [ ] T025 [US2] Add type hints and docstrings to TodoService list functionality
- [ ] T026 [US2] Add type hints and docstrings to CLI list command
- [ ] T027 [US2] Test viewing task list functionality end-to-end

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Complete Tasks (Priority: P2)

**Goal**: Mark tasks as complete or incomplete with proper error handling for non-existent tasks

**Independent Test**: Can be fully tested by marking an incomplete task as complete and verifying its status changes to complete in the task list.

### Tests for User Story 3 ⚠️

- [X] T028 [P] [US3] Unit test for completing an incomplete task in tests/unit/test_todo_service.py
- [X] T029 [P] [US3] Unit test for completing an already completed task in tests/unit/test_todo_service.py
- [X] T030 [P] [US3] Unit test for completing a non-existent task (should fail) in tests/unit/test_todo_service.py

### Implementation for User Story 3

- [X] T031 [P] [US3] Implement complete_task method in TodoService in src/services/todo_service.py
- [ ] T032 [US3] Implement complete command in CLI interface in src/cli/todo_cli.py
- [ ] T033 [US3] Add proper error handling for invalid task IDs
- [X] T034 [US3] Add type hints and docstrings to TodoService complete functionality
- [ ] T035 [US3] Add type hints and docstrings to CLI complete command
- [ ] T036 [US3] Test completing tasks functionality end-to-end

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P3)

**Goal**: Remove tasks from the list with proper error handling for non-existent tasks

**Independent Test**: Can be fully tested by deleting a task and verifying it no longer appears when viewing the task list.

### Tests for User Story 4 ⚠️

- [X] T037 [P] [US4] Unit test for deleting an existing task in tests/unit/test_todo_service.py
- [X] T038 [P] [US4] Unit test for deleting a non-existent task (should fail) in tests/unit/test_todo_service.py
- [X] T039 [P] [US4] Unit test for deleting from an empty list (should fail) in tests/unit/test_todo_service.py

### Implementation for User Story 4

- [ ] T040 [P] [US4] Implement delete_task method in TodoService in src/services/todo_service.py
- [ ] T041 [US4] Implement delete command in CLI interface in src/cli/todo_cli.py
- [ ] T042 [US4] Add proper error handling for invalid task IDs during deletion
- [ ] T043 [US4] Add type hints and docstrings to TodoService delete functionality
- [ ] T044 [US4] Add type hints and docstrings to CLI delete command
- [ ] T045 [US4] Test deleting tasks functionality end-to-end

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Update Task Details (Priority: P3)

**Goal**: Update task title and description with proper error handling for non-existent tasks

**Independent Test**: Can be fully tested by updating a task's title or description and verifying the changes appear when viewing the task list.

### Tests for User Story 5 ⚠️

- [X] T046 [P] [US5] Unit test for updating task title in tests/unit/test_todo_service.py
- [X] T047 [P] [US5] Unit test for updating task description in tests/unit/test_todo_service.py
- [X] T048 [P] [US5] Unit test for updating non-existent task (should fail) in tests/unit/test_todo_service.py

### Implementation for User Story 5

- [ ] T049 [P] [US5] Implement update_task method in TodoService in src/services/todo_service.py
- [ ] T050 [US5] Implement update command in CLI interface in src/cli/todo_cli.py
- [ ] T051 [US5] Add proper validation for updated fields
- [ ] T052 [US5] Add type hints and docstrings to TodoService update functionality
- [ ] T053 [US5] Add type hints and docstrings to CLI update command
- [ ] T054 [US5] Test updating tasks functionality end-to-end

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T055 [P] Implement help command showing available commands in src/cli/todo_cli.py
- [ ] T056 [P] Implement proper error message formatting per constitution requirements
- [ ] T057 [P] Add validation for command arguments in CLI interface
- [ ] T058 [P] Add comprehensive edge case handling
- [ ] T059 [P] Add type hints and docstrings to all remaining functions
- [ ] T060 [P] Add integration tests for complete user workflows in tests/integration/
- [ ] T061 Code cleanup and refactoring
- [ ] T062 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test for adding task with title in tests/unit/test_todo_service.py"
Task: "Unit test for adding task with title and description in tests/unit/test_todo_service.py"
Task: "Unit test for adding task with empty title (should fail) in tests/unit/test_todo_service.py"

# Launch all models for User Story 1 together:
Task: "Implement Task creation with validation in src/models/task.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence