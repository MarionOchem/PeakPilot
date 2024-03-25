package controllers

import (
	"PeakPilot/API/initializers"
	"net/http"

	"github.com/gin-gonic/gin"
)



type Site struct {
	Name string
}

func GetSite(c *gin.Context) {
	// Get all 
	var sites []Site
	result := initializers.DB.Select("name").Find(&sites)
	if result.Error != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to retrieve sites"})
		return
	}

	// Return the list of sites in the JSON response
	c.JSON(http.StatusOK, gin.H{
		"message": "All routes of all sites",
		"sites":   sites,
	})
}