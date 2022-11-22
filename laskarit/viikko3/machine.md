title Tehtävä 3

Main->Machine: Machine()
Machine->FuelTank: FuelTank()
Machine->FuelTank: self._tank.fill(40)
Machine->Engine: Engine(self._tank)

Machine->Engine: self._engine.start()
Engine->FuelTank: self._fuel_tank.consume(5)
Machine->Engine: self._engine.is_running()
activate Engine
Engine-->Machine: true
deactivate Engine

Machine->Engine: self._engine.use_energy()
Engine->FuelTank: self._fuel_tank.consume(10)
Machine->Engine: self._engine.use_energy()
Engine->FuelTank: self._fuel_tank.consume(10)
Machine->Engine: self._engine.use_energy()
Engine->FuelTank: self._fuel_tank.consume(10)
