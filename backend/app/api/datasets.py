from __future__ import annotations

from fastapi import APIRouter, File, UploadFile

from app.api.deps import CurrentClaims, DbSession, SettingsDep
from app.services.dataset_service import DatasetService
from app.services.ingestion_service import IngestionService

router = APIRouter(prefix="/datasets", tags=["datasets"])


@router.get("")
async def list_datasets(claims: CurrentClaims, db: DbSession, settings: SettingsDep, project_id: str | None = None):
    return {"actor": claims["sub"], "items": await DatasetService(db, settings).list(project_id)}


@router.post("/upload")
async def upload_dataset(claims: CurrentClaims, file: UploadFile = File(...), project_id: str = "demo-project"):
    content = await file.read()
    return await IngestionService().register_upload(file.filename or "upload.bin", content, project_id)
