from typing import TypedDict
from stravapy.models.photos_summary_primary import PhotosSummaryPrmary

class PhotoSummary(TypedDict):
    count: int
    primary: PhotosSummaryPrmary 
