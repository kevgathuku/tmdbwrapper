import vcr
from pytest import fixture
from tmdbwrapper import TV

tmdb_vcr = vcr.VCR(filter_query_parameters=['api_key'])


@fixture
def tv_keys():
    # Responsible only for returning the test data
    return ['poster_path', 'overview', 'type', 'networks',
            'original_name', 'created_by', 'id', 'languages',
            'original_language', 'status', 'last_air_date',
            'first_air_date', 'seasons', 'backdrop_path',
            'name', 'homepage', 'popularity', 'vote_average']


@tmdb_vcr.use_cassette('tests/vcr_cassettes/tv-info.yml')
def test_tv_info(tv_keys):
    """Tests an API call to get a TV show's info"""

    tv_instance = TV(1396)
    response = tv_instance.info()

    assert isinstance(response, dict)
    assert response['id'] == 1396, "The ID should be in the response"
    assert set(tv_keys).issubset(response.keys())
    assert isinstance(response['seasons'], list)
    assert isinstance(response['networks'], list)


@tmdb_vcr.use_cassette('tests/vcr_cassettes/tv-popular.yml')
def test_tv_popular():
    """Tests an API call to get a popular tv shows"""

    response = TV.popular()

    assert isinstance(response, dict)
    assert isinstance(response['results'], list)
