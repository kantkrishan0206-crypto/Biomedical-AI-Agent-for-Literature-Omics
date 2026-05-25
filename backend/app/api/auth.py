from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.api.deps import DbSession, SettingsDep, CurrentClaims
from app.schemas.auth import LoginRequest, SignupRequest, TokenResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=TokenResponse)
async def signup(payload: SignupRequest, db: DbSession, settings: SettingsDep):
    service = AuthService(db, settings)
    user = await service.signup(str(payload.email), payload.password, payload.full_name)
    token, user = await service.login(str(payload.email), payload.password)
    return TokenResponse(access_token=token, role=user.role, email=user.email)


@router.post("/login", response_model=TokenResponse)
async def login(payload: LoginRequest, db: DbSession, settings: SettingsDep):
    try:
        token, user = await AuthService(db, settings).login(str(payload.email), payload.password)
    except ValueError as exc:
        raise HTTPException(status_code=401, detail="Invalid credentials") from exc
    return TokenResponse(access_token=token, role=user.role, email=user.email)


@router.get("/session")
async def session(claims: CurrentClaims):
    return {"authenticated": True, "claims": claims}
