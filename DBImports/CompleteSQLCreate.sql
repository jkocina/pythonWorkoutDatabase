SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF exists program;
DROP TABLE IF EXISTS programWorkout;
DROP TABLE IF EXISTS workout;
DROP TABLE IF EXISTS exerciseWorkout;
DROP TABLE IF EXISTS video;
DROP TABLE IF EXISTS famUser;
DROP TABLE IF EXISTS userRole;
DROP TABLE IF EXISTS userStats;
DROP TABLE IF EXISTS userProgram;
DROP TABLE IF EXISTS userProgramDays;
DROP TABLE IF EXISTS userProgramChoice;
DROP TABLE IF EXISTS userProgramWorkout;
DROP TABLE IF EXISTS userProgramWorkoutExercise;
DROP TABLE IF EXISTS userFitnessNeeds;
DROP TABLE IF EXISTS userFavoriteTrainer;
DROP TABLE IF EXISTS userProgress;
DROP TABLE IF EXISTS days;
DROP TABLE IF EXISTS fitnessNeeds;
DROP TABLE IF EXISTS fitnessTip;
DROP TABLE IF EXISTS famGroup;
DROP TABLE IF EXISTS trainerCertifications;
DROP TABLE IF EXISTS certificationAuthority;
DROP TABLE IF EXISTS certifications;
DROP TABLE IF EXISTS exerciseVideo;
DROP TABLE IF EXISTS exercise;
DROP TABLE IF EXISTS exerciseBodyArea;
DROP TABLE IF EXISTS bodyArea;
DROP TABLE IF EXISTS exerciseMuscleGroup;
DROP TABLE IF EXISTS muscleGroup;
DROP TABLE IF EXISTS exerciseTypeExercise;
DROP TABLE IF EXISTS typeExercise;
DROP TABLE IF EXISTS exerciseMeasurementType;
DROP TABLE IF EXISTS measurementType;
DROP TABLE IF EXISTS exerciseEquipment;
DROP TABLE IF EXISTS equipment;

CREATE TABLE days(
    dayId INT NOT NULL AUTO_INCREMENT,
    dayOfWeek VARCHAR(10) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY(dayId)

);

CREATE TABLE exercise(
    exerciseId INT NOT NULL AUTO_INCREMENT,
    exerciseName VARCHAR(100) NOT NULL,
    alternation VARCHAR(50),
    spectrum VARCHAR(10),
    metabolicEquivalent INT,
    flexibility TINYINT,
    weightPattern TINYINT,
    spotter TINYINT,
    difficulty INT,
    equipmentRequired TINYINT,
    targetReps INT(3),
    targetTimeSeconds INT(4),
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY(exerciseId)
);

CREATE TABLE bodyArea (
    bodyAreaId INT NOT NULL AUTO_INCREMENT,
    bodyAreaName VARCHAR(50) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY(bodyAreaId)
);

CREATE TABLE muscleGroup (
    muscleGroupId INT NOT NULL AUTO_INCREMENT,
    muscleGroupName VARCHAR(50) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY(muscleGroupId)
);

CREATE TABLE typeExercise (
    typeId INT NOT NULL AUTO_INCREMENT,
    exerciseTypeName VARCHAR(50) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY(typeId)
);

CREATE TABLE measurementType (
    measureId INT NOT NULL AUTO_INCREMENT,
    measureType VARCHAR(30) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY(measureId)
);

CREATE TABLE equipment (
    equipmentId INT NOT NULL AUTO_INCREMENT,
    equipmentName VARCHAR(50) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY(equipmentId)
);

CREATE TABLE userRole (
    userRoleId INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
    description VARCHAR(50) NOT NULL,
    isAdmin TINYINT,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userRoleId)
);

CREATE TABLE famGroup (
    groupId INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    description TEXT(500) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (groupId)
);

CREATE TABLE fitnessNeeds (
    fitnessNeedId INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description text(500) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (fitnessNeedId)
);

