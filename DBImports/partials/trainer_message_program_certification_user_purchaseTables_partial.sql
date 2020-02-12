SET FOREIGN_KEY_CHECKS=0;

/*
DROP TABLE IF EXISTS message;
DROP TABLE IF EXISTS userFavoriteTrainer;
DROP TABLE IF EXISTS messageHeader;

*/

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS userRole;
DROP TABLE IF EXISTS userStats;
DROP TABLE IF EXISTS userProgram;
DROP TABLE IF EXISTS userProgramDays;
DROP TABLE IF EXISTS userProgramWorkout;
DROP TABLE IF EXISTS userProgramWorkoutExercise;
DROP TABLE IF EXISTS userFitnessNeeds;

DROP TABLE IF EXISTS programWorkout;
DROP TABLE IF EXISTS days;
DROP TABLE IF EXISTS fitnessNeeds;
DROP TABLE IF EXISTS fitnessTip;
DROP TABLE IF EXISTS group;
DROP TABLE IF EXISTS trainerCertifications;
DROP TABLE IF EXISTS certificationAuthority;
DROP TABLE IF EXISTS certifications;
DROP TABLE IF EXISTS exerciseVideo;
DROP TABLE IF EXISTS video;

DROP table if exists exercise;
DROP table if exists exerciseBodyArea;
DROP table if exists bodyArea;
DROP table if exists exerciseMuscleGroup;
DROP table if exists muscleGroup;
DROP table if exists exerciseTypeExercise;
DROP table if exists typeExercise;
DROP table if exists exerciseMeasurementType;
DROP table if exists measurementType;
DROP table if exists exerciseEquipment;
DROP table if exists equipment;



create table exercise(
    exerciseId int not null auto_increment,
    exerciseName varchar(50) not null,
    alternation varchar(5) ,
    spectrum varchar(10),
    metabolicEquivalent int,
    flexibility tinyint not null,
    weightPattern tinyint not null,
    spotter tinyint not null,
    difficulty int not null,
    equipmentRequired tinyint not null,
    videoLink varchar(100),
    createdOn date not null,
    updatedOn date,
    primary Key(exerciseId)
);

create table bodyArea(
    bodyAreaId int not null auto_increment,
    bodyAreaName varchar(20) not null,
    createdOn date not null,
    updatedOn date,
    primary key(bodyAreaId)
);

create table exerciseBodyArea(
	exerciseId int not null,
	bodyAreaId int not null,
        FOREIGN KEY (exerciseId)
            REFERENCES exercise(exerciseId)
            ON UPDATE CASCADE,
        FOREIGN KEY (bodyAreaId)
	    REFERENCES bodyArea(bodyAreaId)
            ON UPDATE CASCADE
);

create table muscleGroup(
    muscleGroupId int not null auto_increment,
    muscleGroupName varchar(20) not null,
    createdOn date not null,
    updatedOn date,
    primary key(muscleGroupId)
);

create table exerciseMuscleGroup(
    exerciseId int not null,
    muscleGroupId int not null,
    FOREIGN KEY (exerciseId)
            REFERENCES exercise(exerciseId)
            ON UPDATE CASCADE,
        FOREIGN KEY (muscleGroupId)
	    REFERENCES muscleGroup(muscleGroupId)
            ON UPDATE CASCADE
);

create table typeExercise (
    typeId int not null auto_increment,
    exerciseTypeName varchar(20) not null,
    createdOn date not null,
    updatedOn date,
    primary key(typeId)
);

create table exerciseTypeExercise (
    exerciseId int not null,
    typeId int not null,
    FOREIGN KEY (exerciseId)
            REFERENCES exercise(exerciseId)
            ON UPDATE CASCADE,
        FOREIGN KEY (typeId)
	    REFERENCES typeExercise(typeId)
            ON UPDATE CASCADE
);

create table measurementType(
    measureId int not null auto_increment,
    measureType varchar(30) not null,
    createdOn date not null,
    updatedOn date,
    primary key(measureId)
);

create table exerciseMeasurementType(
    exerciseId int not null,
    measureId int not null,
    FOREIGN KEY (exerciseId)
            REFERENCES exercise(exerciseId)
            ON UPDATE CASCADE,
        FOREIGN KEY (measureId)
	    REFERENCES measurementType(measureId)
            ON UPDATE CASCADE
);

create table equipment(
    equipmentId int not null auto_increment,
    equipmentName varchar(30) not null,
    createdOn date not null,
    updatedOn date,
    primary key(equipmentId)
);

create table exerciseEquipment(
    exerciseId int not null,
    equipmentId int not null,
    FOREIGN KEY (exerciseId)
            REFERENCES exercise(exerciseId)
            ON UPDATE CASCADE,
        FOREIGN KEY (equipmentId)
	    REFERENCES equipment(equipmentId)
            ON UPDATE CASCADE
);

