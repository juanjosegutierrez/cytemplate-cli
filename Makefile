###############
# Development
###############

REQUIREMENTS='requirements.txt' 


init:
	@echo Installing requirements
	pip3 install -r $(REQUIREMENTS)

	@echo Installing cytemplate
	pip3 install -e .
	@echo


###############
# Testing
###############


test: init
	@echo Running all tests
	py.test --verbose ./tests
	@echo


lint:
	which pycodestyle || pip3 install pycodestyle
	pycodestyle
	@echo