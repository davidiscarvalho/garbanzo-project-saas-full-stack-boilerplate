# routers/userAccount.py

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from db.session import get_session
from models.UserAccount import UserPayment, UserSubscription, UserTier, UserCreditBalance
from schemas.userAccount import (
    UserPaymentCreate, UserPaymentRead,
    UserSubscriptionCreate, UserSubscriptionRead,
    UserTierCreate, UserTierRead,
    UserCreditBalanceCreate, UserCreditBalanceRead,
)
from core.auth import get_current_user, check_permission
from models.User import User

router = APIRouter(prefix="/users", tags=["User Account"])

# UserPayment
@router.post("/payments/", response_model=UserPaymentRead)
def create_payment(*, session: Session = Depends(get_session), payment: UserPaymentCreate, current_user: User = Depends(get_current_user)):
    check_permission(current_user, "create")
    db_payment = UserPayment.from_orm(payment)
    session.add(db_payment)
    session.commit()
    session.refresh(db_payment)
    return db_payment

@router.get("/payments/", response_model=List[UserPaymentRead])
def list_payments(*, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    check_permission(current_user, "read")
    payments = session.exec(select(UserPayment)).all()
    return payments

# UserSubscription
@router.post("/subscriptions/", response_model=UserSubscriptionRead)
def create_subscription(*, session: Session = Depends(get_session), subscription: UserSubscriptionCreate, current_user: User = Depends(get_current_user)):
    check_permission(current_user, "create")
    db_subscription = UserSubscription.from_orm(subscription)
    session.add(db_subscription)
    session.commit()
    session.refresh(db_subscription)
    return db_subscription

@router.get("/subscriptions/", response_model=List[UserSubscriptionRead])
def list_subscriptions(*, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    check_permission(current_user, "read")
    subscriptions = session.exec(select(UserSubscription)).all()
    return subscriptions

# UserTier
@router.post("/tiers/", response_model=UserTierRead)
def create_user_tier(*, session: Session = Depends(get_session), user_tier: UserTierCreate, current_user: User = Depends(get_current_user)):
    check_permission(current_user, "create")
    db_user_tier = UserTier.from_orm(user_tier)
    session.add(db_user_tier)
    session.commit()
    session.refresh(db_user_tier)
    return db_user_tier

@router.get("/tiers/", response_model=List[UserTierRead])
def list_user_tiers(*, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    check_permission(current_user, "read")
    user_tiers = session.exec(select(UserTier)).all()
    return user_tiers

# UserCreditBalance
@router.post("/credit-balance/", response_model=UserCreditBalanceRead)
def create_credit_balance(*, session: Session = Depends(get_session), credit_balance: UserCreditBalanceCreate, current_user: User = Depends(get_current_user)):
    check_permission(current_user, "create")
    db_credit_balance = UserCreditBalance.from_orm(credit_balance)
    session.add(db_credit_balance)
    session.commit()
    session.refresh(db_credit_balance)
    return db_credit_balance

@router.get("/credit-balance/", response_model=List[UserCreditBalanceRead])
def list_credit_balances(*, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    check_permission(current_user, "read")
    credit_balances = session.exec(select(UserCreditBalance)).all()
    return credit_balances