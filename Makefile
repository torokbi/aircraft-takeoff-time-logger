APP = aircraft-timeblock-logger


local-docker-build:
	docker build -t localhost/$(APP):dev .

local-docker-run:
	docker run --rm  -p 8081:80 localhost/$(APP):dev