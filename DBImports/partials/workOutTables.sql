#Workout Tables

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF exists program;
DROP TABLE IF EXISTS programWorkout;
DROP TABLE IF EXISTS workout;
DROP TABLE IF EXISTS exerciseWorkout;
DROP TABLE IF EXISTS video;

CREATE TABLE program(
	programId INT NOT NULL AUTO_INCREMENT,
	programName VARCHAR(100) NOT NULL,
	createdOn DATE NOT NULL,
	updatedOn DATE NOT NULL,
	PRIMARY KEY(programId)
);

CREATE TABLE programWorkout(
	programId INT NOT NULL,
	workoutId INT NOT NULL,
	FOREIGN KEY(programId)
		REFERENCES program(programId)
		ON UPDATE CASCADE,
	FOREIGN KEY (workoutId)
		REFERENCES workout(workoutId)
		ON UPDATE CASCADE
);

CREATE TABLE workout(
	workoutId INT NOT NULL AUTO_INCREMENT,
	workoutName VARCHAR(50) NOT NULL,
	workoutDescription VARCHAR(200),
	createdOn DATE NOT NULL,
	updatedOn DATE NOT NULL,
	PRIMARY KEY(workoutId)
);

CREATE TABLE video(
	videoId INT NOT NULL AUTO_INCREMENT,
	videoLink VARCHAR(200) NOT NULL,
	videoDescription VARCHAR(500),
	createdOn DATE NOT NULL,
	updatedOn DATE NOT NULL,
	PRIMARY KEY(videoId)
);


/*
CREATE TABLE exerciseWorkout(
	workoutId NOT NULL,
	exerciseId NOT NULL,
	FOREIGN KEY (workoutId)
		REFERENCES workout(workoutId)
		ON UPDATE CASCADE,
	FOREIGN KEY (exerciseId)
		REFERENCES exercise(exerciseId)
		ON UPDATE CASCADE
);
*/
