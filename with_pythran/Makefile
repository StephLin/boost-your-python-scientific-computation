PYTHRAN_TARGET := lib.py

all: lib

.PHONY: clean
clean:
	@if compgen -G "$(PWD)/*.so" > /dev/null ; then rm $(PWD)/*.so; fi

lib:
	$(MAKE) clean
	pythran $(PYTHRAN_TARGET)