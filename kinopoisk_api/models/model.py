from typing import List, Optional

from pydantic import BaseModel, Field

from .enums import (
    ProductionStatus,
    FilmType,
    FactType,
    DistributionType,
    ReleaseType,
    RelationType,
    ProfessionKey,
    Sex,
    AccountType,
    RelationType1,
    ReviewType,
    Site,
)


class Fact(BaseModel):
    text: str = Field(
        ...,
        example="В эпизоде, где Тринити и Нео в поисках Морфиуса оказываются на крыше...",
    )
    type: FactType = Field(..., example="BLOOPER")
    spoiler: bool = Field(..., example=False)


class BoxOffice(BaseModel):
    type: str = Field(..., example="BUDGET")
    amount: int = Field(..., example=63000000)
    currencyCode: str = Field(..., example="USD")
    name: str = Field(..., example="US Dollar")
    symbol: str = Field(..., example="$")


class AwardPerson(BaseModel):
    kinopoiskId: int = Field(..., example=1937039)
    webUrl: str = Field(..., example="https://www.kinopoisk.ru/name/1937039/")
    nameRu: Optional[str] = Field(..., example="Джон Т. Рейц")
    nameEn: Optional[str] = Field(..., example="John T. Reitz")
    sex: str = Field(..., example="MALE")
    posterUrl: str = Field(
        ...,
        example="https://kinopoiskapiunofficial.tech/images/actor_posters/kp/1937039.jpg",
    )
    growth: Optional[int] = Field(..., example=178)
    birthday: Optional[str] = Field(..., example="1955-11-02")
    death: Optional[str] = Field(..., example="2019-01-06")
    age: Optional[int] = Field(..., example=21)
    birthplace: Optional[str] = Field(..., example="Лос-Анджелес, Калифорния, США")
    deathplace: Optional[str] = Field(..., example="Лос-Анджелес, Калифорния, США")
    profession: Optional[str] = Field(..., example="Монтажер, Продюсер")


class Company(BaseModel):
    name: str = Field(..., example="Каро-Премьер")


class Episode(BaseModel):
    seasonNumber: int = Field(..., example=1)
    episodeNumber: int = Field(..., example=1)
    nameRu: Optional[str]
    nameEn: Optional[str] = Field(
        ..., example="Chapter One: The Vanishing of Will Byers"
    )
    synopsis: Optional[str] = Field(..., example="The Vanishing of Will Byers...")
    releaseDate: Optional[str] = Field(..., example="2016-07-15")


class Country(BaseModel):
    country: str = Field(..., example="США")


class Genre(BaseModel):
    genre: str = Field(..., example="фантастика")


class FilmSequelsAndPrequelsResponse(BaseModel):
    filmId: int = Field(..., example=301)
    nameRu: str = Field(..., example="Матрица")
    nameEn: str = Field(..., example="The Matrix")
    nameOriginal: str = Field(..., example="The Matrix")
    posterUrl: str = Field(
        ..., example="https://kinopoiskapiunofficial.tech/images/posters/kp/301.jpg"
    )
    posterUrlPreview: str = Field(
        ...,
        example="https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg",
    )
    relationType: RelationType = Field(..., example="SEQUEL")


class StaffResponse(BaseModel):
    staffId: int = Field(..., example=66539)
    nameRu: Optional[str] = Field(..., example="Винс Гиллиган")
    nameEn: Optional[str] = Field(..., example="Vince Gilligan")
    description: Optional[str] = Field(..., example="Neo")
    posterUrl: str = Field(
        ..., example="https://st.kp.yandex.net/images/actor/66539.jpg"
    )
    professionText: str = Field(..., example="Режиссеры")
    professionKey: ProfessionKey = Field(..., example="DIRECTOR")


