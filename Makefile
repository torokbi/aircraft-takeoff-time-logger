APP = aircraft-timeblock-logger


# Docker-specific targets
local-docker-build:
	docker build -t localhost/$(APP):dev .

local-docker-run:
	docker run --rm  -p 8081:80 localhost/$(APP):dev


# GCP-specific targets
gcloud-docker-init:
	gcloud auth configure-docker

gcloud-docker-build:
	docker build -t gcr.io/$(GCP_PROJECT_ID)/$(APP):$(ENVIROMENT) .

gcloud-docker-push:
	docker push gcr.io/$(GCP_PROJECT_ID)/$(APP):$(ENVIROMENT)

gcloud-run-deploy:
	gcloud run deploy $(APP)-$(ENVIROMENT) \
	--region europe-central2 \
	--image gcr.io/$(GCP_PROJECT_ID)/$(APP):$(ENVIROMENT) \
	--port 80 \
	--project $(GCP_PROJECT_ID) \
	--max-instances 1 \
	--platform managed \
	--labels enviroment=$(ENVIROMENT) \
	--allow-unauthenticated