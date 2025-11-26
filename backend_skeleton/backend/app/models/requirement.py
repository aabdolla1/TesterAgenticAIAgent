from sqlalchemy import Column, Integer, String
from .base import Base

class RequirementDocument(Base):
    __tablename__ = "requirement_documents"
    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    source_type = Column(String, default="upload")
    path_or_url = Column(String, nullable=False)