class PremiereResponseItem(BaseModel):
    kinopoiskId: int = Field(..., example=301)
    nameRu: Optional[str] = Field(..., example="Дитя погоды")
    nameEn: Optional[str] = Field(..., example="Tenki no ko")
    year: int = Field(..., example=2019)
    posterUrl: str = Field(
        ..., example="http://kinopoiskapiunofficial.tech/images/posters/kp/1219417.jpg"
    )
    posterUrlPreview: str = Field(
        ...,
        example="https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg",
    )
    countries: List[Country]
    genres: List[Genre]
    duration: Optional[int] = Field(..., example=112)
    premiereRu: str = Field(..., example="2020-06-01")


class DigitalReleaseItem(BaseModel):
    filmId: int = Field(..., example=301)
    nameRu: Optional[str] = Field(..., example="Дитя погоды")
    nameEn: Optional[str] = Field(..., example="Tenki no ko")
    year: Optional[int] = Field(..., example=2019)
    posterUrl: str = Field(
        ..., example="http://kinopoiskapiunofficial.tech/images/posters/kp/1219417.jpg"
    )
    posterUrlPreview: str = Field(
        ...,
        example="https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg",
    )
    countries: List[Country]
    genres: List[Genre]
    rating: Optional[float] = Field(..., example=7.962)
    ratingVoteCount: Optional[int] = Field(..., example=14502)
    expectationsRating: Optional[float] = Field(..., example=99.13)
    expectationsRatingVoteCount: Optional[int] = Field(..., example=1123)
    duration: Optional[int] = Field(..., example=112)
    releaseDate: str = Field(..., example="2020-06-01")


class ApiError(BaseModel):
    message: str = Field(..., example="User test@test.ru is inactive or deleted.")


class FiltersResponseGenres(BaseModel):
    id: Optional[int] = Field(None, example=1)
    genre: Optional[str] = Field(None, example="боевик")


class FiltersResponseCountries(BaseModel):
    id: Optional[int] = Field(None, example=1)
    country: Optional[str] = Field(None, example="США")


class FilmSearchResponseFilms(BaseModel):
    filmId: Optional[int] = Field(None, example=263531)
    nameRu: Optional[str] = Field(None, example="Мстители")
    nameEn: Optional[str] = Field(None, example="The Avengers")
    type: Optional[FilmType] = Field(None, example="FILM")
    year: Optional[str] = Field(None, example="2012")
    description: Optional[str] = Field(None, example="США, Джосс Уидон(фантастика)")
    filmLength: Optional[str] = Field(None, example="2:17")
    countries: Optional[List[Country]] = None
    genres: Optional[List[Genre]] = None
    rating: Optional[str] = Field(
        None,
        example="NOTE!!! 7.9 for released film or 99% if film have not released yet",
    )
    ratingVoteCount: Optional[int] = Field(None, example=284245)
    posterUrl: Optional[str] = Field(
        None, example="http://kinopoiskapiunofficial.tech/images/posters/kp/263531.jpg"
    )
    posterUrlPreview: Optional[str] = Field(
        None,
        example="https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg",
    )


class FilmSearchByFiltersResponseItems(BaseModel):
    kinopoiskId: Optional[int] = Field(None, example=263531)
    imdbId: Optional[str] = Field(None, example="tt0050561")
    nameRu: Optional[str] = Field(None, example="Мстители")
    nameEn: Optional[str] = Field(None, example="The Avengers")
    nameOriginal: Optional[str] = Field(None, example="The Avengers")
    countries: Optional[List[Country]] = None
    genres: Optional[List[Genre]] = None
    ratingKinopoisk: Optional[float] = Field(None, example=7.9)
    ratingImdb: Optional[float] = Field(None, example=7.9)
    year: Optional[float] = Field(None, example=2012)
    type: Optional[FilmType] = Field(None, example="FILM")
    posterUrl: Optional[str] = Field(
        None, example="http://kinopoiskapiunofficial.tech/images/posters/kp/263531.jpg"
    )
    posterUrlPreview: Optional[str] = Field(
        None,
        example="https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg",
    )


