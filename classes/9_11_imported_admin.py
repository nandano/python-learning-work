from admin import Admin

admin_1 = Admin('joseph', 'joestar', 'usa', ['can add users', 'can ban users', 'can delete comments'])
admin_1.privileges.show_privileges()