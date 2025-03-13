from admin import Admin

admin_1 = Admin('albert', 'einstein', 'germany', ['can add users', 'can ban users', 'can add posts', 'can delete posts'])
admin_1.describe_user()
admin_1.privileges.show_privileges()