publish:
	python setup.py sdist bdist_wheel
	@read -p "Do you want to upload the package to PyPI? (y/n) " answer; \
	if [ "$$answer" == "y"  ] ;then \
		twine upload dist/*; \
	fi
	rm -fr build dist mppm.egg-info