class RelatedFilmResponseItems(BaseModel):
    filmId: Optional[int] = Field(None, example=301)
    nameRu: Optional[str] = Field(None, example="Матрица")
    nameEn: Optional[str] = Field(None, example="The Matrix")
    nameOriginal: Optional[str] = Field(None, example="The Matrix")
    posterUrl: Optional[str] = Field(
        None, example="https://kinopoiskapiunofficial.tech/images/posters/kp/301.jpg"
    )
    posterUrlPreview: Optional[str] = Field(
        None,
        example="https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg",
    )
    relationType: Optional[RelationType1] = Field(None, example="SIMILAR")


class ReviewResponseItems(BaseModel):
    kinopoiskId: Optional[int] = Field(None, example=2)
    type: Optional[ReviewType] = None
    date: Optional[str] = Field(None, example="2010-09-05T20:37:00")
    positiveRating: Optional[int] = Field(None, example=122)
    negativeRating: Optional[int] = Field(None, example=12)
    author: Optional[str] = Field(None, example="Username")
    title: Optional[str] = Field(None, example="Title")
    description: Optional[str] = Field(None, example="text")


class ExternalSourceResponseItems(BaseModel):
    url: Optional[str] = Field(
        None,
        example="https://okko.tv/movie/equilibrium?utm_medium=referral&utm_source=yandex_search&utm_campaign=new_search_feed",
    )
    platform: Optional[str] = Field(None, example="Okko")
    logoUrl: Optional[str] = Field(
        None,
        example="https://avatars.mds.yandex.net/get-ott/239697/7713e586-17d1-42d1-ac62-53e9ef1e70c3/orig",
    )
    positiveRating: Optional[int] = Field(None, example=122)
    negativeRating: Optional[int] = Field(None, example=12)
    author: Optional[str] = Field(None, example="Username")
    title: Optional[str] = Field(None, example="Title")
    description: Optional[str] = Field(None, example="text")


class FilmCollectionResponseItems(BaseModel):
    kinopoiskId: Optional[int] = Field(None, example=263531)
    nameRu: Optional[str] = Field(None, example="Мстители")
    nameEn: Optional[str] = Field(None, example="The Avengers")
    nameOriginal: Optional[str] = Field(None, example="The Avengers")
    countries: Optional[List[Country]] = None
    genres: Optional[List[Genre]] = None
    ratingKinopoisk: Optional[float] = Field(None, example=7.9)
    ratingImbd: Optional[float] = Field(None, example=7.9)
    year: Optional[int] = Field(None, example="2012")
    type: Optional[FilmType] = Field(None, example="FILM")
    posterUrl: Optional[str] = Field(
        None, example="http://kinopoiskapiunofficial.tech/images/posters/kp/263531.jpg"
    )
    posterUrlPreview: Optional[str] = Field(
        None,
        example="https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg",
    )


class PersonResponseSpouses(BaseModel):
    personId: Optional[int] = Field(None, example=32169)
    name: Optional[str] = Field(None, example="Сьюзан Дауни")
    divorced: Optional[bool] = Field(None, example=False)
    divorcedReason: Optional[str] = Field(None, example="")
    sex: Optional[Sex] = Field(None, example="MALE")
    children: Optional[int] = Field(None, example=2)
    webUrl: Optional[str] = Field(None, example="https://www.kinopoisk.ru/name/32169/")
    relation: Optional[str] = Field(None, example="супруга")


class PersonResponseFilms(BaseModel):
    filmId: Optional[int] = Field(None, example=32169)
    nameRu: Optional[str] = Field(None, example="Солист")
    nameEn: Optional[str] = Field(None, example="The Soloist")
    rating: Optional[str] = Field(
        None, example="7.2 or 76% if film has not released yet"
    )
    general: Optional[bool] = Field(None, example=False)
    description: Optional[str] = Field(None, example="Steve Lopez")
    professionKey: Optional[ProfessionKey] = Field(None, example="ACTOR")


