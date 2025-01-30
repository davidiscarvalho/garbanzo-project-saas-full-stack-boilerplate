# routers/core.py

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from db.session import get_session
from models.Tier import Tier, TierPrice
from models.User import User, Role, Permission, RolePermission
from schemas.tier import (
    TierCreate, TierRead,
    TierPriceCreate, TierPriceRead,
)
from schemas.user import (
    RoleCreate, RoleRead,
    PermissionCreate, PermissionRead,
    RolePermissionCreate, RolePermissionRead,
)
from core.auth import get_current_user, check_permission

router = APIRouter(prefix="/core", tags=["Core"])

# Tier
@router.post("/tiers/", response_model=TierRead)
def create_tier(*, session: Session = Depends(get_session), tier: TierCreate, current_user: User = Depends(get_current_user)):
    check_permission(current_user, "create")
    db_tier = Tier.from_orm(tier)
    session.add(db_tier)
    session.commit()
    session.refresh(db_tier)
    return db_tier

@router.get("/tiers/", response_model=List[TierRead])
def list_tiers(*, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    check_permission(current_user, "read")
    tiers = session.exec(select(Tier)).all()
    return tiers

# TierPrice
@router.post("/tier-prices/", response_model=TierPriceRead)
def create_tier_price(*, session: Session = Depends(get_session), tier_price: TierPriceCreate, current_user: User = Depends(get_current_user)):
    check_permission(current_user, "create")
    db_tier_price = TierPrice.from_orm(tier_price)
    session.add(db_tier_price)
    session.commit()
    session.refresh(db_tier_price)
    return db_tier_price

@router.get("/tier-prices/", response_model=List[TierPriceRead])
def list_tier_prices(*, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    check_permission(current_user, "read")
    tier_prices = session.exec(select(TierPrice)).all()
    return tier_prices

# Role
@router.post("/roles/", response_model=RoleRead)
def create_role(*, session: Session = Depends(get_session), role: RoleCreate, current_user: User = Depends(get_current_user)):
    check_permission(current_user, "create")
    db_role = Role.from_orm(role)
    session.add(db_role)
    session.commit()
    session.refresh(db_role)
    return db_role

@router.get("/roles/", response_model=List[RoleRead])
def list_roles(*, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    check_permission(current_user, "read")
    roles = session.exec(select(Role)).all()
    return roles

# Permission
@router.post("/permissions/", response_model=PermissionRead)
def create_permission(*, session: Session = Depends(get_session), permission: PermissionCreate, current_user: User = Depends(get_current_user)):
    check_permission(current_user, "create")
    db_permission = Permission.from_orm(permission)
    session.add(db_permission)
    session.commit()
    session.refresh(db_permission)
    return db_permission

@router.get("/permissions/", response_model=List[PermissionRead])
def list_permissions(*, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    check_permission(current_user, "read")
    permissions = session.exec(select(Permission)).all()
    return permissions

# RolePermission
@router.post("/role-permissions/", response_model=RolePermissionRead)
def create_role_permission(*, session: Session = Depends(get_session), role_permission: RolePermissionCreate, current_user: User = Depends(get_current_user)):
    check_permission(current_user, "create")
    db_role_permission = RolePermission.from_orm(role_permission)
    session.add(db_role_permission)
    session.commit()
    session.refresh(db_role_permission)
    return db_role_permission

@router.get("/role-permissions/", response_model=List[RolePermissionRead])
def list_role_permissions(*, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    check_permission(current_user, "read")
    role_permissions = session.exec(select(RolePermission)).all()
    return role_permissions