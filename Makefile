# build the container and give it a name for reference later
build:
	docker build . -t image_test:latest -t image_test:test_tag

# run the container for interactive stuff
dev:
	docker run \
	    -v ${PWD}:/app \
	    -it image_test bash
