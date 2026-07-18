import logging
from dataclasses import asdict, dataclass
from typing import Optional, Union

log = logging.getLogger("socketdev")


@dataclass
class QuotaData:
    quota: int
    maxQuota: int
    nextWindowRefresh: Optional[str] = None

    def __getitem__(self, key):
        return getattr(self, key)

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "QuotaData":
        return cls(
            quota=data["quota"],
            maxQuota=data["maxQuota"],
            nextWindowRefresh=data.get("nextWindowRefresh"),
        )


@dataclass
class GetQuotaResponse:
    success: bool
    status: int
    data: Optional[QuotaData] = None
    message: Optional[str] = None

    def __getitem__(self, key):
        return getattr(self, key)

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "GetQuotaResponse":
        data_value = data.get("data")
        return cls(
            success=data["success"],
            status=data["status"],
            message=data.get("message"),
            data=QuotaData.from_dict(data_value) if data_value else None,
        )


class Quota:
    def __init__(self, api):
        self.api = api

    def get(self, use_types: bool = False) -> Union[dict, GetQuotaResponse]:
        path = "quota"
        response = self.api.do_request(path=path)
        if response.status_code == 200:
            result = response.json()
            if use_types:
                return GetQuotaResponse.from_dict({"success": True, "status": 200, "data": result})
            return result

        error_message = response.json().get("error", {}).get("message", "Unknown error")
        log.error(f"Error getting quota: {response.status_code}, message: {error_message}")
        if use_types:
            return GetQuotaResponse.from_dict(
                {"success": False, "status": response.status_code, "message": error_message}
            )
        return {}
