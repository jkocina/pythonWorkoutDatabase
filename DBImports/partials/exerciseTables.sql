SET FOREIGN_KEY_CHECKS=0;

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
    alternation varchar(5),
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


SET FOREIGN_KEY_CHECKS=1;
