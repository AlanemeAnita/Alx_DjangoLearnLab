\# Advanced Features and Security — Permissions \& Groups



This README documents how custom permissions and user groups are implemented and tested for the `bookshelf` app.



\## Custom permissions (models)

The `Book` model in `bookshelf/models.py` defines the following custom permissions:



\- `can\_view`  — allows viewing book records

\- `can\_create` — allows creating new books

\- `can\_edit`  — allows editing existing books

\- `can\_delete` — allows deleting books



These are declared in the model `Meta.permissions`. Example:

```py

class Meta:

&nbsp;   permissions = \[

&nbsp;       ("can\_view", "Can view book"),

&nbsp;       ("can\_create", "Can create book"),

&nbsp;       ("can\_edit", "Can edit book"),

&nbsp;       ("can\_delete", "Can delete book"),

&nbsp;   ]



