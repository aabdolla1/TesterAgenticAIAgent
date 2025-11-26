from pydantic import BaseModel

class RequirementUpload(BaseModel):
    title: str
    path_or_url: str
