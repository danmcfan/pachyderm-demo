.PHONY: all create_repo upload create_pipeline delete

all: create_repo upload create_pipeline delete

create_repo:
	pachctl create repo images
	pachctl create repo labels

upload:
	pachctl start transaction
	pachctl start commit images@master
	pachctl start commit labels@master
	pachctl finish transaction
	pachctl put file images@master:/ -r -f data/nested/images/n02085620-Chihuahua/
	pachctl put file labels@master:/ -r -f data/nested/labels/n02085620-Chihuahua/
	pachctl finish commit images@master
	pachctl finish commit labels@master

create_pipeline:
	pachctl create pipeline -f pipelines/bbox.yml
	pachctl create pipeline -f pipelines/normalize.yml
	pachctl create pipeline -f pipelines/aggregate.yml
	pachctl create pipeline -f pipelines/montage.yml

delete:
	pachctl delete pipeline --all
	pachctl delete repo --all