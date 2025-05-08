# from fastapi import APIRouter, UploadFile, File, Depends,HTTPException
# from modules.core.auth import get_current_user
# from modules.models.user import UserInDB
# from modules.core.database import users_collection
# from datetime import datetime
# from modules.services.loader import phoWhisper_transcriber
# from modules.services.process_func import create_processed_text
# from uuid import uuid4
# import os


# router = APIRouter()


# @router.post("/transcribe/")
# async def transcribe_audio(file: UploadFile = File(...), current_user: UserInDB = Depends(get_current_user)):
#     try:
#         audio_data = await file.read()
        
#         temp_audio_path = "temp_audio.wav"
#         with open(temp_audio_path, "wb") as f:
#             f.write(audio_data)
#         output = phoWhisper_transcriber(temp_audio_path)
#         processed_entry = create_processed_text(output['text'])
#         current_user.processed_texts.append(processed_entry)
        
#         users_collection.update_one(
#             {"username": current_user.username},
#             {"$set": {"processed_texts": [entry.model_dump() for entry in current_user.processed_texts]}}
#         )
#         os.remove(temp_audio_path)
        
#         return {"text": output['text']}
    
#     except Exception as e:
#         if os.path.exists(temp_audio_path):
#             os.remove(temp_audio_path)
#         raise HTTPException(status_code=500, detail=str(e))