CREATE TABLE video (
	videoId INT NOT NULL AUTO_INCREMENT,
	videoLink VARCHAR(200) NOT NULL,
	videoDescription VARCHAR(500),
	createdOn DATE NOT NULL,
	updatedOn DATE,
  deleted TINYINT,
  modifiedBy INT,
	PRIMARY KEY(videoId)
);

CREATE TABLE workout (
	workoutId INT NOT NULL AUTO_INCREMENT,
	workoutName VARCHAR(50) NOT NULL,
	workoutDescription VARCHAR(200),
	createdOn DATE NOT NULL,
	updatedOn DATE,
  deleted TINYINT,
  modifiedBy INT,
	PRIMARY KEY(workoutId)
);

CREATE TABLE program (
	programId INT NOT NULL AUTO_INCREMENT,
  creatorId INT NOT NULL,
	programName VARCHAR(50) NOT NULL,
  daysAWeek INT(1),
  totalWeeks INT(2),
  price INT(5),
	createdOn DATE NOT NULL,
	updatedOn DATE,
  deleted TINYINT,
  modifiedBy INT,
	PRIMARY KEY(programId),
    FOREIGN KEY (creatorId)
      REFERENCES famUser(userId)
);



CREATE TABLE exerciseWorkout  (
    exerciseWorkoutId INT NOT NULL AUTO_INCREMENT,
    workoutId INT NOT NULL,
    exerciseId INT NOT NULL,
    targetReps INT (3),
    targetTimeSeconds INT(4),
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (exerciseWorkoutId),
      FOREIGN KEY (workoutId)
        REFERENCES workout(workoutId),
      FOREIGN KEY (exerciseId)
        REFERENCES exercise(exerciseId)
);

CREATE TABLE userProgram (
    userProgramId INT NOT NULL AUTO_INCREMENT,
    userId INT NOT NULL,
    programId INT NOT NULL,
    active TINYINT NOT NULL,
    daysCompleted INT,
    weeksCompleted INT,
    amountPaid INT,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userProgramId),
      FOREIGN KEY (userId)
        REFERENCES famUser(userId)
        ON UPDATE CASCADE,
      FOREIGN KEY (programId)
        REFERENCES program(programId)
        ON UPDATE CASCADE
);

CREATE TABLE userProgramDays (
    userProgramDaysId INT NOT NULL AUTO_INCREMENT,
    dayId INT NOT NULL,
    userProgramId INT NOT NULL,
    daysAWeek INT(1),
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userProgramDaysId),
      FOREIGN KEY (dayId)
        REFERENCES day(dayId)
          ON UPDATE CASCADE,
      FOREIGN KEY (userProgramId)
        REFERENCES userProgram(userProgramId)
          ON UPDATE CASCADE
);

CREATE TABLE userProgramWorkout (
  userProgramWorkoutId INT NOT NULL AUTO_INCREMENT,
  userProgramId INT NOT NULL,
  programWorkoutId INT NOT NULL,
  caloriesBurned INT NOT NULL,
  completed TINYINT,
  shared TINYINT,
  shareMethod VARCHAR(20),
  createdOn DATE NOT NULL,
  updatedOn DATE,
  deleted TINYINT,
  modifiedBy INT,
  PRIMARY KEY (userProgramWorkoutId),
    FOREIGN KEY (userProgramId)
      REFERENCES userProgram(userProgramId)
      ON UPDATE CASCADE,
    FOREIGN KEY (programWorkoutId)
      REFERENCES programWorkout(programWorkoutId)
      ON UPDATE CASCADE


);

CREATE TABLE programWorkout (
  programWorkoutId INT NOT NULL AUTO_INCREMENT,
	programId INT NOT NULL,
	workoutId INT NOT NULL,
  createdOn DATE NOT NULL,
  updatedOn DATE,
  deleted TINYINT,
  modifiedBy INT,
  PRIMARY KEY(programWorkoutId),
    	FOREIGN KEY(programId)
    		  REFERENCES program(programId)
    		    ON UPDATE CASCADE,
    	FOREIGN KEY (workoutId)
    		  REFERENCES workout(workoutId)
    		    ON UPDATE CASCADE
);

