from dataclasses import dataclass
import json
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Sources:
    the_1377x: bool
    anidex: bool
    glo: bool
    piratebay: bool
    torrentz2: bool

    @staticmethod
    def from_dict(obj: Any) -> 'Sources':
        assert isinstance(obj, dict)
        the_1377x = from_bool(obj.get("1377x"))
        anidex = from_bool(obj.get("anidex"))
        glo = from_bool(obj.get("glo"))
        piratebay = from_bool(obj.get("piratebay"))
        torrentz2 = from_bool(obj.get("torrentz2"))
        return Sources(the_1377x, anidex, glo, piratebay, torrentz2)

    def to_dict(self) -> dict:
        result: dict = {"1377x": from_bool(self.the_1377_x)}
        result["anidex"] = from_bool(self.anidex)
        result["glo"] = from_bool(self.glo)
        result["piratebay"] = from_bool(self.piratebay)
        result["torrentz2"] = from_bool(self.torrentz2)
        return result


@dataclass
class Config:
    sources: Sources

    @staticmethod
    def from_dict(obj: Any) -> 'Config':
        assert isinstance(obj, dict)
        sources = Sources.from_dict(obj.get("sources"))
        return Config(sources)

    def to_dict(self) -> dict:
        return {"sources": to_class(Sources, self.sources)}

def get_config() -> Config:
    return Config.from_dict(json.load(open("config.json")))


def config_to_dict(x: Config) -> Any:
    return to_class(Config, x)