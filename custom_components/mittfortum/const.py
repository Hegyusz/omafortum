"""Constants for the MittFortum integration."""

from __future__ import annotations

from datetime import timedelta

from homeassistant.const import Platform

# Integration domain
DOMAIN = "mittfortum"

# Platforms
PLATFORMS: list[Platform] = [Platform.SENSOR]

CONF_LOCALE = "locale"

# API endpoints
def get_fortum_base_url(locale: str) -> str:
    if locale == "SV":
        return "https://www.fortum.com/se/el"
    elif locale == "FI":
        return "https://www.fortum.com/fi/sahkoa"
    else:
        raise ValueError(f"Unsupported locale: {locale}")
def get_api_base_url(locale: str) -> str:
    return f"{get_fortum_base_url(locale)}/api"
def get_trpc_base_url(locale: str) -> str:
    return f"{get_api_base_url(locale)}/trpc"
OAUTH_BASE_URL = "https://sso.fortum.com"

def get_auth_index_value(locale: str) -> str:
    if locale == "SV":
        return "SeB2COGWLogin"
    elif locale == "FI":
        return "FIB2CLogin"
    else:
        raise ValueError(f"Unsupported locale: {locale}")

# Session endpoint (for customer details and metering points)
def get_session_url(locale: str) -> str:
    return f"{get_api_base_url(locale)}/auth/session"

# tRPC endpoints (only for time series data)
def get_time_series_base_url(locale: str) -> str:
    return f"{get_trpc_base_url(locale)}/loggedIn.timeSeries.listTimeSeries"

# API request configuration
TRPC_BATCH_PARAM = "1"
DEFAULT_RESOLUTION = "MONTH"
AVAILABLE_RESOLUTIONS = ["HOUR", "DAY", "MONTH", "YEAR"]

# Energy data types
ENERGY_DATA_TYPE = "ENERGY"

# Cost component types
COST_TYPES = {
    "ELCERT_AMOUNT": "Certificate costs",
    "FIXED_FEE_AMOUNT": "Fixed fees",
    "SPOT_VARIABLE_AMOUNT": "Variable spot price",
    "VAR_AMOUNT": "Variable amount",
    "VAR_DISCOUNT_AMOUNT": "Discounts",
}

# OAuth2 configuration
OAUTH_CLIENT_ID = "globalwebprod"
def get_oauth_redirect_uri(locale: str) -> str:
    return f"{get_api_base_url(locale)}/auth/callback/ciamprod"
OAUTH_SECRET_KEY = "shared_secret"
OAUTH_SCOPE = ["openid", "profile", "crmdata"]

# OAuth2 endpoints
OAUTH_CONFIG_URL = f"{OAUTH_BASE_URL}/.well-known/openid-configuration"
OAUTH_TOKEN_URL = f"{OAUTH_BASE_URL}/am/oauth2/access_token"
OAUTH_AUTH_URL = f"{OAUTH_BASE_URL}/am/json/realms/root/realms/alpha/authenticate"

# Update intervals
DEFAULT_UPDATE_INTERVAL = timedelta(minutes=30)
TOKEN_REFRESH_INTERVAL = timedelta(minutes=5)

# Device information
MANUFACTURER = "Fortum"
MODEL = "MittFortum"

# Sensor configuration
ENERGY_SENSOR_KEY = "energy_consumption"
COST_SENSOR_KEY = "total_cost"

# Data storage keys
CONF_CUSTOMER_ID = "customer_id"
CONF_METERING_POINTS = "metering_points"

def get_cost_unit(locale: str) -> str:
    if locale == "SV":
        return "SEK"
    elif locale == "FI":
        return "EUR"
    else:
        raise ValueError(f"Unsupported locale: {locale}")