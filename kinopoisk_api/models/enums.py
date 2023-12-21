from enum import Enum


class ProductionStatus(Enum):
    FILMING = "FILMING"
    PRE_PRODUCTION = "PRE_PRODUCTION"
    COMPLETED = "COMPLETED"
    ANNOUNCED = "ANNOUNCED"
    UNKNOWN = "UNKNOWN"
    POST_PRODUCTION = "POST_PRODUCTION"


class FilmType(Enum):
    FILM = "FILM"
    TV_SHOW = "TV_SHOW"
    VIDEO = "VIDEO"
    MINI_SERIES = "MINI_SERIES"
    TV_SERIES = "TV_SERIES"
    UNKNOWN = "UNKNOWN"


class FactType(Enum):
    FACT = "FACT"
    BLOOPER = "BLOOPER"


class DistributionType(Enum):
    LOCAL = "LOCAL"
    COUNTRY_SPECIFIC = "COUNTRY_SPECIFIC"
    PREMIERE = "PREMIERE"
    ALL = "ALL"
    WORLD_PREMIER = "WORLD_PREMIER"


class ReleaseType(Enum):
    CINEMA = "CINEMA"
    DVD = "DVD"
    DIGITAL = "DIGITAL"
    BLURAY = "BLURAY"


class RelationType(Enum):
    SEQUEL = "SEQUEL"
    PREQUEL = "PREQUEL"
    REMAKE = "REMAKE"
    UNKNOWN = "UNKNOWN"


class ProfessionKey(Enum):
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


class Sex(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    UNKNOWN = "UNKNOWN"


class AccountType(Enum):
    FREE = "FREE"
    EXTENDED = "EXTENDED"
    UNLIMITED = "UNLIMITED"


class RelationType1(Enum):
    SIMILAR = "SIMILAR"


class ReviewType(Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"
    UNKNOWN = "UNKNOWN"


class Site(Enum):
    YOUTUBE = "YOUTUBE"
    KINOPOISK_WIDGET = "KINOPOISK_WIDGET"
    YANDEX_DISK = "YANDEX_DISK"
    UNKNOWN = "UNKNOWN"


class Order(Enum):
    DATE_ASC = "DATE_ASC"
    DATE_DESC = "DATE_DESC"
    USER_POSITIVE_RATING_ASC = "USER_POSITIVE_RATING_ASC"
    USER_POSITIVE_RATING_DESC = "USER_POSITIVE_RATING_DESC"
    USER_NEGATIVE_RATING_ASC = "USER_NEGATIVE_RATING_ASC"
    USER_NEGATIVE_RATING_DESC = "USER_NEGATIVE_RATING_DESC"


class ImageType(Enum):
    STILL = "STILL"
    SHOOTING = "SHOOTING"
    POSTER = "POSTER"
    FAN_ART = "FAN_ART"
    PROMO = "PROMO"
    CONCEPT = "CONCEPT"
    WALLPAPER = "WALLPAPER"
    COVER = "COVER"
    SCREENSHOT = "SCREENSHOT"


class CollectionType(Enum):
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


class Month(Enum):
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