from fastapi import APIRouter, UploadFile, File

from app.docker_logs import get_logger

router = APIRouter(
    prefix="/endpoint_name",
)

logger = get_logger("x-ray-logger")


@router.post("/predict")
async def predict(dicom: UploadFile = File(...)):

    logger.info("File uploaded")

    return {"message": "great success"}