class PersonByNameResponseItems(BaseModel):
    kinopoiskId: Optional[int] = Field(None, example=66539)
    webUrl: Optional[str] = Field(None, example="10096")
    nameRu: Optional[str] = Field(None, example="Винс Гиллиган")
    nameEn: Optional[str] = Field(None, example="Vince Gilligan")
    sex: Optional[Sex] = Field(None, example="MALE")
    posterUrl: Optional[str] = Field(
        None,
        example="https://kinopoiskapiunofficial.tech/images/actor_posters/kp/10096.jpg",
    )


class ImageResponseItems(BaseModel):
    imageUrl: Optional[str] = Field(
        None,
        example="https://avatars.mds.yandex.net/get-kinopoisk-image/4303601/2924f6c4-4ea0-4a1d-9a48-f29577172b27/orig",
    )
    previewUrl: Optional[str] = Field(
        None,
        example="https://avatars.mds.yandex.net/get-kinopoisk-image/4303601/2924f6c4-4ea0-4a1d-9a48-f29577172b27/300x",
    )


class VideoResponseItems(BaseModel):
    url: Optional[str] = Field(
        None, example="https://www.youtube.com/watch?v=gbcVZgO4n4E"
    )
    name: Optional[str] = Field(
        None, example="Мстители: Финал – официальный трейлер (16+)"
    )
    site: Optional[Site] = Field(None, example="YOUTUBE")


class KinopoiskUserVoteResponseItems(BaseModel):
    kinopoiskId: Optional[int] = Field(None, example=263531)
    nameRu: Optional[str] = Field(None, example="Мстители")
    nameEn: Optional[str] = Field(None, example="The Avengers")
    nameOriginal: Optional[str] = Field(None, example="The Avengers")
    countries: Optional[List[Country]] = None
    genres: Optional[List[Genre]] = None
    ratingKinopoisk: Optional[float] = Field(None, example=7.9)
    ratingImbd: Optional[float] = Field(None, example=7.9)
    year: Optional[str] = Field(None, example="2012")
    type: Optional[FilmType] = Field(None, example="FILM")
    posterUrl: Optional[str] = Field(
        None, example="http://kinopoiskapiunofficial.tech/images/posters/kp/263531.jpg"
    )
    posterUrlPreview: Optional[str] = Field(
        None,
        example="https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg",
    )
    userRating: Optional[int] = Field(None, example=7)


class ApiKeyResponseTotalQuota(BaseModel):
    value: int = Field(..., example=1000)
    used: int = Field(..., example=2)


class ApiKeyResponseDailyQuota(BaseModel):
    value: int = Field(..., example=500)
    used: int = Field(..., example=2)


