package controllers

import (
	"PeakPilot/API/initializers"
	"net/http"

	"github.com/gin-gonic/gin"
)

type Route struct {
	Name string
}

func GetRoutes(c *gin.Context) {
	// Get all sites
	var routes []Route
	result := initializers.DB.Select("name").Find(&routes)
	if result.Error != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to retrieve sites"})
		return
	}

	// Return the list of sites in the JSON response
	c.JSON(http.StatusOK, gin.H{
		"message": "All routes of all sites",
		"sites": routes,
	})
}