CREATE TABLE message(
    messageId INT NOT NULL AUTO_INCREMENT,
    messageBody TEXT(500),
    read tinyint NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY(messageId)
);

CREATE TABLE messageHeader(
    messageHeaderId INT NOT NULL AUTO_INCREMENT,
    fromUserId INT NOT NULL,
    toUserId INT NOT NULL,
    messageId INT NOT NULL,
    subject VARCHAR(50),
    createdOn DATE NOT NULL,
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (messageHeaderId),
        FOREIGN KEY (fromUserId)
            REFERENCES user(userId),
        FOREIGN KEY (toUserId)
            REFERENCES user(userId),
        FOREIGN KEY (messageId)
            REFERENCES message(messageId)
);

CREATE TABLE user(
    userId INT NOT NULL AUTO_INCREMENT,
    groupId INT NOT NULL,
    userRoleId INT NOT NULL,
    userName VARCHAR(20) NOT NULL,
    email VARCHAR(345) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zipCode VARCHAR(15),
    passwordDigest VARCHAR(60),
    activationDigest VARCHAR(60),
    createdOn DATE NOT NULL,
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userId),
        FOREIGN KEY (groupId)
            REFERENCES group(groupId),
        FOREIGN KEY (userRoleId)
            REFERENCES userRole(userRoleId)
);

CREATE TABLE userRole(
    userRoleId INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
    description VARCHAR(50) NOT NULL,
    isAdmin TINYINT,
    createdOn DATE NOT NULL,
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userRoleId)
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
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userStatsId),
        FOREIGN KEY (userId)
            REFERENCES user(userId)
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
    updatedOn DATE NOT NULL,
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
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userProgramChoiceId),
        FOREIGN KEY (userId)
        REFERENCES user(userId),
        FOREIGN KEY (programId)
        REFERENCES program(programId)
);

CREATE TABLE userFavoriteTrainer(
    userFavoriteTrainerId INT NOT NULL AUTO_INCREMENT,
    userId INT NOT NULL,
    trainerId INT NOT NULL,
    preferenceRank INT(9) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userFavoriteTrainerId),
        FOREIGN KEY (userId)
        REFERENCES user(userId),
        FOREIGN KEY (trainerId)
        REFERENCES user(userId)
);

CREATE TABLE userFitnessNeeds(
    userFitnessNeedsId INT NOT NULL AUTO_INCREMENT,
    userId INT NOT NULL,
    fitnessNeedId INT NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (userFitnessNeedsId),
        FOREIGN KEY (userId)
        REFERENCES user(userId),
        FOREIGN KEY (fitnessNeedId)
        REFERENCES fitnessNeeds(fitnessNeedId)
);

CREATE TABLE fitnessNeeds(
    fitnessNeedId INT NOT NULL AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    description text(500) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (fitnessNeedId)
);

CREATE TABLE fitnessTip(
    fitnessTipId INT NOT NULL AUTO_INCREMENT,
    fitnessNeedId INT NOT NULL,
    description TEXT(500) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (fitnessTipId),
        FOREIGN KEY (fitnessNeedId)
        REFERENCES fitnessNeeds(fitnessNeedId)
);

CREATE TABLE group(
    groupId INT NOT NULL AUTO_INCREMENT,
    name varchar(30) NOT NULL,
    description TEXT(500) NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (groupId)
);

CREATE TABLE trainerCertifications(
    trainerCertificationsId INT NOT NULL AUTO_INCREMENT,
    userId INT NOT NULL,
    certificationId INT NOT NULL,
    verified TINYINT,
    createdOn DATE NOT NULL,
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (trainerCertificationsId),
        FOREIGN KEY (userId)
        REFERENCES user(userId),
        FOREIGN KEY (certificationId)
        REFERENCES ceritfications(certificationId)
);

CREATE TABLE certificationAuthority(
    certificationAuthorityId INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(345) NOT NULL,
    phone VARCHAR() NOT NULL,
    address VARCHAR() NOT NULL,
    city VARCHAR() NOT NULL,
    state VARCHAR() NOT NULL,
    zipCode VARCHAR() NOT NULL,
    createdOn DATE NOT NULL,
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
    PRIMARY KEY (certificationAuthorityId)
);

CREATE TABLE certifications(
    certifications INT NOT NULL AUTO_INCREMENT,

    createdOn DATE NOT NULL,
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
);

CREATE TABLE exerciseVideo(
    exerciseVideo INT NOT NULL AUTO_INCREMENT,
    createdOn DATE NOT NULL,
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
);

CREATE TABLE video(
    video INT NOT NULL AUTO_INCREMENT,
    createdOn DATE NOT NULL,
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
);

CREATE TABLE purchase(
    purchase INT NOT NULL AUTO_INCREMENT,
    createdOn DATE NOT NULL,
    updatedOn DATE NOT NULL,
    deleted TINYINT,
    modifiedBy INT,
);

SET FOREIGN_KEY_CHECKS=1;
