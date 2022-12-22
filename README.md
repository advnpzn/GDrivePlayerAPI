# GDrivePlayerAPI
A python wrapper for gdriveplayer.co API

### Instructions
```python 
pip install gdriveplayer
```

### Usage

The wrapper consists of 4 main classes.

* `GAnime`
* `GMovie`
* `GDrama`
* `GSeries`

Each of those classes contain very similar methods.

#### `GAnime`

#### Methods

```python
search(title: str | None = '', limit: int | str | None = 10, page: int | str | None = 1) -> List[Anime]
```

Search an Anime. Returns a list of `Anime` Objects.

The `Anime` Object consists of several attributes such as

* `id` 
* `title`
* `poster`
* `genre`
* `summary`
* `status`
* `type`
* `total_episode`
* `sub`
* `player_url`

#### Example

```python
from GDrivePlayer import GAnime

s = GAnime().search(title='Pokemon', limit=3)
print(s)
```
#### `Output`
```python
[<GDrivePlayer.anime.Anime object at 0x7f89b8d63370>, <GDrivePlayer.anime.Anime object at 0x7f89b8d633a0>, <GDrivePlayer.anime.Anime object at 0x7f89b8d63160>]
```

You can see the attributes of individual objects by doing 

```python
from GDrivePlayer import GAnime

s = GAnime().search(title='Bocchi the Rock')

print(s[0].title)
print(s[0].genre)
print(s[0].id)
print(s[0].status)
print(s[0].summary)
print(s[0].total_episode)
```

#### `Output`
```
Bocchi the Rock!
CGDCT, Comedy, Music, Slice of Life
290813
Ongoing
Hitori Gotou is a high school girl whos starting to learn to play the guitar because she dreams of being in a band, but shes so shy that she hasnt made a single friend. However, her dream might come true after she meets Nijika Ijichi, a girl who plays drums and is looking for a new guitarist for her band.
11
```

```python
LatestAnimes(limit: str | int | None = 10, page: str | int | None = 1, order: str | None = "last_updated", sort: str | None = "DESC") -> List[Anime]
```

Returns a list of `LatestAnime` objects. The `LatestAnime` object is very similar to `Anime` object. The only difference is that the former doesn't contain `summary` attribute. This is due to the original API's structure.

```python
animeDetail(id: str | int) -> Anime
```

Returns `Anime` Object of the `id` that is passed to the method.

#### Example

```python
from GDrivePlayer import GAnime

s = GAnime().animeDetail(id=290813)

print(s)
print(s.title)
print(s.summary)
```

#### `Output`

```
<GDrivePlayer.anime.Anime object at 0x7f7e68282290>
Bocchi the Rock!
Hitori Gotou is a high school girl whos starting to learn to play the guitar because she dreams of being in a band, but shes so shy that she hasnt made a single friend. However, her dream might come true after she meets Nijika Ijichi, a girl who plays drums and is looking for a new guitarist for her band.
```

The classes such as `GDrama`, `GMovie` and `GSeries` also contain similar methods and similar Objects like `Anime` and `LatestAnime`.


### Disclaimer

The developer of this wrapper is in no way responsible for how the user utilises, modifies and/or accesses this wrapper.
