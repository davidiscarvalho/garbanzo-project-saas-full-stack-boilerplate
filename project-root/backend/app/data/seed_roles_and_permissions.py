from sqlmodel import Session, select
from ..db import engine
from ..models.User import Role, Permission, RolePermission

# Define roles and their descriptions
ROLES = [
    {"name": "admin", "description": "Administrator with full access"},
    {"name": "integration", "description": "Integration role for third-party services"},
    {"name": "intermediate", "description": "Intermediate user with CRUD access"},
    {"name": "basic", "description": "Basic user with read-only access"},
    {"name": "block", "description": "Blocked user with no access"},
]

# Define permissions
PERMISSIONS = [
    {"name": "create", "description": "Permission to create resources"},
    {"name": "read", "description": "Permission to read resources"},
    {"name": "update", "description": "Permission to update resources"},
    {"name": "delete", "description": "Permission to delete resources"},
    {"name": "swagger/endpoint documentation", "description": "Permission to access Swagger/OpenAPI documentation"},
]

# Define role-permission mappings
ROLE_PERMISSIONS = {
    "admin": ["create", "read", "update", "delete", "swagger/endpoint documentation"],
    "integration": ["read", "swagger/endpoint documentation"],  # Example for integration role
    "intermediate": ["create", "read", "update", "delete"],
    "basic": ["read"],
    "block": [],  # Blocked users have no permissions
}

def seed_roles_and_permissions():
    with Session(engine) as session:
        # Seed roles
        for role_data in ROLES:
            role = session.exec(select(Role).where(Role.name == role_data["name"])).first()
            if not role:
                role = Role(**role_data)
                session.add(role)
                session.commit()
                session.refresh(role)

        # Seed permissions
        for permission_data in PERMISSIONS:
            permission = session.exec(select(Permission).where(Permission.name == permission_data["name"])).first()
            if not permission:
                permission = Permission(**permission_data)
                session.add(permission)
                session.commit()
                session.refresh(permission)

        # Seed role-permission mappings
        for role_name, permission_names in ROLE_PERMISSIONS.items():
            role = session.exec(select(Role).where(Role.name == role_name)).first()
            for permission_name in permission_names:
                permission = session.exec(select(Permission).where(Permission.name == permission_name)).first()
                if role and permission:
                    # Check if the role-permission mapping already exists
                    role_permission = session.exec(
                        select(RolePermission)
                        .where(RolePermission.role_id == role.id, RolePermission.permission_id == permission.id)
                    ).first()
                    if not role_permission:
                        role_permission = RolePermission(role_id=role.id, permission_id=permission.id)
                        session.add(role_permission)
                        session.commit()

        print("Roles, permissions, and role-permission mappings seeded successfully.")


# Run the seeding function
if __name__ == "__main__":
    seed_roles_and_permissions()