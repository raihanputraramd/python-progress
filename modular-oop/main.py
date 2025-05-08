from services.user_service import UserService

service = UserService()
service.add_user("Raihan", "raihan@example.com")

for user in service.users:
    print(f"{user.name} - {user.email}")