from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
import shutil

router = APIRouter(prefix="/file", tags=["file"])


@router.post("/file")
def get_file(file: bytes = File(...)):
    content = file.decode("utf-8")
    lines = content.split("\n")
    return {"lines": lines}


@router.post("/uploadFile")
def upload_file(file: UploadFile = File(...)):
    path = f"files/{file.filename}"
    with open(path, "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "type": file.content_type}


@router.get("download/{name}", response_class=FileResponse)
def get_file(name: str):  # noqa
    path = f"files/{name}"
    return path
