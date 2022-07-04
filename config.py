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
        result: dict = {"1377x": from_bool(self.the_1377x)}
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
#function to write to json file
    def to_json(self) -> str:
        import json
        
        # Data to be written
        data = self.to_dict()
        # Serializing json 
        json_object = json.dumps(data, indent = 4)
        
        # Writing to sample.json
        with open("config.json", "w") as outfile:
            outfile.write(json_object)       

    def change_source(self, source: str, value: bool) -> None:
        if source == "1377x":
            self.sources.the_1377x = value
        elif source == "anidex":
            self.sources.anidex = value
        elif source == "glo":
            self.sources.glo = value
        elif source == "piratebay":
            self.sources.piratebay = value
        elif source == "torrentz2":
            self.sources.torrentz2 = value
        else:
            raise ValueError("Invalid source")
        self.to_json()    
        
    
    def to_dict(self) -> dict:
        return {"sources": to_class(Sources, self.sources)}

def get_config() -> Config:
    return Config.from_dict(json.load(open("config.json")))


def config_to_dict(x: Config) -> Any:
    return to_class(Config, x)