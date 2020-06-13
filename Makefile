########################## KAFKA ##########################
.PHONY: create-kafka
start-kafka:
	@sudo docker-compose -f kafka/docker-compose.yml up -d --build

.PHONY: kill-kafka
kill-kafka:
	@sudo docker-compose -f kafka/docker-compose.yml down