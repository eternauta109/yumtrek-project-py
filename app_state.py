class AppState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppState, cls).__new__(cls)
            cls._instance.current_user = None
            cls._instance.movies_data = None
            cls._instance.selected_movies = []
        return cls._instance

    @staticmethod
    def set_current_user(user):
        app_state = AppState()
        app_state.current_user = user

    @staticmethod
    def get_current_user():
        app_state = AppState()
        return app_state.current_user

    @staticmethod
    def set_movies_data(data):
        app_state = AppState()
        app_state.movies_data = data

    @staticmethod
    def get_movies_data():
        app_state = AppState()
        return app_state.movies_data

    @staticmethod
    def set_selected_movies(selected_movies):
        app_state = AppState()
        app_state.selected_movies = selected_movies

    @staticmethod
    def get_selected_movies():
        app_state = AppState()
        return app_state.selected_movies
