"""API endpoints configuration."""

from __future__ import annotations

import json
import urllib.parse
from datetime import datetime

from ..const import (
    OAUTH_AUTH_URL,
    OAUTH_BASE_URL,
    OAUTH_CONFIG_URL,
    OAUTH_TOKEN_URL,
    get_time_series_base_url,
    get_api_base_url,
    get_auth_index_value
)


class APIEndpoints:
    """API endpoints configuration."""

    # OAuth2 endpoints
    OPENID_CONFIG = OAUTH_CONFIG_URL
    TOKEN_EXCHANGE = OAUTH_TOKEN_URL
    USER_SESSION = f"{OAUTH_BASE_URL}/am/json/users?_action=idFromSession"
    THEME_REALM = "{OAUTH_BASE_URL}/openidm/config/ui/themerealm"
    USER_DETAILS = (
        "{OAUTH_BASE_URL}/am/json/realms/root/realms/alpha/users/{user_id}"
    )
    VALIDATE_GOTO = "{OAUTH_BASE_URL}/am/json/realms/root/realms/alpha/users?_action=validateGoto"

    @staticmethod
    def get_auth_init_url(locale: str) -> str:
        """Get OAuth2 authorization URL."""
        return (
            f"{OAUTH_AUTH_URL}?locale={locale.lower()}&authIndexType=service&authIndexValue={get_auth_index_value(locale).lower()}"
        )
    
    @staticmethod
    def get_session_username_url(locale: str) -> str:
        """Get session username URL."""
        return f"{get_api_base_url(locale)}/get-session-username"
    
    @staticmethod
    def get_session_url(locale: str) -> str:
        """Get session URL."""
        return f"{get_api_base_url(locale)}/auth/session"

    @staticmethod
    def get_time_series_url(
        locale: str,
        metering_point_nos: list[str],
        from_date: datetime,
        to_date: datetime,
        resolution: str = "MONTH",
    ) -> str:
        """Get time series URL with tRPC format."""
        input_data = {
            "0": {
                "json": {
                    "meteringPointNo": metering_point_nos,
                    "fromDate": from_date.isoformat() + "Z",
                    "toDate": to_date.isoformat() + "Z",
                    "resolution": resolution,
                }
            }
        }

        input_json = json.dumps(input_data, separators=(",", ":"))
        input_encoded = urllib.parse.quote(input_json)

        return f"{get_time_series_base_url(locale)}?batch=1&input={input_encoded}"

    @staticmethod
    def get_user_details_url(user_id: str) -> str:
        """Get user details URL."""
        return APIEndpoints.USER_DETAILS.format(user_id=user_id)
