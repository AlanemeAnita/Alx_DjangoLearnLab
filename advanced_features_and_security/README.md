# Django Permissions and Groups Setup

This project demonstrates how to manage permissions and groups in Django.

## Custom Permissions
We added custom permissions in `Book` model (`models.py`):

- `can_view` – allows users to view books
- `can_create` – allows users to create new books
- `can_edit` – allows users to edit books
- `can_delete` – allows users to delete books

## Groups and Permissions
You can create groups from the Django admin panel:
- **Viewers** → assign `can_view`
- **Editors** → assign `can_view`, `can_create`, `can_edit`
- **Admins** → assign all permissions including `can_delete`

## Permission Enforcement in Views
We used `@permission_required` decorator in `views.py` to restrict access:
- `book_list` → requires `can_view`
- `create_book` → requires `can_create`
- `edit_book` → requires `can_edit`
- `delete_book` → requires `can_delete`

This ensures only authorized users can access or modify data.
