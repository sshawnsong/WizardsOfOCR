import sys

sys.path.append('/Users/shawnsong/Development/WizardsOfOCR')
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from api.utils.database import *
import numpy as np
import cv2
import pytesseract

router = APIRouter()
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
custom_config = r'--oem 3 --psm 6 -l eng+kor'


@router.get("/", tags=["root"])
async def get_parcels(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    packages = read_parcels(db, skip=skip, limit=limit)
    return [{"id": package.id, "name": package.name, "is_active": package.is_active} for package in packages]


@router.get("/{parcel_id}", tags=["root"])
async def get_parcel(parcel_id: int, db: Session = Depends(get_db)):
    parcel = read_parcel(db, parcel_id)
    if parcel is None:
        raise HTTPException(status_code=404, detail="Parcel not found")
    return {"id": parcel.id, "name": parcel.name, "is_active": parcel.is_active}


@router.post("/", tags=["root"])
async def post_parcel(file: UploadFile, db: Session = Depends(get_db)):
    try:
        content = await file.read()
        img = cv2.imdecode(np.frombuffer(content, np.uint8), cv2.IMREAD_COLOR)

        extracted_text = pytesseract.image_to_string(img, config=custom_config)

        db_parcel = create_parcel(db, extracted_text, False)

        return {"id": db_parcel.id, "name": db_parcel.name, "is_active": db_parcel.is_active,
                "extracted_text": extracted_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{parcel_id}", tags=["root"])
async def put_parcel(parcel_id: int, new_status: bool, db: Session = Depends(get_db)):
    return update_parcel(db, parcel_id=parcel_id, new_status=new_status)
