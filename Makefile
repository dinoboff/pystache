# Makefile for skeleton
#
# Todo: add help target.



PYTHON  = python
PYTHON3 = python3
SETUP   = $(PYTHON) setup.py $(setupoptions)
SETUP3  = $(PYTHON3) setup.py $(setupoptions)
GIT     = git

DIST_VERSION = `$(SETUP) --version`
RELEASE_BRANCH = master

all: dist

build: clean MANIFEST.in
	@echo "Building squeleton package..."
	$(SETUP) build
	@echo

clean:
	@echo "Removing build and dist directories, and pyc files..."
	rm -rf ./build/
	rm -rf ./dist/
	rm -f distribute-*.tar.gz
	rm -f distribute-*.egg
	find . -name "*.pyc" -print0 | xargs -0 rm
	@echo

dist: clean MANIFEST.in
	@echo "Building src distribution of skeleton..."
	$(SETUP) sdist $(sdistoptions)
	@echo

install:
	$(SETUP) install

release: clean test tag upload
	@echo "Version $(DIST_VERSION) released."
	@echo

tag:
	@echo "Tagging version $(DIST_VERSION)..."
	$(GIT) pull origin $(RELEASE_BRANCH)
	$(GIT) tag v$(DIST_VERSION)
	$(GIT) push origin v$(DIST_VERSION)
	@echo

test: clean
	@echo "Running skeleton unit tests..."
	$(SETUP) test
	@echo

test3: clean
	@echo "Running skeleton unit tests with Python 3..."
	$(SETUP3) test
	@echo

upload: clean MANIFEST.in
	@echo "Uploading source distribution to pypi..."
	$(SETUP) register $(registeroptions) sdist $(sdistoptions) upload $(uploadoptions)
	@echo
	
upload3: clean MANIFEST.in
	@echo "Uploading source distribution to pypi..."
	$(SETUP3) test $(testoptions)
	$(SETUP3) register $(registeroptions) bdist_egg $(sdistoptions) upload $(uploadoptions)
	@echo

MANIFEST.in:
	@echo "Updating MANIFEST.in..."
	$(GIT) ls-files --exclude=".git*" | sed -e 's/^/include /g' > $(srcdir)/MANIFEST.in
	@echo

.PHONY: MANIFEST.in tag clean