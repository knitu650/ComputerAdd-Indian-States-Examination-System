from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from controllers import cv_proctoring_controller, nlp_processing_controller, ml_analytics_controller
from utils.logger import setup_logger

app = FastAPI(
    title="AI/ML Service - Indian States Examination System",
    description="Computer Vision, NLP, and ML services for exam proctoring and analytics",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger = setup_logger(__name__)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "AI/ML Service"}

@app.get("/api/v1/health")
async def api_health():
    return {"status": "healthy", "models_loaded": True}

# Include routers
app.include_router(cv_proctoring_controller.router, prefix="/api/v1/cv", tags=["Computer Vision"])
app.include_router(nlp_processing_controller.router, prefix="/api/v1/nlp", tags=["NLP"])
app.include_router(ml_analytics_controller.router, prefix="/api/v1/ml", tags=["Machine Learning"])

if __name__ == "__main__":
    logger.info("Starting AI/ML Service...")
    uvicorn.run(app, host="0.0.0.0", port=5000)
