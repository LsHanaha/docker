
CREATE TABLE "Playlist" (
	"id" serial,
	"name" TEXT NOT NULL UNIQUE,
	CONSTRAINT "Playlist_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "Track" (
	"id" serial,
	"name" TEXT NOT NULL UNIQUE,
	"url" TEXT NOT NULL UNIQUE,
	CONSTRAINT "Track_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

CREATE TABLE "Cord" (
	"id" serial NOT NULL,
	"playlist_id" integer NOT NULL,
	"track_id" integer NOT NULL,
	CONSTRAINT "Cord_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);

ALTER TABLE "Cord" ADD CONSTRAINT "Cord_fk0" FOREIGN KEY ("playlist_id") REFERENCES "Playlist"("id");
ALTER TABLE "Cord" ADD CONSTRAINT "Cord_fk1" FOREIGN KEY ("track_id") REFERENCES "Track"("id");

--  psql -v ON_ERROR_STOP=1 -1 -U username -h 192.168.99.102 -p 5432 -f test_task.sql postgres