CREATE TABLE userProgramWorkoutExercise (
    userProgramWorkoutExerciseId INT NOT NULL AUTO_INCREMENT,
    userProgramWorkoutId INT NOT NULL,
    exerciseWorkoutId INT NOT NULL,
    exerciseId INT NOT NULL,
    repsCompleted INT(3),
    timeCompletedSeconds INT(10),
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userProgramWorkoutExerciseId),
      FOREIGN KEY (userProgramWorkoutId)
        REFERENCES userProgramWorkout(userProgramWorkoutId)
        ON UPDATE CASCADE,
      FOREIGN KEY (exerciseWorkoutId)
        REFERENCES exerciseWorkout(exerciseWorkoutId)
        ON UPDATE CASCADE,
      FOREIGN KEY (exerciseId)
        REFERENCES exercise(exerciseId)
        ON UPDATE CASCADE
);

CREATE TABLE exerciseBodyArea (
  exerciseBodyAreaId INT NOT NULL AUTO_INCREMENT,
	exerciseId INT NOT NULL,
	bodyAreaId INT NOT NULL,
  createdOn DATE NOT NULL,
  updatedOn DATE,
  deleted TINYINT,
  modifiedBy INT,
  PRIMARY KEY (exerciseBodyAreaId),
      FOREIGN KEY (exerciseId)
          REFERENCES exercise(exerciseId)
              ON UPDATE CASCADE,
      FOREIGN KEY (bodyAreaId)
    	    REFERENCES bodyArea(bodyAreaId)
                ON UPDATE CASCADE
);

CREATE TABLE exerciseMuscleGroup(
    exerciseMuscleGroupId INT NOT NULL AUTO_INCREMENT,
    exerciseId INT NOT NULL,
    muscleGroupId INT NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (exerciseMuscleGroupId),
        FOREIGN KEY (exerciseId)
            REFERENCES exercise(exerciseId)
                ON UPDATE CASCADE,
        FOREIGN KEY (muscleGroupId)
    	      REFERENCES muscleGroup(muscleGroupId)
                ON UPDATE CASCADE
);

CREATE TABLE exerciseTypeExercise (
    exerciseTypeExerciseId INT NOT NULL AUTO_INCREMENT,
    exerciseId INT NOT NULL,
    typeId INT NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (exerciseTypeExerciseId),
      FOREIGN KEY (exerciseId)
        REFERENCES exercise(exerciseId)
            ON UPDATE CASCADE,
      FOREIGN KEY (typeId)
	      REFERENCES typeExercise(typeId)
          ON UPDATE CASCADE
);

CREATE TABLE exerciseMeasurementType(
    exerciseMeasurementTypeId INT NOT NULL AUTO_INCREMENT,
    exerciseId INT NOT NULL,
    measureId INT NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (exerciseMeasurementTypeId),
      FOREIGN KEY (exerciseId)
        REFERENCES exercise(exerciseId)
          ON UPDATE CASCADE,
      FOREIGN KEY (measureId)
        REFERENCES measurementType(measureId)
          ON UPDATE CASCADE
);

CREATE TABLE exerciseEquipment(
    exerciseEquipmentId INT NOT NULL AUTO_INCREMENT,
    exerciseId INT NOT NULL,
    equipmentId INT NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (exerciseEquipmentId),
      FOREIGN KEY (exerciseId)
        REFERENCES exercise(exerciseId)
          ON UPDATE CASCADE,
      FOREIGN KEY (equipmentId)
  	    REFERENCES equipment(equipmentId)
          ON UPDATE CASCADE
);

CREATE TABLE famUser(
    userId INT NOT NULL AUTO_INCREMENT,
    groupId INT NOT NULL,
    userRoleId INT NOT NULL,
    userName VARCHAR(50) NOT NULL,
    email VARCHAR(345) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    passwordDigest VARCHAR(60),
    activationDigest VARCHAR(60),
    userKey VARCHAR(60),
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userId),
        FOREIGN KEY (groupId)
            REFERENCES famGroup(groupId)
              ON UPDATE CASCADE,
        FOREIGN KEY (userRoleId)
            REFERENCES userRole(userRoleId)
              ON UPDATE CASCADE
);

