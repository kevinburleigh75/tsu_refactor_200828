import pytest
import subprocess

random_seeds = [
    '1111',
    '1234',
    '2222',
    '3333',
    '4', ## no one goes to jail
    '4321',
    '4444',
    '5555',
]

@pytest.fixture(scope='module', params=random_seeds)
def random_seed(request):
    yield request.param

def test_output_for_given_seed(random_seed):

    golden_output = open('./golden_outputs/seed_{}.txt'.format(random_seed)).read()

    ## capture the output from running cmd
    actual_output = subprocess.run(
        ['python', 'trivia.py', str(random_seed)],
        capture_output=True
    ).stdout.decode('utf-8')

    assert actual_output == golden_output


