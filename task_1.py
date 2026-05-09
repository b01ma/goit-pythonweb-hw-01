from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)


# Abstract product
class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        raise NotImplementedError


# Concrete product
class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info("%s %s: Двигун запущено", self.make, self.model)


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info("%s %s: Мотор заведено", self.make, self.model)


# Abstract Factory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        raise NotImplementedError

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        raise NotImplementedError


# Concrete Factory
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, f"{model} (EU Spec)")


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    us_car = us_factory.create_car("Ford", "Mustang")
    us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    eu_car = eu_factory.create_car("Volkswagen", "Golf")
    eu_motorcycle = eu_factory.create_motorcycle("BMW", "R nineT")

    vehicles: list[Vehicle] = [us_car, us_motorcycle, eu_car, eu_motorcycle]

    for vehicle in vehicles:
        vehicle.start_engine()


if __name__ == "__main__":
    main()
