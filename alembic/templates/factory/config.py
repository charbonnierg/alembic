from pathlib import Path

from alembic.config import Config


HERE = Path(__file__).parent


def factory(config: Config) -> None:
    """Configures an Alembic Config object."""

    config.set_main_option("script_location", HERE.as_posix())
    config.set_main_option(
        "version_locations", HERE.joinpath("versions").as_posix()
    )
    config.set_main_option(
        "sqlalchemy.url", "driver://user:pass@localhost/dbname"
    )
