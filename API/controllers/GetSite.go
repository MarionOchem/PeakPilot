package controllers

import (
	"PeakPilot/API/initializers"
	"net/http"

	"github.com/gin-gonic/gin"
)



func GetSite(c *gin.Context) {
	// Get all sites names data
	var sites []Site
	result := initializers.DB.Select("name").Find(&sites)
	if result.Error != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to retrieve sites"})
		return
	}

	// Return the list of sites in the JSON response
	c.JSON(http.StatusOK, sites)
}