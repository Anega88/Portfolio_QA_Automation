from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Kinopoisk_testing_ui:
    def __init__(self, test_config):
        self.test_config = test_config
        self._driver = None

    def set_driver(self, driver):
        self._driver = driver

    def search_main_page_movie(self, movie_name: str):
        """
        Request to search for a movie from the homepage of the website.
        """
        search_input = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'input[name="kp_query"]')
                )
            )
        search_input.clear()
        search_input.send_keys(movie_name)
        self.click_main_search_button()

    def search_main_page_actor(self, actor: str):
        """
        Request to search for an actor from the homepage of the website.
        """
        search_input = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'input[name="kp_query"]')
                )
            )
        search_input.send_keys(actor)
        self.click_main_search_button()

    def click_main_search_button(self):
        """
        Request to click the "Search" button on the homepage of the website.
        """
        try:
            search_button_svg = WebDriverWait(self._driver, 10).until(
                 EC.presence_of_element_located(
                     (By.XPATH, '//button[contains(@class, "styles_submit__2AIpj") and @aria-label="Найти"]')
                     )
                     )
            search_button_svg.click()
        except Exception as e:
            print(f"Error clicking main SVG search button: {e}")

    def click_extended_search_button(self):
        """
        Request to click the "Search" button in the advanced search section.
        """
        search_button_alt = self._driver.find_element(
            By.CSS_SELECTOR, 'input[class="el_18 submit nice_button"]'
            )
        search_button_alt.click()

    def extended_search_movie(
            self, movie_name: str = None, year: int = None, country: str = None, actor: str = None, genre: str = None
            ):
        """
        Request with extended search parameters, such as film year, country of 
        origin, actor appearing in the film, and film genre. 
        Parameters are set according to the required filtering criteria.
        """
        if not movie_name:
            movie_name = self.test_config.movie_to_search
        if not year:
            year = self.test_config.movie_year
        if not country:
            country = self.test_config.country
        if not actor:
            actor = self.test_config.actor
        if not genre:
            genre = self.test_config.genre

        wait = WebDriverWait(self._driver, 10)

        try:
            wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'a[aria-label="Расширенный поиск"]')
                    )).click()

            input_movie_name = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, '#find_film')
                    ))
            input_movie_name.send_keys(movie_name)

            input_year = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, '#year')
                    ))
            input_year.send_keys(year)

            input_country = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, '#country')
                    ))
            input_country.send_keys(country)

            input_actor = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'input[name="m_act[actor]"]')
                    ))
            input_actor.send_keys(actor)

            genre_dropdown = wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, 'id="m_act[genre]"')
                    ))
            genre_option = genre_dropdown.find_element(
                By.XPATH, f'//option[@value="{genre}"]'
                )
            genre_option.click()

        except Exception as e:
            print(f"Error while performing extended search: {e}")

    def open_reviews(self, movie_name: str):
        """
        Request that finds a movie by its title on the homepage of 
        the website and opens the "User Reviews" section for the found movie.
        """
        driver = self._driver
        wait = WebDriverWait(driver, 10)

        self.search_main_page_actor(movie_name)
        self.click_main_search_button()

        movie_link = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f'//a[text()="{movie_name}"]')
                )
                )
        movie_link.click()
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.styles_reviewCountLight__XNZ9P.styles_reviewCount__w_RrM')
                )).click()
        reviews_link = wait.until(
            EC.presence_of_element_located(
                (By.LINK_TEXT, "Рецензии зрителей")
                )
                )

        # Клик по ссылке "Рецензии зрителей"
        reviews_link.click()

    def open_filmography(self, actor: str):
        """
        A request that finds an actor by name on the homepage
        of the website and opens the actor's Filmography.
        """
        driver = self._driver
        wait = WebDriverWait(driver, 10)

        self.search_main_page_actor(actor)
        self.click_main_search_button()
        actor_link = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f'//a[text()="{actor}"]')
                )
                )
        actor_link.click()

        driver.execute_script("window.scrollBy(0, 2800)")

        # Scrolling to the "Filmography" button using ActionChains.
        filmography_button = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'button[data-tid="9fd92bab"] .styles_title__skJ4z')
                )
                )
        ActionChains(driver).scroll_to_element(filmography_button).perform()

        # Clicking on the "Filmography" button.
        filmography_button.click()