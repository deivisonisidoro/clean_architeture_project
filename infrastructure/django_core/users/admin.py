from django.contrib import admin
from users.models.user import User


class UserAdmin(admin.ModelAdmin):
    """
    Admin configuration for the User model.

    This class defines how the User model is displayed and interacted with in the Django admin interface.
    It specifies the fields that are displayed in the list view of the admin interface for the User model.

    Attributes:
        model (User): The User model to be associated with this admin configuration.
        list_display (tuple, list): A tuple or list of field names to be displayed in the list view of the admin interface.
                      Each field name corresponds to a column in the admin interface's list view for the User model.

    Example:
        admin.site.register(User, UserAdmin)
    """

    model = User
    list_display = ("username", "email", "is_active", "is_admin", "created_at")


admin.site.register(User, UserAdmin)
