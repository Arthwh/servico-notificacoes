import uvicorn
from app.core import config

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=config.INSTANCE_PORT, reload=True)