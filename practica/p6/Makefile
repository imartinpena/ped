# Makefile para la Práctica 6

# Directorio para la aplicación 1
APP1_DIR = app1

# Directorio para la aplicación 2
APP2_DIR = app2

# Objetivos para la aplicación 1
runApp1Serv:
	@echo "Ejecutando el servidor para la aplicación 1..."
	python3 $(APP1_DIR)/serv6_1.py

runApp1Cli:
	@echo "Ejecutando el cliente para la aplicación 1..."
	python3 $(APP1_DIR)/cli6_1.py

# Objetivos para la aplicación 2
runApp2Serv:
	@echo "Ejecutando el servidor para la aplicación 2..."
	python3 $(APP2_DIR)/serv6_2.py

runApp2Cli:
	@echo "Ejecutando el cliente para la aplicación 2..."
	python3 $(APP2_DIR)/cli6_2.py

# Limpieza
clean:
	@echo "Limpiando archivos temporales..."
	rm -rf __pycache__

# Instrucciones para ejecución específica
help:
	@echo "Objetivos disponibles:"
	@echo "runApp1Serv  - Ejecuta el servidor para la aplicación 1"
	@echo "runApp1Cli   - Ejecuta el cliente para la aplicación 1"
	@echo "runApp2Serv  - Ejecuta el servidor para la aplicación 2"
	@echo "runApp2Cli   - Ejecuta el cliente para la aplicación 2"
	@echo "clean        - Limpia los archivos temporales"