class Film(BaseModel):
    kinopoiskId: int = Field(..., example=301)
    kinopoiskHDId: Optional[str] = Field(
        ..., example="4824a95e60a7db7e86f14137516ba590"
    )
    imdbId: Optional[str] = Field(..., example="tt0133093")
    nameRu: Optional[str] = Field(..., example="Матрица")
    nameEn: Optional[str] = Field(..., example="The Matrix")
    nameOriginal: Optional[str] = Field(..., example="The Matrix")
    posterUrl: str = Field(
        ..., example="https://kinopoiskapiunofficial.tech/images/posters/kp/301.jpg"
    )
    posterUrlPreview: str = Field(
        ...,
        example="https://kinopoiskapiunofficial.tech/images/posters/kp_small/301.jpg",
    )
    coverUrl: Optional[str] = Field(
        ...,
        example="https://avatars.mds.yandex.net/get-ott/1672343/2a0000016cc7177239d4025185c488b1bf43/orig",
    )
    logoUrl: Optional[str] = Field(
        ...,
        example="https://avatars.mds.yandex.net/get-ott/1648503/2a00000170a5418408119bc802b53a03007b/orig",
    )
    reviewsCount: int = Field(..., example=293)
    ratingGoodReview: Optional[float] = Field(..., example=88.9)
    ratingGoodReviewVoteCount: Optional[int] = Field(..., example=257)
    ratingKinopoisk: Optional[float] = Field(..., example=8.5)
    ratingKinopoiskVoteCount: Optional[int] = Field(..., example=524108)
    ratingImdb: Optional[float] = Field(..., example=8.7)
    ratingImdbVoteCount: Optional[int] = Field(..., example=1729087)
    ratingFilmCritics: Optional[float] = Field(..., example=7.8)
    ratingFilmCriticsVoteCount: Optional[int] = Field(..., example=155)
    ratingAwait: Optional[float] = Field(..., example=7.8)
    ratingAwaitCount: Optional[int] = Field(..., example=2)
    ratingRfCritics: Optional[float] = Field(..., example=7.8)
    ratingRfCriticsVoteCount: Optional[int] = Field(..., example=31)
    webUrl: str = Field(..., example="https://www.kinopoisk.ru/film/301/")
    year: Optional[int] = Field(..., example=1999)
    filmLength: Optional[int] = Field(..., example=136)
    slogan: Optional[str] = Field(..., example="Добро пожаловать в реальный мир")
    description: Optional[str] = Field(
        ..., example="Жизнь Томаса Андерсона разделена на\xa0две части:"
    )
    shortDescription: Optional[str] = Field(
        ...,
        example="Хакер Нео узнает, что его мир — виртуальный. Выдающийся экшен, доказавший, что зрелищное кино может быть умным",
    )
    editorAnnotation: Optional[str] = Field(
        ..., example="Фильм доступен только на языке оригинала с русскими субтитрами"
    )
    isTicketsAvailable: bool = Field(..., example=False)
    productionStatus: Optional[ProductionStatus] = Field(..., example="POST_PRODUCTION")
    type: FilmType = Field(..., example="FILM")
    ratingMpaa: Optional[str] = Field(..., example="r")
    ratingAgeLimits: Optional[str] = Field(..., example="age16")
    hasImax: Optional[bool] = Field(..., example=False)
    has3D: Optional[bool] = Field(..., example=False)
    lastSync: str = Field(..., example="2021-07-29T20:07:49.109817")
    countries: List[Country]
    genres: List[Genre]
    startYear: Optional[int] = Field(..., example=1996)
    endYear: Optional[int] = Field(..., example=1996)
    serial: Optional[bool] = Field(None, example=False)
    shortFilm: Optional[bool] = Field(None, example=False)
    completed: Optional[bool] = Field(None, example=False)


class FactResponse(BaseModel):
    total: int = Field(..., example=5)
    items: List[Fact]


class BoxOfficeResponse(BaseModel):
    total: int = Field(..., example=5)
    items: List[BoxOffice]


class Award(BaseModel):
    name: str = Field(..., example="Оскар")
    win: bool = Field(..., example=True)
    imageUrl: Optional[str] = Field(
        ...,
        example="https://avatars.mds.yandex.net/get-kinopoisk-image/1600647/09035193-2458-4de7-a7df-ad8f85b73798/orig",
    )
    nominationName: str = Field(..., example="Лучший звук")
    year: int = Field(..., example=2000)
    persons: Optional[List[AwardPerson]] = None


class Distribution(BaseModel):
    type: DistributionType = Field(..., example="PREMIERE")
    subType: Optional[ReleaseType] = Field(..., example="CINEMA")
    date: Optional[str] = Field(..., example="1999-05-07")
    reRelease: Optional[bool] = Field(..., example=False)
    country: Optional[Country]
    companies: List[Company]


class Season(BaseModel):
    number: int = Field(..., example=1)
    episodes: List[Episode]


class FiltersResponse(BaseModel):
    genres: List[FiltersResponseGenres]
    countries: List[FiltersResponseCountries]


