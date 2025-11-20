## Implementation Notes

This document uses **pseudo-code** to illustrate function logic. Helper functions (encrypt(), find_closest_worldline(), transmute(), etc.) represent:

1. **Internal utilities** - Lower-level operations (implementation details for Phase 2)
2. **Force interactions** - Some are shorthand for force operations documented in INTERACTION_MECHANICS.md
3. **Abstractions** - Conceptual operations whose exact implementation will be specified in Phase 2 code

**Phase 1 Goal:** Show WHAT functions do, not complete implementation stack
**Phase 2 Goal:** Implement all helper functions with proper signatures

### Type System (Phase 1 Status)

This document uses **informal typing** appropriate for Phase 1 conceptual documentation:

**Defined Types** (see [Base Structure](../../../01_foundation/base_structure/00_index.md)):
- `Agent` - Conscious entity
- `StateSignature` - Encoded self-state
- `Timeline` - Worldline path
- `Event` - Occurrence

**Informal Types** (Phase 2 will formalize):
- `Status` - String or enum ("transmuted", "suppressed", "success")
- `AccessLevel` - Permission state
- `SearchProcess` - Active search operation
- Mixed returns (e.g., ascend() returns Status OR continue(lesson_loop))

**Phase 2 will define:**
- Complete type hierarchy
- Formal return type specifications
- Type validation rules
- Union types where multiple returns possible

**For now:** Focus on WHAT functions do, not precise typing.

---

