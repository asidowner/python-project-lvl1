# Install project
install:
	poetry install

# Run brain-games locally, work after install
brain-games:
	poetry run brain-games

# Run game "even" locally, work after install
brain-even:
	poetry run brain-even

# Run game "calculate" locally, work after install
brain-calc:
	poetry run brain-calc

# Run game "gcd" locally, work after install
brain-gcd:
	poetry run brain-gcd

# Run game "progression" locally, work after install
brain-progression:
	poetry run brain-progression

# Run game "prime" locally, work after install
brain-prime:
	poetry run brain-prime

# build project and make package on dist folder
build:
	poetry build

# Test publish project
publish:
	poetry publish --dry-run

# Install package
package-install:
	python3 -m pip install --user dist/*.whl

# Install package if use project venv
package-install-local-venv:
	python3 -m pip install dist/*.whl

# Remove package
package-remove:
	python3 -m pip uninstall hexlet-code

# Check lint by flake8, see setup.cfg
lint:
	poetry run flake8 brain_games