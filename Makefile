########################## KAFKA ##########################
.PHONY: create-kafka
create-kafka:
	@sudo docker-compose -f kafka/docker-compose.yml up -d --build

.PHONY: kill-kafka
kill-kafka:
	@sudo docker-compose -f kafka/docker-compose.yml down

.PHONY: create-topic
create-topic:
	@sudo docker-compose -f kafka/docker-compose.yml exec broker kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic ${topic}

.PHONY: delete-topic
delete-topic:
	@sudo docker-compose -f kafka/docker-compose.yml exec broker kafka-topics --delete --bootstrap-server localhost:9092 --topic ${topic}
