runApp1Serv:
	@echo "Ejecutando Servidor en App1 - Transferencia de Archivos"
	@cd app1 && python3 serv4_1.py

runApp1Cli:
	@echo "Ejecutando Cliente en App1 - Transferencia de Archivos"
	@cd app1 && python3 cli4_1.py hola.txt

runApp2Serv:
	@echo "Ejecutando Servidor en App2 - Fecha y Hora"
	@cd app2 && python3 serv4_2.py

runApp2Cli:
	@echo "Ejecutando Cliente en App2 - Fecha y Hora"
	@cd app2 && python3 cli4_2.py

clean:
	@echo "Limpiando..."
	@rm -f /tmp/cli4_serv4_app1_socket
	@rm -f /tmp/cli4_serv4_app2_socket
	@pkill -f serv4_1.py
	@pkill -f serv4_2.py