class FilmSearchResponse(BaseModel):
    keyword: str = Field(..., example="мстители")
    pagesCount: int = Field(..., example=7)
    searchFilmsCountResult: int = Field(..., example=134)
    films: List[FilmSearchResponseFilms]


class FilmSearchByFiltersResponse(BaseModel):
    total: int = Field(..., example=7)
    totalPages: int = Field(..., example=1)
    items: List[FilmSearchByFiltersResponseItems]


class RelatedFilmResponse(BaseModel):
    total: int = Field(..., example=7)
    items: List[RelatedFilmResponseItems]


class ReviewResponse(BaseModel):
    total: int = Field(
        ..., description="Суммарное кол-во пользовательских рецензий", example=12
    )
    totalPages: int = Field(..., example=2)
    totalPositiveReviews: int = Field(..., example=1)
    totalNegativeReviews: int = Field(..., example=7)
    totalNeutralReviews: int = Field(..., example=12)
    items: List[ReviewResponseItems]


class ExternalSourceResponse(BaseModel):
    total: int = Field(..., description="Суммарное кол-во сайтов", example=12)
    items: List[ExternalSourceResponseItems]


class FilmCollectionResponse(BaseModel):
    total: int = Field(..., example=200)
    totalPages: int = Field(..., example=7)
    items: List[FilmCollectionResponseItems]


class PersonResponse(BaseModel):
    personId: int = Field(..., example=66539)
    webUrl: Optional[str] = Field(..., example="10096")
    nameRu: Optional[str] = Field(..., example="Винс Гиллиган")
    nameEn: Optional[str] = Field(..., example="Vince Gilligan")
    sex: Optional[Sex] = Field(..., example="MALE")
    posterUrl: str = Field(
        ...,
        example="https://kinopoiskapiunofficial.tech/images/actor_posters/kp/10096.jpg",
    )
    growth: Optional[int] = Field(..., example="174")
    birthday: Optional[str] = Field(..., example="1965-04-04")
    death: Optional[str] = Field(..., example="2008-01-22")
    age: Optional[int] = Field(..., example=55)
    birthplace: Optional[str] = Field(..., example="Манхэттэн, Нью-Йорк, США")
    deathplace: Optional[str] = Field(..., example="Манхэттэн, Нью-Йорк, США")
    hasAwards: Optional[int] = Field(..., example=1)
    profession: Optional[str] = Field(..., example="Актер, Продюсер, Сценарист")
    facts: List[str]
    spouses: List[PersonResponseSpouses]
    films: List[PersonResponseFilms]


class PersonByNameResponse(BaseModel):
    total: int = Field(..., example=35)
    items: List[PersonByNameResponseItems]


class ImageResponse(BaseModel):
    total: int = Field(..., description="Общее кол-во изображений", example=50)
    totalPages: int = Field(..., description="Код-во доступных страниц", example=3)
    items: List[ImageResponseItems]


class PremiereResponse(BaseModel):
    total: int = Field(..., example=34)
    items: List[PremiereResponseItem]


class DigitalReleaseResponse(BaseModel):
    page: int = Field(..., example=1)
    total: int = Field(..., example=34)
    releases: List[DigitalReleaseItem]


class VideoResponse(BaseModel):
    total: int = Field(..., example=50)
    items: List[VideoResponseItems]


class KinopoiskUserVoteResponse(BaseModel):
    total: int = Field(..., example=200)
    totalPages: int = Field(..., example=7)
    items: List[KinopoiskUserVoteResponseItems]


class ApiKeyResponse(BaseModel):
    totalQuota: ApiKeyResponseTotalQuota
    dailyQuota: ApiKeyResponseDailyQuota
    accountType: AccountType = Field(..., example="FREE")


class SeasonResponse(BaseModel):
    total: int = Field(..., example=5)
    items: List[Season]


class DistributionResponse(BaseModel):
    total: int = Field(..., example=5)
    items: List[Distribution]


class AwardResponse(BaseModel):
    total: int = Field(..., example=5)
    items: List[Award]
