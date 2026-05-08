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
