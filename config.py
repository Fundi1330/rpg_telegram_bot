from json import loads
from os import environ
from pydantic_settings import BaseSettings, DotEnvSettingsSource, YamlConfigSettingsSource, SettingsConfigDict
from database import DataBase

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        yaml_file='config.yml',
        env_file='.env',
        extra='forbid',
        env_ignore_empty=True,
        case_sensitive=True,
    )

    @classmethod
    def settings_customise_sources(cls, settings_cls, init_settings, env_settings, dotenv_settings, file_secret_settings):
        return (init_settings, env_settings, dotenv_settings, YamlConfigSettingsSource(settings_cls), file_secret_settings)

    # .env variables
    DATABASE_URI: str
    TELEGRAM_BOT_API_TOKEN: str

    # yaml variables
    assets_dir: str
    music_dir: str

    # Messages
    welcome_message: str
    help_message: str
    select_music_message: str
    stats_message: str
    first_name_message: str
    last_name_message: str
    after_auth_message: str
    wrong_part_of_fullname_message: str
    select_action_in_town_message: str
    board_message: str

config = Settings()

db: DataBase = DataBase(config.DATABASE_URI)