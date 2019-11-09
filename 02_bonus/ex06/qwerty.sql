CREATE SCHEMA music;

CREATE  TABLE test.playlist ( 
	id                   integer  NOT NULL ,
	name                 text  NOT NULL ,
	music_list           integer[]   ,
	CONSTRAINT pk_playlist_id PRIMARY KEY ( id ),
	CONSTRAINT unq_playlist_music UNIQUE ( music ) 
 );

CREATE  TABLE test.tracks ( 
	id                   integer  NOT NULL ,
	name                 text  NOT NULL ,
	url                  text  NOT NULL ,
	CONSTRAINT pk_tracks_id PRIMARY KEY ( id )
 );

