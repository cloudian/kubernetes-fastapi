from fastapi import APIRouter

from .endpoints.hello import router as triage_router
from .endpoints.lambda_handler import router as lambda_router

router = APIRouter()
router.include_router(triage_router)
router.include_router(lambda_router)
