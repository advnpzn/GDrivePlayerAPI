# GDrivePlayerAPI
A python wrapper for gdriveplayer.co API

### Instructions
```python 
pip install gdriveplayer
```

### Usage

The wrapper consists of 3 main classes.

* `GAnime`
* `GMovie`
* `GDrama`

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

s = GAnime().search(title='Pokemon')
```
