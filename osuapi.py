import enum

__all__ = ('Mods', 'url')

class Mods(enum.Enum):
	No                = 0
	NoFail            = 1
	Easy              = 2
	TouchDevice       = 4
	Hidden            = 8
	HardRock          = 16
	SuddenDeath       = 32
	DoubleTime        = 64
	Relax             = 128
	HalfTime          = 256
	Nightcore         = 512
	Flashlight        = 1024
	Autoplay          = 2048
	SpunOut           = 4096
	Relax2            = 8192
	Perfect           = 16384
	Key4              = 32768
	Key5              = 65536
	Key6              = 131072
	Key7              = 262144
	Key8              = 524288
	FadeIn            = 1048576
	Random            = 2097152
	Cinema            = 4194304
	Target            = 8388608
	Key9              = 16777216
	KeyCoop           = 33554432
	Key1              = 61708864
	Key3              = 134217728
	Key2              = 268435456
	ScoreV2           = 536870912
	LastMod           = 1073741824
	KeyMod            = Key1 | Key2 | Key3 | Key4 | Key5 | Key6 | Key7 | Key8 | Key9 | KeyCoop
	FreeModAllowed    = NoFail | Easy | Hidden | HardRock | SuddenDeath | Flashlight | FadeIn | Relax | Relax2 | SpunOut | KeyMod
	ScoreIncreaseMods = Hidden | HardRock | DoubleTime | Flashlight | FadeIn

base = 'https://osu.ppy.sh/api/get_{}?k={}'
supported_args = {
	'beatmaps': {'s', 'b', 'u', 'type', 'm', 'a', 'h', 'limit', 'mods', 'since'},
	'user': {'u', 'm', 'type', 'event_days'},
	'scores': {'b', 'u', 'm', 'mods', 'type', 'limit'},
	'user_best': {'u', 'm', 'limit', 'type'},
	'user_recent': {'u', 'm', 'limit', 'type'},
	'match': {'mp'},
	'replay': {'m', 'b', 'u', 'type', 'mods'}
}

def url(part, key, **kwargs):
	if part not in supported_args:
		raise ValueError('Incorrect API part')
	url = base.format(part, key)
	for kw in kwargs:
		if kw in supported_args[part]:
			url += '?{}={}'.format(kw, kwargs[kw])
	return url