CREATE TABLE userStats(
    userStatsId INT NOT NULL AUTO_INCREMENT,
    userId INT NOT NULL,
    height INT(3),
    weight INT(3),
    restingHeartRate INT(3),
    waistHipRatio INT(3),
    bmi INT(2),
    dob DATE,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userStatsId),
        FOREIGN KEY (userId)
            REFERENCES famUser(userId)
);

CREATE TABLE userProgress(
    userProgressId INT NOT NULL AUTO_INCREMENT,
    userProgramChoiceId INT NOT NULL,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    daysAWeek INT(1) NOT NULL,
    totalWeeks INT(2) NOT NULL,
    daysCompleted INT(2) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userProgressId),
        FOREIGN KEY (userProgramChoiceId)
            REFERENCES userProgramChoice(userProgramChoiceId)
);

CREATE TABLE userProgramChoice(
    userProgramChoiceId INT NOT NULL AUTO_INCREMENT,
    userId INT NOT NULL,
    programId INT NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userProgramChoiceId),
        FOREIGN KEY (userId)
            REFERENCES famUser(userId),
        FOREIGN KEY (programId)
            REFERENCES program(programId)
);

CREATE TABLE userFavoriteTrainer(
    userFavoriteTrainerId INT NOT NULL AUTO_INCREMENT,
    userId INT NOT NULL,
    trainerId INT NOT NULL,
    preferenceRank INT(9) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userFavoriteTrainerId),
        FOREIGN KEY (userId)
            REFERENCES famUser(userId)
              ON UPDATE CASCADE,
        FOREIGN KEY (trainerId)
            REFERENCES famUser(userId)
              ON UPDATE CASCADE
);

CREATE TABLE userFitnessNeeds(
    userFitnessNeedsId INT NOT NULL AUTO_INCREMENT,
    userId INT NOT NULL,
    fitnessNeedId INT NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userFitnessNeedsId),
      FOREIGN KEY (userId)
        REFERENCES famUser(userId)
          ON UPDATE CASCADE,
      FOREIGN KEY (fitnessNeedId)
        REFERENCES fitnessNeeds(fitnessNeedId)
          ON UPDATE CASCADE
);

CREATE TABLE fitnessTip(
    fitnessTipId INT NOT NULL AUTO_INCREMENT,
    fitnessNeedId INT NOT NULL,
    description TEXT(500) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (fitnessTipId),
        FOREIGN KEY (fitnessNeedId)
            REFERENCES fitnessNeeds(fitnessNeedId)
);

CREATE TABLE trainerCertifications(
    trainerCertificationsId INT NOT NULL AUTO_INCREMENT,
    userId INT NOT NULL,
    certificationId INT NOT NULL,
    verified TINYINT,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (trainerCertificationsId),
        FOREIGN KEY (userId)
            REFERENCES famUser(userId)
              ON UPDATE CASCADE,
        FOREIGN KEY (certificationId)
            REFERENCES ceritfications(certificationId)
              ON UPDATE CASCADE
);

CREATE TABLE certificationAuthority(
    certificationAuthorityId INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(345),
    phone VARCHAR(15),
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (certificationAuthorityId)
);

CREATE TABLE certifications(
    certificationId INT NOT NULL AUTO_INCREMENT,
    certificationAuthorityId INT NOT NULL,
    certificationName VARCHAR(50) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (certificationId),
        FOREIGN KEY (certificationAuthorityId)
            REFERENCES certificationAuthority(certificationAuthorityId)
              ON UPDATE CASCADE
);

CREATE TABLE exerciseVideo(
    exerciseVideoId INT NOT NULL AUTO_INCREMENT,
    videoId INT NOT NULL,
    exerciseId INT NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (exerciseVideoId),
        FOREIGN KEY (videoId)
            REFERENCES video(videoId)
            ON UPDATE CASCADE
);
