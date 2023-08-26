import numpy as np
import pandas as pd
import uvicorn as uvicorn
from fastapi import FastAPI, UploadFile, File
import shutil
from fastapi.responses import FileResponse, JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST
from fastapi.middleware.cors import CORSMiddleware
import cv2

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/tg/file")
async def tg_file(file: UploadFile = File(...), platform: str = "TGStat"):
    return JSONResponse({"platform": platform})


@app.post("/picture")
async def upload_file(file: UploadFile = File(...)):
    image = await file.read()
    print(file.content_type)
    image = np.fromstring(image, np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Match', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return JSONResponse({"status": "ok"})


if __name__ == '__main__':
    uvicorn.run(app)
