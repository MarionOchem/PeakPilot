// Get all routes names data

package controllers

import (
	"PeakPilot/API/initializers"
	"net/http"

	"github.com/gin-gonic/gin"
)



func GetRoutes(c *gin.Context) {

	// Define a slice to store the retrieved data
	var routes []Route

	// Query db
	result := initializers.DB.Select("name").Find(&routes)
	if result.Error != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to retrieve sites"})
		return
	}

	// Return the list of routes in the JSON response
	c.JSON(http.StatusOK, routes)
}