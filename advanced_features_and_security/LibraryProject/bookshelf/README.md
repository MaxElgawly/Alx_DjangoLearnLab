# Permissions and Groups Setup

## Custom Permissions
Defined in `Book` model:
- can_view
- can_create
- can_edit
- can_delete

## Groups
Created in admin or via `python manage.py setup_groups`:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

## Enforcement
Each view in `bookshelf/views.py` uses `@permission_required` to enforce permissions.
