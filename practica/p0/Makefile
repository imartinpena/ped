SRC=hw
EXE=$(SRC)

do: console

all: console clean

console: run clean

run: $(SRC).py
	@echo "Hello world en $@..."
	python3 $<

clean:
	@echo "Limpiando..."
	rm -f $(EXE) HelloWorld.class