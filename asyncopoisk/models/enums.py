from enum import Enum


class ProductionStatus(str, Enum):
    FILMING = "FILMING"
    PRE_PRODUCTION = "PRE_PRODUCTION"
    COMPLETED = "COMPLETED"
    ANNOUNCED = "ANNOUNCED"
    UNKNOWN = "UNKNOWN"
    POST_PRODUCTION = "POST_PRODUCTION"


class FilmType(str, Enum):
    FILM = "FILM"
    TV_SHOW = "TV_SHOW"
    VIDEO = "VIDEO"
    MINI_SERIES = "MINI_SERIES"
    TV_SERIES = "TV_SERIES"
    UNKNOWN = "UNKNOWN"


class FactType(str, Enum):
    FACT = "FACT"
    BLOOPER = "BLOOPER"


class DistributionType(str, Enum):
    LOCAL = "LOCAL"
    COUNTRY_SPECIFIC = "COUNTRY_SPECIFIC"
    PREMIERE = "PREMIERE"
    ALL = "ALL"
    WORLD_PREMIER = "WORLD_PREMIER"


class ReleaseType(str, Enum):
    CINEMA = "CINEMA"
    DVD = "DVD"
    DIGITAL = "DIGITAL"
    BLURAY = "BLURAY"


class RelationType(str, Enum):
    SEQUEL = "SEQUEL"
    PREQUEL = "PREQUEL"
    REMAKE = "REMAKE"
    UNKNOWN = "UNKNOWN"


class ProfessionKey(str, Enum):
    WRITER = "WRITER"
    OPERATOR = "OPERATOR"
    EDITOR = "EDITOR"
    COMPOSER = "COMPOSER"
    PRODUCER_USSR = "PRODUCER_USSR"
    HIMSELF = "HIMSELF"
    HERSELF = "HERSELF"
    HRONO_TITR_MALE = "HRONO_TITR_MALE"
    HRONO_TITR_FEMALE = "HRONO_TITR_FEMALE"
    TRANSLATOR = "TRANSLATOR"
    DIRECTOR = "DIRECTOR"
    DESIGN = "DESIGN"
    PRODUCER = "PRODUCER"
    ACTOR = "ACTOR"
    VOICE_DIRECTOR = "VOICE_DIRECTOR"
    VOICE_FEMALE = "VOICE_FEMALE"
    VOICE_MALE = "VOICE_MALE"
    UNKNOWN = "UNKNOWN"


class Sex(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    UNKNOWN = "UNKNOWN"


class AccountType(str, Enum):
    FREE = "FREE"
    EXTENDED = "EXTENDED"
    UNLIMITED = "UNLIMITED"


class RelationType1(str, Enum):
    SIMILAR = "SIMILAR"


class ReviewType(str, Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"
    UNKNOWN = "UNKNOWN"


class Site(str, Enum):
    YOUTUBE = "YOUTUBE"
    KINOPOISK_WIDGET = "KINOPOISK_WIDGET"
    YANDEX_DISK = "YANDEX_DISK"
    UNKNOWN = "UNKNOWN"


class Order(str, Enum):
    DATE_ASC = "DATE_ASC"
    DATE_DESC = "DATE_DESC"
    USER_POSITIVE_RATING_ASC = "USER_POSITIVE_RATING_ASC"
    USER_POSITIVE_RATING_DESC = "USER_POSITIVE_RATING_DESC"
    USER_NEGATIVE_RATING_ASC = "USER_NEGATIVE_RATING_ASC"
    USER_NEGATIVE_RATING_DESC = "USER_NEGATIVE_RATING_DESC"


class ImageType(str, Enum):
    STILL = "STILL"
    SHOOTING = "SHOOTING"
    POSTER = "POSTER"
    FAN_ART = "FAN_ART"
    PROMO = "PROMO"
    CONCEPT = "CONCEPT"
    WALLPAPER = "WALLPAPER"
    COVER = "COVER"
    SCREENSHOT = "SCREENSHOT"


class CollectionType(str, Enum):
    TOP_POPULAR_ALL = "TOP_POPULAR_ALL"
    TOP_POPULAR_MOVIES = "TOP_POPULAR_MOVIES"
    TOP_250_TV_SHOWS = "TOP_250_TV_SHOWS"
    TOP_250_MOVIES = "TOP_250_MOVIES"
    VAMPIRE_THEME = "VAMPIRE_THEME"
    COMICS_THEME = "COMICS_THEME"
    CLOSES_RELEASES = "CLOSES_RELEASES"
    FAMILY = "FAMILY"
    OSKAR_WINNERS_2021 = "OSKAR_WINNERS_2021"
    LOVE_THEME = "LOVE_THEME"
    ZOMBIE_THEME = "ZOMBIE_THEME"
    CATASTROPHE_THEME = "CATASTROPHE_THEME"
    KIDS_ANIMATION_THEME = "KIDS_ANIMATION_THEME"


class Month(str, Enum):
    JANUARY = "JANUARY"
    FEBRUARY = "FEBRUARY"
    MARCH = "MARCH"
    APRIL = "APRIL"
    MAY = "MAY"
    JUNE = "JUNE"
    JULY = "JULY"
    AUGUST = "AUGUST"
    SEPTEMBER = "SEPTEMBER"
    OCTOBER = "OCTOBER"
    NOVEMBER = "NOVEMBER"
    DECEMBER = "DECEMBER"


class SearchOrder(str, Enum):
    RATING = "RATING"
    NUM_VOTE = "NUM_VOTE"
    YEAR = "YEAR"


class SearchFilmType(str, Enum):
    FILM = "FILM"
    TV_SHOW = "TV_SHOW"
    MINI_SERIES = "MINI_SERIES"
    TV_SERIES = "TV_SERIES"
    ALL = "ALL"
