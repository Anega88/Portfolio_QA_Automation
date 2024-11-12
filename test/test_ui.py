import pytest
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.epic("Search functionality")
@allure.feature("UI testing")
@allure.story("Search for a movie on the main page")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui
def test_search_movie_main_page(setup_auth_and_driver, test_config):
    """Sample UI test."""
    with allure.step("Open the website and check the CAPTCHA checkbox."):
        auth_ui, driver = setup_auth_and_driver
    with allure.step(
        "Enter the movie title in the search bar and click the search button."
    ):
        auth_ui.search_main_page_movie(test_config.movie_to_search)

    with allure.step("Check if the search result is displayed."):
        try:
            with allure.step("Check if there is a search result on the page."):
                if driver.find_elements(By.CSS_SELECTOR, '.search_results'):
                    with allure.step(
                        "Check if the movie is displayed in the search results."
                    ):
                        film_name_element = driver.find_element(
                            By.CSS_SELECTOR, '.search_results .name a'
                            )
                        assert film_name_element.text.strip().lower() == test_config.movie_to_search.strip().lower(), (
                            "Film name is not as expected."
                            )
                elif driver.find_elements(By.CSS_SELECTOR, 'h2.textorangebig'):
                    no_results_message = driver.find_element(
                        By.CSS_SELECTOR, 'h2.textorangebig'
                        ).text
                    assert no_results_message == (
                        "К сожалению, по вашему запросу ничего не найдено...", "Unexpected message when no results found."
                        )
                else:
                    assert False, "No search results or error message found."

        except Exception as e:
            assert False, (
                f"Search for '{
                    test_config.movie_to_search}' resulted in an error: {e}"
                )


@allure.epic("Search functionality")
@allure.feature("UI testing")
@allure.story("Search for a actor on the main page")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui
def test_search_actor_main_page(setup_auth_and_driver, test_config):
    with allure.step("Open the website and check the CAPTCHA checkbox."):
        auth_ui, driver = setup_auth_and_driver
    with allure.step(
        "Enter the actor's name in the search bar and click the search button."
    ):
        auth_ui.search_main_page_actor(test_config.actor)

    with allure.step("Check that the search result is displayed."):
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '.search_results')
                )
                )
            search_results_text = driver.find_element(
                By.CSS_SELECTOR, '.search_results_topText'
                ).text
            print(f"Results text: {search_results_text}")  # Debug output

            match = re.search(r'результаты: (\d+)', search_results_text)

            if match:
                results_count = int(match.group(1))
                assert results_count > 0, (
                    "No search results found for the actor."
                    )

                with allure.step(
                    "Check that the actor's name is displayed on the page."
                ):
                    actor_name_element = driver.find_element(
                        By.CSS_SELECTOR, '.search_results_topText b'
                        )

                with allure.step(
                    "Compare the actor's name displayed in the search results with the expected name."
                ):
                    assert actor_name_element.text.strip().lower() == test_config.actor.strip().lower(), (
                        "Actor name is not as expected."
                        )
            else:
                assert False, (
                    "Results count not found in the search results text."
                    )

        except Exception as e:
            assert False, (
                f"Search for '{test_config.actor}' resulted in an error: {e}"
                )


@allure.epic("Search functionality")
@allure.feature("UI testing")
@allure.story("Search for a movie using the extended search")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui
def test_extended_search_movie(setup_auth_and_driver, test_config):
    with allure.step("Open the website and check the CAPTCHA checkbox."):
        auth_ui, driver = setup_auth_and_driver
        expected_movie_text = (
            f"{test_config.movie_to_search} ({test_config.movie_year})"
            )

    with allure.step(
        "Go to the advanced search page and enter the search parameters."
    ):
        auth_ui.extended_search_movie(
            test_config.movie_to_search, test_config.movie_year, test_config.country, test_config.actor, test_config.genre
            )
    with allure.step("Click the Search button"):
        auth_ui.click_extended_search_button()

    with allure.step(
        "Compare the expected result with the actual one (title and year of the film.)"
    ):
        try:
            h1_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'h1[data-tid="f22e0093"]')
                    ))
            movie_element = h1_element.find_element(
                By.CSS_SELECTOR, 'span[data-tid="75209b22"]'
                )
            assert movie_element.text == expected_movie_text, (
                f"Expected '{
                    expected_movie_text}', but got '{movie_element.text}'"
                )
        except Exception as e:
            assert False, (
                f"Movie '{
                    expected_movie_text}' was not found in search results: {e}"
                )


@allure.epic("Search functionality")
@allure.feature("UI testing")
@allure.story("Open the movie reviews")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui
def test_search_and_open_movie_reviews(setup_auth_and_driver, test_config):
    with allure.step("Open the website and check the CAPTCHA checkbox."):
        auth_ui, driver = setup_auth_and_driver
    with allure.step(
        "Find a movie by movie title and go to the viewer reviews page."
    ):
        auth_ui.open_reviews(test_config.movie_name)
        all_reviews_label = driver.find_element(
            By.XPATH, '//span[text()="Все:"]'
            )

    with allure.step(
        "Find the number of displayed viewer reviews in the All section"
    ):
        all_reviews_count = all_reviews_label.find_element(
            By.XPATH, 'following-sibling::b'
            ).text

    number_of_reviews = int(all_reviews_count)

    with allure.step("Make sure there are more than 0 of them."):
        assert number_of_reviews > 0, (
            f"Expected at least one review, but found {number_of_reviews}."
            )


@allure.epic("Search functionality")
@allure.feature("UI testing")
@allure.story("Open the actor's filmography")
@allure.feature("READ")
@allure.severity("blocker")
@pytest.mark.ui
def test_search_and_open_actor_filmography(setup_auth_and_driver, test_config):
    with allure.step("Open the site, check the captcha checkbox"):
        auth_ui, driver = setup_auth_and_driver
    with allure.step(
        "Find an actor by name and go to the actor's filmography"
    ):
        auth_ui.open_filmography(test_config.actor)

    wait = WebDriverWait(driver, 10)
    actor_header = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, f'//h1[contains(text(), "{test_config.actor}")]')
            )
            )

    with allure.step("Make sure the title contains the actor's name"):
        assert actor_header.is_displayed(), (
            f"Filmography for actor '{test_config.actor}' could not be opened."
            )

    with allure.step("Check if the number of movies is greater than 0"):
        film_count_element = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'span.styles_subtitle__V93vt')
                )
                )
        film_count_text = film_count_element.text
        film_count = int(film_count_text.split()[0])
        assert film_count > 0, (
            f"No movies found for actor '{
                test_config.actor}'. Number of films: {film_count_text}."
            )
