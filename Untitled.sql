CREATE SCHEMA test;

CREATE  TABLE test.Playlist ( 
	id                   integer NOT NULL ,
	name                 text  NOT NULL UNIQUE,
	music                integer[]   ,
	CONSTRAINT pk_Playlist_id PRIMARY KEY ( id )
 );

CREATE  TABLE test.Tracks ( 
	id                   integer  NOT NULL ,
	name                 text  NOT NULL UNIQUE,
	CONSTRAINT pk_Tracks_id PRIMARY KEY ( id )
 );
