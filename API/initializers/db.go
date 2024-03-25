package initializers

import (
	"log"
	"os"

	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

// Create a global variable that point to a gorm.DB object (provided by GORM lib representing a connection to a postgres db and provides method for interactig with it)
var DB *gorm.DB


func ConnectToDb() {
	var err error
	dsn := os.Getenv("DB_CONFIG")
	DB, err = gorm.Open(postgres.Open(dsn), &gorm.Config{})

	if err != nil {
		log.Fatal("Failed to connect to database")
	}
}